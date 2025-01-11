#!/usr/bin/env python3
#-*- coding: utf_8 -*-

import os, sys, cmd, subprocess
import readline

try:
    from .__init__ import __version__ as version
except ImportError:
    from __init__ import __version__ as version
try:    
    from .dbase3 import DbaseFile, Connection, Cursor, SQLParser
except ImportError:
    from dbase3 import DbaseFile, Connection, Cursor, SQLParser


class SQL(cmd.Cmd):

    intro = f"Welcome to pybase3 SQL shell v. {version}\nSQL for dBase III+\nType 'help' for help.\n"
    returnline = "\nBye, dBase SQL lovers...\n"
    prompt = "sql> "

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.connection = Connection(os.getcwd())

    def emptyline(self):
        print('', end='')
        return

    def do_version(self, _):
        """Prints the version of the program"""
        print(f"v. {version}")

    def do_tables(self, _):
        """Lists the tables in the current directory"""
        print()
        tables = self.connection.tablenames
        if tables:
            for table in tables:
                print(table)
        else:
            print("No tables found in the current directory.")

    def do_fields(self, table):
        """Usage: fields <tablename>\nLists the fields in the specified table"""
        print()
        for i, name in enumerate(self.connection.tablenames):
            if table.lower() == name.lower():
                seltable = self.connection.tables[i]
                for field in seltable.field_names:
                    print(field)
                break

    def do_select(self, line):
        """Executes an SQL 'select' command"""
        line = f"select {line}{';' if not line.endswith(';') else ''}"
        print(line)
        print()
        try:
            sqlparser = SQLParser(line)
            #print(sqlparser.parts)
            tablename = sqlparser.tables[0]
            if tablename not in self.connection.tablenames:
                print(f"Table '{tablename}' not found.")
                return
            table = self.connection.tables[self.connection.tablenames.index(tablename)]
            function = "pretty_table" if len(table.field_names) < 6 else "csv"
            cursor = table.execute(line)
            recs = cursor.fetchall()
            # recs.insert(0, cursor.description)
            if function == "pretty_table":
                for rec in table.pretty_table(records=recs):
                    print(rec)
            elif function == "csv":
                print(table.csv_headers_line)
                for rec in table.csv(records=recs):
                    print(rec)
            else:
                print(recs)
        except Exception as e:
            print(e)

    def do_EOF(self, eof):
        """Exit the program"""
        print(self.returnline)
        raise SystemExit(0)

    def do_exit(self, eof):
        """Exit the program"""
        return self.do_EOF('')

    def do_quit(self, eof):
        """Exit the program"""
        return self.do_EOF('')
    
def main():
    sql = SQL()
    if os.name == 'posix':
        subprocess.run(['clear'])
    elif os.name == 'nt':
        subprocess.run(['cls']) 

    try:
        sql.cmdloop()
    except KeyboardInterrupt:
        print(SQL.returnline)

if __name__ == '__main__':
    main()


