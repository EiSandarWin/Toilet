# coding: UTF -8
import wiringpi as wiringpi
#from time import sleep
from datetime import datetime
import time
import threading

GPIO_LED = 18
GPIO_SW = 17

wiringpi.wiringPiSetupGpio()

wiringpi.pinMode(GPIO_LED, 1)  # sets GPIO 18 to output
wiringpi.pinMode(GPIO_SW, 0)  # sets GPIO 17 to input
wiringpi.pullUpDnControl(GPIO_SW, wiringpi.PUD_DOWN)

wiringpi.digitalWrite(GPIO_LED, 0)  # sets port 18 to 0 (0V, on)

log2_file = "./LOG/log2.txt"
error2_log = "./LOG/error2_log.txt"
status2_log = "./LOG/status2_log.txt"




def start():
    current_time = datetime.now()
    old_time = datetime.now()
    duration = 0
    mode = ""
    alert_duration = 60  # 1 min
    read0 = 1

    while True:
        time.sleep(0.1)
        read1 = wiringpi.digitalRead(GPIO_SW)
        #        print "read1= %d" % read1

        if mode == "Busy":
            duration = datetime.now() - old_time
            if duration.seconds >= alert_duration:
                print ("女子 duration :" + str(alert_duration/60))
                print("女子　Please go out")
                alert_duration = alert_duration  + 60
        else:
            old_time = datetime.now()

        if read0 == read1:

            continue

        time.sleep(0.05)
        read2 = wiringpi.digitalRead(GPIO_SW)
        start = datetime.now()
        end = datetime.now()
        #        print "read0= %d" % read0
        if read1 == read2:
            if read1 == 1:
                alert_duration = 60
                wiringpi.digitalWrite(GPIO_LED, 0) # switch on LED. Sets port 18 to 1 (3V3, on)
                mode = "Busy"
                store2_log("女子 トイレ使用開始\n")
                status2("Busy")
                print "\n 女子トイレ使用開始"
                print "start=%s\n" % start


            else:
                old_time = datetime.now()
                wiringpi.digitalWrite(GPIO_LED, 1) # switch off LED. Sets port 18 to 0 (0V, off)

                mode = "Free"
                store2_log("女子 トイレ使用終了\n")
                status2("Free")
                print "\n女子トイレ使用終了"
                print "end=%s" % end

        read0 = read1



def store2_log(log):
    now = datetime.now()
    date_time = now.strftime("[%Y/%m/%d  %H:%M:%S]")
    text_log = date_time + " " + log
    try:
        f = open(log2_file, "a+")
        f = f.write(text_log)
        f.close()
    except:
        store_error2("file open error!!\n")


def status2(log):
    #   print(log)
    try:
        f = open(status2_log, "w+")
        f.write(log)
        f.close()
    except:
        store_error2("file open error!!\n")


def store_error2(log):
    now = datetime.now()
    date_time = now.strftime("[%Y/%m/%d  %H:%M:%S]")
    text_log = date_time + " " + log
    try:
        f = open(error2_log, "a+")
        f.write(text_log)
        f.close()
    except:
        print("ERROR")

x1= threading.Thread(target = start)
x1.start()


