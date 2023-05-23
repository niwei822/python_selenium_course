## all about driver: https://www.selenium.dev/documentation/en/webdriver/driver_requirements/
# Error: “chromedriver” cannot be opened because the developer cannot be verified.
# Solution: xattr -d com.apple.quarantine /Users/admas/Downloads/chromedriver

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# option 1 (Selenium 3)
# driver = webdriver.Chrome(executable_path='/Users/admas/Downloads/chromedriver')
# driver.get("https://google.com")

# option 1 (Selenium 4)
# se = Service(executable_path='/Users/admas/Downloads/chromedriver')
# driver = webdriver.Chrome(service=se)

#option 2 is adding the executable to system path

driver = webdriver.Chrome()

