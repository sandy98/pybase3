#-*- coding: utf_8 -*-

# This is a simple test script for the dbase3 module.
# It creates a test database, updates some records, and deletes one.
# It then writes the changes to the database file.
# The script can be run with the -d option to show intermediate results.
# The script will create a directory 'db' in the current directory if it doesn't exist.
# The script will create a file 'test.dbf' in the 'db' directory if it doesn't exist.

import os, sys, subprocess
try:
    from dbase3 import DbaseFile, FieldType, SQLParser
except ImportError:
    from pybase3.dbase3 import DbaseFile, FieldType, SQLParser

def test_sql():
    subprocess.run(['clear'])
    sqlstr = "SELECT name as nombre, age FROM kids WHERE age > 18;"
    sql_parser = SQLParser(sqlstr)
    print("SQL parser parts:", sql_parser.parts)
    kids = DbaseFile('db/kids.dbf')
    print("\nKids database\n-------------------")
    print(kids.csv_headers_line)
    for csv in kids.csv():
        print(csv)
    print(f"\nSQL command: {sqlstr}\n-------------------")
    oldies = kids.filter(sql_parser.field_param, sql_parser.value_param, 
                         compare_function=sql_parser.compare_func)
    noldies = kids.fields_view(fields=sql_parser.fields, records=oldies)
    print("\nResult of SQL query\n-------------------")
    for record in noldies:
        for k, v in record.items():
            print(f"{k}: {v}", end=' - ' if k != 'age' else '\n')
    print("\n")
    sqlstr = "SELECT name as nombre, age FROM kids WHERE name like 'B';"
    sql_parser = SQLParser(sqlstr)
    print("SQL parser parts:", sql_parser.parts)
    print(f"\nSQL command: {sqlstr}\n-------------------")
    oldies = kids.filter(sql_parser.field_param, sql_parser.value_param, 
                         compare_function=sql_parser.compare_func)
    noldies = kids.fields_view(fields=sql_parser.fields, records=oldies)
    print("\nResult of SQL query\n-------------------")
    for record in noldies:
        for k, v in record.items():
            print(f"{k}: {v}", end=' - ' if k != 'age' else '\n')
    print("\n")
    os.sys.exit()    


def mk_pediatras():
    from time import time as timestamp
    medicos = None
    pediatras = None
    try:
        medicos = DbaseFile('db/medicos.dbf')
    except FileNotFoundError:
        print("Error: Can't open 'medicos.dbf'.")
        return
    medicos.indexhits = 0
    t0 = timestamp()
    pediatras = medicos.filter("Especialida", 27)
    t1 = timestamp()
    difftime = round(t1 - t0, 3)
    print(f"The list of pediatricians with {len(pediatras)} registers was created in {difftime} seconds with {medicos.indexhits} index uses")
    print(f"The first pediatrician is: {pediatras[0].NOMBRE}")
    print(f"The pediatrician in the middle is: {pediatras[len(pediatras)//2].NOMBRE}")
    print(f"The last pediatrician is: {pediatras[-1].NOMBRE}")

    return medicos, pediatras

def create_test_db():
    test = DbaseFile.create('db/test.dbf',
                        [('name', FieldType.CHARACTER.value, 50, 0),
                            ('age', FieldType.NUMERIC.value, 3, 0)])
    test.add_record('John Doe', 30)
    test.add_record('Jane Doe', 25)
    test.add_record('John Smith', 40)
    test.add_record('Jane Smith', 35)
    test.add_record('John Brown', 50)
    test.add_record('Jane Brown', 45)
    return test

def testdb():
    dbg = False
    rm = False
    if len(sys.argv) > 1:
        if sys.argv[1] in ['-d', '--debug']:
            dbg = True
        elif sys.argv[1] in ['-r', '--remove']:
            rm = True
        elif sys.argv[1] in ['-h', '--help'] or len(sys.argv[1]):   
            print("Usage: test.py [-d] [-r]")
            sys.exit(1)

    if (dbg or rm) and os.path.exists('db/test.dbf'):
        os.remove('db/test.dbf')

    subprocess.run(['clear'])

    if os.path.exists('db/test.dbf'):
        test = DbaseFile('db/test.dbf')
    else:
        if os.path.exists('db'):
            if os.path.isdir('db'):
                test = create_test_db()
            else:
                print("Error: db is not a directory.\nCan't create 'test.dbf'.")
                sys.exit(1)
        else:
            try:
                os.mkdir('db')
            except:
                print("Error: Can't create directory 'db'.")
                sys.exit(1)
            test = create_test_db()

    print("Database prior to updates:")
    print("\nTest.db\n-------")
    for r in test:
        print(r)
    if not dbg:
        input("\nPress Enter to continue...")

    index, jdoe = test.search('name', 'John Doe')
    jdoe['age'] += 1
    test.update_record(index, jdoe)
    jdoe = test[index]
    index, jadoe = test.search('name', 'Jane Doe')
    if index >= 0:
        jadoe['name'] = 'Janet Elizabeth Doe'
        test.update_record(index, jadoe)
    else:
        print("Jane Doe not found. She probably changed her name.")
    index = test.index('name', 'John Smith')
    if index >= 0:
        test.del_record(index)
    else:
        print("John Smith not found. He must have been deleted already.")

    print("\nDatabase after updates:")
    print("\nTest.db\n-------")
    for r in test[:]:
        print(r)
    if not dbg:
        input("\nPress Enter to continue...")

    test.commit()

    print("\nDatabase after comitting deletions:")
    print("\nTest.db\n-------")
    for r in test:
        print(r)
    if not dbg:
        input("\nPress Enter to finish...")

if __name__ == "__main__":
    testdb()
