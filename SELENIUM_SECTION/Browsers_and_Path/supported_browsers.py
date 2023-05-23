## all about driver: https://www.selenium.dev/documentation/en/webdriver/driver_requirements/
# Error: “chromedriver” cannot be opened because the developer cannot be verified.
# Solution: xattr -d com.apple.quarantine /Users/admas/Downloads/chromedriver
# Solution: xattr -d com.apple.quarantine /usr/local/bin/geckodriver


from selenium import webdriver


##### Chrome
# driver = webdriver.Chrome()
# driver.get('http://demostore.supersqa.com')

#### Firefox
# driver = webdriver.Firefox()
# driver.get('http://demostore.supersqa.com')

### Safari
driver = webdriver.Safari()
driver.get('http://demostore.supersqa.com')