from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART = (By.ID, 'nav-cart-count')

@given('open amazon page')
def open_amazon_main_page(context):
    context.driver.get('https://www.amazon.com/')

@when('Search for {search_word} on amazon')
def search_product(context, search_word):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(search_word)
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()
    sleep(1)

@when('Click on the first product')
def the_first_product_selected(context):
    context.driver.find_element(By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]").click()

@when('Click on Add to cart button')
def click_add_to_cart(context):
    sleep(4)
    context.driver.find_element(By.CSS_SELECTOR, ".a-button-inner #add-to-cart-button").click()

@when('Open cart page')
def Open_cart_page(context):
    context.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')

@then('Verify cart has {expected_count} item')
def Verify_cart_has_the_product(context, expected_count):
    actual_text = context.driver.find_element(*CART).text
    print(actual_text)
    assert expected_count == actual_text, f'Expected {expected_count} ,but got different #'