

#coding = 'UTF_8'
from flask import Flask, render_template, Response, jsonify, request
import threading ,time, json, random
import wiringthread

import wiringthread2
#import ftp

import logTable



app = Flask(__name__)

status_log = "/home/pi/Desktop/simple_flask/LOG/status_log.txt"
status2_log = "/home/pi/Desktop/simple_flask/LOG/status2_log.txt"
power_log = "/home/pi/Desktop/simple_flask/LOG/powerlog.txt"
shutdown_log = "/home/pi/Desktop/simple_flask/LOG/shutdown.txt"

def store_log():
    try:
        f = open(status_log, "r+")
        return f.readline()
    except:
        print("error file")

        return "error"

def store2_log():
    try:
        f = open(status2_log, "r+")
        return f.readline()
    except:
        print("error file")
        return "error"



@app.route('/daily')
def data():
    results = logTable.one_day()
    return jsonify(results)

@app.route("/hourly", methods=['GET'])
def hourly_data():
    print(request.args["date"], request.args["gender"])
    results = logTable.one_hour(request.args["date"], request.args["gender"])
    return jsonify(results)



@app.route('/avg_one_day',methods = ['GET'])
def avg_one_day():
    print( request.args["gender"])
    results = logTable.average_one_day( request.args["gender"])
    return jsonify(results)


@app.route('/avg_one_hour', methods = ['GET'])
def avg_one_hour():
    print(request.args["date"], request.args["gender"])
    results = logTable.average_one_hour(request.args["date"], request.args["gender"])
    return jsonify(results)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1> <p>The resource could not be found.</p>",404


@app.route("/home")
def home():
    lable = "Boy Toilet"
    return render_template('home.html', lable = lable)
#
# @app.route('/home')
# def information():
#     status = status_log
#     status2 = status2_log
#     return render_template("home.html", status=status,status2 = status2)

@app.route('/log_power')
def log_power():
    try:
        f = open(power_log, "r+")
        return Response(f.read(), mimetype="text/plain")
    except:
        print("error file")

        return Response("error log", mimetype="text/plain")


@app.route('/log_shutdown')
def log_shutdown():
    try:
        f = open(shutdown_log, "r+")
        return Response(f.read(), mimetype="text/plain")
    except:
        print("error file")

        return Response("error log", mimetype="text/plain")


@app.route('/real')
def test():
   def generate_random_data():
      while True:
         status = store_log()

#         print(status)

         data = "data:"+status+"\n\n"
         yield data
         time.sleep(1)
   return Response(generate_random_data(), mimetype='text/event-stream')

@app.route('/real1')
def test1():
   def generate_random_data():
      while True:
         status2 = store2_log()
#         print(status2)
         data = "data:" + status2 + "\n\n"
         yield data
         time.sleep(1)
   return Response(generate_random_data(), mimetype='text/event-stream')



#def test():
#    print("thread")



def start_web():

    app.run(debug=False, host="0.0.0.0")

if __name__ == '__main__':
    sw1 = threading.Thread(target=wiringthread.start, args=())
    sw2 = threading.Thread(target=wiringthread2.start, args=())
    sw1.start()
    sw2.start()

    print("restart")
    start_web()


    #web = threading.Thread(target=start_web, args=())
    #raspberry = threading.Thread(target=start_web, args=())
    #raspberry.start()
   #web_start()


