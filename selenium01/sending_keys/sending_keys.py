import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('http://demostore.supersqa.com')
driver.maximize_window()

my_account_btn = driver.find_element(By.LINK_TEXT, "My account")
my_account_btn.click()

username_field = driver.find_element(By.ID, "username")
username_field.send_keys("aqui estoy")

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("Aqui estoy!2143")

home_btn = driver.find_element(By.LINK_TEXT, "Home")
home_btn.click()

search_field = driver.find_element(By.ID, "woocommerce-product-search-field-0")
search_field.send_keys("hoodie")
time.sleep(3)
search_field.send_keys(Keys.ENTER)
product_title = driver.find_element(By.CLASS_NAME, "woocommerce-products-header__title").text
if product_title == "Search results: “hoodie”":
    print("PASS")
else:
    print("FAILED")


