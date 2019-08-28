#!/usr/bin/python

import sys
import time
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="/tmp/chromedriver")

# open blank page
driver.get("about:blank")

i = 1
# while i < len(sys.argv):
while i < 3:
    phrase = sys.argv[i]

    open_link = "http://maps.google.com/maps?q=" + phrase

    driver.execute_script('window.open("{}","_blank");'.format(open_link))
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[-1])

    print driver.current_url
    time.sleep(1)

    zoom = driver.current_url.split('/')[6].split(',')[2].replace("z", "")

    lat = driver.current_url.split('/')[6].split(',')[0].replace("@", "")
    long = driver.current_url.split('/')[6].split(',')[1]

    link = driver.current_url

    coordinates = lat + "," + long
    print(phrase + " , " + coordinates + " , " + zoom + " , " + link)

    # Open new tab
    # next_link = "about:blank"
    # driver.execute_script('window.open("{}","_blank");'.format(next_link))

    # driver.execute_script("window.open('about:blank');")
    # driver.execute_script('window.open("next_link,"_blank");')
    # driver.execute_script('''window.open('''next_link'',"_blank");''')

    # driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
    # driver.get('http://google.com')
    # ActionChains(driver).key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()

    # driver.get(open_link)

    i += 1

# driver.quit()
sys.exit()
