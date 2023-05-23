# open browser
# go to webpage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://practicetestautomation.com/practice-test-login/")

# $x("//tag[@attribute='value']")

username_locator = driver.find_element(By.ID, "username")
username_locator.send_keys("student")
password_locator = driver.find_element(By.NAME, "password")
password_locator.send_keys("Password123")
submit_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
submit_locator.click()
time.sleep(2)

actual_url = driver.current_url
assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"

loginmsg_locator = driver.find_element(By.TAG_NAME, "h1")
actual_text = loginmsg_locator.text
assert actual_text == "Logged In Successfully"

logout_locator = driver.find_element(By.LINK_TEXT, "Log out")
assert logout_locator.is_displayed()