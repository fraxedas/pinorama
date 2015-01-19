#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M%S")
Duration=5000

raspistill -t $Duration -o $DATE.h264