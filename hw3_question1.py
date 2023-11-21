from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# init driver
service = Service(executable_path='/Users/jaeundelio/Desktop/python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# click Orders button
search = driver.find_element(By.CSS_SELECTOR, "a[href='/gp/css/order-history?ref_=nav_orders_first']").click()
# click Create your Amazon account button
search = driver.find_element(By.CSS_SELECTOR, '#createAccountSubmit').click()

# find amazon logo
driver.find_element(By.CSS_SELECTOR, ".a-icon.a-icon-logo")

# find Create account
driver.find_element(By.XPATH, "//h1[text()='Create account ']")

# find name input
driver.find_element(By.CSS_SELECTOR,"#ap_customer_name")

# find email input
driver.find_element(By.CSS_SELECTOR, "ap_email")

# find pwd input
driver.find_element(By.CSS_SELECTOR, "ap_password")

# find re-enter pwd input
driver.find_element(By.CSS_SELECTOR,"ap_password_check")

# find the Passwords must be at least 6 characters
driver.find_element(By.XPATH, "//div[contains(text(),'must be')]")

# find Continue button
driver.find_element(By.CSS_SELECTOR, "#continue")

# find the condition_of_use
driver.find_element(By.CSS_SELECTOR, "[href*='notification_condition_of_use']")

# find the condition_privacy_notice
driver.find_element(By.CSS_SELECTOR, "[href*='notification_condition_privacy_notice']")

# find sing in
driver.find_element(By.CSS_SELECTOR, "[href*='/ap/signin']")

driver.quit()