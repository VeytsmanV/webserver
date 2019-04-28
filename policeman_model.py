class PolicemanModel:
    def __init__(self, connection):
        self.connection = connection

    def init_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS policeman
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                             policeman_name VARCHAR(50),
                             password_hash VARCHAR(128)
                             )''')
        cursor.close()
        self.connection.commit()

    def insert(self, policeman_name, password_hash):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO policeman
                          (policeman_name, password_hash)
                          VALUES (?,?)''', (policeman_name, password_hash))
        cursor.close()
        self.connection.commit()

    def get(self, policeman_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM policeman WHERE id = ?", (str(policeman_id),))
        row = cursor.fetchone()
        return row

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM policeman")
        rows = cursor.fetchall()
        return rows

    def exists(self, policeman_name, password_hash):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM policeman WHERE policeman_name = ? AND password_hash = ?", (policeman_name, password_hash))
        row = cursor.fetchone()
        return (True, row[0]) if row else (False,)
