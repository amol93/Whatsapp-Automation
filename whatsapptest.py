from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


driver= webdriver.Firefox()
driver.get('https://web.whatsapp.com')
time.sleep(10)
#Scan QR code from your mobile, then you are good to go

time.sleep(2)
elem = driver.find_element_by_class_name('input-search')
elem.send_keys(('Roomies@342'))
# clickr = driver.find_element_by_class_name('chat-body')
# clickr.click()
elem.send_keys(Keys.RETURN)
# elem=driver.find_element_by_class_name('chat-body')
# elem.click()
# time.sleep(2)

elem = driver.find_element_by_class_name('input')
elem.send_keys('Hi , this message is generated using Python Script')
elem.send_keys(Keys.RETURN)
