from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class SearchResultsPage(Page):
    LOCATOR = (By.CSS_SELECTOR, "[href*='Cart.svg']")
    CART = (By.XPATH, "//h1[text()='Your cart is empty']")

    def open_target_main_page(self):
        self.open_url('https://www.target.com/')

    def click_orders_button(self):
        self.find_element(*self.LOCATOR).click()

    def verify_message_is_shown(self):
        actual_result = self.find_element(*self.CART).text
        assert 'Your cart is empty' in actual_result, f'{actual_result} Is not the right page'
