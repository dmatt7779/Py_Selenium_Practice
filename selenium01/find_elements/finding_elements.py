
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver_service = Service(executable_path='C:\Program Files\WebDrivers\chromedriver.exe')
driver = webdriver.Chrome(service=driver_service)

driver.get('http://demostore.supersqa.com/')

cart = driver.find_element(By.ID, 'site-header-cart')
cart.click()

# my_account_header = driver.find_element(By.CSS_SELECTOR, "#site-navigation > div:nth-child(2) > ul > li.page_item.page-item-9 > a")
my_account_header = driver.find_element(By.LINK_TEXT, 'My account')
my_account_header.click()
time.sleep(5)

