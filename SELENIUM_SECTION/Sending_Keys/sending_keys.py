

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

######### Example 1  #########
# driver.get('http://demostore.supersqa.com/my-account/')
#
# u_name = driver.find_element('id', 'username')
# u_name.send_keys('abcde')
#
# p_field = driver.find_element('id', 'password')
# p_field.send_keys('mypassword')
#
# submit_btn = driver.find_element('css selector', '#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > button')
# submit_btn.click()


######### Example 2  #########
# driver.get('http://demostore.supersqa.com')
#
# search_field = driver.find_element('id', 'woocommerce-product-search-field-0')
# search_field.send_keys('hoodie')
# time.sleep(3)
# search_field.send_keys(Keys.ENTER)

######### Example 3  #########
driver.get('http://demostore.supersqa.com/my-account/')
u_name = driver.find_element('id', 'username')
u_name.send_keys('abcd')
time.sleep(3)
u_name.send_keys(Keys.TAB)