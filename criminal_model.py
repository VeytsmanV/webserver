class CriminalsModel:
    def __init__(self, connection):
        self.connection = connection

    def init_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS criminals
                                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                 title VARCHAR(100),
                                 content VARCHAR(1000),
                                 policeman_id INTEGER
                                 )''')
        cursor.close()
        self.connection.commit()

    def insert(self, title, content, policeman_id):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO criminals
                          (title, content, policeman_id)
                          VALUES (?,?,?)''', (title, content, str(policeman_id)))
        cursor.close()
        self.connection.commit()

    def get(self, criminals_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM criminals WHERE id = ?", (str(criminals_id),))
        row = cursor.fetchone()
        return row

    def get_all(self, policeman_id=None):
        cursor = self.connection.cursor()
        if policeman_id:
            cursor.execute("SELECT * FROM criminals WHERE policeman_id = ?", (str(policeman_id),))
        else:
            cursor.execute("SELECT * FROM criminals")
        rows = cursor.fetchall()
        return rows

    def delete(self, criminals_id):
        cursor = self.connection.cursor()
        cursor.execute('''DELETE FROM criminals WHERE id = ?''', (str(criminals_id),))
        cursor.close()
        self.connection.commit()