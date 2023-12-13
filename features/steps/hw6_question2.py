from selenium.webdriver.common.by import By
from behave import given, when, then


@given('open target main page')
def open_target_main_page(context):
    context.app.main_page.open_main()


@when('click cart button')
def click_orders_button(context):
    context.app.main_page.click_cart()


@then('Verify message is shown')
def verify_message_is_shown(context):
    context.app.cart_page.verify_cart_msg()
