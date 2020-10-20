# coding: UTF -8
import wiringpi as wiringpi
# from time import sleep
from datetime import datetime
import time
import threading

GPIO_LED = 12
GPIO_SW = 26

wiringpi.wiringPiSetupGpio()

wiringpi.pinMode(GPIO_LED, 1)  # sets GPIO 12 to output
wiringpi.pinMode(GPIO_SW, 0)  # sets GPIO 26 to input
wiringpi.pullUpDnControl(GPIO_SW, wiringpi.PUD_DOWN)

wiringpi.digitalWrite(GPIO_LED, 0)  # sets port 26 to 0 (0V, on)

log_file = "./LOG/log.txt"
error_log = "./LOG/error_log.txt"
status_log = "./LOG/status_log.txt"


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
                print("customer duration :" + str(alert_duration / 60))
                print("Please go out")
                alert_duration = alert_duration + 60
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
                wiringpi.digitalWrite(GPIO_LED, 0)  # switch on LED. Sets port 12 to 1 (3V3, on)
                mode = "Busy"

                store_log("トイレ使用開始\n")
                status("Busy")
                print("\nトイレ使用開始")
                print("start=%s\n" % start)


            else:
                old_time = datetime.now()
                wiringpi.digitalWrite(GPIO_LED, 1)  # switch off LED. Sets port 12 to 0 (0V, off)
                mode = "Free"
                store_log("トイレ使用終了\n")
                status("Free")
                print("\nトイレ使用終了")
                print("end=%s" % end)

        read0 = read1


x = threading.Thread(target=start)


def store_log(log):
    now = datetime.now()
    date_time = now.strftime("[%Y/%m/%d  %H:%M:%S]")
    text_log = date_time + " " + log
    try:
        f = open(log_file, "a+")
        f = f.write(text_log)
        f.close()
    except:
        store_error("file open error!!\n")


def status(log):
    #   print(log)
    try:
        f = open(status_log, "w+")
        f.write(log)
        f.close()
    except:
        store_error("file open error!!\n")


def store_error(log):
    now = datetime.now()
    date_time = now.strftime("[%Y/%m/%d  %H:%M:%S]")
    text_log = date_time + " " + log
    try:
        f = open(error_log, "a+")
        f.write(text_log)
        f.close()
    except:
        print("ERROR")


x.start()
wiringthread2.start()
