import sqlite3
from datetime import datetime

# from wiringthread import mytable


sqlite_file = '/home/pi/Desktop/simple_flask/ToData.db'
conn = sqlite3.connect(sqlite_file, check_same_thread=False)


def create_table():
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS DATA(id INTEGER PRIMARY KEY,kinds INT, date DATETIME,time DATETIME, mode INT, message TEXT , duration FLOAT )"  )     

    cur.close()

def create_table():
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS SYSTEM(FTPTIME DATETIME)")
       
    cur.close()

    

def insert_table1(FTPTIME):
    cur = conn.cursor()
    cur.execute("INSERT INTO SYSTEM (FTPTIME ) VALUES (?)",
                (FTPTIME,))

    conn.commit()
    cur.close()
    return cur.lastrowid



def insert_table(kinds, date,time, mode, message, duration=0):
    cur = conn.cursor()
    cur.execute("INSERT INTO DATA(kinds, date, time, mode, message, duration) VALUES (?, ?, ?, ?, ?,?)",
                (kinds, date, time, mode, message, duration))

    conn.commit()
    cur.close()
    return cur.lastrowid

def one_day():
    cur = conn.cursor()
    cur.execute("select kinds, date, count(date) from DATA WHERE mode = 1 group by date, kinds order by date DESC ,kinds")
    return cur.fetchall()


def one_hour(date, gender):
    cur = conn.cursor()
    cur.execute("select strftime('%H:00:00', time),"
                " count(strftime('%H', time)) from DATA where mode = 1 AND date =? AND kinds=? "
                "group by strftime('%H', time) order by kinds",
                (date, gender,))
    return cur.fetchall()

#def average_one_day():
#    cur = conn.cursor()
#    cur.execute("select kinds, date, count(date), avg(duration) from DATA WHERE mode = 1 group by date order by date DESC ,kinds")
#    return cur.fetchall()

def average_one_day(gender):
    cur = conn.cursor()
    cur.execute("select date,avg(duration),"
                "count(date) from DATA where mode =1  AND kinds = ?"
                "group by date order by date DESC, kinds",
                (gender,))

    return cur.fetchall()

def average_one_hour(date,gender):
    cur = conn.cursor()
    cur.execute("select strftime('%H:00:00',time),avg(duration),"
                "count(strftime('%H',time)) from DATA where mode = 1 AND date = ? AND kinds = ?"
                "group by strftime('%H',time) order by kinds",
                (date, gender,))
    return cur.fetchall()


def update_table(user_id, duration):
    cur = conn.cursor()
    cur.execute("UPDATE DATA SET duration = ? WHERE id=?", (duration, user_id))
    conn.commit()
    cur.close()

def update_table1(FTP):
    cur = conn.cursor()
    cur.execute("UPDATE SYSTEM SET FTP = ? ",(FTP))
    conn.commit()
    cur.close()
#
#print(average_one_day())