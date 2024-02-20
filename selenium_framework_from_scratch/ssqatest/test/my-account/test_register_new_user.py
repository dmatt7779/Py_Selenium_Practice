import time
from ssqatest.src.pages.MyAccountSignedIn import MyAccountSignedIn
import pytest
from ssqatest.src.helpers.generic_helpers import generate_random_email_pwd


@pytest.mark.usefixtures('driver')
class TestRegisterNewUser:

    @pytest.mark.tcid2
    def test_register_valid_user(self, driver):
        email_generated, pwd_generated = generate_random_email_pwd('gmail.com', 'pepe_')
        expected_label = "Log out"
        register_test = MyAccountSignedIn(driver)
        register_test.go_to_my_account()
        register_test.register_email(email_generated)
        register_test.register_pwd(pwd_generated)
        register_test.click_register_btn()
        login_label = register_test.get_login_title_label()
        assert login_label.casefold() == expected_label.casefold()
        time.sleep(2)


