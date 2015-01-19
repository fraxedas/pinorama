import RPi.GPIO as GPIO
import time
import sys

#Servo pins in use
#pan -> 7
#tilt -> 18

pin = int(sys.argv[1]) 
cycle = float(sys.argv[2]) 

GPIO.setmode(GPIO.BOARD)

GPIO.setup(pin, GPIO.OUT)
servo = GPIO.PWM(pin,50)
servo.start(cycle)

try:
    #Neutral
    servo.ChangeDutyCycle(cycle)
    time.sleep(1)
finally:
    servo.stop()
    GPIO.cleanup()