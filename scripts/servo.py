import RPi.GPIO as GPIO
import time

def move(pin,cycle):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    servo = GPIO.PWM(pin,50)
    servo.start(cycle)

    try:
        servo.ChangeDutyCycle(cycle)
        time.sleep(1)
    finally:
        servo.stop()
        GPIO.cleanup()