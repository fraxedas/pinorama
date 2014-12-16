#!/bin/bash

#Requires mencoder

#Timelapse parameters
FPS=30
DATE=$(date +"%Y-%m-%d_%H%M%S")

#Get the list of files
ls *.jpg > stills.txt

#Encode the video
mencoder -nosound -ovc lavc -lavcopts vcodec=mpeg4:aspect=16/9:vbitrate=8000000 -vf scale=1920:1080 -o timelapse_$DATE.avi -mf type=jpeg:fps=$FPS mf://@stills.txt
