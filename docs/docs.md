# pybase3 Documentation

## Any

Special type indicating an unconstrained type.

- Any is compatible with every type.
- Any assumed to have all methods.
- All values assumed to be instances of Any.

Note that all the above statements are true from the point of view of
static type checkers. At runtime, Any should not be used with instance
checks.

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

## Enum

Create a collection of name/value pairs.

Example enumeration:

>>> class Color(Enum):
...     RED = 1
...     BLUE = 2
...     GREEN = 3

Access them by:

- attribute access::

>>> Color.RED
<Color.RED: 1>

- value lookup:

>>> Color(1)
<Color.RED: 1>

- name lookup:

>>> Color['RED']
<Color.RED: 1>

Enumerations can be iterated over, and know how many members they have:

>>> len(Color)
3

>>> list(Color)
[<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]

Methods can be added to enumerations, and members can have their own
attributes -- see the documentation for details.

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

## Thread

A class that represents a thread of control.

This class can be safely subclassed in a limited fashion. There are two ways
to specify the activity: by passing a callable object to the constructor, or
by overriding the run() method in a subclass.

## ThreadPool

Class which supports an async version of applying functions to arguments.

## coerce_number

No documentation available.

## connect

Returns a Connection object for the specified directory.

## dataclass

Add dunder methods based on the fields defined in the class.

Examines PEP 526 __annotations__ to determine fields.

If init is true, an __init__() method is added to the class. If repr
is true, a __repr__() method is added. If order is true, rich
comparison dunder methods are added. If unsafe_hash is true, a
__hash__() method is added. If frozen is true, fields may not be
assigned to after instance creation. If match_args is true, the
__match_args__ tuple is added. If kw_only is true, then by default
all fields are keyword-only. If slots is true, a new class with a
__slots__ attribute is returned.

## datetime

datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])

The year, month and day arguments are required. tzinfo may be None, or an
instance of a tzinfo subclass. The remaining arguments may be ints.

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

No documentation available.

## getMonth

No documentation available.

## getYear

No documentation available.

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

No documentation available.

## make_pretty_table_lines

Generates all the lines for a table-like object , 'box lines' style

## make_raw_lines

Generates all the lines for a table-like object , 'raw' (no separators) style

## make_table_lines

Generates all the lines for a table-like object , 'sqlite3 .table' style

## make_topline

Returns the top line of a table-like object of the type specified by linetype

## to_bytes

No documentation available.

## to_str

No documentation available.

