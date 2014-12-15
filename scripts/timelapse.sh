#!/bin/bash

#Timelapse parameters
Duration=3600000
Interval=1000

raspistill -t $Duration -tl $Interval -o photo%04d.jpg