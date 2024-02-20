
from ssqatest.src.pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from ssqatest.src.helpers.config_helpers import get_base_url
import logging as log


class MyAccountSignedIn(BasePage):

    email_field = (By.ID, "reg_email")
    password_field = (By.ID, "reg_password")
    register_btn = (By.CSS_SELECTOR, "button[value='Registrarse']")
    login_label = (By.LINK_TEXT, "Log out")
    endpoint = "/mi-cuenta/"

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_my_account(self):
        base_url = get_base_url()
        final_url = base_url + self.endpoint
        self.driver.get(final_url)
        log.info(f'Going to {final_url}')

    def register_email(self, email):
        self.write_text(email, self.email_field)

    def register_pwd(self, pwd):
        self.write_text(pwd, self.password_field)

    def click_register_btn(self):
        self.click_on(self.register_btn)

    def get_login_title_label(self):
        return self.get_element_text(self.login_label)
