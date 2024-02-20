import logging as log
from ssqatest.src.pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from ssqatest.src.helpers.config_helpers import get_base_url


class MyAccountSignedOut(BasePage):
    login_btn = (By.CSS_SELECTOR, "button.woocommerce-form-login__submit")
    username_field = (By.ID, "username")
    pwd_field = (By.ID, "password")
    error_msg = (By.CSS_SELECTOR, "ul[role='alert'] li")
    endpoint = '/mi-cuenta/'

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_my_account(self):
        base_url = get_base_url()
        final_url = base_url + self.endpoint
        self.driver.get(final_url)
        log.info(f'Going to {final_url}')

    def input_login_username(self, username):
        self.write_text(username, self.username_field)

    def input_login_password(self, pwd):
        self.write_text(pwd, self.pwd_field)

    def click_login_btn(self):
        self.click_on(self.login_btn)

    def get_error_msg(self):
        return self.get_element_text(self.error_msg)
