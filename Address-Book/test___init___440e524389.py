import unittest
from tkinter import *
import tkinter.messagebox

class TestInit(unittest.TestCase):

    def test_init_success_case(self):
        root = Tk()
        parent = root.winfo_toplevel()
        app = __init__(self, parent)
        self.assertIsInstance(app, __init__)
        root.destroy()

    def test_init_failure_case(self):
        root = Tk()
        parent = root.winfo_toplevel()
        with self.assertRaises(TypeError):
            app = __init__(parent)
        root.destroy()

if __name__ == '__main__':
    unittest.main()
