import time
import random
import string
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

url = "http://demostore.supersqa.com/"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
scroll_action = ActionChains(driver)

account_btn_opt = driver.find_element(By.LINK_TEXT, "My account")
account_btn_opt.click()

#generate random emails
letters = string.ascii_lowercase
rand_string = ''.join(random.choice(letters) for i in range(10))
random_email = rand_string + '@supersqa.com'

# Type oin the email field
#Scroll until an element
email_field = driver.find_element(By.ID, "reg_email")
pwd_field = driver.find_element(By.ID, "reg_password")
register_btn = driver.find_element(By.CSS_SELECTOR, "button[value='Register']")
scroll_action.move_to_element(email_field).perform()
email_field.send_keys(random_email)
scroll_action.move_to_element(pwd_field).perform()
pwd_field.send_keys(rand_string)
time.sleep(2)
register_btn.click()
logout_btn = driver.find_element(By.LINK_TEXT, "Logout")
if logout_btn.is_displayed():
    print(f'TEST PASS ----> {logout_btn.is_displayed()}')
else:
    raise Exception("TEST FAILED")
