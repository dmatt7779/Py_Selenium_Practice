from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'file:///C:/Users/mateo.aguilar/Documents/Udemy_PythonSelenium/selenium01/radios/radios_example.html'
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

value_to_select = '61-80'
locator_by_value = '#radios > div > input[value="{value}"]'

default_element = driver.find_element(By.CSS_SELECTOR, locator_by_value.format(value=value_to_select))
default_element.click()
time.sleep(3)
assert default_element.is_selected(), f'Default value {value_to_select} is not present in the options to select'
