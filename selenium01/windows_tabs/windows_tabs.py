import time

from selenium.webdriver.common.by import By
from selenium import webdriver

url = "file:///C:/Users/mateo.aguilar/Documents/Udemy_PythonSelenium/selenium01/windows_tabs/windows-and_tabs_example.html"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

new_tab1 = driver.find_element(By.CSS_SELECTOR, "#windows > a.btn.btn-warning")
new_tab1.click()
time.sleep(2)

windows_tabs_handle = driver.window_handles
print(f'AQUI ----> {windows_tabs_handle}')
original_window_handle = windows_tabs_handle[0]
page01 = windows_tabs_handle[1]
driver.switch_to.window(page01)
print(f'AQUI ----> {driver.title}')
page_title = driver.find_element(By.TAG_NAME, "h1")
print(f'AQUI ---> {page_title.text}')
time.sleep(2)

print("After get all data from page 01 - back to original page")
driver.switch_to.window(original_window_handle)
print(f'AQUI ----> {driver.title}')

new_tab2 = driver.find_element(By.CSS_SELECTOR, "#windows > a.btn.btn-success")
new_tab2.click()
time.sleep(2)

windows_tabs_handle = driver.window_handles
print(f'AQUI ----> {windows_tabs_handle}')
page02 = windows_tabs_handle[2]
driver.switch_to.window(page02)
page_title = driver.find_element(By.TAG_NAME, "h1")
print(f'AQUI ----> {driver.title}')
print(f'AQUI ---> {page_title.text}')
driver.close()
driver.switch_to.window(page01)
driver.close()
print("On original page")
driver.switch_to.window(original_window_handle)
print(f'AQUI ----> {driver.title}')
page_title = driver.find_element(By.TAG_NAME, "h1")
print(f'AQUI ---> {page_title.text}')
time.sleep(2)
