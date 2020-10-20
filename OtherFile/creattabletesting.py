import sqlite3

from sqlite3 import Error

def sql_connection():
    
    try:
        con = sqlite3.connect('testing.db')
        return con
    
    except Error:
        print(Error)


def sql_table(con):

    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE employees(id integer PRIMARY KEY AUTOINCREMENT, name text, phoneno integer, hiredate date)")
    con.commit()

con = sql_connection()

sql_table(con)