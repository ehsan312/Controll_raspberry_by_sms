from flask import Flask
import ippanel
from ippanel import Client
import RPi.GPIO as GPIO

api_key = "api-key"
sms = Client(API)

app = Flask(__name__)


@app.route('/')
def main_page():
    return "Hi"

@app.route('/get_sms')
def get_sms():
    a = sms.fetch_inbox()
    b = a[0][0]
    return b.message

c = get_sms()

if c == "1":
    for i in range(a):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18,GPIO.OUT)


        GPIO.output(18,GPIO.LOW)

        time.sleep(0.1)


        GPIO.output(18,GPIO.HIGH)

        time.sleep(0.1)

        GPIO.output(18,GPIO.LOW)
        GPIO.cleanup()

