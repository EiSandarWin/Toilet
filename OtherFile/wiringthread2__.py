# coding: UTF -8
import wiringpi as wiringpi
#from time import sleep
from datetime import datetime
import time
import threading
import pygame
from signal import pause
import logTable

logTable.create_table()




pygame.mixer.init(frequency=44800, size=-16, channels=2, buffer =614)
pygame.mixer.stop()

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

global counter
counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
user_id = 0


def count2_people():
    now = datetime.now()
    date_time = now.strftime("[%Y/%m/%d")
    f = open(log2_file, "r", )
    data1 = f.read().split("\n")
    f.close()
    temp = 0
    for x in data1:
        if date_time in x:
            temp = temp + 1

    return temp





def aa():
    global counter1
    global user_id
    global duration
    counter1 += 1
    print "女子 duration : 1 minutes", counter1
    sound1 = pygame.mixer.Sound('/home/pi/Desktop/simple_flask/announce/announce1.wav')
    channel1 = pygame.mixer.Channel(1)
    channel1.play(sound1)
    channel1.set_volume(0.0, 1.0)
    logTable.update_table(user_id, 1)



def bb():
    global counter2
    global user_id
    global duration
    counter2 += 1
    print "女子 duration : 2 minutes", counter2
    sound1 = pygame.mixer.Sound('/home/pi/Desktop/simple_flask/announce/announce2.wav')
    channel1 = pygame.mixer.Channel(1)
    channel1.play(sound1)
    channel1.set_volume(0.0, 1.0)
    logTable.update_table(user_id, 2)


def cc():
    global counter3
    global user_id
    global duration
    counter3 += 1
    print "女子 duration : 3 minutes", counter3
    sound1 = pygame.mixer.Sound('/home/pi/Desktop/simple_flask/announce/announce3.wav')
    channel1 = pygame.mixer.Channel(1)
    channel1.play(sound1)
    channel1.set_volume(0.0, 1.0)
    logTable.update_table(user_id, 3)


def dd():
    global counter4
    global user_id
    global duration
    counter4 += 1
    print "女子 duration : 4  minutes", counter4
    sound1 = pygame.mixer.Sound('/home/pi/Desktop/simple_flask/announce/announce4.wav')
    channel1 = pygame.mixer.Channel(1)
    channel1.play(sound1)
    channel1.set_volume(0.0, 1.0)
    logTable.update_table(user_id, 4)



t = threading.Timer(60,aa)
t1 = threading.Timer(120,bb)
t2 = threading.Timer(180, cc)
t3 = threading.Timer(240, dd)

def start_waiting():
    global t
    global t1
    global t2
    global t3
    t = threading.Timer(60, aa)
    t1 = threading.Timer(120, bb)
    t2 = threading.Timer(180, cc)
    t3 = threading.Timer(240, dd)

    t.start()
    t1.start()
    t2.start()
    t3.start()

def stop_waiting():
    t.cancel()
    t1.cancel()
    t2.cancel()
    t3.cancel()

def start():
    global counter
    global user_id
    global dur
    read0 = 1
    log2count = count2_people()
    while True:
        time.sleep(0.1)
        read1 = wiringpi.digitalRead(GPIO_SW)
        #        print "read1= %d" % read1


        if read0 == read1:

            continue

        time.sleep(0.05)
        read2 = wiringpi.digitalRead(GPIO_SW)
        now = datetime.now()
        current_date = now.strftime("%Y:%m:%d")
        current_time = now.strftime("%H:%M:%S")
        end = datetime.now()
        #        print "read0= %d" % read0
        if read1 == read2:
            if read1 == 1:
                log2count = log2count + 1
                print "person count:" + str(log2count)
                print now
                print " 女子トイレ使用開始\n"
                start_waiting()
                wiringpi.digitalWrite(GPIO_LED, 0) # switch on LED. Sets port 18 to 0 (3V3, on)
                store2_log( str(log2count) + "女子 トイレ使用開始\n")

                user_id = logTable.insert_table(2, current_date, current_time, 1, "Girl Busy", 1.0)
                status2("Busy")





            else:
                stop_waiting()
                wiringpi.digitalWrite(GPIO_LED, 1) # switch off LED. Sets port 18 to 1 (0V, off)
                pygame.mixer.Channel(1).stop()
                store2_log("女子 トイレ使用終了\n")
                user_id = logTable.insert_table(2,current_date, current_time, 2, "Girl Free", 0.0)
                status2("Free")
                print "\n女子トイレ使用終了"
                print end

                

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


