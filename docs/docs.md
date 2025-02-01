# pybase3 Documentation


## BoxType

Enum for box drawing characters.

## Connection

Connection class for database operations.
Implements the cursor() and execute(sqlcmd) methods indicated 
by the Python DB API 2.0 specification

## Cursor

Cursor class for database operations.
Implements the fetchone(), fetchall() and fetchmany() methods indicated by
the Python DB API 2.0 specification

## DbaseField

Class to represent a field (aka column) in a DBase III database file.

## DbaseFile

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

## DbaseHeader

Class to represent the header of a DBase III database file.

## FieldType

Enum for dBase III field types.

## Record

Class to represent a record in a DBase III database.
Inherits from SmartDict, a dictionary with dot notation access to keys.

## SQLParser

The SQLParser class provides a simple way to parse SQL statements. 
The tokenize() method splits the SQL statement into tokens, while the parse() method 
parses the SQL statement. 
The parse_columns(), parse_tables(), and parse_where() methods parse 
the columns, tables, and WHERE clause, respectively. 
The parse_order() method parses the ORDER BY clause if present.
The test() function demonstrates how to use the SQLParser class.

## SmartDict

SmartDict class with attributes equating dict keys


## coerce_number

Coerces a string to an int or float if possible.

## connect

Returns a Connection object for the specified directory.


## field

Return an object to identify dataclass fields.

default is the default value of the field.  default_factory is a
0-argument function called to initialize a field's value.  If init
is true, the field will be a parameter to the class's __init__()
function.  If repr is true, the field will be included in the
object's repr().  If hash is true, the field will be included in the
object's hash().  If compare is true, the field will be used in
comparison functions.  metadata, if specified, must be a mapping
which is stored but not otherwise examined by dataclass.  If kw_only
is true, the field will become a keyword-only parameter to
__init__().

It is an error to specify both default and default_factory.

## getDay

Gets day of last write to dbf file.

## getMonth

Gets month of last write to dbf file.

## getYear

Gets year (0-100, 0 for 2000, 99 for 2099) of last write to dbf file.

## make_bottomline

Returns the bottom line of a table-like object of the type specified by linetype

## make_csv_lines

Generates all the lines for a table-like object , 'csv' style

## make_cursor_line

Returns a data line (field values) of a table-like object of the type specified by linetype

## make_cursor_lines

Generates all the lines for a table-like object of the type specified by linetype

## make_header_line

Returns the header line (field names) of a table-like object of the type specified by linetype

## make_intermediateline

Returns the intermediate (line joiner) line of a table-like object of the type specified by linetype

## make_list_lines

Generates all the lines for a table-like object , 'list lines' like sqlite3 style

## make_pretty_table_lines

Generates all the lines for a table-like object , 'box lines' style

## make_raw_lines

Generates all the lines for a table-like object , 'raw' (no separators) style

## make_table_lines

Generates all the lines for a table-like object , 'sqlite3 .table' style

## make_topline

Returns the top line of a table-like object of the type specified by linetype

## to_bytes

Coerces a string-like object to bytes using the given encoding, or default utf-8.

## to_str

Coerces a string-like object to string (decodes it) using the given encoding, or default utf-8.

