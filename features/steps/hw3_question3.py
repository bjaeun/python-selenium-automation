from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('open amazon main page')
def open_amazon_main_page(context):
    context.driver.get('https://www.amazon.com/')

@when('click orders button')
def click_orders_button(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href='/gp/css/order-history?ref_=nav_orders_first']").click()

@then('Verify the sign in page open')
def verify_the_signin_page_open(context):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small').text
    assert 'Sign-In' in actual_result, f'{actual_result} Is not the right page'