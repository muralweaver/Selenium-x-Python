import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

'''
Write a simple test by inheriting the TestCase class
simply import the <unittest> module and define a class that inherits the TestCase class

1) def setUp(self):
    Using setUp() Method to Manage Test Pre-requisites. It works as an entry point for the test cases. We can use it to run a fixed set of actions before executing a test

2) def test_search_in_wikipedia(self):    
    Similar to the <setup()> method, test methods get implemented in the TestCase class.
    While adding these methods, it’s a good practice to prefix their names with the word test. Having such a name helps Test Runner distinguish between a test and other methods

3) def tearDown(self):
    Define Cleanup Strategy to Free Resources Post Test Execution
    Once the test execution finishes, the pre-requisites specified in the setup() method have to be cleaned up
    So to achieve this, the base TestCase class provides another method i.e. tearDown() which the runner calls after test execution
    It lets us clean the values initialized at the beginning of the test via setup() method.
'''
class sendInput(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_search_in_wikipedia(self):
        driver = self.driver
        driver.get('https://www.wikipedia.org/')
        wikiSearch = driver.find_element(By.ID, 'searchInput')
        wikiSearch.send_keys("Python")
        wikiSearch.send_keys(Keys.RETURN)

    def tearDown(self):
        self.driver.close()

# Below is the piece of code to facilitate command line execution. We’ll need to add it in our test script towards the end. It’ll get the test result details displayed on the console.
if __name__ == "__main__":
    unittest.main()
