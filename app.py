from flask import Flask
import ippanel
from ippanel import Client
import RPi.GPIO as GPIO

api_key = "api-key"
sms = Client(config.api_keys)

app = Flask(__name__)


@app.route('/')
def main_page():
    return "Hi"

@app.route('/v1/process')
def process():
    a = sms.fetch_inbox()
    b = a[0][0]
    return b.message


def turn_on():
    c = get_sms()
    if c == "1":
        for i in range(a):
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(18,GPIO.OUT)
            GPIO.output(18,1)



if __name__ == "__main__":
    app.run("0.0.0.0", 5000, debug=True)
