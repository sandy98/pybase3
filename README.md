<p align="center">
  <img src="https://raw.githubusercontent.com/sandy98/pybase3/main/img/pybase3t.png" alt="pybase3 logo">
</p>

# DBase III Python Library

Python library meant to manipulate DBase III database files. It allows reading, writing, adding, and updating records in the database.

Even though this file format for databases is largely no longer in use, the present work is a minitool useful to retrieve legacy data, as much as a tribute to a beautiful part of computer history.

Initiating from versions updated on 2025-01-04, `pybase3` supports indexing through `.pmdx` files (Python + .mdx), which results in astonishingly fast queries. See below for details.

## Features

- Read DBase III database files
- Write to DBase III database files
- Add new records
- Update existing records
- Filter and search records

## Installation

To install the library, clone this repository and navigate to the project directory:

```bash
git clone https://github.com/sandy98/pybase3.git
cd pybase3
```

or

```bash 
pip install pybase3
```

## Usage

### Main class

```python
from pybase3.dbase3 import DBaseFile, FieldType
test = DbaseFile.create('db/test.dbf',
                    [('name', FieldType.CHARACTER.value, 50, 0),
                        ('age', FieldType.NUMERIC.value, 3, 0)])
test.add_record('John Doe', 30)
test.add_record('Jane Doe', 25)

print(test)
print(len(test))
print(test[:])
print(test.filter('name', 'ja', comp_func=self.istartswith))

```

### Database browser utility

```bash
python3 dbfview.py <dbf_file>
```
or, even better, if pybase3 is installed using pip, it will install dbfview as a script, thus:
```bash
dbfview <dbf_file>
```
A convenient CLI cursed based utility to browse .dbf files.

### Test utility

```bash
python3 dbftest.py [-r|-d]
```
or, even better, if pybase3 is installed using pip, it will install dbftest as a script, thus:
```bash
dbftest  [-r|-d]
```
This is a simple test script for the dbase3 module.
It creates a test database (`db/test.dbf`), updates some records, and deletes one.
It then writes the changes to the database file.
The script can be run with the -d option to show intermediate results or the -r option to erase an existing test.dbf.
The script will create a directory 'db' in the current directory if it doesn't exist.
The script will create a file 'test.dbf' in the 'db' directory if it doesn't exist.

### Module level usage

By issuing the command:
```bash
python3 -m pybase3 [-v|-i|-h]
```
the module itself is invoked (more specifically, __main__.py), resulting in a traversal of the file system lookinf for .dbf files. At the end, should the search be successful, the user is offered with a numbered menu of existing dbf files, ready to be read by dbfview.

As of version 1.9.5 new options were added: -v, --version for retrieving current version of the software, -i, --info for getting full information, and -h, --help for usage instructions.

A command line option ```pybase3``` was also added in version 1.9.5 , which works the same way as invoking the module, for example:
```bash
pybase3 [-v|-i|-h]
```



### Comments

The module itself, DBaseFile class and all its methods are thoroughly documented, so it should be easy to follow up.

Esentially, each instance of DBaseFile, be it instanced through an existing DBase III file, or created through the factory method DBaseFile.create(filename), is a list like object with indexing capabilities, which also acts as an iterator through the records present in the .dbf file. It also supports the 'len' method, reporting the number of records present in the database, even those marked for deletion.
On top of that, there is a group of methods meant for data manipulation (add_record for inserts, update_record for updates and del_record for marking/unmarking deletions).
There is also a group of methods (search, index, find, filter) to aid in retrieving selected data.

At it present stage of development, there is not support for memo fields or index fields, though this is planned for future releases, should enough interest arise.
It's also planned an `exec` method to execute SQL-like statements. not functional right now.

For further information see the documentation below.

## Documentation

### Classes

#### `DBaseFile`

Class to manipulate DBase III database files.

### Dunder and 'private' Methods

- `__init__(self, filename: str)`: Initializes an instance of DBase3File from an existing dbf file.
- `__del__(self)`: Closes the database file when the instance is destroyed.
- `__len__(self)`: Returns the number of records in the database, including records marked to be deleted. Allows writing: `len(dbasefileobj)`
- `__getitem__(self, key)`: Returns a single record or a list of records (if slice notation is used) from the database. Allows: `dbasefileobj[3]` or `dbasefileobj[3:7]`  
- `__iter__(self)`: Returns an iterator over the records in the database. Allows `for record in dbasefileobj: ...`
- `__str__(self)`: Returns a string representation of the database.
- `_init(self)`: Initializes the database structure by reading the header and fields. Meant for private use by DBaseFile instances.
- `def _test_key(self, key)`: Tests if the key is within the valid range of record indexes. Raises an IndexError if the key is out of range. Meant for internal use only.
    
