# Selenium Testing in Python

## Getting Started

Use pip to install the selenium package (perhaps in a virtual environment):

`pip install selenium`

Selenium needs a WebDriver before it can do anything useful. There are currently drivers for Firefox, Chrome, Edge and Safari.

### Installing Chromedriver

The installation process is pretty simple, chromedriver just needs to be executable on the development system so Selenium can interact with it during testing. Check the [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) Downloads page for the latest version of the driver to download and install.

`curl -L https://chromedriver.storage.googleapis.com/2.32/chromedriver_linux64.zip -o chromedriver.zip`

`sudo mkdir -p /usr/local/bin/`

`sudo unzip chromedriver.zip -d /usr/local/bin/`

`sudo chmod +x /usr/local/bin/chromedriver`


### Driving Chrome with Python

With chromedriver ready to go, all that is left is to import the WebDriver package from Selenium and tell it to use chromedriver.


`from selenium import webdriver`

`driver = webdriver.Chrome()`

`...`


### Going Headless

--headless, tells Chrome to execute the actions without rendering anything.

## Additional Resources

- [Installing ChromeDriver on macOS](https://www.kenst.com/2015/03/installing-chromedriver-on-mac-osx/)
- [Consistent Selenium Testing in Python](https://chrxs.net/articles/2017/09/01/consistent-selenium-testing/#going-headless)
