from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pdb

url = "file:///C:/Users/mateo.aguilar/Documents/Udemy_PythonSelenium/selenium01/checkboxes/checkbox_example.html"
drop_down_options = []
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

"""
to_locate_value = '61-80'
locator_by_value = f'input[name="age-group-checkbox"][value="{to_locate_value}"]'
my_choice = driver.find_element(By.CSS_SELECTOR, locator_by_value)
my_choice.click()
time.sleep(3)
"""

expected_number_of_options = 4
all_checkboxes = driver.find_elements(By.NAME, "age-group-checkbox")
for checkbox in all_checkboxes:
    checkbox.click()
    value = checkbox.get_attribute('value')
    time.sleep(1)
    if checkbox.is_selected():
        print(f'Checkbox with value {value} is selectable')
        assert checkbox.is_selected()
    else:
        raise Exception(f'Value {value} is not selectable')
assert len(all_checkboxes) == expected_number_of_options, "Number of checkboxes is not the expected"