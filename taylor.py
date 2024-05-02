from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium import webdriver
import utils

webdriver.ActionChains.sleep = utils.sleep

#driver = webdriver.Chrome()
driver = webdriver.Firefox()
first_window = driver.current_window_handle

action = webdriver.ActionChains(driver)
wait3 = WebDriverWait(driver, 3)
wait5 = WebDriverWait(driver, 5)
wait10 = WebDriverWait(driver, 10)

driver.get("https://www.tandfonline.com/search/advanced")

#onetrust-close-btn-handler onetrust-close-btn-ui banner-close-button ot-close-icon

wait10.until(EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler")))
action.sleep(1)
robot = driver.find_elements(By.ID, "onetrust-accept-btn-handler")
robot.pop().click()
#   onetrust-accept-btn-handler
action.sleep(2)
wait3.until(EC.presence_of_element_located((By.ID, "searchText-5b691e35-8ace-4857-9d5b-0fa615808a4c")))
search_bar = driver.find_element(By.ID, "searchText-5b691e35-8ace-4857-9d5b-0fa615808a4c")

#advSearch_keyw_for_1

search_bar.send_keys("John")
action.sleep(1)
#wait5.until(EC.element_to_be_clickable((By.ID, "custom-range")))
#action.sleep(1)
#custom_range = driver.find_element(By.ID, "custom-range")
#custom_range.click()

wait5.until(EC.presence_of_all_elements_located((By.ID, "timeFrame")))
time_frame = driver.find_element(By.ID, "timeFrame")
custom_range = driver.find_element(By.ID, "custom-range")
action.click(custom_range)
#action.sleep(1)



after = driver.find_element(By.ID, "AfterYear")
before = driver.find_element(By.ID, "BeforeYear")

after.value_of_css_property(2015)
before.value_of_css_property(2024)
#SearchUtil.clearMonthYearDropDown()
action.sleep(10)
driver.quit()
exit()

clique = WebDriverWait(driver, 10).until(    
    EC.presence_of_all_elements_located((By.CLASS_NAME, "yuRUbf"))
)
s = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[13]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/span/a")
print(s.get_attribute("href"))
action.sleep(3)
s.click()
#wait3.until(EC.presence_of_element_located((By.CLASS_NAME, "LC20lb MBeuO DKV0Md")))
#action.sleep(3)
#input_element = driver.find_element(By.CLASS_NAME, "LC20lb MBeuO DKV0Md")

action.sleep(10)
driver.quit()
exit()

driver.switch_to.new_window("tab")
driver.switch_to.window(first_window)
driver.close()
for window_handle in driver.window_handles:
    driver.switch_to.window(window_handle)

driver.quit()



