from pandas import *
from openpyxl import *
xls = ExcelFile('/home/shubham/Personal Project/*/Library/book_list.xls')
df = xls.parse(xls.sheet_names[0])
# print (df.to_dict())
Data = (df.to_dict())
Book_Author_inlist = list(Data.values())
# print(Book_Author_list)
for Book_Author_dict in Book_Author_inlist:
    print(f"{Book_Author_dict}\n")
    print(type(Book_Author_dict))
    BookandAuthor = list(Book_Author_dict.values())
    print(BookandAuthor)
    print(type(BookandAuthor))

