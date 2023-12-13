from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class SignInPage(Page):
    ID = (By.XPATH,  "//span[contains(text(),'Sign into your Target account')]")

    def verify_sign_in_form(self):
        actual_result = self.find_element(*self.ID).text
    #    print(actual_result)
        assert 'Sign into your Target account' in actual_result, f"'{actual_result}' Is not right result!"