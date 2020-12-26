from flask import Flask, jsonify, request
import RPi.GPIO as GPIO
import flask
import time 
app = Flask(__name__)


@app.route('/v1/', methods=['GET','POST'])
def process():
    if flask.request.method == 'POST':
        data = request.form
        sender = data['from']
        message = data['message']
        print (message)
        if  message == "1":
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(18,GPIO.OUT)
            GPIO.output(18, 1)
            time.sleep(10)
            GPIO.cleanup()
        elif message == "2":
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(18,GPIO.OUT)
            GPIO.output(18,0)
            GPIO.cleanup()

        ret = {"message":"processed"}
        return jsonify(ret), 200
    else:
        return 'Hi!!!!!!'


# def turn_on():
   #  c = process()
   #  if c == "1":
   #      for i in range(a):
   #         GPIO.setmode(GPIO.BCM)
   #         GPIO.setup(18,GPIO.OUT)
   #         GPIO.output(18,1)



if __name__ == "__main__":
    app.run("0.0.0.0", 5000, debug=True)
