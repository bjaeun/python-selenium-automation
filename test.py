from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='/Users/jaeundelio/Desktop/python-selenium-automation/chromedriver')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# click Orders button
search = driver.find_element(By.ID, 'nav-orders').click()

# find Sing-in
driver.find_element(By.CSS_SELECTOR, "[class='a-spacing-small']")

assert 'ap/signin?' in driver.current_url, f'{driver.current_url} Is not the right page'

driver.quit()