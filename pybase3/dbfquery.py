#!/usr/bin/env python3
#-*- coding: utf_8 -*-

import os, sys, cmd, subprocess
# import readline
from argparse import ArgumentParser

try:    
    from .__init__ import __version__ as version
    from .dbase3 import DbaseFile, Connection
    from .dbase3 import make_raw_lines, make_list_lines, make_csv_lines
    from .dbase3 import make_table_lines, make_pretty_table_lines
    # print("Imported from package")
except ImportError:
    from __init__ import __version__ as version
    from dbase3 import DbaseFile, Connection
    from dbase3 import make_raw_lines, make_list_lines, make_csv_lines
    from dbase3 import make_table_lines, make_pretty_table_lines
    # print("Imported from local")

display_function = make_pretty_table_lines

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

    def do_mode(self, mode):
        """Usage: mode <mode>\nSets the display mode. Available modes: raw, list, csv, table, pretty_table"""
        global display_function
        if mode not in ('raw', 'list', 'csv', 'table', 'pretty_table'):
            print("Invalid mode. Available modes: raw, list, csv, table, pretty_table")
            return
        display_function = eval(f"make_{mode}_lines")
        print(f"Mode set to '{mode}', display function: {display_function.__name__}")

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

    def do_insert(self, line):
        """Usage: insert into <tablename> values(<values>)\nInserts a new record in the specified table"""
        line = f"insert {line}{';' if not line.endswith(';') else ''}"
        print(line)
        print()
        try:
            numrecs = self.connection.execute(line).fetchone()
            print(f"Total: {numrecs} record(s) after insertion.")
        except Exception as e:
            print(e)
        finally:
            print()
            
    def do_select(self, line):
        """Executes an SQL 'select' command"""
        line = f"select {line}{';' if not line.endswith(';') else ''}"
        print(line)
        print()
        try:
            for l in display_function(self.connection.execute(line)):
                print(l)
        except Exception as e:
            print(e)
        finally:
            print()

    def do_view(self, table):
        """Usage: view <tablename>\nShows the entire table using external utility 'dbfview' """
        table = self.get_table(table)
        if table:
            subprocess.run(['dbfview', table.filename])
        else:
            print(f"Table '{table}' not found.")

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
    argslen = len(sys.argv)
    # if argslen > 1:
    #     parser.add_argument("dirname", nargs=1, default=".", help="The dBase III+ directory to open.")

    if argslen > 1:
        parser.add_argument("dirname", nargs=1, default=".", help="The dBase III+ directory to open.")
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {version}")

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


