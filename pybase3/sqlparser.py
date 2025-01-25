#-*- coding: utf-8 -*-

# Provides a class to parse SQL statements.


# Import the necessary modules.
import subprocess, re


class SQLParser:
    """
    The SQLParser class provides a simple way to parse SQL statements. 
    The tokenize() method splits the SQL statement into tokens, while the parse() method 
    parses the SQL statement. 
    The parse_columns(), parse_tables(), and parse_where() methods parse 
    the columns, tables, and WHERE clause, respectively. 
    The parse_order() method parses the ORDER BY clause if present.
    The test() function demonstrates how to use the SQLParser class.
   
    """

    sqlkeywords = ["SELECT", "INSERT", "UPDATE", "DELETE", "VALUES", "INTO",
                   "FROM", "WHERE", "ORDER", "BY", "AS", 
                   "LIKE", "SET", "AND", "OR", "NOT", 
                   "IS", "NULL"]
    
    def __init__(self, sqlcmd):
        """
        Initialize the SQLParser object.
        
        Args:
            sqlcmd (str): The SQL statement to parse.
        
        """
        self.sql = re.sub(r"(values|VALUES)\(", "VALUES (", sqlcmd, flags=re.IGNORECASE)
        self.sql = re.sub(r"\s*\=\s*", "=", self.sql, flags=re.IGNORECASE)
        self.tokens = self.tokenize()
        self.pos = 0
        self.parsed = self.parse()
        self.pos = 0

    def tokenize(self):
        """
        Tokenize the SQL statement.
        
        Returns:
            list: A list of tokens.
        
        """
        tokens = []
        token = ""
        in_string = False

        for char in self.sql:
            if char == "'":
                in_string = not in_string
            if char == " " and not in_string:
                token = token.strip().rstrip(',;').lstrip('(').rstrip(')')
                tokens.append(token.upper() if token.upper() in self.sqlkeywords else token)
                token = ""
            else:
                token += char

        if token:
            token = token.strip().rstrip(',;').lstrip('(').rstrip(')')
            tokens.append(token.upper() if token.upper() in self.sqlkeywords else token)

        if tokens[-1] != ";":
            tokens.append(";")

        return tokens

    def parse(self):
        """
        Parse the SQL statement.
        
        Returns:
            dict: A dictionary of parsed elements.
        
        """
        
        if not len(self.tokens):
            raise ValueError("Invalid SQL statement or failure to invoke tokenizer.")
        
        parsed = {}

        if self.tokens[self.pos].upper() == "SELECT":
            parsed["command"] = "SELECT"
            self.pos += 1
            parsed["columns"] = self.parse_columns()
            parsed["tables"] = self.parse_tables()
            parsed["where"] = self.parse_where()
            parsed["order"] = self.parse_order()
        elif self.tokens[self.pos].upper() == "INSERT":
            parsed["command"] = "INSERT"
            self.pos += 1
            if self.tokens[self.pos].upper() == "INTO":
                self.pos += 1
                if self.tokens[self.pos] == ";":
                    raise ValueError("Invalid SQL statement. No table name found after INTO.")
                parsed["tables"] = [self.tokens[self.pos]]
            else:
                raise ValueError("Invalid SQL statement. INSERT clause must be followed by INTO.")
            parsed["values"] = self.parse_values()
        elif self.tokens[self.pos].upper() == "UPDATE":
            # raise NotImplementedError("UPDATE command not supported yet.")
            parsed["command"] = "UPDATE"
            self.pos += 1
            if self.tokens[self.pos] == ";":
                raise ValueError("Invalid SQL statement. No table name found after UPDATE.")
            parsed["tables"] = [self.tokens[self.pos]]
            self.pos += 1
            parsed["updates"] = self.parse_updates()
            parsed["where"] = self.parse_where()
        elif self.tokens[self.pos].upper() == "DELETE":
            # raise NotImplementedError("DELETE command not supported yet.")
            parsed["command"] = "DELETE"
            self.pos += 1
            if self.tokens[self.pos] == ";":
                raise ValueError("Invalid SQL statement. No table name found after DELETE.")
            elif self.tokens[self.pos].upper() == "*":
                self.pos += 1
            if self.tokens[self.pos].upper() != "FROM":
                raise ValueError("Invalid SQL statement. No FROM clause found after DELETE.")
            self.pos += 1
            parsed["tables"] = [self.tokens[self.pos]]     
            parsed["where"] = self.parse_where()
        else:
            raise NotImplementedError("Only SELECT, INSERT, UPDATE and DELETE commands are supported.")

        if parsed['command'] == 'SELECT':
            for entry in parsed.get('columns'):
                if entry['table'] is None:
                    entry['table'] = parsed.get('tables')[0]
                else:
                    if entry['table'] not in parsed.get('tables'):
                        raise ValueError(f"Invalid SQL statement. Table {entry['table']} not found.")  
        
        return parsed

    def parse_updates(self):
        endmark = len(self.tokens)
        if ";" in self.tokens:
            endmark = self.tokens.index(";")
        if "WHERE" in self.tokens:
            endmark = self.tokens.index("WHERE")
    
        updates = []
        if self.tokens[self.pos] != "SET":
            raise ValueError("Invalid SQL UPDATE statement. No SET clause found.")
        self.pos += 1
        while self.pos < endmark:
            if self.tokens[self.pos] != ";":
                updates.append(self.tokens[self.pos])
            self.pos += 1
        return updates
    
    def parse_columns(self):
        """
        Parse the columns in the SQL statement.
        
        Returns:
            list: A list of columns.
        
        """
        columns = []

        self.pos = 1

        while self.tokens[self.pos].upper() != "FROM":
            token = self.tokens[self.pos]
            table, column = None, None
            if token == "AS":
                self.pos += 1    
                token = self.tokens[self.pos]
                columns[-1]["alias"] = token
            else:
                if self.pos == 0 or self.tokens[self.pos - 1] != "AS":
                    splitted = token.split(".")
                    if len(splitted) == 2:
                        table, column = splitted
                    else:
                        column = token
                    columns.append(dict(column=column, alias=column, table=table))
            self.pos += 1
        return columns

    def parse_tables(self):
        """
        Parse the table or tables in the SQL statement.
        
        Returns:
            list:  table/s name/s.
        
        """

        tables = []
        # self.pos += 1
        pos = self.tokens.index("FROM")
        if pos == -1:
            raise ValueError("Invalid SQL statement. No FROM clause found.")
        self.pos = pos + 1

        endmark = len(self.tokens)
        if "WHERE" in self.tokens:
            endmark = self.tokens.index("WHERE")
        elif "ORDER" in self.tokens:
            endmark = self.tokens.index("ORDER")

        while self.pos < endmark:
            if self.tokens[self.pos] != ";":
                tables.append(self.tokens[self.pos])
            self.pos += 1

        return tables

    def parse_where(self):
        """
        Parse the WHERE clause in the SQL statement.
        
        Returns:
            str: The WHERE clause.
        
        """
        pos = self.tokens.index("WHERE") if "WHERE" in self.tokens else -1
        if pos == -1:
            return ""
        
        where = ""

        posend = self.tokens.index("ORDER") if "ORDER" in self.tokens else len(self.tokens)

        self.pos = pos + 1

        while self.pos < posend:
            if self.tokens[self.pos] != ";":
                where += self.tokens[self.pos] + " "
            self.pos += 1
        
        return where.strip()

    def parse_order(self):
        """
        Parse the ORDER BY clause in the SQL statement.
        
        Returns:
            str: The ORDER BY clause.
        
        """
        
        pos = self.tokens.index("ORDER") if "ORDER" in self.tokens else -1
        if pos == -1:
            return ""
        
        order = ""

        self.pos = pos + 2

        while self.pos < len(self.tokens):
            if self.tokens[self.pos] != ";":
                order += self.tokens[self.pos] + " "
            self.pos += 1

        return order.strip()

    def parse_values(self):
        """
        Parse the values in the SQL INSERT statement.
        
        Returns:
            list:  values to be inserted.
        
        """

        values = []
        # self.pos += 1
        pos = self.tokens.index("VALUES")
        if pos == -1:
            raise ValueError("Invalid SQL statement. No VALUES clause found.")
        self.pos = pos + 1

        endmark = len(self.tokens)
        if "WHERE" in self.tokens:
            endmark = self.tokens.index("WHERE")
        elif "ORDER" in self.tokens:
            endmark = self.tokens.index("ORDER")

        while self.pos < endmark:
            if self.tokens[self.pos] != ";":
                values.append(self.tokens[self.pos])
            self.pos += 1

        return values

