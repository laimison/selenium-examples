#!/bin/bash

PWD=`pwd`

pip install selenium --user

link="https://chromedriver.storage.googleapis.com/76.0.3809.126/chromedriver_mac64.zip"

cd /tmp && ls chromedriver* | grep -q [a-zA-Z] || (wget ${link} && unzip chromedriver_mac64.zip && chmod +x chromedriver)
./chromedriver --version

cd $PWD
echo "Do you use the latest Chrome? Did you download latest Chrome Driver - see the script?"
