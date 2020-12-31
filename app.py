from flask import Flask, jsonify, request
import RPi.GPIO as GPIO
import flask
import time
import requests
import config 
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
            time.sleep()
            GPIO.cleanup(20)
            send_sms(sender, 'Your system ON')
            print ('your system ON')
        elif message == "2":
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(18,GPIO.OUT)
            GPIO.output(18,0)
            GPIO.cleanup()
            send_sms(sender, 'your system OFF')
            print ('your system OFF')
        elif message == 'HELP':
            send_sms(sender, 'For turn on send number 1 /n and for turn of send number 2')
        else:
            send_sms(sender, 'Your number is wrong, for more information send /n HELP/n to me!!!')
        ret = {"message":"processed"}
        return jsonify(ret), 200
    else:
        return 'Hi!!!!!!'

def send_sms(receptor, message):
    url = f'https://api.kavenegar.com/v1/{config.API_KEY}/sms/send.json'
    data = {"message": message,
            "receptor": receptor}
    res = requests.post(url, data)


if __name__ == "__main__":
    app.run("0.0.0.0", 5000, debug=True)
