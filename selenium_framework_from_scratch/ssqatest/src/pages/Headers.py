
from selenium.webdriver.common.by import By
from ssqatest.src.pages.BasePage import BasePage


class Headers(BasePage):

    cart_header = (By.CSS_SELECTOR, "a > span.woocommerce-Price-amount.amount")
    count_products = (By.CSS_SELECTOR, "ul#site-header-cart span.count")

    def __init__(self, driver):
        super().__init__(driver)

    def click_cart_right_header(self):
        self.click_on(self.cart_header)

    def wait_until_amount_count(self, count):
        expected_text = str(count) + " producto"
        self.wait_until_element_contain_text(expected_text, self.count_products)
