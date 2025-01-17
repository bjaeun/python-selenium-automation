from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from behave import given, when, then
from time import sleep

@given('Open target circle page')
def open_target_circle_page(context):
    context.driver.get('https://www.target.com/circle')

@then('Verify 5 benefit boxes are present')
def verify_boxes_are_present(context):
    links = context.driver.find_elements(By.CSS_SELECTOR, "[class*='styles__BenefitCard-sc-']")
    assert 5 == len(links), f'{context.driver.current_url} Is not the right page'