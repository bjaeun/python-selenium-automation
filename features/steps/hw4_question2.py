from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART = (By.ID, 'nav-cart-count')


@when('Search for {search_word} on target')
def search_product(context, search_word):
    context.driver.find_element(By.CSS_SELECTOR, '[aria-label="What can we help you find? suggestions appear below"]').send_keys(search_word)
    context.driver.find_element(By.CSS_SELECTOR, '[aria-label="search"]').click()
    sleep(2)

@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "#addToCartButtonOrTextIdFor80266924").click()

@when('Click on Add to cart button from right side navigation menu')
def click_add_to_cart_navigation_menu(context):
    context.driver.find_element(By.CSS_SELECTOR, "#addToCartButtonOrTextIdFor80266924").click()

@then('Verify cart has {expected_count} item')
def Verify_cart_has_the_product(context, expected_count):
    actual_text = context.driver.find_element(*CART).text
    print(actual_text)
    assert expected_count == actual_text, f'Expected {expected_count} ,but got different #'