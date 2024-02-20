import logging

from ssqatest.src.helpers.config_helpers import get_base_url
from selenium.webdriver.common.by import By
from ssqatest.src.pages.BasePage import BasePage


class HomePage(BasePage):

    product01 = (By.CSS_SELECTOR, "a[aria-label='Añade “Beanie” a tu carrito']")

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_home_page(self):
        base_url = get_base_url()
        self.driver.get(base_url)
        logging.info(f'Going to {base_url}')

    def click_on_product(self):
        self.click_on(self.product01)
