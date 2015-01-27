#!/bin/bash

Photo=$(date +%y%m%d%H%M%S)
Pan=3
Tilt=2

if [ $# -ge 1 ]; then
	Photo=$1
fi
if [ $# -ge 2 ]; then
	Pan=$2
fi
if [ $# -eq 3 ]; then
	Tilt=$3
fi

python panorama.py $Photo $Pan $Tilt
        

