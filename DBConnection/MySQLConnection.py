import mysql.connector


class MySQLDb:
    def __init__(self, host, port, user, password, dbname=None):
        self.conn = mysql.connector.connect(host=host, port=port, user=user, password=password, database=dbname)
        self.cursor = self.conn.cursor(buffered=True)

    def create_database(self, dbname):
        query = f"CREATE DATABASE IF NOT EXISTS {dbname}"
        if self.cursor is not None:
            self.cursor.execute(query)
            self.cursor.execute('SHOW DATABASES')

    def create_table(self, table, dbname=None, **kwargs):
        query1 = f"USE {dbname}"
        query2 = f'CREATE TABLE IF NOT EXISTS {table}('
        for key, value in kwargs.items():
            query2 += f'{key} {value},'
        query2 = query2[:-1]
        query2 += ")"
        print(query2)
        if self.cursor is not None:
            if dbname is not None:
                self.cursor.execute(query1)
            self.cursor.execute(query2, multi=True)
            self.cursor.execute("SHOW TABLES")
            if table in self.cursor:
                print(table)

    def insert_data(self, table, column_data: dict):
        columns = ', '.join(column_data.keys())
        placeholders = ', '.join(['%s'] * len(column_data))
        values = list(column_data.values())

        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        print(query)
        if self.cursor is not None:
            self.cursor.execute(query, values)
            self.cursor.execute(f"SELECT * from {table}")
            result = self.cursor.fetchall()
            for row in result:
                print(row)
        self.conn.commit()
        result = 'inserted values are \n'
        for key, value in column_data.items():
            result += f'{key} : {value},\n'
        print(result)

    def get_data(self, table, column_list: list, condition=None):
        columns = ', '.join(column_list)
        if condition is not None:
            query = f"SELECT {columns} FROM {table} WHERE {condition}"
        else:
            query = f"SELECT {columns} FROM {table}"
        print(query)
        if self.cursor is not None:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            for row in result:
                print(row)
        self.conn.commit()


    def update_data(self, table, column_data: dict, condition = None):
        columns = list(column_data.keys())
        values = list(column_data.values())
        query = f"UPDATE {table} SET "
        for key, value in column_data.items():
            query += f"{key} = '{value}',"
        query = query[:-1]
        if condition is not None:
            query += f' WHERE {condition}'
        print(query)
        if self.cursor is not None:
            self.cursor.execute(query)
            self.cursor.execute(f"SELECT * from {table}")
            result = self.cursor.fetchall()
            for row in result:
                print(row)
        self.conn.commit()
