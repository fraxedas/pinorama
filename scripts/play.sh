#!/bin/bash

video=*.h264

if [ $# -eq 1 ]; then
	video=$1
fi

omxplayer -o video