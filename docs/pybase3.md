# pybase3 Documentation

This documentation is generated from the docstrings in the module.

## Class: `Any`

Special type indicating an unconstrained type.

- Any is compatible with every type.
- Any assumed to have all methods.
- All values assumed to be instances of Any.

Note that all the above statements are true from the point of view of
static type checkers. At runtime, Any should not be used with instance
checks.

### Method: `__new__`

Create and return a new object.  See help(type) for accurate signature.

## Class: `BoxType`

Enum for box drawing characters.

## Class: `Connection`

Connection class for database operations.
Implements the cursor() and execute(sqlcmd) methods indicated 
by the Python DB API 2.0 specification

### Method: `Cursor`

Method included in order to comply with the Python DB API 2.0 specification.

:returns: Cursor object for database operations.

### Method: `__init__`

Initializes the Connection object.

:param dirname: Directory name where the database files are located.
                Adds the non-standard 'dirname' attribute to the Connection object,
                as well as the 'name' attribute with the base name of the directory, 
                and 'tablenames' attribute with the list of table names.    

### Method: `_load_files`

Loads the .dbf files in the directory specified in the 'dirname' attribute.
For private use by '__init__' method.

### Method: `execute`

Executes a SQL command on the database file specified within it.

:params sql: SQL command to execute.
:returns: Cursor object with the results of the SQL command.

## Class: `Cursor`

Cursor class for database operations.
Implements the fetchone(), fetchall() and fetchmany() methods indicated by
the Python DB API 2.0 specification

### Method: `__eq__`

Return self==value.

### Method: `__init__`

Initialize self.  See help(type(self)) for accurate signature.

### Method: `__repr__`

Return repr(self).

### Method: `execute`

No documentation available.

### Method: `fetchall`

Returns all records from the cursor.

### Method: `fetchmany`

Returns the next 'size' records from the cursor.

### Method: `fetchone`

Returns the next record from the cursor.

## Class: `DbaseField`

Class to represent a field (aka column) in a DBase III database file.

### Method: `__eq__`

Return self==value.

### Method: `__init__`

Initialize self.  See help(type(self)) for accurate signature.

### Method: `__post_init__`

Validates the field attributes.

### Method: `__repr__`

Return repr(self).

### Method: `load_bytes`

Transforms a byte string (usually read from disk) into a DbaseField object.

### Method: `to_bytes`

Transforms a DbaseField object into a byte string (usually to write to disk).

## Class: `DbaseFile`

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

### Method: `__del__`

Closes the database file when the instance is destroyed.

### Method: `__getitem__`

Returns a single record (dictionary with field names and field values) 
from the database or a list of them (if a slice is used).

:param key: Index of the record to retrieve, or a slice.

### Method: `__init__`

Initializes an instance of DBase3.

:param filename: Name of the database file.

### Method: `__iter__`

Returns an iterator over the records in the database, 
allowing notation like 'for record in dbf'.

### Method: `__len__`

Returns the number of records in the database, including records marked to be deleted.

### Method: `__str__`

Returns a string with information about the database file.

### Method: `_execute_delete`

Receives a parsed SQL DELETE command and returns a Cursor object with the results.

:param sql_parser: SQLParser object with the parsed SQL command.
:returns Cursor object with the results of the DELETE command.

### Method: `_execute_insert`

Receives a parsed SQL INSERT command and returns a Cursor object with the results.

:param sql_parser: SQLParser object with the parsed SQL command.
:returns Cursor object with the results of the INSERT command.

### Method: `_execute_select`

Receives a parsed SQL SELECT command and returns a Cursor object with the results.

:param sql_parser: SQLParser object with the parsed SQL command.
:returns Cursor object with the results of the SELECT command.

### Method: `_execute_update`

Receives a parsed SQL UPDATE command and returns a Cursor object with the results.

:param sql_parser: SQLParser object with the parsed SQL command.
:returns Cursor object with the results of the UPDATE command.

### Method: `_format_field`

Returns a string with the field value aligned to the field length.
If the field is a character field, it is left aligned, otherwise it is right aligned.

### Method: `_indexed_search`

Searches for a record with the specified value in the specified field,
starting from the specified index, for which the specified comparison function returns True,
using the field index.

### Method: `_init`

Initializes the database structure by reading the header and fields.

### Method: `_load_mdx`

Loads the MDX (.pmdx) index file, if it exists.

### Method: `_save_mdx`

Saves the MDX index file (dbfname.pmdx).

### Method: `_test_key`

Tests if the key is within the valid range of record indexes.
Raises an IndexError if the key is out of range.
Meant for internal use only.

### Method: `add_record`

Adds a new record to the database.

:param record_data: SmartDictionary with the new record's data.

