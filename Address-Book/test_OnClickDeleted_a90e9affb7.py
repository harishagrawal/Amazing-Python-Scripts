import unittest
from tkinter import *
import tkinter.messagebox as messagebox

class TestOnClickDeleted(unittest.TestCase):

    def test_onClickDeleted_success(self):
        Name = "John"
        expected = "John got deleted"
        
        with self.assertLogs():
            self.assertEqual(onClickDeleted(), expected)
        self.assertLogs()
        
    def test_onClickDeleted_emptyName(self):
        Name = ""
        expected = "Name cannot be empty"
        
        with self.assertRaises(Exception):
            self.assertEqual(onClickDeleted(), expected)

if __name__ == '__main__':
    unittest.main()
