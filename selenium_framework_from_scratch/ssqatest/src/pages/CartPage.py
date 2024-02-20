
from selenium.webdriver.common.by import By
from ssqatest.src.pages.BasePage import BasePage


class CartPage(BasePage):

    products_in_cart = (By.CSS_SELECTOR, "tr.cart_item > td.product-name")
    coupon_field = (By.ID, "coupon_code")
    apply_coupon_btn = (By.CSS_SELECTOR, "div.coupon > button.button")
    coupon_status_sign = (By.CSS_SELECTOR, "div.woocommerce-message")
    coupon_checkout_row = (By.CSS_SELECTOR, "tr.cart-discount.coupon-ssqa100 > th")
    checkout_btn = (By.CSS_SELECTOR, "a.checkout-button")

    def __init__(self, driver):
        super().__init__(driver)

    def get_products_in_cart(self):
        return self.wait_and_get_elements(self.products_in_cart)

    def get_products_in_cart_text(self):
        webelements_list = self.get_products_in_cart()
        return self.get_elements_text(webelements_list)

    def set_coupon_code(self, coupon_code):
        self.write_text(coupon_code, self.coupon_field)

    def click_apply_coupon_btn(self):
        self.click_on(self.apply_coupon_btn)

    def get_coupon_process_status(self):
        return self.get_element_text(self.coupon_status_sign)

    def get_coupon_applied(self):
        return self.get_element_text(self.coupon_checkout_row)

    def click_checkout_btn(self):
        self.click_on(self.checkout_btn)
