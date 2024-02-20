
from selenium import webdriver
from selenium.common import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

service_driver = Service(executable_path='C:\Program Files\WebDrivers\chromedriver.exe')
driver = webdriver.Chrome(service=service_driver)
wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
# exp_wait = WebDriverWait(driver, 10)
url = 'file:///C:/Users/mateo.aguilar/Documents/Udemy_PythonSelenium/selenium01/Waits/page_with_slow_image.html'
driver.get(url)

# selenium_logo = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'the_slow_image')))
# selenium_logo = exp_wait.until(expected_conditions.visibility_of_element_located((By.ID, 'the_slow_image')))

selenium_logo = wait.until(expected_conditions.visibility_of_element_located((By.ID, 'the_slow_image')))

if selenium_logo:
    assert True
    print("PASS")
else:
    assert False
    print("FAILED")
# print("Found image")
