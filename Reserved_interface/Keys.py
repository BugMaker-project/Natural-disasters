import xlrd
import xlwt
from tkinter import *
from Reserved_interface.Error import *
def returnObject(keysXlsx:str):
    """Read File,Return Book Object."""
    keys=xlrd.open_workbook(keysXlsx)
    return keys
def read(Books:xlrd.book.Book):
    """Read Objects to return List"""
    