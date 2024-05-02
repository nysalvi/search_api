from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

#service = Service(executable_path="./chrome.exe")
#driver = webdriver.Chrome(service=service)
#options = webdriver.ChromeOptions()
#options.add_argument('"--headless=new"')

driver = webdriver.Firefox()
action = webdriver.ActionChains(driver)

driver.get("https://www.google.com")


WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear()
input_element.send_keys("tech with tim" + Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Tech With Tim"))
)
link = driver.find_element(By.PARTIAL_LINK_TEXT, "Tech With Tim")
#links = driver.find_elements(By.PARTIAL_LINK_TEXT, "Tech With Tim")

action.pause(5)
action.perform()
link.click()
action.pause(5)
action.perform()


driver.quit()
#input_element = driver.find_element(By.CLASS_NAME, "advSearchHomeLink")