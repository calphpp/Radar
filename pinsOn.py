import RPi.GPIO as GPIO

pinNum = 17

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinNum, GPIO.OUT)

GPIO.output(pinNum, GPIO.HIGH)

