#-*- coding: utf_8 -*-
"""
pybase3

This module provides a class to manipulate DBase III database files.
It allows reading, writing, adding, updating and deleting records in the database.
Includes classes Connection and Cursor to interact with the database in a Python DB-API 2.0 compliant way. 

Classes:
    DbaseFile (Main class)
    DbaseHeader
    DbaseField
    Record
    FieldType
    SQLParser 
        (Additional class for SQL queries. 
         It stands alone and can be used independently of the DBaseFile class.
         It's used internally by the DBaseFile class to parse SQL queries.
         Resides in its own module, sqlparser.py)
    Connection
    Cursor

Functions:
    connect(filename: str) -> Connection
    make_raw_lines(curr: Cursor)-> Generator[str, None, None]
    make_list_lines(curr: Cursor)-> Generator[str, None, None]
    make_csv_lines(curr: Cursor)-> Generator[str, None, None]
    make_table_lines(curr: Cursor)->Generator[str, None, None]
    make_pretty_table_lines(curr: Cursor)-> Generator[str, None, None]

CLI scripts:
    dbfview: (dbfview.py) A simple command line utility to view DBase III files.
    dbfquery: (dbfquery.py) A simple command line utility to query/update DBase III 
               files using SQL commands.
    dbfheader: (header_reader.py) A simple command line utility to read the header
    test: (test.py) A simple command line utility to test the library.
"""

# Title: dBase III File Reader and Writer

# Description:
__version__ = "1.98.13"
__author__ = "Domingo fE. Savoretti"
__email__ = "esavoretti@gmail.com"
__license__ = "MIT"
__url__ = "https://github.com/sandy98/pybase3"
__description__ = "A simple library to read and write dbase III files."

# Import the necessary modules.
import struct, os, pickle, sqlite3, re, subprocess, shlex
# from mmap import mmap as memmap, ACCESS_WRITE
from enum import Enum
from typing import List, Tuple, Generator, AnyStr, Any, Callable
from dataclasses import dataclass, field #, fields, field, is_dataclass
from datetime import datetime
from threading import Thread, Lock
from multiprocessing.pool import ThreadPool
# from multiprocessing import Pool
# from multiprocessing import Lock

try:
    # Import from the package
    from pybase3.utils import SmartDict, coerce_number
    from pybase3.sqlparser import SQLParser
except ImportError:
    # Import from the local module
    from utils import SmartDict, coerce_number
    from sqlparser import SQLParser

to_bytes = lambda x: x.encode('latin1') if type(x) == str else x
to_str = lambda x: x.decode('latin1') if type(x) == bytes else x

# getYear = lambda: datetime.now().year - 1900
getYear = lambda: datetime.now().year - 2000
getMonth = lambda: datetime.now().month
getDay = lambda: datetime.now().day

