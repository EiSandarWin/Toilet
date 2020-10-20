import sqlite3

con = sqlite3.connect('testing.db')

def sql_insert(con, entries):

    cursorObj = con.cursor()

    cursorObj.execute('INSERT INTO employees(name, phoneno, hiredate) VALUES (?,?,?)',entries)

    con.commit()

entries = ('Rathana Va', '080-987-776', '2020/05/09')

sql_insert(con, entries)