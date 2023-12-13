from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_BAR = (By.ID, 'search')
SEARCH_BTN = (By.CSS_SELECTOR, '[aria-label="search"]')
LISTINGS = (By.CSS_SELECTOR, '[class*="StyledCardWrapper"]')
PRODUCT_NAME = (By.CSS_SELECTOR, '[data-test="product-title"]')
PRODUCT_IMAGE = (By.CSS_SELECTOR, '[class*="ProductCardImageWrapper"]')

@When('Search for {product}')
def search_for_product(context, product):
    context.driver.find_element( *SEARCH_BAR).send_keys(product)
    context.driver.find_element(*SEARCH_BTN).click()
    sleep(2)

@then('Verify every product has a name and image')
def every_product_name_img(context):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(2)
    context.driver.execute_script("window.scrollBy(0,2000)", "")

    all_products = context.driver.find_elements(*LISTINGS)
    for product in all_products:
        name = product.find_element(*PRODUCT_NAME).text
        assert name, 'Product title not shown'
        image = product.find_element(*PRODUCT_NAME).text
        assert image, 'Product image not shown'
