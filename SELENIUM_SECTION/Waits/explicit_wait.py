

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get('file:///Users/admas/Google%20Drive/PROJECTS/SuperSQA/Courses/MegaCourses/SeleniumPython/course-code/course-code-py-selenium-video/course-selenium-and-python/SELENIUM_SECTION/Waits/page_with_slow_image.html')

# my_image = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.ID, 'the_slow_image')))

my_image = wait.until(EC.visibility_of_all_elements_located((By.ID, 'the_slow_image')))

print("Found image")