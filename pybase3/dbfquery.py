#!/usr/bin/env python3
#-*- coding: utf_8 -*-

import cmd, subprocess
import readline

returnline = "\nBye, sqlers...\n"

class SQL(cmd.Cmd):

    prompt = "sql> "

    def emptyline(self):
        print('', end='')
        return

    def do_select(self, line):
        """Executes an SQL 'select' command"""
        print(f"select {line}{';' if not line.endswith(';') else ''}")

    def do_EOF(self, eof):
        """Exit the program"""
        print(returnline)
        raise SystemExit(0)

    def do_exit(self, eof):
        """Exit the program"""
        return self.do_EOF('')

def main():
    sql = SQL()
    subprocess.run(['clear'])
    try:
        sql.cmdloop()
    except KeyboardInterrupt:
        print(returnline)

if __name__ == '__main__':
    main()


