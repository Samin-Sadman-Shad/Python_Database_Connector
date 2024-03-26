import psycopg2


class PostgresDB():
    def __init__(self, host, port, db_name, user, password):
        self.host = host
        self.port = port
        self.db_name = db_name
        self.user = user
        self.password = password

    def create_connection(self):
        self.conn = psycopg2.connect(
            dbname=self.db_name,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port)
        # Open a cursor to perform database operations
        self.cursor = self.conn.cursor()


    def insert_data(self, table, column_data):
        columns = ', '.join(column_data.keys())
        placeholders = ', '.join(['{}'] * len(column_data))
        values = tuple(column_data.values())

        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        if self.cursor is not None:
            self.cursor.execute(query, values)
            inserted_data = self.conn.fetchall()
            self.conn.commit()
            return dict(zip(column_data.keys(), inserted_data))
        else:
            raise Exception("cursor is not defined")

    def update_data(self, table, column_data, condition):
        columns = column_data.keys()
        values = column_data.values()

        query = f"UPDATE {table} SET "
        for column, value in column_data.items():
            query += f'{column} = {value}'
        query += f' WHERE {condition}'

        if self.cursor is not None:
            self.cursor.execute(query)
            self.conn.commit()
        else:
            raise Exception("cursor is not defined")

    def get_data(self, table, column_names):
        columns = ', '.join(column_names)
        query = f"SELECT {columns} FROM {table}"
        if self.conn.cursor is not None:
            self.cursor.execute(query)
            self.conn.commit()
        else:
            raise Exception("cursor is not defined")

    def delete_data(self, table, column, value):
        query = f'DELETE FROM {table} WHERE {column}={value}'
        if self.conn.cursor is not None:
            self.cursor.execute(query)
            self.conn.commit()
        else:
            raise Exception("cursor is not defined")
