from selenium.webdriver.common.by import By
from behave import given, when, then


# @given('open target main page')
# def open_target_main_page(context):
#     context.app.main_page.open_main()


@when('Click Sign In')
def click_sign_in(context):
    context.app.main_page.click_sign_in()


@when('From right side navigation menu, click Sign In')
def right_side_menu_click(context):
    context.app.main_page.click_nav_sign_in()


@then('Verify Sign In form opened')
def verify_Sign_In_form_opened(context):
    context.app.sign_in_page.verify_sign_in_form()
