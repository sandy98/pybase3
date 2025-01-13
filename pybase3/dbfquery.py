#!/usr/bin/env python3
#-*- coding: utf_8 -*-

import os, sys, cmd, subprocess, readline
from argparse import ArgumentParser

try:
    from .__init__ import __version__ as version
except ImportError:
    from __init__ import __version__ as version
try:    
    from .dbase3 import DbaseFile, Connection, Cursor, SQLParser
except ImportError:
    from dbase3 import DbaseFile, Connection, Cursor, SQLParser


class SQL(cmd.Cmd):

    returnline = "\nBye, thank you for using SQL with dBase III\n"
    prompt = "sql> "

    def __init__(self, dirname=os.getcwd(), *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cache = {}
        self.dirname = os.path.abspath(dirname)
        self.connection = Connection(self.dirname)
        self.intro = f"""Welcome to pybase3 SQL shell v. {version}
SQL for dBase III+
Working directory: {self.dirname} / {len(self.connection.tablenames)} tables found.
Type 'help' for help.\n
"""

    def get_table(self, tablename):
        if tablename in self.cache:
            return self.cache[tablename]
        for i, name in enumerate(self.connection.tablenames):
            if tablename.lower() == name.lower():
                filename = self.connection.filenames[i]    
                table = DbaseFile(filename)
                self.cache[tablename] = table
                return table
        return None

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
                print(table, end='\t')
            print()
        else:
            print("No tables found in the current directory.")

    def do_fields(self, table):
        """Usage: fields <tablename>\nLists the fields in the specified table"""
        print(f"Fields in table '{table}':", end='\n')
        for i, name in enumerate(self.connection.tablenames):
            if table.lower() == name.lower():
                seltable = self.get_table(table)
                if seltable:
                    for field in seltable.field_names:
                        print(field, end='\t')
                    print()
                else:
                    print(f"Table '{table}' not found.")
                break

    def do_select(self, line):
        """Executes an SQL 'select' command"""
        line = f"select {line}{';' if not line.endswith(';') else ''}"
        print(line)
        print()
        # try:
        #     sqlparser = SQLParser(line)
        #     #print(sqlparser.parts)
        #     tablename = sqlparser.tables[0]
        #     if tablename not in self.connection.tablenames:
        #         print(f"Table '{tablename}' not found.")
        #         return
        #     table = self.get_table(self.connection.tablenames[self.connection.tablenames.index(tablename)])
        #     if not table:
        #         print(f"Table '{tablename}' not found.")
        #         return
        #     function = "pretty_table" if len(table.field_names) < 5 else "csv"
        #     cursor = table.execute(line)
        #     recs = cursor.fetchall()
        #     # recs.insert(0, cursor.description)
        #     if function == "pretty_table":
        #         for rec in table.pretty_table(records=recs):
        #             print(rec)
        #     elif function == "csv":
        #         print(table.csv_headers_line)
        #         for rec in table.csv(records=recs):
        #             print(rec)
        #     else:
        #         print(recs)
        # except Exception as e:
        #     print(e)
        try:
            cursor = self.connection.execute(line)
            recs = cursor.fetchall()
            print(", ".join(cursor.description))
            for rec in recs:
                print(", ".join(map(str, rec.values())))
        except Exception as e:
            print(e)

    def do_shell(self, _):
        """Exits to system's shell.\nType 'exit' to return to dbfquery"""
        shellname = 'bash' if os.name == 'posix' else 'cmd'
        subprocess.run([shellname])

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
    parser = ArgumentParser(description="A simple SQL shell for dBase III+ files.")
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {version}")
    argslen = len(sys.argv)
    if argslen > 1:
        parser.add_argument("dirname", nargs=1, default=[os.getcwd()], help="The dBase III+ directory to open.")
    
    args = parser.parse_args()

    if argslen > 1:
        sql = SQL(args.dirname[0])
    else:
        sql = SQL()
    if os.name == 'posix':
        subprocess.run(['clear'])
    elif os.name == 'nt':
        subprocess.run(['cls']) 
    # print("args.dirname", args.dirname)

    try:
        sql.cmdloop()
    except KeyboardInterrupt:
        print(SQL.returnline)

if __name__ == '__main__':
    main()


