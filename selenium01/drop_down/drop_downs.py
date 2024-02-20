import pdb

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pdb

url = "file:///C:/Users/mateo.aguilar/Documents/Udemy_PythonSelenium/selenium01/drop_down/drop_down_example.html"
drop_down_options = []
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()


classic_drop_down = driver.find_element(By.ID, "age-range-select")

drop_down_object = Select(classic_drop_down)
for option in drop_down_object.options:
    drop_down_options.append(option.text)
drop_down_object.select_by_value('81+')
print("Aqui esta la lista --> ", drop_down_options)

dropdown_btn = driver.find_element(By.ID, "dropdownMenuButton")
dropdown_btn.click()
time.sleep(3)
my_account_opt = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/ul/li[2]/a")
my_account_opt.click()
time.sleep(3)

