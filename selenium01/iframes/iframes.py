import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = "file:///C:/Users/mateo.aguilar/Documents/Udemy_PythonSelenium/selenium01/iframes/iFrames_example.html"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

outframe_btn = driver.find_element(By.ID, "btnOutFrame")
outframe_btn.click()
time.sleep(2)
my_alert = driver.switch_to.alert
my_alert.accept()

iframe01 = driver.find_element(By.ID, "myFrame1")
driver.switch_to.frame(iframe01)
inframe_btn = driver.find_element(By.ID, "btnInFrame")
inframe_btn.click()
time.sleep(2)
my_alert.accept()

#Back to main content - from into iframe to out of iframe
driver.switch_to.default_content()
outframe_btn.click()
time.sleep(3)
my_alert.accept()
