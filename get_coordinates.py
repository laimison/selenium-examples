#!/usr/bin/python

import sys
import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="/root/chromedriver")

i = 1
while i < len(sys.argv):
# while i < 4:
    phrase = sys.argv[i]

    open_link = "http://maps.google.co.uk/maps?q=" + phrase

    driver.get(open_link)

    time.sleep(8)

    lat = driver.current_url.split('/')[6].split(',')[0].replace("@", "")
    long = driver.current_url.split('/')[6].split(',')[1]
    zoom = driver.current_url.split('/')[6].split(',')[2].replace("z", "")
    link = driver.current_url

    print(phrase + " , " + lat + "," + long + " , " + zoom + " , " + link)

    i += 1

# driver.quit()
sys.exit()
