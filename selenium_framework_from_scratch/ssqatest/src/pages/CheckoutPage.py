
from selenium.webdriver.common.by import By
from ssqatest.src.pages.BasePage import BasePage
from ssqatest.src.helpers.generic_helpers import generate_random_email_pwd, generate_random_chars, \
    generate_address, generate_random_number


class CheckoutPage(BasePage):

    checkout_name_field = (By.ID, "billing_first_name")
    checkout_last_name_field = (By.ID, "billing_last_name")
    checkout_address_field = (By.ID, "billing_address_1")
    checkout_city_field = (By.ID, "billing_city")
    checkout_phone_num_field = (By.ID, "billing_phone")
    checkout_email_field = (By.ID, "billing_email")
    make_order_btn = (By.ID, "place_order")

    def __init__(self, drive):
        super().__init__(drive)

    def set_name_data(self):
        self.write_text("PEPE", self.checkout_name_field)

    def set_last_name_data(self):
        self.write_text("PEPE", self.checkout_last_name_field)

    def set_address_data(self):
        self.write_text("CALLE 66 PEPE 12-23", self.checkout_address_field)

    def set_city_field(self):
        self.write_text("MEDELLÍN", self.checkout_city_field)

    def set_phone_number_field(self):
        self.write_text("31163144", self.checkout_phone_num_field)

    def set_email_data_field(self):
        email, pwd = generate_random_email_pwd()
        self.write_text("DMAT3213@GMAIL.COM", self.checkout_email_field)

    def register_new_usr_to_checkout(self):
        self.set_name_data()
        self.set_last_name_data()
        self.set_address_data()
        self.set_city_field()
        self.set_phone_number_field()
        self.set_email_data_field()