### Method: `as_cursor`

Returns a cursor object for the database.

### Method: `commit`

Writes the database to a file. 
If no filename is specified, the original file is overwritten.
Skips records marked as deleted, thus effectively deleting them, 
and adjusts the header accordingly.

### Method: `csv`

Returns a generator of CSV strings, each one with the CSV repr o a record in the database.

### Method: `del_mdx`

Deletes the .pmdx index file.

### Method: `del_record`

Marks a record as deleted.
To effectively delete the record, use the commit() method afterwards.

### Method: `execute`

Executes a SQL command on the database.

:param sql_cmd: SQL command to execute
:param args: List of arguments to be passed to the SQL command.
:returns Cursor object with the results of the SQL command.

### Method: `export_to`

Exports the database to a destination of the specified type.

### Method: `fields_view`

Returns a generator yielding a record with fields specified in the fields dictionary.

:param start: Index of the first record to return.
:param stop: Index of the last record to return. len(self) if None.
:param step: Step between records to return.
:param fields: List of fields to include in the records.
:param records: List of records to include in the view. If omitted, self[:] is used
:returns: Generator yielding records with the specified fields.

### Method: `filter`

Returns a list of records (dictionaries) that meet the specified criteria.

### Method: `find`

Wrapper for search() with funcname="find".
Returns the first record (dictionary) found, or None if no record meeting given criteria is found.

### Method: `get_field`

Returns the field object with the specified name, case sensitive.

### Method: `get_record`

Retrieves a record (dictionary with field names and field values) from the database.
Used internally by the __getitem__ method.

### Method: `headers_line`

Returns a string containing the field names right aligned to max field lengths.

### Method: `iendswith`

Checks if the string 'f' ends with the string 'v', ignoring case.

:param f: String to check.
:param v: Suffix to look for.
:return: True if 'f' ends with 'v', False otherwise.

### Method: `index`

Wrapper for search() with funcname="index".
Returns index of the first record found, or -1 if no record meeting given criteria is found.

### Method: `istartswith`

Checks if the string 'f' starts with the string 'v', ignoring case.

:param f: String to check.
:param v: Prefix to look for.
:return: True if 'f' starts with 'v', False otherwise.

### Method: `line`

Returns a string with the record at the specified index, with fields right aligned to max field lengths.

### Method: `lines`

Returns a generator which resolves to an array of strings, each one with 
with the records in the specified range, with fields right aligned to max field lengths.

### Method: `list`

Returns a generator, corresponding to the list of records from the database.

### Method: `make_mdx`

Generates a .pmdx index for the specified field.

:param fieldname: Name of the field to index. If '*', indexes all fields.

### Method: `max_field_length`

Returns the maximum length of the specified field (including length of field name) in the database.

### Method: `pack`

Same as commit(). Included for compatibility with long lost dBase past.

### Method: `parse_conditions`

Parses the WHERE clause of a SQL statement and returns a list of tuples
with the field name, the value to compare and the comparison function.

### Method: `pretty_table`

Returns a  generator yielding a string for each line representing a record in the database, 
wrapped in cute lines.

### Method: `save_record`

Writes a record (dictionary with field names and field values) to the database
at the specified index.

### Method: `search`

Searches for a record with the specified value in the specified field,
starting from the specified index, for which the specified comparison function returns True.
It will try to use the field index if available.

### Method: `table`

Returns a  generator yielding a string for each line representing a record in the database, 
wrapped in sqlite3 style (.mode table) lines.

### Method: `transform`

Returns a record with the specified fields, usually with
fields 'deleted' and 'metadata' stripped.

### Method: `update_mdx`

Updates the .pmdx index file.

### Method: `update_record`

Updates an existing record in the database.

:param index: Index of the record to update.
:param record_data: SmartDictionary with the updated data.
:raises IndexError: If the record index is out of range.

## Class: `DbaseHeader`

Class to represent the header of a DBase III database file.

### Method: `__eq__`

Return self==value.

### Method: `__init__`

Initialize self.  See help(type(self)) for accurate signature.

### Method: `__post_init__`

Validates the header fields.

### Method: `__repr__`

Return repr(self).

### Method: `load_bytes`

Transforms a byte string (usually read from disk) into a DbaseHeader object.

### Method: `to_bytes`

Transforms a DbaseHeader object into a byte string (usually to write to disk).

## Class: `Enum`

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

### Method: `__new__`

Create and return a new object.  See help(type) for accurate signature.

## Class: `FieldType`

Enum for dBase III field types.

## Class: `Record`

Class to represent a record in a DBase III database.
Inherits from SmartDict, a dictionary with dot notation access to keys.

### Method: `__delattr__`

Implement delattr(self, name).

### Method: `__getattr__`

