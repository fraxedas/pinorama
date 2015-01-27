#!/bin/bash

Photo=$(date +%y%m%d%H%M%S)
Duration=3600000
Interval=1000

if [ $# -ge 1 ]; then
	Photo=$1
fi
if [ $# -ge 2 ]; then
	Duration=$2
fi
if [ $# -eq 3 ]; then
	Interval=$3
fi

raspistill -t $Duration -tl $Interval -o $Photo%04d.jpg
./stich.sh $Photo
ls $Photo.avi