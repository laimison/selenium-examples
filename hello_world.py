#!/usr/bin/python

import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="/tmp/chromedriver")

driver.get('https://google.com')
time.sleep(3)

search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(3)

driver.execute_script("javascript:window.scrollBy(0,5000)")
time.sleep(3)
driver.quit()
