# from selenium.webdriver.common.by import By
# from behave import given, when, then
# from time import sleep
#
# CART = (By.ID, 'nav-cart-count')
# SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR,"div [class*='h-padding-l-tight']")
#
# @when('Search for {product} on target')
# def search_product(context, product):
#     context.driver.find_element(By.CSS_SELECTOR, '[aria-label="What can we help you find? suggestions appear below"]').send_keys(product)
#     context.driver.find_element(By.CSS_SELECTOR, '[aria-label="search"]').click()
#     sleep(2)
#
# @when('Click on Add to cart button')
# def click_add_to_cart(context):
#     context.driver.find_element(By.CSS_SELECTOR, "#addToCartButtonOrTextIdFor87791923").click()
#
# @when('Click on Add to cart button from right side navigation menu')
# def click_add_to_cart_navigation_menu(context):
#     context.driver.find_element(By.CSS_SELECTOR, "#addToCartButtonOrTextIdFor87791923").click()
#     context.driver.wait.until(
#         EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME),
#         message='Product name not shown in side navigation'
#     )
# @then('Verify cart has {expected_product} item')
# def Verify_cart_has_the_product(context, expected_product):
#     actual_product = context.driver.find_element(*CART).text
#     print(actual_product)
#     assert expected_count == actual_text, f'Expected {expected_product} ,but got different {actual_product}'