### Class Methods

- `create(cls, filename: str, fields: List[Tuple[str, FieldType, int, int]])`: Creates a new DBase III database file with the specified fields. Returns a DbaseFile object pointing to newly created dbase file.

### Data Manipulation methods

- `add_record(self, record_data: dict)`: Adds a new record to the database.
- `update_record(self, index: int, record_data: dict)`: Updates an existing record in the database.
- `save_record(self, key, record)`: Writes a record (dictionary with field names and field values) to the database at the specified index. Params: key is the index (0 based position in dbf file). record is a dictionary corresponding to an item in the database (i.e: {'id': 1, 'name': "Jane Doe"}) Used internally by `update_record` 
- `del_record(self, key, value = True)`: Marks for deletion the record identified by the index 'key', or unmarks it if `value == False`. To efectively erase the record from disk the deletion must be confirmed by using `dbasefileobj.commit()`
- `commit(self, filename=None)`: Formerly named `write`, it writes the current file to disk, skipping records marked for deletion. If a filename is provided, other the current filename, saves the database file to the new destination, keeping previous filename as is. Its worth noting that `add_record` and `update_record` commit changes to disk inmediatly, so it's not needed to call `commit` after using them. It won't harm to do it, either.

### Data searching/filtering methods

-  `search(self, fieldname, value, start=0, funcname="", comp_func=None)`: Searches for a record with the specified value in the specified field, starting from the specified index, for which the specified comparison function returns True. Returns a tuple with index:int and record:dict
-  `find(self, fieldname, value, start=0, comp_func=None)`: Wrapper for search() with funcname="find". Returns the first record (dictionary) found, or None if no record meeting given criteria is found.
-  `index(self, fieldname, value, start=0, comp_func=None)`:  Wrapper for search() with funcname="index". Returns index of the first record found, or -1 if no record meeting given criteria is found.
-  `filter(self, fieldname, value, comp_func=None)`: Returns a list of records (dictionaries) that meet the specified criteria.
- `exec(self, sql_cmd:str)`: Meant for retrieving data in a custom manner. Not operational yet. Invoking it raises a NotImplemented error. 

### Data listing methods

-  `list(self, start=0, stop=None, fieldsep="|", recordsep='\n', records:list=None)`: Returns a list of records from the database, starting at 'start', ending at 'stop' or EOF, having fields separated by 'fieldsep' and records separated by '\n'. If 'records' is not None, the provided list is used instead of retrieving values from the database.
-  `csv(self, start=0, stop=None, records:list = None)`: Wrapper for 'list', using ',' as fieldsep.
-  `table(self, start=0, stop=None, records:list = None)`: Retrieves selected records using ad-hoc format, same as provided by sqlite3 CLI in .table mode.
-  `pretty_table(self, start=0, stop=None, records:list = None)`: Retrieves selected records using ad-hoc format, like `table` but with prettier lines.
- `lines(self, start=0, stop=None, records:list = None)`: Retrieves selected records with field values aligned to their widths.

Its worth noting that all these last five methods return generators instead of lists, which makes them much lighter in case of bulky recordsets.

### Static Methods (Auxiliary functions for searching/filtering)

- `istartswith(f: str, v: str) -> bool`: Checks if the string `f` starts with the string `v`, ignoring case.
- `iendswith(f: str, v: str) -> bool`: Checks if the string `f` ends with the string `v`, ignoring case.

### Properties

- 'fields': Retrieves the list of fields from which the database records are assembled. Each field object in the list has a name, type (as per FieldType Enum) and length.

- 'field_names': Retrieves a list with the name of each field in the database.

- 'field_types': Retrieves a list with the type of each field in the database.

- 'field_lengths': Retrieves a list with the length of each field in the database.

- 'max_field_lengths': Returns the maximum length of the specified field (including length of field name) in the database. Useful for retrieving lines with adjusted width for each field. Internally uses `def max_field_length(self, field)`

- 'tmax_field_lengths': Same as max_field_lengths, threaded version, in an unsuccessful attemp of accelerating the process. Anyway, it works.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions or suggestions, please contact [Domingo E. Savoretti](mailto:esavoretti@gmail.com).

```

```
