#!/usr/bin/env python3
#-*- coding: utf_8 -*-

"""
dbase3.py

This module provides a class to manipulate DBase III database files.
It allows reading, writing, adding, updating and deleting records in the database.

Classes:
    DBaseFile (Main class)
    DbaseHeader
    DbaseField
    Record
    FieldType
"""

# Title: dBase III File Reader and Writer

import struct, os
from mmap import mmap as memmap, ACCESS_WRITE
from enum import Enum
from typing import List, Dict, Tuple, Callable, AnyStr, ByteString
from dataclasses import dataclass, field #, fields, field, is_dataclass
from datetime import datetime
from multiprocessing.pool import ThreadPool
# from multiprocessing import Pool
from threading import Lock
# from multiprocessing import Lock

try:
    from pybase3.utils import Dict
except ImportError:
    from utils import Dict



to_bytes = lambda x: x.encode('latin1') if type(x) == str else x
to_str = lambda x: x.decode('latin1') if type(x) == bytes else x

getYear = lambda: datetime.now().year - 1900
getMonth = lambda: datetime.now().month
getDay = lambda: datetime.now().day

class Record(Dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.deleted = False

    def __repr__(self):
        return "\n".join(f"{k}: {v}" for k, v in self.items())

    def __str__(self):
        return self.__repr__() + "\n"
    
class FieldType(Enum):
    CHARACTER = 'C'
    DATE = 'D'
    FLOAT = 'F'
    LOGICAL = 'L'
    MEMO = 'M'
    NUMERIC = 'N'

    def __repr__(self):
        return self.value   

    def __str__(self):
        return self.value

    # def __eq__(self, char):
    #     return self.value == to_bytes(char)   

class BoxType(Enum):
    UP_L = '\u250C'
    UP_R = '\u2510'
    DOWN_L = '\u2514'
    DOWN_R = '\u2518'
    HORZ = '\u2500'
    VERT = '\u2502'
    CROSS = '\u253C'
    T_L = '\u251C'
    T_R = '\u2524'
    T_UP = '\u2534'
    T_DOWN = '\u252C'
    T_LEFT_RIGHT = '\u2534'
    T_UP_DOWN = '\u252C'
    T_ALL = '\u253C'
    T_LEFT_UP = '\u251C'
    T_LEFT_DOWN = '\u2514'
    T_RIGHT_UP = '\u251C'
    T_RIGHT_DOWN = '\u2518'

    def __repr__(self):
        return self.value
    
    def __str__(self):
        return self.value
    
@dataclass
class DbaseHeader:
    version: int = 3 # 1 byte
    year: int = getYear() # 1 byte
    month: int = getMonth() # 1 byte
    day: int = getDay() # 1 byte
    records: int = 0 # 4 bytes
    header_size: int = 0 # 2 bytes
    record_size: int = 0 # 2 bytes
    reserved: bytes = b'\x00' * 20

    def load_bytes(self, bytes):
        (self.version, self.year, self.month, self.day, 
         self.records, self.header_size, self.record_size, 
         self.reserved) = struct.unpack('<BBBBLHH20s', bytes)
 
    def to_bytes(self):
        return struct.pack('<BBBBLHH20s', self.version, self.year, self.month, self.day, 
                           self.records, self.header_size, self.record_size, 
                           self.reserved)
    
    def __post_init__(self):
        curr_year = getYear()
        # curr_month = getMonth()
        # curr_day = getDay()
        if not (3 == self.version & 0b111):
            raise ValueError(f"Version must be a byte (3-5), got {self.version}")            
        if not (0 <= self.year <= curr_year):
            raise ValueError(f"Year must be a byte (0-{curr_year}), got {self.year}")
        if not (1 <= self.month <= 12):
            raise ValueError(f"Month must be a byte (1-12), got {self.month}")    
        if not (1 <= self.day <= 31):
            raise ValueError(f"Day must be a byte (1-31), got {self.day}")
        if not (0 <= self.records <= 2**32-1):
            raise ValueError(f"Records must be a 4-byte integer (0-{2**32-1}), got {self.records}")
        if not (0 <= self.header_size <= 2**16-1):
            raise ValueError(f"Header size must be a 2-byte integer (0-{2**16-1}), got {self.header_size}")
        if not (0 <= self.record_size <= 2**16-1):
            raise ValueError(f"Record size must be a 2-byte integer (0-{2**16-1}), got {self.record_size}")
        if not (20 == len(self.reserved)):
            raise ValueError(f"Reserved must be 20 bytes, got {len(self.reserved)}")


@dataclass
class DbaseField:
    name: str = '\x00' * 11  # Field name, 11 bytes
    type: str = 'C'  # Field type (C, N, etc.), 1 byte
    address: int = 0  # 1st reserved, 4 bytes
    length: int = 0  # Field length (maximun 254), 1 byte 
    decimal: int = 0  # Decimal places for numeric fields, 1 byte
    reserved: bytes = b'\x00' * 14  #  14 reserved bytes

    def load_bytes(self, bytes):
        # Extract the name as exactly 11 bytes
        raw_name = bytes[:11].rstrip(b'\x00').strip()  # Strip null terminators
        self.name = raw_name.decode('latin1')
        # Extract the type and other attributes
        self.type = chr(bytes[11])  # Field type is the next byte
        (self.address, self.length, self.decimal, self.reserved) = struct.unpack('<IBB14s', bytes[12:])
        
    def to_bytes(self):
        return struct.pack(
            '<11sBIBB14s',
            to_bytes(self.name)[:11].ljust(11, b'\x00'),  # Ensure name is exactly 11 bytes
            ord(self.type),
            self.address,
            self.length,
            self.decimal,
            self.reserved
        )


class DbaseFile:
    """
    Class to manipulate DBase III database files (read and write).

    Methods:
        __init__(self, filename: str)
        __del__(self)
        __len__(self)
        __getitem__(self, key)
        __iter__(self)
         _init(self)
        istartswith(f: str, v: str) -> bool
        iendswith(f: str, v: str) -> bool
        create(cls, filename: str, fields: List[Tuple[str, FieldType, int, int]])
        add_record(self, record_data: dict)
        update_record(self, index: int, record_data: dict)
        del_record(self, key, value = True)
        get_record(self, key)
        get_field(self, fieldname)
        search(self, fieldname, value, start=0, funcname="", comp_func=None)
        find(self, fieldname, value, start=0, comp_func=None)
        index(self, fieldname, value, start=0, comp_func=None)
        filter(self, fieldname, value, comp_func=None)
        save_record(self, key, record)
        write(self)
    """
    
    @staticmethod
    def istartswith(f: str, v: str) -> bool:
        """
        Checks if the string 'f' starts with the string 'v', ignoring case.

        :param f: String to check.
        :param v: Prefix to look for.
        :return: True if 'f' starts with 'v', False otherwise.
        """

        return f.lower().startswith(v.lower())

    @staticmethod
    def iendswith(f: str, v: str) -> bool:
        """
        Checks if the string 'f' ends with the string 'v', ignoring case.

        :param f: String to check.
        :param v: Suffix to look for.
        :return: True if 'f' ends with 'v', False otherwise.
        """
        return f.lower().endswith(v.lower())

    @classmethod
    def create(cls, filename: str, fields: List[Tuple[str, str, int, int]]):
        """
        Creates a new DBase III database file with the specified fields.

        :param filename: Name of the file to create.
        :param fields: List of tuples describing the fields (name, type, length, decimals).
        :raises FileExistsError: If the file already exists.
        """
        if os.path.exists(filename):
            raise FileExistsError(f"File {filename} already exists")
        with open(filename, 'wb') as file:
            header = DbaseHeader()
            header.header_size = 32 + 32 * len(fields) + 1
            header.record_size = sum(field[2] for field in fields) + 1
            file.write(header.to_bytes())
            for field in fields:
                name, ftype, length, decimal = field
                name = to_bytes(name)
                field = DbaseField(name, ftype, 0, length, decimal)
                file.write(field.to_bytes())
            file.write(b'\x0D')
        dbf = cls(filename)
        return dbf

    def __init__(self, filename):
        """
        Initializes an instance of DBase3.

        :param filename: Name of the database file.
        """
        self.lock = Lock()
        self.filename = filename
        self.filesize = os.path.getsize(filename)
        self.file = open(filename, 'r+b')
        # self.memfile = memmap(self.file.fileno(), 0, access=ACCESS_WRITE)
        self.num_fields = 0
        self.fields = []
        self.header = None
        self.datasize = 0
        self. _init()

    def __del__(self):
        """
        Closes the database file when the instance is destroyed.
        """
        self.file.close()

    def __len__(self):
        """
        Returns the number of records in the database, including records marked to be deleted.
        """
        return self.header.records
    
    def __getitem__(self, key):
        """
        Returns from the database a single record (dictionary with field names and field values) 
        or a list of them (if a slice is used).
        """
        if isinstance(key, slice):
            start = key.start or 0
            stop = key.stop or self.header.records
            step = key.step or 1
            if start < 0:
                start += self.header.records + 1
            if stop < 0:
                stop += self.header.records + 1
            if stop < start:
                if step > 0:
                    step = -step
            elif stop > start:
                if step < 0:
                    step = -step    
            else:
                return []
            if stop > self.header.records:
                stop = self.header.records

            return [self.get_record(i) for i in range(start, stop, step)]
        else:
            if -self.header.records > key or key >= self.header.records:
                raise IndexError("Record index out of range")
            if key < 0:
                key += self.header.records 
            return self.get_record(key)

    def __iter__(self):
        """
        Returns an iterator over the records in the database, 
        allowing notation like 'for record in dbf'.
        """
        self.file.seek(self.header.header_size)
        return iter(self.get_record(i) for i in range(self.header.records))
        
    def __str__(self):
        """
        Returns a string with information about the database file.
        """
        lastmodified = datetime.strftime(datetime(1900 + self.header.year, self.header.month, self.header.day), '%Y-%m-%d')
        return f"""
        File version: {self.header.version}
        File name: {self.filename}
        File size; {self.filesize}
        Last Modified: {lastmodified}
        Header Size: {self.header.header_size}
        Record Size: {self.header.record_size}
        Records: {self.header.records}
"""
    
    def _init(self):
        """
        Initializes the database structure by reading the header and fields.
        """
        self.header = DbaseHeader()
        self.header.load_bytes(self.file.read(32))
        self.num_fields = (self.header.header_size - 32) // 32
        self.datasize = self.header.record_size * self.header.records
        for i in range(self.num_fields):
            raw_bytes = self.file.read(32)
            field = DbaseField()
            field.load_bytes(raw_bytes)
            if not field.name:  # Stop if the field name is empty
                break
            self.fields.append(field)
        # assert(self.header.header_size + self.datasize == self.filesize)

    @property
    def field_names(self):
        """
        Returns a list with the name of each field in the database.
        """
        return [field.name.strip() for field in self.fields]
    
    @property
    def field_types(self):
        """
        Returns a list with the type of each field in the database.
        """
        return [field.type for field in self.fields]
    
    @property
    def field_lengths(self):
        """
        Returns a list with the length of each field in the database.
        """
        return [field.length for field in self.fields]
    
    def max_field_length(self, fieldname):
        """
        Returns the maximum length of the specified field (including length of field name) in the database.
        """
        # with self.lock:
        #     records = self[:]
        #     records = filter(lambda r: r is not None, records)
        #     max_record_len = max((len(str(record[fieldname])) for record in records))
        #     return max([len(fieldname), max_record_len])
        field = None
        for f in self.fields:
            if f.name.strip() == fieldname:
                field = f
                break
        if not field:
            return 0
        return max([len(fieldname), field.length])
           
    @property
    def max_field_lengths(self):
        """
        Returns the maximum length of each field (including length of field name) in the database.
        """
        return [self.max_field_length(field) for field in self.field_names]

    @property
    def tmax_field_lengths(self):
        """
        Returns the maximum length of each field (including length of field name) in the database.
        Threaded version.
        """
        res = []
        fields = self.field_names
        with ThreadPool() as pool:
        # with Pool() as pool:
            for result in pool.map(self.max_field_length, fields):
                res.append(result)
        return res

    def commit(self, filename=None):
        """
        Writes the database to a file. 
        If no filename is specified, the original file is overwritten.
        Skips records marked as deleted, thus effectively deleting them, 
        and adjusts the header accordingly.
        """
        numdeleted = 0
        for record in self:
            if record.get('deleted'):
                numdeleted += 1
        file = open('tmp.dbf', 'wb')
        file.write(self.header.to_bytes())
        for field in self.fields:
            file.write(field.to_bytes())
        file.write(b'\x0D')
        for record in self:
            if record['deleted']:    
                # self.file.write(b'*')
                continue
            else:   
                file.write(b' ')
            for field in self.fields:
                ftype = field.type
                if ftype == 'C':
                    file.write(record[field.name].ljust(field.length, ' ').encode('latin1'))
                elif ftype == 'N' or ftype == 'F':
                    file.write(str(record[field.name]).rjust(field.length, ' ').encode('latin1'))   
                elif ftype == 'D':
                    file.write(record[field.name].strftime('%Y%m%d').encode('latin1'))
                elif ftype == 'L':
                    file.write(b'T' if record[field.name] else b'F')
                else:
                    raise ValueError(f"Unknown field type {field.type}")
        # file.write(b'\x1A')
        self.header.records -= numdeleted
        self.filesize -= numdeleted * self.header.record_size
        self.datasize = self.header.record_size * self.header.records
        file.seek(0)
        file.write(self.header.to_bytes())
        file.flush()
        self.file.close()
        if not filename:
            filename = self.filename
            os.remove(filename)
        self.filename = filename
        os.rename('tmp.dbf', self.filename)
        self.file = open(self.filename, 'r+b')
        self.num_fields = 0
        self.fields = []
        self.header = None
        self.datasize = 0
        self. _init()

    # def add_field(self, name, type, length, decimal=0):
    #     if len(self.records) > 0:
    #         raise ValueError("Cannot add field after records")
    #     if len(self.fields) > 0:
    #         address = self.fields[-1].address + self.fields[-1].length
    #     else:
    #         address = 1
    #     field = DbaseField(name, type, address, length, decimal)
    #     self.fields.append(field)
    #     self.header.header_size += 32

    def _test_key(self, key):
        """
        Tests if the key is within the valid range of record indexes.
        Raises an IndexError if the key is out of range.
        Meant for internal use only.
        """
        if 0 > key >= self.header.records:  
            raise IndexError("Record index out of range")

    def add_record(self, *data):
        """
        Adds a new record to the database.

        :param record_data: Dictionary with the new record's data.
        """
        if len(data) != len(self.fields):
            raise ValueError("Wrong number of fields")
        value = b''
        for field, val in zip(self.fields, data):
            ftype = field.type
            if ftype == 'C':
                value += str(val).encode('latin1').ljust(field.length, b' ')
            elif ftype == 'N' or ftype == 'F':
                value += str(val).encode('latin1').rjust(field.length, b' ')
            elif ftype == 'D':
                value += val.strftime('%Y%m%d').encode('latin1')
            elif ftype == 'L':
                value = b'T' if val else b'F'
        self.file.seek(self.filesize)
        self.file.write(b'\x20' + value)
        self.header.records += 1
        self.filesize = self.header.header_size + self.header.record_size * self.header.records
        hoy = datetime.now()
        self.header.year = hoy.year - 1900
        self.header.month = hoy.month
        self.header.day = hoy.day
        self.datasize = self.header.record_size * self.header.records
        self.file.seek(0)
        self.file.write(self.header.to_bytes())        
        self.file.flush()

    def del_record(self, key, value = True):
        """
        Marks a record as deleted.
        To effectively delete the record, use the write() method afterwards.
        """
        self._test_key(key)
        record = self.get_record(key)
        record['deleted'] = value
        self.save_record(key, record)
        self.file.flush()

    def update_record(self, key, record):
        """
        Updates an existing record in the database.

        :param index: Index of the record to update.
        :param record_data: Dictionary with the updated data.
        :raises IndexError: If the record index is out of range.
        """
        self._test_key(key)
        if record.get('deleted'):
            self.commit()
        else:
            self.save_record(key, record)
            self.file.flush()

    def get_record(self, key):
        """
        Retrieves a record (dictionary with field names and field values) from the database.
        Used internally by the __getitem__ method.
        """
        self._test_key(key)
        offset = self.header.header_size + key * self.header.record_size
        self.file.seek(offset)
        rec_bytes = self.file.read(self.header.record_size)
        if len(rec_bytes) != self.header.record_size:
            err_msg = f"Error reading record {key}: expected {self.header.record_size} bytes, got {len(rec_bytes)}"
            os.sys.stderr.write(f"{err_msg}\n")
            os.sys.stderr.flush()
            return None
        to_be_deleted = (rec_bytes[0] == 0x2A)
        rec_bytes = rec_bytes[1:]
        record = Record(deleted=to_be_deleted, metadata=Dict(offset=offset, index=key))
        for field in self.fields:
            fieldtype = field.type
            fieldname = field.name.strip("\0x00").strip()
            fieldcontent = rec_bytes[:field.length].decode('latin1').strip("\x00") .strip()
            fieldcontent = fieldcontent.replace('\x00', ' ')
            if fieldtype == 'C':
                record[fieldname] = fieldcontent
            elif fieldtype == 'N':
                if fieldcontent == '':
                    fieldcontent = 0
                try: 
                    record[fieldname] = int(fieldcontent)
                except ValueError:
                    try:
                        record[fieldname] = float(fieldcontent)
                    except:
                        record[fieldname] = fieldcontent
            elif fieldtype == 'F':
                if fieldcontent == '':
                    fieldcontent = 0
                try:
                    record[fieldname] = float(fieldcontent)
                except:
                    record[fieldname] = fieldcontent
            elif fieldtype == 'D':
                try:
                    record[fieldname] = datetime.strptime(fieldcontent, '%Y%m%d')
                except:
                    record[fieldname] = fieldcontent
            elif fieldtype == 'L':
                record[fieldname] = fieldcontent in ['T', 't', 'Y', 'y']
            else:
                raise ValueError(f"Unknown field type {fieldtype}")
            rec_bytes = rec_bytes[field.length:]
        return record
    
    def get_field(self, fieldname):
        """
        Returns the field object with the specified name, case insensitive.
        """
        for field in self.fields:
            if field.name.strip().lower() == fieldname.strip().lower():
                return field
        return None

    def search(self, fieldname, value, start=0, funcname="", comp_func=None):
        """
        Searches for a record with the specified value in the specified field,
        starting from the specified index, for which the specified comparison function returns True.
        """
        if funcname not in ("find", "index", ""):
            raise ValueError("Invalid function name") 
        field = self.get_field(fieldname)
        if not field:
            raise ValueError(f"Field {fieldname} not found")
        elif fieldname != field.name.strip():
            fieldname = field.name.strip()
        fieldtype = field.type
        if not comp_func:
            if fieldtype == FieldType.CHARACTER.value:
                # comp_func = lambda f, v: f.lower().startswith(v.lower())
                comp_func = self.istartswith
            elif fieldtype == FieldType.NUMERIC.value or fieldtype == FieldType.FLOAT.value:
                comp_func = lambda f, v: f == v 
            elif fieldtype == FieldType.DATE.value:
                comp_func = lambda f, v: f == v
            else:
                raise ValueError(f"Invalid field type {fieldtype} for comparison")
            
        for i, record in enumerate(self[start:]):
            if comp_func(record[fieldname], value):
                if funcname == "":
                    return i + start, record
                elif funcname == "find":
                    return record
                elif funcname == "index":
                    return i + start
        if funcname == "":
            return -1, None
        elif funcname == "find":
            return None
        elif funcname == "index":
            return -1

    def find(self, fieldname, value, start=0, comp_func=None): 
        """
        Wrapper for search() with funcname="find".
        Returns the first record (dictionary) found, or None if no record meeting given criteria is found.
        """ 
        return self.search(fieldname, value, start, "find", comp_func)
    
    def index(self, fieldname, value, start=0, comp_func=None):
        """
        Wrapper for search() with funcname="index".
        Returns index of the first record found, or -1 if no record meeting given criteria is found.
        """ 
        return self.search(fieldname, value, start, "index", comp_func)

    def filter(self, fieldname, value, comp_func=None):
        """
        Returns a list of records (dictionaries) that meet the specified criteria.
        """
        ret = []
        index = -1
        while True:
            index, record = self.search(fieldname, value, index + 1, "", comp_func)  
            if index < 0:
                return ret
            else:    
                ret.append(record)

    def list(self, start=0, stop=None, fieldsep="|", records:list=None):
        """
        Returns a generator, corresponding to the list of records from the database.
        """
        if start is None:
            start = 0
        if stop is None:
            stop = self.header.records
        l = records or [self.get_record(i) for i in range(start, stop)]
        # return recordsep.join(fieldsep.join(str(record[field.name]) for field in self.fields) for record in l)
        return (fieldsep.join(str(record[field.name]) for field in self.fields) for record in l)
    
    def csv(self, start=0, stop=None, records:list = None):
        """
        Returns a generator of CSV strings, each one with the CSV repr o a record in the database.
        """
        return self.list(start, stop, ",", records)
    
    @property
    def csv_headers_line(self):
        """
        Returns a CSV string with the field names.
        """
        return ",".join(self.field_names)
    
    def table(self, start=0, stop=None, records:list = None):
        """
        Returns a table string with the records in the database, sqlite3 style.
        """
        def _format_field(field, record):
            if field.type == FieldType.CHARACTER.value:
                return record.get(field.name).ljust(field.length + 2)
            else: 
                return str(record.get(field.name)).rjust(field.length + 2)
            
        if start is None:
            start = 0
        if stop is None:
            stop = self.header.records
        l = records or [self.get_record(i) for i in range(start, stop)]
        line_bracket = "+"
        line_divider = line_bracket + line_bracket.join("-" * (field.length + 2) for field in self.fields) + line_bracket + "\n"
        header_line = "|" + "|".join(field.name.center(field.length + 2) for field in self.fields) + "|" + "\n"
        record_lines =  ('\n' + line_divider).join("|" + "|".join(_format_field(field, record) for field in self.fields) + "|" for record in l)
        return line_divider + header_line + line_divider + record_lines + "\n" + line_divider

    def pretty_table(self, start=0, stop=None, records:list = None):
        """
        Returns a  string representing records in the database.
        """

        def _format_field(field, record):
            if field.type == FieldType.CHARACTER.value:
                return record.get(field.name).ljust(field.length + 2)
            else: 
                return str(record.get(field.name)).rjust(field.length + 2)
            
        if start is None:
            start = 0
        if stop is None:
            stop = self.header.records
        l = records or [self.get_record(i) for i in range(start, stop)]
        top_line = BoxType.UP_L.value + BoxType.T_DOWN.value.join(BoxType.HORZ.value * (field.length + 2) for field in self.fields) + BoxType.UP_R.value + "\n"
        line_divider = BoxType.T_L.value + BoxType.CROSS.value.join(BoxType.HORZ.value * (field.length + 2) for field in self.fields) + BoxType.T_R.value       
        header_line = BoxType.VERT.value + BoxType.VERT.value.join(field.name.center(field.length + 2) for field in self.fields) + BoxType.VERT.value + "\n"
        bot_line = BoxType.DOWN_L.value + BoxType.T_UP.value.join(BoxType.HORZ.value * (field.length + 2) for field in self.fields) + BoxType.DOWN_R.value + "\n" 
        # record_lines =  ('\n' + line_divider).join(BoxType.VERT.value + BoxType.VERT.value.join(_format_field(field, record) for field in self.fields) + BoxType.VERT.value for record in l)
        # return top_line + header_line + line_divider + record_lines + "\n" + bot_line
        yield top_line + header_line + line_divider
        for record in l[:-1]:
            yield BoxType.VERT.value + BoxType.VERT.value.join(_format_field(field, record) for field in self.fields) + BoxType.VERT.value + "\n" + line_divider
        yield BoxType.VERT.value + BoxType.VERT.value.join(_format_field(field, l[-1]) for field in self.fields) + BoxType.VERT.value + "\n" + bot_line

    def line(self, index, fieldsep="", names_lengths:list=None):
        """
        Returns a string with the record at the specified index, with fields right aligned to max field lengths.
        """
        record = self.get_record(index)
        names_lengths = names_lengths or zip(self.field_names, self.max_field_lengths)
        # names_lengths = names_lengths or zip(self.field_names, self.field_lengths)
        afields = [f"{str(record.get(name)).rjust(length).ljust(length+1)}" for name, length in names_lengths]
        return fieldsep.join(afields)
    
    def lines(self, start=0, stop=None, fieldsep=""):
        """
        Returns a generator which resolves to an array of strings, each one with 
        with the records in the specified range, with fields right aligned to max field lengths.
        """
        if start is None:
            start = 0
        if stop is None:
            stop = self.header.records
        names_lengths = list(zip(self.field_names, self.max_field_lengths))
        # names_lengths = list(zip(self.field_names, self.field_lengths))
        # return recordsep.join([self.line(i, fieldsep, names_lengths=names_lengths)
        #                         for i in range(start, stop)])
        return (self.line(i, fieldsep, names_lengths=names_lengths) for i in range(start, stop)) 
       
    def headers_line(self, fieldsep=""):
        """
        Returns a string containing the field names right aligned to max field lengths.
        """
        names_lengths = zip(self.field_names, self.max_field_lengths)
        # names_lengths = zip(self.field_names, self.field_lengths)
        afields = [f"{name.rjust(length).ljust(length+1)}" for name, length in names_lengths]
        return fieldsep.join(afields)
    
    def save_record(self, key, record):
        """
        Writes a record (dictionary with field names and field values) to the database
        at the specified index.
        """
        self._test_key(key)
        self.file.seek(self.header.header_size + key * self.header.record_size)
        if record.get('deleted'):
            self.file.write(b'*')
        else:
            self.file.write(b' ')
        for field in self.fields:
            ftype = field.type
            if ftype == 'C':
                self.file.write(record[field.name].ljust(field.length, ' ').encode('latin1'))
            elif ftype == 'N' or ftype == 'F':
                self.file.write(str(record[field.name]).rjust(field.length, ' ').encode('latin1'))
            elif ftype == 'D':
                self.file.write(record[field.name].strftime('%Y%m%d').encode('latin1'))
            elif ftype == 'L':
                self.file.write(b'\x01' if record[field.name] else b'\x00')
            else:
                raise ValueError(f"Unknown field type {field.type}")
        self.file.flush()

    def exec(self, sql_cmd: str):
        """
        Executes a SQL command on the database.
        """
        raise NotImplementedError("SQL commands are not supported as yet.")



if __name__ == '__main__':
    from test import testdb
    testdb()
    print("Done!")
    
