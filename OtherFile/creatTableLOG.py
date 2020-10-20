import sqlite3 as lite
import sys

sqlite_file = 'toiletData.db'
conn = lite.connect(sqlite_file)
c = conn.cursor()
conn.execute ("CREATE TABLE LOG_BOY(id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp DATETIME, annountime DATETIME, logtime DATETIME)")
conn.commit()
conn.close()

