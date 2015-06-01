#!/bin/bash

photo=*.jpg

if [ $# -eq 1 ]; then
	photo=$1
fi

fbi $photo