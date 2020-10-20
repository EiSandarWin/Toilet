import time
import datetime


Time = time.asctime(time.localtime(time.time()))
with open("/home/pi/Desktop/simple_flask/LOG/shutdown.txt", "a+") as f:
    f.write( "Shutdown: " + Time + "\n")
    f.close()