from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Search for {product} on target')
def search_product(context, product):
    context.app.main_page.search(product)


@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.app.cart_page.add_to_cart_btn()


@when('Click on Add to cart button from right side navigation menu')
def click_add_to_cart_navigation_menu(context):
    context.app.cart_page.click_checkout_from_nav_menu()

@then('Verify cart has {expected_product} item')
def Verify_cart_has_the_product(context, expected_product):
    context.app.cart_page.verify_cart_has_the_item(expected_product)