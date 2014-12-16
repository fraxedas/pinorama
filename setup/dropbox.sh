#!/bin/bash

echo 'Installing Dropbox-Uploader'
cd ~ 
git clone https://github.com/andreafabrizi/Dropbox-Uploader.git
ls
cd Dropbox-Uploader
ls
chmod +x dropbox_uploader.sh
./dropbox_uploader.sh