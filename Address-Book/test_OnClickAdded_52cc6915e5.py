import pytest
from tkinter import *
import tkinter.messagebox

def TestOnClickAdded_52cc6915e5():
    # Test case 1: Verify if the correct message box is displayed after clicking the "OK" button
    Name = Entry()
    Name.insert(0, "John Doe") # TODO: Change the value as per requirement
    tkinter.messagebox.showinfo = pytest.Mock()

    onClickAdded()

    tkinter.messagebox.showinfo.assert_called_with(" ", "John Doe got added")

    # Test case 2: Verify if the Name entry is cleared after the message box is closed
    Name = Entry()
    Name.insert(0, "Jane Smith") # TODO: Change the value as per requirement

    onClickAdded()

    assert Name.get() == ""
