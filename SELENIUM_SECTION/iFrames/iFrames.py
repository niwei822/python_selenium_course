"""
NOTES:
    to switch to the frame use
        WebElement
        ID
        NAME
        INDEX
"""

from selenium import webdriver

driver = webdriver.Chrome()

url = 'file:///Users/admas/Google%20Drive/PROJECTS/SuperSQA/Courses/MegaCourses/SeleniumPython/course-code/course-code-py-selenium-video/course-selenium-and-python/SELENIUM_SECTION/iFrames/iFrames_example.html'

driver.get(url)

## example without iFrame
# driver.find_element('id', 'btnOutFrame').click()
# my_alert = driver.switch_to.alert
# my_alert_text = my_alert.text
# assert my_alert_text == 'Just Clicked Outside iFrame', "Should've gotten outside message"
# my_alert.dismiss()

# example of iFrame
# useing 'WebElement'
my_frame = driver.find_element('id', 'myFrame1')
driver.switch_to.frame(my_frame)
driver.find_element('id', 'btnInFrame').click()
print(driver.switch_to.alert.text)
driver.switch_to.alert.dismiss()

driver.switch_to.default_content()
driver.find_element('id', 'btnOutFrame').click()
driver.switch_to.alert.dismiss()



# using 'ID'
# driver.switch_to.frame('myFrame1')
# driver.find_element('id', 'btnInFrame').click()
# print(driver.switch_to.alert.text)
# driver.switch_to.alert.dismiss()

# Using 'Index'
# driver.switch_to.frame(2)
# driver.find_element('id', 'btnInFrame').click()
# print(driver.switch_to.alert.text)
# driver.switch_to.alert.dismiss()