#!/usr/bin/python

import sys
import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="/tmp/chromedriver")

i = 1
while i < len(sys.argv):
    phrase = sys.argv[i]

    driver.get("http://maps.google.com/maps?q=" + phrase)
    time.sleep(5)

    zoom = driver.current_url.split('/')[6].split(',')[2].replace("z", "")

    lat = driver.current_url.split('/')[6].split(',')[0].replace("@", "")
    long = driver.current_url.split('/')[6].split(',')[1]

    coordinates = lat + "," + long
    print(phrase + ", " + coordinates + ", " + zoom)

    i += 1

# driver.quit()
sys.exit()