No documentation available.

### Method: `__hasattr__`

No documentation available.

### Method: `__init__`

Initialize self.  See help(type(self)) for accurate signature.

### Method: `__repr__`

Return repr(self).

### Method: `__setattr__`

Implement setattr(self, name, value).

### Method: `__str__`

Return str(self).

### Method: `copy`

D.copy() -> a shallow copy of D

## Class: `SQLParser`

The SQLParser class provides a simple way to parse SQL statements. 
The tokenize() method splits the SQL statement into tokens, while the parse() method 
parses the SQL statement. 
The parse_columns(), parse_tables(), and parse_where() methods parse 
the columns, tables, and WHERE clause, respectively. 
The parse_order() method parses the ORDER BY clause if present.
The test() function demonstrates how to use the SQLParser class.

### Method: `__init__`

Initialize the SQLParser object.

Args:
    sqlcmd (str): The SQL statement to parse.

### Method: `parse`

Parse the SQL statement.

Returns:
    dict: A dictionary of parsed elements.

### Method: `parse_columns`

Parse the columns in the SQL statement.

Returns:
    list: A list of columns.

### Method: `parse_order`

Parse the ORDER BY clause in the SQL statement.

Returns:
    str: The ORDER BY clause.

### Method: `parse_tables`

Parse the table or tables in the SQL statement.

Returns:
    list:  table/s name/s.

### Method: `parse_updates`

No documentation available.

### Method: `parse_values`

Parse the values in the SQL INSERT statement.

Returns:
    list:  values to be inserted.

### Method: `parse_where`

Parse the WHERE clause in the SQL statement.

Returns:
    str: The WHERE clause.

### Method: `tokenize`

Tokenize the SQL statement.

Returns:
    list: A list of tokens.

## Class: `SmartDict`

SmartDict class with attributes equating dict keys

### Method: `__delattr__`

Implement delattr(self, name).

### Method: `__getattr__`

No documentation available.

### Method: `__hasattr__`

No documentation available.

### Method: `__init__`

Initialize self.  See help(type(self)) for accurate signature.

### Method: `__setattr__`

Implement setattr(self, name, value).

### Method: `copy`

D.copy() -> a shallow copy of D

## Class: `Thread`

A class that represents a thread of control.

This class can be safely subclassed in a limited fashion. There are two ways
to specify the activity: by passing a callable object to the constructor, or
by overriding the run() method in a subclass.

### Method: `__init__`

This constructor should always be called with keyword arguments. Arguments are:

*group* should be None; reserved for future extension when a ThreadGroup
class is implemented.

*target* is the callable object to be invoked by the run()
method. Defaults to None, meaning nothing is called.

*name* is the thread name. By default, a unique name is constructed of
the form "Thread-N" where N is a small decimal number.

*args* is a list or tuple of arguments for the target invocation. Defaults to ().

*kwargs* is a dictionary of keyword arguments for the target
invocation. Defaults to {}.

If a subclass overrides the constructor, it must make sure to invoke
the base class constructor (Thread.__init__()) before doing anything
else to the thread.

### Method: `__repr__`

Return repr(self).

### Method: `_bootstrap`

No documentation available.

### Method: `_bootstrap_inner`

No documentation available.

### Method: `_delete`

Remove current thread from the dict of currently running threads.

### Method: `_reset_internal_locks`

No documentation available.

### Method: `_set_ident`

No documentation available.

### Method: `_set_native_id`

No documentation available.

### Method: `_set_tstate_lock`

Set a lock object which will be released by the interpreter when
the underlying thread state (see pystate.h) gets deleted.

### Method: `_stop`

No documentation available.

### Method: `_wait_for_tstate_lock`

No documentation available.

### Method: `getName`

Return a string used for identification purposes only.

This method is deprecated, use the name attribute instead.

### Method: `isDaemon`

Return whether this thread is a daemon.

This method is deprecated, use the daemon attribute instead.

### Method: `is_alive`

Return whether the thread is alive.

This method returns True just before the run() method starts until just
after the run() method terminates. See also the module function
enumerate().

### Method: `join`

Wait until the thread terminates.

This blocks the calling thread until the thread whose join() method is
called terminates -- either normally or through an unhandled exception
or until the optional timeout occurs.

When the timeout argument is present and not None, it should be a
floating point number specifying a timeout for the operation in seconds
(or fractions thereof). As join() always returns None, you must call
is_alive() after join() to decide whether a timeout happened -- if the
thread is still alive, the join() call timed out.

When the timeout argument is not present or None, the operation will
block until the thread terminates.

A thread can be join()ed many times.

join() raises a RuntimeError if an attempt is made to join the current
thread as that would cause a deadlock. It is also an error to join() a
thread before it has been started and attempts to do so raises the same
exception.

