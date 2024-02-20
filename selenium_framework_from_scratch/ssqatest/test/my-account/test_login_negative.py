import time
import logging as log
import pytest
from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut


@pytest.mark.usefixtures("driver")
class TestLoginNegative:

    def test_login_none_existing_user(self, driver):
        log.info('Starting Test Login Negative')
        expected_error_msg = "Error: The username pepe is not registered on this site. If you are unsure of your username, try your email address instead."
        test = MyAccountSignedOut(driver)
        test.go_to_my_account()
        test.input_login_username('pepe')
        test.input_login_password('123')
        test.click_login_btn()
        error_msg = test.get_error_msg()
        assert error_msg == expected_error_msg
