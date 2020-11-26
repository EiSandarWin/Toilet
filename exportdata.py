#!usr/bin/env python
import sqlite3
from datetime import datetime
import csv
from ftplib import FTP
import fileinput
import time
import os
from datetime import datetime, timedelta
import logTable

sqlite_file = '/home/pi/Desktop/simple_flask/ToData.db'
conn = sqlite3.connect(sqlite_file, check_same_thread=False)


ftp = FTP()

cur = conn.cursor()

cur.execute("SELECT DISTINCT date, kinds ,mode  FROM DATA JOIN SYSTEM on DATA.date > SYSTEM.FTPTIME ")
start_time =time.time()
DataSend = "/home/pi/Desktop/simple_flask/output.csv"
    #Export dat into csv file


with open (DataSend, "w+") as out_csv_file:
    csv_out = csv.writer(out_csv_file, delimiter = ";")
    csv_out.writerow([d[0] for d in cur.description])
    for result in cur:
        csv_out.writerow(result)
        
    

Output_Directory = "/log/BH3030386_3/"
cur.close()
duration = time.time() - start_time
print (duration)
filesize = os.path.getsize(DataSend)
print (str(filesize)+"byte")



ftp.set_debuglevel(2)
ftp.connect("sv2255.xserver.jp", 21)
ftp.login("flcadmin@4leaf-clover.com", "2XUvgQ32")
print(ftp.pwd())
now = datetime.now()
current_time =now.strftime('%Y/%m/%d %H:%M:%f')
    
ftp.cwd(Output_Directory)

foutput = open (DataSend, "rb")
   
ftp.storbinary('STOR %s' % os.path.basename(DataSend) , foutput)
FTP = logTable.insert_table1(FTPTIME=current_time)   

foutput.close()
    
        

    
   


