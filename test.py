from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By


options = Options()

driver = webdriver.Chrome(
    options=options,
)

# Your further WebDriver code here...
driver.get("https://geo.brdtest.com/mygeo.json")
time.sleep(4)
print("IP Address: ", driver.find_element(By.XPATH, "/html").text)
time.sleep(2)