def test():
    """
    Test the SQLParser class.
    
    """
    subprocess.run(["clear"])

    print("Testing SELECT statement:")
    sql = "SELECT first_name, last_name, employees.age AS years FROM employees WHERE age > 30 order by last_name asc;"
    print (f"'{sql}'\n")
    parser = SQLParser(sql)
    for key in parser.parsed: print(f"{key} = {parser.parsed[key]}")
    input("\nPress <Enter> to continue...\n")
    print("Testing INSERT statement:")
    sql = "INSERT INTO employees VALUES ('John', 'Doe', 35);"
    print (f"'{sql}'\n")
    parser = SQLParser(sql)
    for key in parser.parsed: print(f"{key} = {parser.parsed[key]}")
    input("\nPress <Enter> to continue...\n")
    print("Testing UPDATE statement:")
    sql = "UPDATE employees SET age = 36 WHERE last_name = 'Doe';"
    print (f"'{sql}'\n")
    parser = SQLParser(sql)
    for key in parser.parsed: print(f"{key} = {parser.parsed[key]}")
    input("\nPress <Enter> to continue...\n")
    print("Testing DELETE statement:")
    sql = "DELETE FROM employees WHERE last_name = 'Doe';"
    print (f"'{sql}'\n")
    parser = SQLParser(sql)
    for key in parser.parsed: print(f"{key} = {parser.parsed[key]}")
    input("\nPress <Enter> to continue...\n")


if __name__ == "__main__":
    test()

