
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

driver_service = Service(executable_path='C:\Program Files\WebDrivers\chromedriver.exe')
driver = webdriver.Chrome(service=driver_service)
driver.implicitly_wait(4)

driver.get('file:///C:/Users/mateo.aguilar/Documents/Udemy_PythonSelenium/selenium01/Waits/page_with_slow_image.html')

selenium_logo = driver.find_element(By.ID, 'the_slow_image')
selenium_logo.click()
print("Found image")