### Method: `run`

Method representing the thread's activity.

You may override this method in a subclass. The standard run() method
invokes the callable object passed to the object's constructor as the
target argument, if any, with sequential and keyword arguments taken
from the args and kwargs arguments, respectively.

### Method: `setDaemon`

Set whether this thread is a daemon.

This method is deprecated, use the .daemon property instead.

### Method: `setName`

Set the name string for this thread.

This method is deprecated, use the name attribute instead.

### Method: `start`

Start the thread's activity.

It must be called at most once per thread object. It arranges for the
object's run() method to be invoked in a separate thread of control.

This method will raise a RuntimeError if called more than once on the
same thread object.

## Class: `ThreadPool`

Class which supports an async version of applying functions to arguments.

### Method: `Process`

No documentation available.

### Method: `__del__`

No documentation available.

### Method: `__enter__`

No documentation available.

### Method: `__exit__`

No documentation available.

### Method: `__init__`

Initialize self.  See help(type(self)) for accurate signature.

### Method: `__reduce__`

Helper for pickle.

### Method: `__repr__`

Return repr(self).

### Method: `_check_running`

No documentation available.

### Method: `_get_sentinels`

No documentation available.

### Method: `_get_tasks`

No documentation available.

### Method: `_get_worker_sentinels`

No documentation available.

### Method: `_guarded_task_generation`

Provides a generator of tasks for imap and imap_unordered with
appropriate handling for iterables which throw exceptions during
iteration.

### Method: `_handle_results`

No documentation available.

### Method: `_handle_tasks`

No documentation available.

### Method: `_help_stuff_finish`

No documentation available.

### Method: `_join_exited_workers`

Cleanup after any worker processes which have exited due to reaching
their specified lifetime.  Returns True if any workers were cleaned up.

### Method: `_maintain_pool`

Clean up any exited workers and start replacements for them.
        

### Method: `_map_async`

Helper function to implement map, starmap and their async counterparts.

### Method: `_repopulate_pool`

No documentation available.

### Method: `_repopulate_pool_static`

Bring the number of pool processes up to the specified number,
for use after reaping workers which have exited.

### Method: `_setup_queues`

No documentation available.

### Method: `_wait_for_updates`

No documentation available.

### Method: `apply`

Equivalent of `func(*args, **kwds)`.
Pool must be running.

### Method: `apply_async`

Asynchronous version of `apply()` method.

### Method: `close`

No documentation available.

### Method: `imap`

Equivalent of `map()` -- can be MUCH slower than `Pool.map()`.

### Method: `imap_unordered`

Like `imap()` method but ordering of results is arbitrary.

### Method: `join`

No documentation available.

### Method: `map`

Apply `func` to each element in `iterable`, collecting the results
in a list that is returned.

### Method: `map_async`

Asynchronous version of `map()` method.

### Method: `starmap`

Like `map()` method but the elements of the `iterable` are expected to
be iterables as well and will be unpacked as arguments. Hence
`func` and (a, b) becomes func(a, b).

### Method: `starmap_async`

Asynchronous version of `starmap()` method.

### Method: `terminate`

No documentation available.

## Function: `coerce_number`

No documentation available.

## Function: `connect`

Returns a Connection object for the specified directory.

## Function: `dataclass`

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

## Class: `datetime`

datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])

The year, month and day arguments are required. tzinfo may be None, or an
instance of a tzinfo subclass. The remaining arguments may be ints.

## Function: `field`

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

## Function: `getDay`

No documentation available.

## Function: `getMonth`

No documentation available.

## Function: `getYear`

No documentation available.

## Function: `make_bottomline`

Returns the bottom line of a table-like object of the type specified by linetype

## Function: `make_csv_lines`

Generates all the lines for a table-like object , 'csv' style

## Function: `make_cursor_line`

Returns a data line (field values) of a table-like object of the type specified by linetype

## Function: `make_cursor_lines`

Generates all the lines for a table-like object of the type specified by linetype

## Function: `make_header_line`

Returns the header line (field names) of a table-like object of the type specified by linetype

## Function: `make_intermediateline`

Returns the intermediate (line joiner) line of a table-like object of the type specified by linetype

## Function: `make_list_lines`

No documentation available.

## Function: `make_pretty_table_lines`

Generates all the lines for a table-like object , 'box lines' style

## Function: `make_raw_lines`

Generates all the lines for a table-like object , 'raw' (no separators) style

## Function: `make_table_lines`

Generates all the lines for a table-like object , 'sqlite3 .table' style

## Function: `make_topline`

Returns the top line of a table-like object of the type specified by linetype

## Function: `to_bytes`

No documentation available.

## Function: `to_str`

No documentation available.

