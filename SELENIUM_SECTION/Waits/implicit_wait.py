

from selenium import webdriver


driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('file:///Users/admas/Google%20Drive/PROJECTS/SuperSQA/Courses/MegaCourses/SeleniumPython/course-code/course-code-py-selenium-video/course-selenium-and-python/SELENIUM_SECTION/Waits/page_with_slow_image.html')
my_image = driver.find_element('id', 'the_slow_image')
my_image.click()
print("Found image")