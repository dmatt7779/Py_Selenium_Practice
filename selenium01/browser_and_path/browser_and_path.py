
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver_service = Service(executable_path='C:/Program Files/WebDrivers/chromedriver.exe')

driver = webdriver.Chrome(service=driver_service)
driver.get("https://google.com")
driver.quit()
