import sqlite3
from datetime import datetime
import csv
from ftplib import FTP
import fileinput
import time
import os

sqlite_file = '/home/pi/Desktop/simple_flask/ToData.db'
conn = sqlite3.connect(sqlite_file, check_same_thread=False)

cur = conn.cursor()
cur.execute("SELECT date, time, kinds ,mode  FROM DATA where kinds = 1")

#Export dat into csv file
with open ("output.csv", "wb") as out_csv_file:
    csv_out = csv.writer(out_csv_file, delimiter = ";")
    csv_out.writerow([d[0] for d in cur.description])
    for result in cur:
        csv_out.writerow(result)


Output_Directory = "/log"
#cur.close()

DataSend = "/home/pi/Desktop/simple_flask/output.csv"


ftp = FTP()
ftp.set_debuglevel(2)
ftp.connect("sv2255.xserver.jp", 21)
ftp.login("flcadmin@4leaf-clover.com", "2XUvgQ32")
print(ftp.pwd())

ftp.cwd(Output_Directory)

foutput = open (DataSend, "rb")

ftp.storbinary('STOR %s' % os.path.basename(DataSend) , foutput, 1024)

foutput.close()




