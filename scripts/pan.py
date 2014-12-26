import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
cycle = sys.argv[1] 

pan = GPIO.PWM(7,50)
pan.start(cycle)

try:
    #Neutral
    pan.ChangeDutyCycle(cycle)
    time.sleep(1)
finally:
    pan.stop()
    GPIO.cleanup()