class Record(SmartDict):
    """

    Class to represent a record in a DBase III database.
    Inherits from SmartDict, a dictionary with dot notation access to keys.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.deleted = False

    @property
    def datafields(self):
        return [k for k in self.keys() if k not in ['deleted', 'metadata']]

    @property
    def to_datafields(self):
        return SmartDict({k: self[k] for k in self.datafields})
    
    def __repr__(self):
        return "\n".join(f"{k}: {v}" for k, v in self.items())

    def __str__(self):
        return self.__repr__() + "\n"


class FieldType(Enum):
    """Enum for dBase III field types."""

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
    """Enum for box drawing characters."""

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
    """Class to represent the header of a DBase III database file."""

    version: int = 3 # 1 byte
    year: int = getYear() # 1 byte
    month: int = getMonth() # 1 byte
    day: int = getDay() # 1 byte
    records: int = 0 # 4 bytes
    header_size: int = 0 # 2 bytes
    record_size: int = 0 # 2 bytes
    reserved: bytes = b'\x00' * 20

    def load_bytes(self, bytes):
        """Transforms a byte string (usually read from disk) into a DbaseHeader object."""
        (self.version, self.year, self.month, self.day, 
         self.records, self.header_size, self.record_size, 
         self.reserved) = struct.unpack('<BBBBLHH20s', bytes)
 
    def to_bytes(self):
        """Transforms a DbaseHeader object into a byte string (usually to write to disk)."""
        return struct.pack('<BBBBLHH20s', self.version, self.year, self.month, self.day, 
                           self.records, self.header_size, self.record_size, 
                           self.reserved)
    
    def __post_init__(self):
        """Validates the header fields."""
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
    """Class to represent a field (aka column) in a DBase III database file."""

    name: str = '\x00' * 11  # Field name, 11 bytes
    type: str = 'C'  # Field type (C, N, etc.), 1 byte
    address: int = 0  # 1st reserved, 4 bytes
    length: int = 0  # Field length (maximun 254), 1 byte 
    decimal: int = 0  # Decimal places for numeric fields, 1 byte
    reserved: bytes = b'\x00' * 14  #  14 reserved bytes

    def __post_init__(self):
        """Validates the field attributes."""

        self._alias = self.name

    @property
    def alias(self):
        """
        Returns the field alias, if set, or the field name otherwise.
        The alias is used in SQL queries to refer to the field.
        For example: 'select fieldname as aliasname from tablename'
        """

        return self._alias if self._alias != ('\x00' * 11) else self.name
    
    @alias.setter
    def alias(self, value):
        self._alias = value

    @alias.deleter
    def alias(self):
        self._alias = '\x00' * 11

    def load_bytes(self, bytes):
        """Transforms a byte string (usually read from disk) into a DbaseField object."""

        # Extract the name as exactly 11 bytes
        raw_name = bytes[:11].rstrip(b'\x00').strip()  # Strip null terminators
        self.name = raw_name.decode('latin1')
        # Extract the type and other attributes
        self.type = chr(bytes[11])  # Field type is the next byte
        (self.address, self.length, self.decimal, self.reserved) = struct.unpack('<IBB14s', bytes[12:])
        
    def to_bytes(self):
        """Transforms a DbaseField object into a byte string (usually to write to disk)."""

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
        create(filename: str, fields: List[Tuple[str, str, int, int]]) -> DbaseFile
        import_from(filename:str, tablename:str=None, stype:str='sqlite3', exportname:str=None) -> DbaseFile
        export_to(desttype:str='sqlite3', filename:str=None) -> bool
        __init__(filename: str)
        __del__()
        __len__() -> int
        __getitem__(key) -> Record
        __iter__() -> Generator[Record, None, None]
        __str__() -> str
        _init()
        _load_mdx()
        _save_mdx()
        schema() -> str
        fields_info() -> str
        field_names() -> List[str]
        field_alias() -> List[str]
        field_types() -> List[str]
        field_lengths() -> List[int]
        max_field_length(fieldname: str) -> int
        max_field_lengths() -> List[int]
        tmax_field_lengths() -> List[int]
        commit(filename:str=None) -> Tuple[bool, int]
        pack(filename:str=None) -> Tuple[bool, int]
        add_record(*data)
        del_record(key, value=True)
        update_record(key, record)
        get_record(key) -> Record
        get_field(fieldname) -> DbaseField
        search(fieldname, value, start=0, funcname="", compare_function=None)
        update_mdx()
    """

    import_types = ['sqlite3', 'sqlite', 'csv']
    export_types = ['sqlite3', 'sqlite', 'csv']

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
    def create(cls, filename: str, fields: List[Tuple[str, str, int, int]]) :
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
            file.write(b'\x1A')
        dbf = cls(filename)
        return dbf

    @classmethod
    def import_from(cls, filename:str, tablename:str=None, stype:str='sqlite3', exportname:str=None):
        """
        Imports a database from a source of the specified type.
        """

        if '.' in filename:
            srctype = filename.split('.')[-1]
        else:
            srctype = stype
        if srctype not in cls.import_types:
            raise ValueError(f"Invalid source type {srctype}")
        if not tablename:
            tablename = os.path.basename(filename).split('.')[0]

        if srctype.startswith('sqlite'):
            # raise NotImplementedError("SQLite import not implemented yet")
            if not os.path.exists(filename):
                raise FileNotFoundError(f"File {filename} not found")
            conn = sqlite3.Connection(filename)
            curr = conn.execute(f"SELECT * FROM sqlite_master WHERE type='table' AND name='{tablename}';")
            if not curr.fetchone():
                raise ValueError(f"Table {tablename} not found")
            curr = conn.execute(f"PRAGMA table_info({tablename});")
            fields = []
            for row in curr.fetchall():
                fields.append([row[1], row[2], 0, 0])
            for field in fields:
                if field[1].startswith('TEXT'):
                    field[1] = 'C'
                    field[2] = 50
                    field[3] = 0
                elif field[1].startswith('INT'):
                    field[1] = 'N'
                    field[2] = 8
                    field[3] = 0
                elif field[1].startswith('REAL'):
                    field[1] = 'F'
                    field[2] = 8
                    field[3] = 2
                elif field[1].startswith('BOOL'):
                    field[1] = 'L'
                    field[2] = 1
                    field[3] = 0
                else:
                    field[1] = 'C'
                    field[2] = 50
                    field[3] = 0

            dbfname = exportname or filename.replace('sqlite', 'dbf')
            dbf = cls.create(dbfname, fields)
            curr = conn.execute(f"SELECT * FROM {tablename};")
            for row in curr.fetchall():
                dbf.add_record(*row)
            return dbf

        elif srctype == 'csv':
            # raise NotImplementedError("CSV import not implemented yet")
            if not os.path.exists(filename):
                raise FileNotFoundError(f"File {filename} not found")
            with open(filename, 'r') as file:
                header = file.readline().strip()
                fields = header.split(',')
                firstline = file.readline().strip()
                if not firstline:
                    raise ValueError("No records found")
                else:
                    values = firstline.split(',')
                    if len(values) != len(fields):
                        raise ValueError("Inconsistent number of fields and values")
                    dbFields: List[Tuple[str,str, int, int]] = []
                    for header, value in zip(fields, values):
                        if value.isdigit():
                            ftype = 'N'
                        elif value.replace('.', '', 1).isdigit():
                            ftype = 'F'
                        elif value in ['T', 'F']:
                            ftype = 'L'
                        else:
                            ftype = 'C'
                        if ftype == 'N':
                            dbFields.append((header, ftype, 8, 0))
                        elif ftype == 'F':
                            dbFields.append((header, ftype, 8, 2))
                        elif ftype == 'L': 
                            dbFields.append((header, ftype, 1, 0))
                        else:
                            dbFields.append((header, ftype, len(value) * 3, 0))
                dbfname = exportname or filename.replace('csv', 'dbf')
                dbf = cls.create(dbfname, dbFields)
                dbf.add_record(*values)
                for line in file.readlines():
                    values = line.strip().split(',')
                    dbf.add_record(*values)
                return dbf
            return False
        
    def export_to(self, desttype:str='sqlite3', filename:str=None):
        """
        Exports the database to a destination of the specified type.
        """

        if desttype not in self.export_types:
            raise ValueError(f"Invalid destination type {desttype}")
        if desttype.startswith('sqlite'):
            # raise NotImplementedError("SQLite export not implemented yet")
            if not filename:
                filename = self.filename.replace('dbf', 'sqlite')
            conn = sqlite3.Connection(filename)
            conn.execute(self.schema)
            for record in self:
                rec = SmartDict([(k, record[k]) for k in record.datafields])
                fieldslist = ','.join(rec.keys())
                placeholders = ','.join('?' * len(rec))
                values = tuple(rec.values())
                sql = f"INSERT INTO {self.tablename} ({fieldslist}) VALUES ({placeholders});"                
                conn.execute(sql, values)
            conn.commit()
            return True
        elif desttype == 'csv':
            # raise NotImplementedError("CSV export not implemented yet")
            header_line = self.csv_headers_line
            fname = filename or self.filename.replace('dbf', 'csv')
            with open(fname, 'w') as file:
                file.write(header_line + "\n")
                for line in self.csv():
                    file.write(line + "\n")
                return True

    def __init__(self, filename):
        """
        Initializes an instance of DBase3.

        :param filename: Name of the database file.
        """

        self.lock = Lock()
        self.filename = filename
        self.filesize = os.path.getsize(filename)
        self.file = open(filename, 'r+b')

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
        Returns a single record (dictionary with field names and field values) 
        from the database or a list of them (if a slice is used).
        
        :param key: Index of the record to retrieve, or a slice.
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
        
        self.num_fields = 0
        self.fields = []
        self.header = None
        self.datasize = 0
        self.indexes = {}
        self.indexhits = 0
        self.tablename = os.path.basename(self.filename).split('.')[0]
        self.header = DbaseHeader()
        self.file.seek(0)
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
        try:
            assert((self.header.header_size + self.datasize + 1) == self.filesize)
        except AssertionError:
            try:
                assert((self.header.header_size + self.datasize) == self.filesize)
            except AssertionError:
                # raise ValueError(f"File size mismatch: expected {self.header.header_size + self.datasize + 1}, got {self.filesize}")
                os.sys.stderr.write(f"File size mismatch: expected {self.header.header_size + self.datasize + 1}, got {self.filesize}\n")
                os.sys.stderr.flush()
        self._load_mdx()

    def _load_mdx(self):
        """
        Loads the MDX (.pmdx) index file, if it exists.
        """

        mdxfile = self.filename.replace('.dbf', '.pmdx')
        if os.path.exists(mdxfile):
            with open(mdxfile, 'rb') as file:
                self.indexes = pickle.load(file)

    def _save_mdx(self):
        """
        Saves the MDX index file (dbfname.pmdx).
        """

        mdxfile = self.filename.replace('.dbf', '.pmdx')
        with open(mdxfile, 'wb') as file:
            pickle.dump(self.indexes, file)

    @property
    def schema(self):
        """
        Returns a string with the schema of the database.
        """

        prefix = f"""
        CREATE TABLE IF NOT EXISTS {self.tablename} (
"""
        suffix = f"""
        );
        """
        fields = []
        for field in self.fields:
            if field.type == 'C':
                fields.append(f"    {field.name} TEXT")
            elif field.type == 'N':
                fields.append(f"    {field.name} INTEGER")
            elif field.type == 'F':
                fields.append(f"    {field.name} REAL")
            elif field.type == 'D':
                fields.append(f"    {field.name} DATE")
            elif field.type == 'L':
                fields.append(f"    {field.name} INTEGER")

        return prefix + ",\n".join(fields) + suffix

    @property
    def fields_info(self) :
        """
        Returns a string with information about the fields in the database.
        """

        return "\n".join(f"{field.name} ({field.type}): {field.length}" for field in self.fields)

    @property
    def field_names(self) -> List[str]:
        """
        Returns a list with the name of each field in the database.
        """

        return [field.name.strip() for field in self.fields]
    
    @property
    def field_alias(self) -> List[str]:
        """
        Returns a list with the name of each field in the database.
        """

        return [field.alias.strip() for field in self.fields]
    
    @property
    def field_types(self) -> List[str]:
        """
        Returns a list with the type of each field in the database.
        """

        return [field.type for field in self.fields]
    
    @property
    def field_lengths(self) -> List[int]:
        """
        Returns a list with the length of each field in the database.
        """

        return [field.length for field in self.fields]
    
    def max_field_length(self, fieldname):
        """
        Returns the maximum length of the specified field (including length of field name) in the database.
        """

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
        file.write(b'\x1A')
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
    
        self. _init()
        self.update_mdx() 
        return True, self.header.records  

    def pack(self, filename=None):
        """Same as commit(). Included for compatibility with long lost dBase past."""

        return self.commit(filename)
    
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

        :param record_data: SmartDictionary with the new record's data.
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
        self.file.seek(self.filesize - 1)
        self.file.write(b'\x20' + value + b'\x1A')
        self.header.records += 1
        self.filesize = self.header.header_size + self.header.record_size * self.header.records + 1
        hoy = datetime.now()
        self.header.year = hoy.year - (2000 if hoy.year > 2000 else 1900)
        self.header.month = hoy.month
        self.header.day = hoy.day
        self.datasize = self.header.record_size * self.header.records
        self.file.seek(0)
        self.file.write(self.header.to_bytes())        
        self.file.flush()
        self.update_mdx()

    def del_record(self, key, value = True):
        """
        Marks a record as deleted.
        To effectively delete the record, use the commit() method afterwards.
        """

        self._test_key(key)
        record = self.get_record(key)
        record['deleted'] = value
        self.save_record(key, record)
        self.file.flush()
        self.update_mdx()

    def update_record(self, key, record):
        """
        Updates an existing record in the database.

        :param index: Index of the record to update.
        :param record_data: SmartDictionary with the updated data.
        :raises IndexError: If the record index is out of range.
        """

        self._test_key(key)
        if record.get('deleted'):
            self.commit()
        else:
            self.save_record(key, record)
            self.file.flush()
            self.update_mdx()

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
        record = Record(deleted=to_be_deleted, metadata=SmartDict(offset=offset, index=key))
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
        Returns the field object with the specified name, case sensitive.
        """

        cond_true = lambda f: (
            f.name.strip() == fieldname.strip()
            or f.alias.strip() == fieldname.strip()
            )
        if isinstance(fieldname, DbaseField):
            return fieldname
        for field in self.fields:
            if cond_true(field):
                return field
        return None

    def search(self, fieldname, value, start=0, funcname="", compare_function=None):
        """
        Searches for a record with the specified value in the specified field,
        starting from the specified index, for which the specified comparison function returns True.
        It will try to use the field index if available.
        """

        for i, alias in enumerate(self.field_alias):
            if alias == fieldname:
                fieldname = self.fields[i].name

        if fieldname in self.indexes:
            return self._indexed_search(fieldname, value, start, funcname, compare_function)
        
        if funcname not in ("find", "index", ""):
            raise ValueError("Invalid function name")
        if not fieldname:
            if compare_function:
                result = compare_function(fieldname, value)
            else:
                result = True
            if not result:
                if funcname == "":
                    return -1, None
                elif funcname == "find":
                    return None
                elif funcname == "index":
                    return -1
            else:
                if funcname == "":
                    return start, self.get_record(start)
                elif funcname == "find":
                    return self.get_record(start)
                elif funcname == "index":    
                    return start

        field = self.get_field(fieldname)
        if not field:
            raise ValueError(f"Field {fieldname} not found")
        elif fieldname != field.name.strip():
            fieldname = field.name.strip()
        fieldtype = field.type
        if not compare_function:
            if fieldtype == FieldType.CHARACTER.value:
                # compare_function = lambda f, v: f.lower().startswith(v.lower())
                compare_function = self.istartswith
            elif fieldtype == FieldType.NUMERIC.value or fieldtype == FieldType.FLOAT.value:
                compare_function = lambda f, v: f == v 
            elif fieldtype == FieldType.DATE.value:
                compare_function = lambda f, v: f == v
            else:
                raise ValueError(f"Invalid field type {fieldtype} for comparison")
            
        for i, record in enumerate(self[start:]):
            if compare_function(record[fieldname], value):
                if funcname not in ("find", "index"):
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

    def _indexed_search(self, fieldname, value, start=0, funcname="", compare_function=None):
        """
        Searches for a record with the specified value in the specified field,
        starting from the specified index, for which the specified comparison function returns True,
        using the field index.
        """

        if fieldname not in self.indexes:
            raise ValueError(f"Index {fieldname} not found.")

        if not compare_function:
            compare_function = (self.istartswith if self.get_field(fieldname).type == FieldType.CHARACTER.value 
                         else lambda f, v: f == v)        
        record = None
        entry = self.indexes[fieldname]
        candidates = []
        for k in entry.keys():
            if compare_function(k, value):
                candidates.extend(entry[k])
        for index in candidates:
            if index >= start:
                record = self.get_record(index)
                break
        if record:
            self.indexhits += 1
            if funcname not in ("find", "index"):
                return index, record
            elif funcname == "find":    
                return record
            elif funcname == "index":
                return index    
        else:
            if funcname not in ("find", "index"):
                return -1, None
            elif funcname == "find":
                return None
            elif funcname == "index":
                return -1

    def find(self, fieldname, value, start=0, compare_function=None): 
        """
        Wrapper for search() with funcname="find".
        Returns the first record (dictionary) found, or None if no record meeting given criteria is found.
        """ 

        return self.search(fieldname, value, start, "find", compare_function)
    
    def index(self, fieldname, value, start=0, compare_function=None):
        """
        Wrapper for search() with funcname="index".
        Returns index of the first record found, or -1 if no record meeting given criteria is found.
        """ 

        return self.search(fieldname, value, start, "index", compare_function)

    def filter(self, fieldname, value, compare_function=None):
        """
        Returns a list of records (dictionaries) that meet the specified criteria.
        """

        ret = []
        index = -1
        while True:
            index += 1
            if index >= self.header.records:
                return ret
            index, record = self.search(fieldname, value, index, "", compare_function)  
            if index < 0 or index >= self.header.records:
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
        l = records or (self.get_record(i) for i in range(start, stop))
        # return recordsep.join(fieldsep.join(str(record[field.name]) for field in self.fields) for record in l)
        # return (fieldsep.join(str(record[field.name]) for field in self.fields) for record in l)
        return (fieldsep.join(str(record[fieldname] or '') for fieldname in record.datafields) for record in l)
    
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

        return ",".join(field_name for field_name in self.field_names)

    @staticmethod
    def _format_field(field, record):
        """
        Returns a string with the field value aligned to the field length.
        If the field is a character field, it is left aligned, otherwise it is right aligned.
        """

        if field.type == FieldType.CHARACTER.value:
            return str(record.get(field.name) or record.get(field.alias) or '').ljust(field.length + 2)
        else: 
            return str(record.get(field.name) or '').rjust(field.length + 2)
    
    def table(self, start=0, stop=None, records:list = None):
        """
        Returns a  generator yielding a string for each line representing a record in the database, 
        wrapped in sqlite3 style (.mode table) lines.
        """

        if start is None:
            start = 0
        if stop is None:
            stop = self.header.records
        l = records or [self.get_record(i) for i in range(start, stop)]
        line_bracket = "+"
        line_divider = line_bracket + line_bracket.join("-" * (field.length + 2) for field in self.fields) + line_bracket
        header_line = "|" + "|".join(field.name.center(field.length + 2) for field in self.fields) + "|" + "\n"
        # record_lines =  ('\n' + line_divider).join("|" + "|".join(_format_field(field, record) for field in self.fields) + "|" for record in l)
        # return line_divider + header_line + line_divider + record_lines + "\n" + line_divider
        yield line_divider + '\n' + header_line + line_divider
        for record in l[:]:
            yield "|" + "|".join(self._format_field(field, record) for field in self.fields) + "|" + "\n" + line_divider

    def pretty_table(self, start=0, stop=None, records:list = None) -> Generator[str, None, None]:
        """
        Returns a  generator yielding a string for each line representing a record in the database, 
        wrapped in cute lines.
        """

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
            yield BoxType.VERT.value + BoxType.VERT.value.join(self._format_field(field, record) for field in self.fields) + BoxType.VERT.value + "\n" + line_divider
        yield BoxType.VERT.value + BoxType.VERT.value.join(self._format_field(field, l[-1]) for field in self.fields) + BoxType.VERT.value + "\n" + bot_line

    def line(self, record, fieldsep="", names_lengths:list=None):
        """
        Returns a string with the record at the specified index, with fields right aligned to max field lengths.
        """

        #record = self.get_record(index)
        names_lengths = names_lengths or zip(self.field_names, self.max_field_lengths)
        # names_lengths = names_lengths or zip(self.field_names, self.field_lengths)
        afields = [f"{(str(record.get(name)) if record.get(name) is not None else '').rjust(length).ljust(length+1)}" for name, length in names_lengths]
        return fieldsep.join(afields)
    
    def lines(self, start=0, stop=None, fieldsep="", records:list=None):
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
        records = records or self[start:stop]
        return (self.line(r, fieldsep, names_lengths=names_lengths) for r in records) 
       
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

    def transform(self, record:Record, fields:List[DbaseField]):
        """
        Returns a record with the specified fields, usually with
        fields 'deleted' and 'metadata' stripped.
        """

        ret = Record()
        for field in [self.get_field(f) for f in fields]:
            # ret[fields[field]] = record.get(field.name)
            ret[field.alias] = record.get(field.name) or record.get(field.alias)
        return ret

    def as_cursor(self, records:List[Record]=None, fields:List[DbaseField]=None,
                  start:int=0, stop:int=None, step:int=1):
        """
        Returns a cursor object for the database.
        """

        if not fields:
            fields = self.fields
        else:
            fields = [self.get_field(field) for field in fields]
        if not records:
            records = self[start:stop:step]

        description = [(i, field.alias, field.name, field.type, 
                        field.length, field.decimal) for i, field in enumerate(fields)]
        records = (self.transform(r, fields) for r in records)
        return Cursor(description, records)

    def parse_conditions(self, wherestr: str) -> List[Tuple[str, Any, Callable]]:
        """
        Parses the WHERE clause of a SQL statement and returns a list of tuples
        with the field name, the value to compare and the comparison function.
        """

        if not wherestr:
            return [(self.field_names[0], 0 if self.field_types[0] in ['N', 'F'] else '', lambda f, v: True)]

        operator_map = {
            "=": "==",
            "!=": "!=",
            "<": "<",
            ">": ">",
            "<=": "<=",
            ">=": ">="
        }
        conditions = re.split(r'\s+(AND|OR)\s+', wherestr, 0, re.IGNORECASE)
        # Just for now will only parse first condition
        condition = conditions[0]
        match = re.match(r"(\w+)\s*(=|<=|>=|<|>|!=|LIKE)\s*'?([^']*)'?", condition, 
                         re.IGNORECASE)
        if not match:
            raise ValueError("Invalid WHERE clause format")
        lhs, operator, rhs = match.groups()
        if operator == 'LIKE' or operator == 'like':
            if rhs[0] == '%' and rhs[-1] == '%':
                operator = 'in'
                rhs = rhs[1:-1]
                # lhs, rhs = rhs, lhs
            elif rhs[0] == '%':
                operator = 'endswith'
                rhs = rhs[1:]
            elif rhs[-1] == '%':
                operator = 'startswith'
                rhs = rhs[:-1]
            else:
                operator = 'in'
                # lhs, rhs = rhs, lhs
        else:
            if operator not in operator_map:
                raise ValueError(f"Invalid operator {operator}")
            operator = operator_map[operator]

        if rhs.isdigit():
            rhs = coerce_number(rhs)
        if operator == 'in':
            lambdasrc = f"lambda f, v: f.find(v) >= 0"
        elif operator == 'startswith':
            lambdasrc = f"lambda f, v: f.startswith(v)" 
        elif operator == 'endswith':
            lambdasrc = f"lambda f, v: f.endswith(v)"
        else:
            lambdasrc = f"lambda f, v: f {operator} v"
        searchfunc = eval(lambdasrc)
        return [(lhs, rhs, searchfunc)]

    def _execute_select(self, sql_parser: SQLParser, args=[]):
        """
        Receives a parsed SQL SELECT command and returns a Cursor object with the results.

        :param sql_parser: SQLParser object with the parsed SQL command.
        :returns Cursor object with the results of the SELECT command.
        """

        fieldobjs = {}
        parsed = sql_parser.parsed

        columns = parsed['columns']
        for field in columns:
            if field['column'] == '*':
                fieldobjs = {**fieldobjs, **{name: name for name in self.field_names}}
                break
            if field['column'] not in self.field_names:
                raise ValueError(f"Field {field['column']} not found")
            fieldobjs = {**fieldobjs, **{field['column']: field['alias']}}
        selectedfields = []
        for field in fieldobjs:
            f = self.get_field(field)
            f.alias = fieldobjs[field]
            selectedfields.append(f)
        
        field_param, value_param, compare_function = self.parse_conditions(parsed['where'])[0]
        filteredrecords = self.filter(field_param, value_param, 
                                      compare_function=compare_function)
        if parsed.get('order'):
            orderdata = shlex.split(parsed['order'])
            ordersrc = orderdata[0]
            reverse = orderdata[-1].lower() == 'desc'
            filteredrecords = sorted(filteredrecords, key=lambda r: r[ordersrc], reverse=reverse)

        recordslen = len(filteredrecords)
        records = self.fields_view(fields=selectedfields, records=filteredrecords)
        cursor = Cursor(description=[(i, f.alias, f.name, f.type, f.length, f.decimal) 
                                     for i, f in enumerate(selectedfields)], 
                                     records=records)
        cursor.rowsaffected = recordslen
        return cursor

    def _execute_update(self, sql_parser: SQLParser, args=[]):
        """
        Receives a parsed SQL UPDATE command and returns a Cursor object with the results.
        
        :param sql_parser: SQLParser object with the parsed SQL command.
        :returns Cursor object with the results of the UPDATE command.
        """

        parsed = sql_parser.parsed
        field_param, value_param, compare_function = self.parse_conditions(parsed['where'])[0]
        filteredrecords = self.filter(field_param, value_param, compare_function=compare_function)

        numupdated = len(filteredrecords)
        # pairs = [re.split(r"\s*,\s*", pair) for pair in parsed['updates']]
        pairs = parsed['updates']
        dict_update = {}
        for pair in pairs:
            key, value = re.split(r"\s*=\s*", pair)
            dict_update[key] = value

        for record in filteredrecords:
            for k, v in dict_update.items():
                record[k] = coerce_number(v.strip().strip("'"))
            self.save_record(record.metadata.index, record)
        self.commit()
        cursor = Cursor(description=[(0, 'records', 'records', 'N', 10, 0)], records=(n for n in [numupdated]))
        cursor.rowsaffected = numupdated
        return cursor
    
    def _execute_delete(self, sql_parser: SQLParser, args=[]):
        """
        Receives a parsed SQL DELETE command and returns a Cursor object with the results.
        
        :param sql_parser: SQLParser object with the parsed SQL command.
        :returns Cursor object with the results of the DELETE command.
        """

        parsed = sql_parser.parsed
        field_param, value_param, compare_function = self.parse_conditions(parsed['where'])[0]
        filteredrecords = self.filter(field_param, value_param, 
                                      compare_function=compare_function)
        numdeleted = len(filteredrecords)
        for record in filteredrecords:
            record['deleted'] = True
            self.save_record(record.metadata.index, record)
        self.commit()
        cursor = Cursor(description=[(0, 'records', 'records', 'N', 10, 0)], records=(n for n in [numdeleted]))
        cursor.rowsaffected = numdeleted
        return cursor
    
    def _execute_insert(self, sql_parser: SQLParser, args=[]):
        """
        Receives a parsed SQL INSERT command and returns a Cursor object with the results.

        :param sql_parser: SQLParser object with the parsed SQL command.
        :returns Cursor object with the results of the INSERT command.
        """

        # print(f"Inserting {sql_parser._values}")
        parsed = sql_parser.parsed
        # values = [coerce_number(v.strip().strip("'")) for v in sql_parser._values.split(",")]
        values = [coerce_number(v.strip().strip("'")) for v in parsed.get('values')]
        if len(values) != len(self.fields):
            raise ValueError(f"Wrong number of fields: expected {len(self.fields)}, got {len(values)}") 
        if values[0] == '?':
            if not len(args):
                raise ValueError("No values specified. When using '?' in the SQL command, values must be passed as arguments.")
            real_values = [coerce_number(v) for v in args]
            if len(real_values) != len(self.fields):
                raise ValueError(f"Wrong number of fields: expected {len(self.fields)}, got {len(real_values)}") 
            values = real_values               
        self.add_record(*values)
        cursor = Cursor(description=[(0, 'records', 'records', 'N', 10, 0)], records=(n for n in [1]))
        cursor.rowsaffected = 1
        return cursor
    
    def execute(self, sql_cmd: str, args=[]):
        """
        Executes a SQL command on the database.
        
        :param sql_cmd: SQL command to execute
        :param args: List of arguments to be passed to the SQL command.
        :returns Cursor object with the results of the SQL command.
        """

        sql_parser = SQLParser(sql_cmd)
        sql_type = sql_parser.parsed['command']
        if sql_type not in ['SELECT', 'INSERT', 'DELETE', 'UPDATE']:
            raise ValueError("Only SELECT, INSERT, UPDATE and DELETE commands are supported right now.")
        if sql_type == 'SELECT':
            return self._execute_select(sql_parser, args)
        elif sql_type == 'INSERT':
            return self._execute_insert(sql_parser, args)
        elif sql_type == 'DELETE':
            return self._execute_delete(sql_parser, args)
        elif sql_type == 'UPDATE':
            return self._execute_update(sql_parser, args)
        
    def fields_view(self, start=0, stop=None, step=1, fields:List[DbaseField]=None, records=None):
        """
        Returns a generator yielding a record with fields specified in the fields dictionary.
        
        :param start: Index of the first record to return.
        :param stop: Index of the last record to return. len(self) if None.
        :param step: Step between records to return.
        :param fields: List of fields to include in the records.
        :param records: List of records to include in the view. If omitted, self[:] is used
        :returns: Generator yielding records with the specified fields.
        """

        records = records if isinstance(records, list) else self[start:stop:step]
        if not fields:
            fields = self.fields
        return (self.transform(record, fields) for record in records)

    def make_mdx(self, fieldname:str="*"):
        """
        Generates a .pmdx index for the specified field.

        :param fieldname: Name of the field to index. If '*', indexes all fields.
        """
        
        if fieldname == "*":
            for field in self.fields:
                self.make_mdx(field.name)
            return
        if fieldname not in self.field_names:
            raise ValueError(f"Field {fieldname} not found")
        def do_index(fieldname):
            self.indexes[fieldname] = {}
            for i, record in enumerate(self):
                if not self.indexes[fieldname].get(record[fieldname]):
                    self.indexes[fieldname][record[fieldname]] = [i]
                else:
                    self.indexes[fieldname][record[fieldname]].append(i)
            self._save_mdx()
        indexing_thread = Thread(target=do_index, args=(fieldname,), daemon=True)
        indexing_thread.start()

    def update_mdx(self):
        """
        Updates the .pmdx index file.
        """

        for field in self.indexes.keys():
            self.make_mdx(field)

    def del_mdx(self,entry:str="*"):
        """
        Deletes the .pmdx index file.
        """

        if entry == "*":
            mdxfile = self.filename.replace('.dbf', '.pmdx')
            if os.path.exists(mdxfile):
                os.remove(mdxfile)
            self.indexes = {}
        else:
            if entry in self.indexes:
                del self.indexes[entry]
                self._save_mdx()
            else:
                raise ValueError(f"Index {entry} not found")


@dataclass
class Cursor:
    """
    Cursor class for database operations.
    Implements the fetchone(), fetchall() and fetchmany() methods indicated by
    the Python DB API 2.0 specification
    """

    description: List[Tuple[int, str, str, str, int, int]] = field(default_factory=list)
    records: Generator = None

    def __init__(self, description:List[Tuple[str, str, str, int, int]]=None, 
                 records:List[Record]=None, **kwargs):
        self.description = description or [] 
        self.records = records
        if '_connection' in kwargs:
            self._connection = kwargs['_connection']
        else:
            self._connection = None

    def fetchone(self):
        """
        Returns the next record from the cursor.
        """
        try:
            return next(self.records) if self.records else None
        except StopIteration:
            return None

    def fetchall(self):
        """
        Returns all records from the cursor.
        """
        return list(self.records) if self.records else []

    def fetchmany(self, size):
        """
        Returns the next 'size' records from the cursor.
        """
        retval = []
        for _ in range(size):
            record = self.fetchone()
            if record:
                retval.append(record)
            else:
                break
        return retval

    def execute(self, sql:str, args=[]):
        if not self._connection:
            raise ValueError("No connection, cannot execute SQL command")
        return self._connection.execute(sql, args)
    

class Connection:
    """
    Connection class for database operations.
    Implements the cursor() and execute(sqlcmd) methods indicated 
    by the Python DB API 2.0 specification
    """
    
    def __init__(self, dirname:str):
        """
        Initializes the Connection object.
        
        :param dirname: Directory name where the database files are located.
                        Adds the non-standard 'dirname' attribute to the Connection object,
                        as well as the 'name' attribute with the base name of the directory, 
                        and 'tablenames' attribute with the list of table names.    
        """

        self.dirname = dirname
        if os.path.exists(dirname):
            if os.path.isdir(dirname):
                pass
            else:
                raise ValueError(f"{dirname} is not a directory")
        else:
            os.makedirs(dirname)

        self.name = os.path.basename(dirname)
        self._files = []
        self.tables = []
        self._load_files()

    def _load_files(self):
        """
        Loads the .dbf files in the directory specified in the 'dirname' attribute.
        For private use by '__init__' method.
        """

        for root, _, files in os.walk(self.dirname):
            for file in files:
                if file.endswith('.dbf'):
                    self._files.append(os.path.abspath(os.path.join(root, file)))
        
        # self.tables = [DbaseFile(file) for file in self._files]
        self.tables = [os.path.splitext(os.path.basename(file))[0] for file in self._files]
          
    @property
    def tablenames(self):
        """
        Returns the list of table names within the directory pointed by 'dirname'
        and its subdirectories.
        """

        # return [table.tablename for table in self.tables]
        return self.tables    

    @property
    def filenames(self):
        """
        Returns the list of filenames within the directory pointed by 'dirname'
        Includes the full path of each, including the extension.
        """

        return self._files
    
    def Cursor(self):
        """
        Method included in order to comply with the Python DB API 2.0 specification.

        :returns: Cursor object for database operations.
        """

        return Cursor(_connection=self)
    
    def execute(self, sql:str, args=[]) -> Cursor:
        """
        Executes a SQL command on the database file specified within it.
        
        :params sql: SQL command to execute.
        :returns: Cursor object with the results of the SQL command.
        """

        sql_parser = SQLParser(sql)
        sql_parser_type = sql_parser.parsed['command']
        if sql_parser_type not in ['SELECT', 'INSERT', 'DELETE', 'UPDATE']:
            raise ValueError("Only SELECT, INSERT, UPDATE and DELETE commands are supported right now.")
        parsertable = sql_parser.parsed['tables'][0]
        for i, table in enumerate(self.tables):
            if table == parsertable:
                dbf = DbaseFile(self.filenames[i])
                cursor = dbf.execute(sql, args)
                return cursor
        raise ValueError(f"Table '{parsertable}' not found")


def connect(dirname:str):
    """Returns a Connection object for the specified directory."""

    return Connection(dirname)

toplines = {
    'pretty_table': {'left': BoxType.UP_L.value, 
                     'join': BoxType.T_DOWN.value,
                      'line': BoxType.HORZ.value,
                      'right': BoxType.UP_R.value
                    },
    'table': {'left': '+', 'join': '+', 'line': '-', 'right': '+'},
    'line':  {'left': ' ', 'join': ' ', 'line': ' ', 'right': ' '},
    'list':  {'left': ' ', 'join': ' ', 'line': ' ', 'right': ' '},
    'csv':   {'left': ' ', 'join': ' ', 'line': ' ', 'right': ' '},
}

seplines = {
    'pretty_table': {'left': BoxType.T_L.value, 
                     'join': BoxType.CROSS.value,
                      'line': BoxType.HORZ.value,
                      'right': BoxType.T_R.value
                    },
    'table': {'left': '+', 'join': '+', 'line': '-', 'right': '+'},
    'line':  {'left': ' ', 'join': ' ', 'line': ' ', 'right': ' '},
    'list':  {'left': ' ', 'join': ' ', 'line': ' ', 'right': ' '},
    'csv':   {'left': ' ', 'join': ' ','line': ' ', 'right': ' '},
}

bottomlines = {
    'pretty_table': {'left': BoxType.DOWN_L.value, 
                     'join': BoxType.T_UP.value,
                      'line': BoxType.HORZ.value,
                      'right': BoxType.DOWN_R.value
                    },
    'table': {'left': '+', 'join': '+', 'line': '-', 'right': '+'},
    'line':  {'left': ' ', 'join': ' ', 'line': ' ', 'right': ' '},
    'list':  {'left': ' ', 'join': ' ', 'line': ' ', 'right': ' '},
    'csv':   {'left': ' ', 'join': ' ', 'line': ' ', 'right': ' '},
}

separators = {
    'pretty_table': BoxType.VERT.value,
    'table': '|',
    'line':  ' ',
    'list':  '|',
    'csv':   ',',
}

# Display functions

def make_topline(linetype:str, description: List[Tuple[int, str, str, str, int, int]])-> str:
    """Returns the top line of a table-like object of the type specified by linetype"""
    d = toplines[linetype]
    string = d['left']
    string += d['join'].join([d['line'] * max([t[4], len(t[1])]) for t in description])
    string += d['right']
    return string

def make_bottomline(linetype:str, description: List[Tuple[int, str, str, str, int, int]])-> str:
    """Returns the bottom line of a table-like object of the type specified by linetype"""
    d = bottomlines[linetype]
    string = d['left']
    string += d['join'].join([d['line'] * max([t[4], len(t[1])]) for t in description])
    string += d['right']
    return string

def make_intermediateline(linetype:str, description: List[Tuple[int, str, str, str, int, int]])-> str:
    """Returns the intermediate (line joiner) line of a table-like object of the type specified by linetype"""
    d = seplines[linetype]
    string = d['left']
    string += d['join'].join([d['line'] * max([t[4], len(t[1])]) for t in description])
    string += d['right']
    return string

def make_header_line(linetype:str, description: List[Tuple[int, str, str, str, int, int]])-> str:
    """Returns the header line (field names) of a table-like object of the type specified by linetype"""
    d = separators[linetype]
    string = d if linetype  != 'csv' else ' '
    string += d.join([t[1].center(max([t[4], len(t[1])])) for t in description])
    string += d if linetype  != 'csv' else ' '
    return string

def make_cursor_line(linetype:str, r: Record, description: List[Tuple[int, str, str, str, int, int]])-> str:
    """Returns a data line (field values) of a table-like object of the type specified by linetype"""
    adjstr = lambda v, w:  str(v).rjust(w) if str(v).isdigit() else str(v).ljust(w)
    d = separators[linetype]
    string = d if linetype  != 'csv' else ' '
    string += d.join([adjstr(r[t[1]], max([t[4], len(t[1])])) for t in description])
    string += d if linetype  != 'csv' else ' '
    return string

def make_cursor_lines(linetype:str, curr: Cursor)-> Generator[str, None, None]:
    """Generates all the lines for a table-like object of the type specified by linetype"""
    description = curr.description
    yield make_topline(linetype, description)
    yield make_header_line(linetype, description)
    for record in curr.fetchall():
        if linetype in ('pretty_table', 'table'):
            yield make_intermediateline(linetype, description)
        yield make_cursor_line(linetype, record, description)
    yield make_bottomline(linetype, description)

def make_raw_lines(curr: Cursor)-> Generator[str, None, None]:
    """Generates all the lines for a table-like object , 'raw' (no separators) style"""
    return make_cursor_lines('line', curr)

def make_list_lines(curr: Cursor)-> Generator[str, None, None]:
    return make_cursor_lines('list', curr)

def make_csv_lines(curr: Cursor)-> Generator[str, None, None]:
    """Generates all the lines for a table-like object , 'csv' style"""
    return make_cursor_lines('csv', curr)

def make_table_lines(curr: Cursor)->Generator[str, None, None]:
    """Generates all the lines for a table-like object , 'sqlite3 .table' style"""
    return make_cursor_lines('table', curr)

def make_pretty_table_lines(curr: Cursor)-> Generator[str, None, None]:
    """Generates all the lines for a table-like object , 'box lines' style"""
    return make_cursor_lines('pretty_table', curr)

if __name__ == '__main__':
    """
    Tests for the dbf module.
    """

    subprocess.run(['clear'])
    conn = connect('db')
    curr = conn.execute("update todos set task = 'Do something useful...' where id = 4;")
    curr = conn.execute("select * from todos;")
    for line in make_pretty_table_lines(curr):
        print(line)
    os.sys.exit(0)
#############################################################
    # dbf = DbaseFile("db/teams.dbf")
    conn = connect('db')
    curr = conn.execute("SELECT nombre as Team, titles as Championships FROM teams where id >= 3;")
    for line in make_pretty_table_lines(curr):
        print(line)
    os.sys.exit(0)
#############################################################
    dbf = DbaseFile("db/teams.dbf")
    sqli = "insert into teams (id, nombre, titles) values(6, 'Tiro Federal', 1);"
    curr = dbf.execute(sqli)
    print("Result of insertion: ", curr.fetchone())
    dbf.commit()
    curr = dbf.execute("SELECT * FROM teams where id >= 3;")
    rows = curr.fetchall()
    print(f"There are {len(rows)} rows.")
    for row in rows:
        print(row.nombre)
    dbf.execute("update teams set titles=200 where id=14;")
    print(dbf[12])
    os.sys.exit(0)
#############################################################
    teams = DbaseFile('db/teams.dbf')
    curr = teams.execute("select * from teams where id > 0;")
    recteams = curr.fetchall()
    print(f"There are {len(recteams)} teams.")
    # from test import testdb
    # testdb()
    # print("Done!")
    pass
    
