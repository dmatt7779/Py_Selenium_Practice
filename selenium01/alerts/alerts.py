import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = "file:///C:/Users/mateo.aguilar/Documents/Udemy_PythonSelenium/selenium01/alerts/alerts_example.html"
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

alert_btn1 = driver.find_element(By.CSS_SELECTOR, "#jsAlertExample > button")
alert_btn1.click()
time.sleep(2)
alert_sign = driver.switch_to.alert
print(f' AQUI ---> {alert_sign.text}')
assert alert_sign.text == "I am a JavaScript Alert"
alert_sign.accept()

alert_btn2 = driver.find_element(By.CSS_SELECTOR, "#jsConfirmExample > button")
alert_btn2.click()
time.sleep(2)
print(f'alert btn 2 {alert_sign.text}')
alert_sign.accept()
status_msg = driver.find_element(By.ID, "userResponse1").text
print(f'status message option | {status_msg}')
time.sleep(2)

alert_btn3 = driver.find_element(By.CSS_SELECTOR, "#jsPromptExample > button")
alert_btn3.click()
alert_sign.send_keys("MATEO AGUILAR: EXAMPLE")
alert_sign.accept()
prompt_msg = driver.find_element(By.ID, "userResponse2").text
print(f'prompt message --> {prompt_msg}')
time.sleep(2)
