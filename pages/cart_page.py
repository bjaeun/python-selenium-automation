from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Page

class CartPage(Page):
    CART_MSG = (By.CSS_SELECTOR, "h1[class*='StyledHeading']")
    CART = (By.CSS_SELECTOR, "[data-test='cartItem-title'}")
    SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "div [class*='h-padding-l-tight']")
    CART_BTN = (By.CSS_SELECTOR, "[data-test='addToCartButton']")
    CHECKOUT_BTN = (By.XPATH, "//a[contains(text(),'View cart & check out')]")
    def verify_cart_msg(self):
        expected = 'Your cart is empty'
        actual = self.find_element(*self.CART_MSG).text
        assert expected == actual, f'Expected text {expected} did not match {actual}'

    def add_to_cart_btn(self):
        self.find_element(*self.CART_BTN).click()
        self.wait.until(
            EC.visibility_of_element_located(*self.SIDE_NAV_PRODUCT_NAME),
            message='Product name not shown in side navigation'
        )

    def click_checkout_from_nav_menu(self):
        self.find_element(*self.CHECKOUT_BTN).click()

    def verify_cart_has_the_item(self, product):
        actual_product = self.find_element(*self.CART).text
        print(actual_product)
        assert product == actual_product, f"Expected '{expected_product}' ,but got different '{actual_product}'"

