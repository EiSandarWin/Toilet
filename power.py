import time


currentTime = time.asctime(time.localtime(time.time()))
with open("/home/pi/Desktop/simple_flask/LOG/powerlog.txt", "a+") as f:
    f.write("Run at: " + currentTime + "\n")
    f.close()



