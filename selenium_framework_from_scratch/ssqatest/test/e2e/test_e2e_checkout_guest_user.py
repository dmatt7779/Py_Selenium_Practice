import logging
import time

import pytest

from ssqatest.src.pages.CheckoutPage import CheckoutPage
from ssqatest.src.pages.HomePage import HomePage
from ssqatest.src.pages.Headers import Headers
from ssqatest.src.pages.CartPage import CartPage
from ssqatest.src.configs.generic_configs import GenericConfigs
from ssqatest.src.pages.OrderReceived import OrderReceived


@pytest.mark.usefixtures('driver')
class TestE2ECheckoutGuestUser:

    @pytest.mark.tcid3
    def test_e2e_checkout_guest_user(self, driver):
        homepage = HomePage(driver)
        homepage.go_to_home_page()
        homepage.click_on_product()

        header = Headers(driver)
        header.wait_until_amount_count(1)
        header.click_cart_right_header()

        cartpage = CartPage(driver)
        products_list = cartpage.get_products_in_cart_text()
        print(f'AQUI ----> {products_list}')
        assert len(products_list) == 1, "More than 1 product on cart"

        coupon_code = GenericConfigs.FREE_COUPON
        cartpage.set_coupon_code(coupon_code)
        cartpage.click_apply_coupon_btn()
        status_coupon_process = cartpage.get_coupon_process_status()
        print(f'AQUI Process Status ---> {status_coupon_process}')
        assert status_coupon_process == "El código de cupón se ha aplicado correctamente."

        coupon_applied = cartpage.get_coupon_applied()
        print(f'AQUI COUPON APPLIED ---> {coupon_applied}')
        if GenericConfigs.FREE_COUPON.casefold() in coupon_applied.casefold():
            cartpage.click_checkout_btn()
        else:
            raise ValueError('Coupon not applied correctly')

        checout_page = CheckoutPage(driver)
        checout_page.register_new_usr_to_checkout()
        time.sleep(10)  # Too slow on local machine

        order_received = OrderReceived(driver)
        order_received.wait_until_text_appear("Pedido recibido")
        order_status = order_received.get_order_status_label()
        print(f'AQUI ORDER STATUS ---> {order_status}')
        assert order_status == 'Pedido recibido'
        order_id = order_received.get_order_id()
        print(f'AQUI Order ID ---> {order_id}')
        time.sleep(5)

        order_received.get_order_id_from_db(order_id)
