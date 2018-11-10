import RPi.GPIO as GPIO
import time

from flask import Flask 
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

#############################################
# 	SECTOR	TRIG	ECHO
#	0	13	27
#	1	6	22
#	2	5	23
#	3	26	24
#	4	20	25
#############################################

TRIG = [13, 6, 5, 26, 20]
ECHO = [27, 22, 23, 24, 25]

for port in range(5):
    GPIO.setup(TRIG[port],GPIO.OUT)
    GPIO.setup(ECHO[port],GPIO.IN)

    print ("Sensor Init %d..." % port)

    GPIO.output(TRIG[port], False)

time.sleep(2)
print ("Server Start..")

from flask import request
@app.route('/', methods=['GET'])

def index():
    argParam = request.args.get('sector')

    print ("Client call... Sector: " + argParam)

    argIndex = int(argParam)

    GPIO.output(TRIG[argIndex], True)
    time.sleep(0.00001)
    GPIO.output(TRIG[argIndex], False)

    while GPIO.input(ECHO[argIndex])==0:
        pulse_start = time.time()

    while GPIO.input(ECHO[argIndex])==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)
    
    print("The answer is", distance)
    
    return str(distance) 

if __name__ == "__main__":
    app.run(debug=True, port=80, host='0.0.0.0')
