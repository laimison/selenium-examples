#!/usr/bin/python

import sys
import time
from selenium import webdriver

address = sys.argv[1]
count = int(sys.argv[2])

print "HTTP address received:", address
print "Count received:", count

driver = webdriver.Chrome(executable_path="/tmp/chromedriver")  

if (address and count):
  driver.get(address)
  time.sleep(8)

  for numer in range(1,count):
    driver.execute_script("javascript:window.scrollBy(0,5000)")
    time.sleep(1)

# driver.quit()

sys.exit()
