#!/bin/bash

Photo=$(date +%y%m%d%H%M%S)
Pan=4
Tilt=3

#Servo configs
MinPan = 2.5
MaxPan = 12.5
MinTilt = 2.5
MaxTilt = 7

if [ $# -ge 1 ]; then
	Photo=$1
fi
if [ $# -ge 2 ]; then
	Pan=$2
fi
if [ $# -eq 3 ]; then
	Tilt=$3
fi


for i in 'seq 1 10';
     . photo.sh Photo-$i.jpg
done
        

