import unittest
import sqlite3
from sqlite3 import Error

def create_connection(database):
    conn = None
    try:
        conn = sqlite3.connect(database)
    except Error as e:
        pass
    return conn

class TestCreateConnection(unittest.TestCase):

    def test_create_connection_success(self):
        db_file = "test.db" # TODO: Change the value with a valid database file
        conn = create_connection(db_file)
        self.assertIsNotNone(conn) # Check if connection object is not None
        
    def test_create_connection_failure(self):
        db_file = "invalid_file.db" # TODO: Change the value with an invalid database file
        conn = create_connection(db_file)
        self.assertIsNone(conn) # Check if connection object is None
        
        
if __name__ == '__main__':
    unittest.main()
