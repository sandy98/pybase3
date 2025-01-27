<p align="center">
  <img src="https://raw.githubusercontent.com/sandy98/pybase3/main/img/pybase3t.png" alt="pybase3 logo">
</p>

<!--![PyPI - Current Version](https://img.shields.io/pypi/v/pybase3)-->

<p>
  <a href="https://pypi.org/project/pybase3">
    <img src="https://img.shields.io/pypi/v/pybase3" alt="PyPI - Current Version">
  </a>
  <img src="https://img.shields.io/pypi/dm/pybase3">
</p>

# DBase III Python Library

Python library meant to manipulate DBase III database files. It allows reading, writing, adding, and updating records in the database.

Beginning with version 1.90. ...  classes Connection and Cursor were added, beginning the road to fully conformance with  Python Database API Specification v2.0 (PEP 249).
To this point, both Cursor and Connection support `execute` method, which accepts `select, insert, update and delete` commands. Further support for SQL (`create, etc`) is underway.
This features work in a stable manner as of version 1.98.3, even though there are some use limitations, mainly the fact that right now, queries are 'table-centered', meaning they don't work on more than one table at a time. This will be adressed in future versions, as it is a requisite to become fully conformant.
Hopefully pybase3 will become listed with the other Python DB API conformant modules (Sqlite3, MySQL, Postgre, etc)

Even though this file format for databases is largely no longer in use, the present work is a useful tool to retrieve legacy data, as much as a tribute to a beautiful part of computer history.

Initiating from versions updated on 2025-01-04, `pybase3` supports indexing through `.pmdx` files (Python + .mdx), which results in astonishingly fast queries. See below for details.

## Features
- Connection and Cursor DB API classes
- Read DBase III database files
- Write to DBase III database files
- Add new records
- Update existing records
- Filter and search records
- Import from/ export to `.csv` files. (New in v. 1.12.1) See `import_from` and `export_to`
- Import from/ export to `sqlite` databases. (New in v. 1.13.1) See `import_from` and `export_to`

## Installation

To install the library, use `pip` to download it from Pypi. This is the preferred method: 

```bash
pip install pybase3
```

or clone the repository and navigate to the project directory:

```bash
git clone https://github.com/sandy98/pybase3.git
cd pybase3
```

## Usage

### `Connection` class

```python
import pybase3
from pybase3 import Connection

# Connects to 'db' directory. All .dbf files within will be included.
conn = Connection('db') 
# Gets a Cursor object from the connection by executing a SQL command
curr = conn.execute('select id, nombre as name, titles from teams order by titles desc;')
# Hands the cursor to a data formatting function 
for line in pybase3.make_pretty_table_lines(curr):
  print(line)
# or, alternatively, invokes a method of the cursor objects to retrieve the rows
curr = conn.execute('select id, nombre as name, titles from teams order by titles desc;')
rows = curr.fetchall()
print(f"{len(rows)} records retrieved.")
```

### `DbaseFile` class

```python
from pybase3 import DBaseFile, FieldType
test = DbaseFile.create('db/test.dbf',
                    [('name', FieldType.CHARACTER.value, 50, 0),
                        ('age', FieldType.NUMERIC.value, 3, 0)])
test.add_record('John Doe', 30)
test.add_record('Jane Doe', 25)

print(test)
print(len(test))
print(test[:])
print(test.filter('name', 'ja', compare_function=self.istartswith))

```

### `dbfquery` utility

```bash
dbfquery <dbf_directory>

# Example of use

$ dbfquery db

Welcome to pybase3 SQL shell v. 1.98.7
SQL for dBase III+
Working directory: /home/ernesto/Programas/2025/python/pybase3 / 22 tables found.
Type 'help' for help.

sql> select * from teams where titles > 40 order by titles desc;

┌────┬──────────────────────────────────────────────────┬──────┐
│ id │                      nombre                      │titles│
├────┼──────────────────────────────────────────────────┼──────┤
│   1│River Plate                                       │    77│
├────┼──────────────────────────────────────────────────┼──────┤
│   2│Boca Juniors                                      │    75│
├────┼──────────────────────────────────────────────────┼──────┤
│   3│Racing Club                                       │    47│
├────┼──────────────────────────────────────────────────┼──────┤
│  13│Sarmiento de Junín                                │    43│
└────┴──────────────────────────────────────────────────┴──────┘

sql> quit 
Bye, thank you for using SQL with dBase III

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

This is a simple test script for the pybase3 module.
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

A command line option ``pybase3`` was also added in version 1.9.5 , which works the same way as invoking the module, for example:

```bash
pybase3 [-v|-i|-h]
```

### Comments

The module itself, DBaseFile class and all its methods are thoroughly documented, so it should be easy to follow up.

Esentially, each instance of DBaseFile, be it instanced through an existing DBase III file, or created through the factory method DBaseFile.create(filename), is a list like object with indexing capabilities, which also acts as an iterator through the records present in the .dbf file. It also supports the 'len' method, reporting the number of records present in the database, even those marked for deletion.
On top of that, there is a group of methods meant for data manipulation (add_record for inserts, update_record for updates and del_record for marking/unmarking deletions).
There is also a group of methods (search, index, find, filter) to aid in retrieving selected data.

At it present stage of development, there is not support for memo fields or index fields, though this is planned for future releases, should enough interest arise.
Version 1.14.2 added `execute` method to execute SQL-like statements returning a cursor object.

For further information see:

<a href="docs/pybase3.md">Pybase3 Docs</a>

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions or suggestions, please contact [Domingo E. Savoretti](mailto:esavoretti@gmail.com).

```

```
