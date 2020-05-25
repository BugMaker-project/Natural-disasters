import xlrd
from Error import *
def returnObject(keysXlsx: str):
    """Read File,Return Book Object."""
    keys = xlrd.open_workbook(keysXlsx)
    return keys
def read(Books: xlrd.book.Book):
    """Read Objects to return List"""
    ListOfXlsx = []
    sheet = Books.sheet_by_index(0)
    nrows = sheet.nrows
    for i in range(nrows):
        object = sheet.row_values(i)
        for j in object:
            ListOfXlsx.append(j)
    return ListOfXlsx
def isIn(EnterKey: str, Keys: list):
    return EnterKey.upper() in Keys
