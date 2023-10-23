import sqlite3
from sqlite3 import Error
import unittest


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


class TestCreateTable(unittest.TestCase):

    def test_create_table_success(self):
        conn = sqlite3.connect(':memory:')
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS test_table (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        );
        """
        create_table(conn, create_table_sql)
      
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='test_table';")
        result = cursor.fetchone()

        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
