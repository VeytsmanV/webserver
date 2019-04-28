import sqlite3

class DB:
    def __init__(self):
        connection = sqlite3.connect('criminal.db', check_same_thread = False)
        self.connection = connection

    def get_connection(self):
        return self.connection

    def __del__(self):
        self.connection.close()