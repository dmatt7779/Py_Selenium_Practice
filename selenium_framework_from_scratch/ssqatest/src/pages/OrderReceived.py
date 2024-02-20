
from ssqatest.src.pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from ssqatest.src.helpers.data_base_helper import get_order_by_order_id


class OrderReceived(BasePage):

    order_status_label = (By.TAG_NAME, "h1")
    order_id = (By.CSS_SELECTOR, "li.order > strong")

    def __init__(self, driver):
        super().__init__(driver)

    def get_order_status_label(self):
        return self.get_element_text(self.order_status_label)

    def wait_until_text_appear(self, text_to_look):
        self.wait_until_element_contain_text(text_to_look, self.order_status_label)

    def get_order_id(self):
        return self.get_element_text(self.order_id)

    @staticmethod
    def get_order_id_from_db(order_id):
        sql = get_order_by_order_id(order_id, "shop_order")
        print(f'AQUI ---> SQL {sql}')
