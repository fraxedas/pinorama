#!/bin/bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install fbi
sudo apt-get install omxplayer

curl -sL https://deb.nodesource.com/setup | sudo bash -
sudo apt-get install nodejs
sudo npm install -g forever
sudo npm install -g grunt-cli