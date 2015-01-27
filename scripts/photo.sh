#!/bin/bash

photo=$(date +%y%m%d%H%M%S).jpg

if [ $# -eq 1 ]; then
	photo=$1
fi

raspistill -o $photo
ls $photo