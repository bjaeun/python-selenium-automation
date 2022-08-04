from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('open amazon bestseller page')
def open_amazon_main_page(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

@then('Verify 5 links')
def verify_the_bestseller_page_open(context):
    links = context.driver.find_elements(By.CSS_SELECTOR, "#zg_header div[class*='celwidget c-f'] a[href*='/ref=zg_bs_tab']")
    assert 5 == len(links), f'{context.driver.current_url} Is not the right page'