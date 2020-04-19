from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

'''
This clear function will take a WebElement, get the length of its value attribute, and simulate hitting the BACK_SPACE until all text is removed from the field.
'''


def clear(element):
    value = element.get_attribute('value')
    if len(value) > 0:
        for char in value:
            element.send_keys(Keys.BACK_SPACE)


driver = webdriver.Chrome()
driver.get('https://www.google.com/')
el = driver.find_element(By.NAME, 'q')
el.send_keys('selenium')
el.send_keys(Keys.RETURN)
# Selenium will need to find the element again because the page has changed. Call clear() function to clear.
el = driver.find_element(By.NAME, 'q')
clear(el)
