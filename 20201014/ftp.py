#coding = 'UTF_8'
from ftplib import FTP
import os
import fileinput
import time




File2Send = "/home/pi/Desktop/simple_flask/LOG/log.txt"
FileSend = "/home/pi/Desktop/simple_flask/LOG/log2.txt"
PowerSend = "/home/pi/Desktop/simple_flask/LOG/powerlog.txt"
ShutdownSend = "/home/pi/Desktop/simple_flask/LOG/shutdown.txt"
Status = "/home/pi/Desktop/simple_flask/LOG/status_log.txt"
Output_Directory = "/log"

ftp = FTP()
ftp.set_debuglevel(2)
ftp.connect ("sv2255.xserver.jp", 21)
ftp.login("flcadmin@4leaf-clover.com", "2XUvgQ32")

print (ftp.pwd())

ftp.cwd(Output_Directory)
#session = ftplib.FTP("sv2255.xserver.jp", "flcadmin@4leaf-clover.com", "2XUvgQ32")

#def send_file():
    
fp = open(File2Send, "rb")
fp1 = open(FileSend, "rb")
fp2 = open(PowerSend, "rb")
 #   fp3 = open(PowerSend, "rb")
 #   fp3 = open(ShutdownSend, "rb")


ftp.storbinary('STOR %s' % os.path.basename(File2Send) , fp, 1024)
ftp.storbinary('STOR %s' % os.path.basename(FileSend) , fp1, 1024)
ftp.storbinary('STOR %s' % os.path.basename(PowerSend) , fp2, 1024)
 #   session.storbinary('test' , fp3)
 #   session.storbinary('STOR %s' % os.path.basename(File2Send) , fp3, 1024)

fp.close()
fp1.close()
fp2.close()
 #   fp3.close()
 #   session.quit()
#send_file()

#def schedules_send():

 #    while True:
#         send_file()
 #        time.sleep(60)

#x = threading.Thread(target=schedules_send,args=())
#x.start()
    







