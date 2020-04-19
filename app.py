from selenium import webdriver
'''
 A simple task: getting the "word of the day" from Merriam-Webster's website.
 Searching the page reveals that this class is unique, so it can be used by Selenium to identify the element and get its content like so:
 Running the above should invoke a Chrome window that loads the word of the day page and then closes. The Python script should output the word before exiting. 
'''
driver = webdriver.Chrome()
driver.get('https://www.merriam-webster.com/word-of-the-day')
element = driver.find_element_by_css_selector('.word-and-pronunciation h1')
print(element.text)
driver.close()
