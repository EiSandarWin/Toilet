# coding: UTF -8
import sqlite3 as lite
import sys
from flask import Flask, render_template, Response
import threading ,time, json, random
from datetime import datetime
#import wiringthread

sqlite_file = 'toiletData.db'


conn = lite.connect(sqlite_file)
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS LOG(logboy TEXT , loggirl TEXT)")

#cur.execute("CREATE TABLE IF NOT EXISTS COUNT(id INTEGER PRIMARY KEY AUTOINCREMENT , countlog INTEGER)")

f = open("./LOG/log2.txt",'r+') 
loggirl = f.read()
f.close()

f = open("./LOG/log.txt",'r+') 
logboy = f.read()
f.close()
    
 
cur.execute("INSERT INTO LOG (logboy, loggirl) VALUES ('%s', '%s')"  %(logboy, loggirl))

cur.execute("SELECT logboy,COUNT(*) FROM LOG WHERE COUNT(*) ='BoyBusy'")
     
results = cur.fetchall()
#cur.execute("SELECT COUNT(logboy) FROM LOG GROUP BY logboy HAVING logboy =='BoyBusy'")

conn.commit()
conn.close()

#countlog = cur.execute("SELECT COUNT(logboy) FROM LOG GROUP BY logboy HAVING COUNT(*) == 'BoyBusy'")
#cur.execute("INSERT INTO COUNT(countlog) VALUES (?)", (countlog))

