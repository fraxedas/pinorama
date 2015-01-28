import sys
import functions
import servo
import console

#Servo pins in use
panServo = 7
tiltServo = 18

name = sys.argv[1] 
pans = int(sys.argv[2]) 
tilts = int(sys.argv[3]) 

#Servo configs
minPan = 2.5
maxPan = 12.5
minTilt = 5
maxTilt = 12.5

panStep = round((maxPan-minPan)/pans,1)
tiltStep = round((maxTilt-minTilt)/pans, 1)

for p in functions.step_range(minPan, maxPan, panStep):
    servo.move(panServo,p)
    for t in functions.step_range(minTilt, maxTilt, tiltStep):
        servo.move(tiltServo,t)
        console.run(["./photo.sh", functions.name(name,p,t)])


    




