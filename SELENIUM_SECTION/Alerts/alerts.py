

from selenium import webdriver

driver = webdriver.Chrome()

url = 'file:///Users/admas/Google%20Drive/PROJECTS/SuperSQA/Courses/MegaCourses/SeleniumPython/course-code/course-code-py-selenium-video/course-selenium-and-python/SELENIUM_SECTION/Alerts/alerts_example.html'

driver.get(url)

# # Ex 1
# alert_1_btn = driver.find_element('css selector', 'div#jsAlertExample button')
# alert_1_btn.click()
#
# my_alert = driver.switch_to.alert
# assert my_alert.text == 'I am a JavaScript Alert', "Unexpected text on alert."
# my_alert.accept()
# # my_alert.dismiss()
# import pdb; pdb.set_trace()
#
# # alert_1_btn = driver.find_element('css selector', 'div#jsAlertExample button')

# Ex 2
my_js_confirm_btn = driver.find_element('css selector', 'div#jsConfirmExample button')
my_js_confirm_btn.click()
my_confirm_alert = driver.switch_to.alert
# my_confirm_alert.accept()
# rs_message = driver.find_element('id', 'userResponse1').text
# assert rs_message == 'Great! You will love it!', "Wrong message after accepting"

my_confirm_alert.dismiss()
rs_message = driver.find_element('id', 'userResponse1').text
assert rs_message == "Too bad!!! You would've loved it!", "Wrong message after accepting"