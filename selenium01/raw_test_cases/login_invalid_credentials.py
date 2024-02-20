import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class InvalidUserLoginError:

    invalid_email = "abc@supersqa.com"
    invalid_pwd = "123!"
    url = "http://demostore.supersqa.com/my-account/"
    expected_msg = f'Error: The password you entered for the email address {invalid_email} is incorrect. Lost your password?'

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def go_to_webpage(self):
        self.driver.get(self.url)

    def input_email(self):
        username_field = self.driver.find_element(By.ID, 'username')
        username_field.send_keys(self.invalid_email)

    def input_password(self):
        pwd_field = self.driver.find_element(By.ID, 'password')
        pwd_field.send_keys(self.invalid_pwd)

    def click_on_login_btn(self):
        self.driver.find_element(By.NAME, 'login').click()

    def verify_error_msg(self):
        error_msg = self.driver.find_element(By.CSS_SELECTOR, "ul[role='alert'] li")
        print(f' AQUI ----> {error_msg.text}')
        assert error_msg.text == self.expected_msg

    def main(self):
        self.go_to_webpage()
        self.input_email()
        self.input_password()
        self.click_on_login_btn()
        self.verify_error_msg()
        time.sleep(3)
        self.driver.quit()


if __name__ == '__main__':

    obj = InvalidUserLoginError()
    obj.main()
