import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

pan = GPIO.PWM(7,50)
pan.start(7.5)

tilt = GPIO.PWM(7,50)
tilt.start(7.5)

try:
    while True:
        #Neutral
        pan.ChangeDutyCycle(7.5)
        tilt.ChangeDutyCycle(7.5)
        time.sleep(1)
        #180
        pan.ChangeDutyCycle(12.5)
        tilt.ChangeDutyCycle(12.5)
        time.sleep(1)
        #0
        pan.ChangeDutyCycle(2.5)
        tilt.ChangeDutyCycle(2.5)
        time.sleep(1)

except KeyboardInterrupt:
    pan.stop()
    tilt.stop()
    GPIO.cleanup()