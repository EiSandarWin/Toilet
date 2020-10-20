import sqlite3
from sqlite3 import Error


def sql_connection():

    try:
        con = sqlite3.connect('testing.db')
        print("Connection is established :Database is created in memo")
    
    except Error:
        print(Error)

    finally:
       con.close()
    
sql_connection()


