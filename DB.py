import sqlite3

class DB:
    def __init__(self):
        self.url = r"C:\Users\Test\PycharmProjects\Test\DB.sqlite"

    def query(self, query):
        """Regular Query To The Database"""
        try:
            conn = sqlite3.connect(self.url)
            cursor = conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except sqlite3.Error as error:
            print('Error occured - ', error)
        finally:
            if conn:
                conn.close()
                print('SQLite Connection closed')

    def Uquery(self, query):
        """Update Query To The Database"""
        try:
            conn = sqlite3.connect(self.url)
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            return True
        except sqlite3.Error as error:
            print('Error occured - ', error)
            return False
        finally:
            if conn:
                conn.close()
                print('SQLite Connection closed')


