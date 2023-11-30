from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class MainPage(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink'}")
    SIGN_ICON = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")

    def open_main(self):
        self.open_url('https://www.target.com/')

    def search(self, product):
        self.input(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(4)


    def click_cart(self):
        self.find_element(*self.CART_ICON)


    def click_sign_in(self):
        self.click(*self.SIGN_ICON)
