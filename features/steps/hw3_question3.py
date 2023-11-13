from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('click sign in')
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//span[contain(text(),'Sing in')]").click()
    sleep((1))
    context.driver.find_element(By.XPATH, "//span[contain(text(),'Sing in')]").click()

@then('Verify Sign In form opened')
def verify_Sign_In_form_opened(context):

    actual_result = context.driver.find_element(By.XPATH,  "//span[contain(text(),'Sign into your Target account')]").text
    assert 'Your cart is empty' in actual_result, f'{actual_result} Is not the right page'