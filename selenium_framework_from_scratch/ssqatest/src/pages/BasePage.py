
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.default_timeout = None
        self.driver = driver

    def click_on(self, *locator):
        WebDriverWait(self.driver, timeout=10).until(EC.element_to_be_clickable(*locator)).click()

    def write_text(self, input_data, *locator):
        WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(*locator)).send_keys(input_data)

    def get_element_text(self, *locator):
        return WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(*locator)).text

    def wait_until_element_contain_text(self, text, *locator):
        WebDriverWait(self.driver, timeout=10).until(EC.text_to_be_present_in_element(*locator, text))

    def wait_and_get_elements(self, *locator):
        return WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_all_elements_located(*locator))

    def get_elements_text(self, webelements):
        webelement_text = [element.text for element in webelements]
        return webelement_text
