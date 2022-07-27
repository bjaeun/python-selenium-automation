from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='/Users/jaeundelio/Desktop/python-selenium-automation/chromedriver')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# click Orders button
search = driver.find_element(By.CSS_SELECTOR, "a[href='/gp/css/order-history?ref_=nav_orders_first']").click()

# find Sing-in
actual_result = driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small').text

# verify
assert 'Sign-In' in actual_result, f'{actual_result} Is not the right page'

driver.quit()