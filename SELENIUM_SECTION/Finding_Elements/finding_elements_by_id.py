

from selenium import webdriver
from selenium.webdriver.common.by import By
import pdb


driver = webdriver.Chrome()
driver.get('http://demostore.supersqa.com')

cart = driver.find_element(By.ID, 'site-header-cart')
cart.click()

driver.get('http://demostore.supersqa.com/my-account/')
u_name = driver.find_element(By.ID, 'username')
u_name.send_keys('myusername')
pdb.set_trace()

# NOTE: to find available methods just do dir(<varialbe>)
# Example: dir(driver)
# Example: dir(cart)