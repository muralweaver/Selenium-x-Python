from selenium import webdriver
from selenium.webdriver.common.by import By
'''
Every WebElement class (the result of the various find_element methods) has a send_keys method that can be used to simulate typing in an element.

Running the code should leave you with a Chrome window open to Wikipedia's results page for Python.
'''
driver = webdriver.Chrome()
driver.get('https://www.wikipedia.org/')
el = driver.find_element(By.ID, 'searchInput')
el.send_keys('Python')
form = driver.find_element(By.ID, 'search-form')
form.submit()
