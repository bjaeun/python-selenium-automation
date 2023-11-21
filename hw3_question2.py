from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('open target main page')
def open_target_main_page(context):
    context.driver.get('https://www.target.com/')

@when('click cart button')
def click_orders_button(context):
    context.driver.find_element(By.CSS_SELECTOR, "[href*='Cart.svg']").click()

@then('Verify message is shown')
def verify_message_is_shown(context):
    actual_result = context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
    assert 'Your cart is empty' in actual_result, f'{actual_result} Is not the right page'
