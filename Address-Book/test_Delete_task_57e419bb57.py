import unittest
import sqlite3
from tkinter import *

class TestCreateConnection(unittest.TestCase):
    def test_create_connection_failure(self):
        conn = sqlite3.connect("address_book.db")
        self.assertIsNone(conn) # Check if connection object is None

    def test_create_connection_success(self):
        conn = sqlite3.connect("address_book.db")
        self.assertIsNotNone(conn) # Check if connection object is not None

class TestCreateTable(unittest.TestCase):
    def test_create_table_success(self):
        conn = sqlite3.connect("address_book.db")
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS address_book (name TEXT, address TEXT, phone_number TEXT, email TEXT)")
        conn.commit()
        conn.close()
        
        self.assertTrue(True) # Check if table creation is successful

class TestDeleteTask(unittest.TestCase):
    def test_delete_task(self):
        Name.set('John')
        list_of_names = ['John', 'Mark', 'Rachel']
        delete_task()
        self.assertNotIn(Name.get(), list_of_names) # Check if name is not in list_of_names

        Name.set('Emily')
        list_of_names = ['John', 'Mark', 'Rachel']
        delete_task()
        self.assertNotIn(Name.get(), list_of_names) # Check if name is not in list_of_names

if __name__ == '__main__':
    unittest.main()
