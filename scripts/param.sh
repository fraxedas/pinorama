#!/bin/bash

param=$(date +%y%m%d%H%M%S).jpg

if [ $# -eq 1 ]; then
	param=$1
fi

export param