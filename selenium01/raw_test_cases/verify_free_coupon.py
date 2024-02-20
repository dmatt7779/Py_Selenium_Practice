import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def add_1_to_cart():
    item_store = driver.find_element(By.CSS_SELECTOR, "a[aria-label='Add “Album” to your cart']")
    item_store.click()
    time.sleep(2)


def click_cart_in_top_menu():
    cart = driver.find_element(By.CSS_SELECTOR, "a[title='View your shopping cart']")
    cart.click()
    time.sleep(2)


def input_coupon_in_hit_enter():
    coupon_field = driver.find_element(By.ID, "coupon_code")
    scroll_action.move_to_element(coupon_field).perform()
    coupon_field.send_keys("SSQA100")
    time.sleep(2)
    apply_coupon_btn = driver.find_element(By.CSS_SELECTOR, "button[value='Apply coupon']")
    apply_coupon_btn.click()


def verify_total_0():
    print("AQUI VERIFYING TOTAL")
    pass

if __name__ == '__main__':
    url = "http://demostore.supersqa.com/"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    scroll_action = ActionChains(driver)

    add_1_to_cart()
    click_cart_in_top_menu()
    input_coupon_in_hit_enter()
    time.sleep(3)
    verify_total_0()
