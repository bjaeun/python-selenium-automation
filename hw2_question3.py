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

# find Sing-in
driver.find_element(By.ID,'nav-link-accountList-nav-line-1').click()

# find amazon logo
driver.find_element(By.XPATH, "//div[@class='a-section a-padding-medium auth-workflow']//i[@class='a-icon a-icon-logo']")

# find Email field
driver.find_element(By.ID, 'ap_email')

# find Continue button
driver.find_element(By.ID, 'continue')

# find Conditions of use link
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")

# find Privacy Notice link
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")

# find Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

# find Forgot your password link - N/A
# find Other issues with Sign-In link - N/A

# find Create your Amazon account button
driver.find_element(By.ID, 'createAccountSubmit')

print('Test Passed')

driver.quit()
