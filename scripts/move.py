import servo
import sys

#Servo pins in use
#pan -> 7
#tilt -> 18

pin = int(sys.argv[1]) 
cycle = float(sys.argv[2]) 

servo.move(pin, cycle)