#!/bin/bash

PWD=`pwd`

pip install selenium --user

cd /tmp && ls chromedriver* | grep -q [a-zA-Z] || (wget https://chromedriver.storage.googleapis.com/2.45/chromedriver_mac64.zip && unzip chromedriver_mac64.zip && chmod +x chromedriver)
./chromedriver --version

cd $PWD
