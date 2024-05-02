from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import threading

#service = Service(executable_path="./chromedriver")
#driver = webdriver.Chrome(service=service)
driver = webdriver.Chrome()

driver.get("https://www.youtube.com")

time.sleep(10)

input_element = driver.find_element(By.CLASS_NAME, "ytd-searchbox")
input_element.clear()

time.sleep(3)
input_element.send_keys("tech with tim")
time.sleep(3)
input_element.clear()
time.sleep(10)

driver.quit()

#input_element = driver.find_element(By.CLASS_NAME, "advSearchHomeLink")