from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('click sign in')
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//span[contains(text(),'Sign in')]").click()

@when('From right side navigation menu, click Sign In')
def right_side_menu_click(context):
    context.driver.find_element(By.XPATH,
                            "//span[@class='styles__ListItemText-sc-diphzn-1 jaMNVl' and text()='Sign in']").click()
@then('Verify Sign In form opened')
def verify_Sign_In_form_opened(context):
    actual_result = context.driver.find_element(By.XPATH,  "//span[contains(text(),'Sign into your Target account')]").text
    assert 'Sign into your Target account' in actual_result, f'{actual_result} Is not right result!'