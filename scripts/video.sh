#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M%S")
Duration=5000

if [ $# -ge 1 ]; then
	DATE=$1
fi

if [ $# -eq 2 ]; then
	Duration=$1
fi

raspistill -t $Duration -o $DATE.h264