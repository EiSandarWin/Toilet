import sqlite3


try:
    conn = sqlite3.connect('toiletData.db')
    c = conn.cursor()
    c.execute("INSERT INTO Variable(currentdate, name, phoneno) VALUES (date('now'), '?', '?')")
    conn.commit()
finally:
    conn.close()