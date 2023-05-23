


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = 'file:///Users/admas/Google%20Drive/PROJECTS/SuperSQA/Courses/MegaCourses/SeleniumPython/course-code/course-code-py-selenium-video/course-selenium-and-python/SELENIUM_SECTION/Radios/radios_example.html'

driver.get(url)


expected_default_value = '21-40'

locator_by_value = 'input[name="age-group-radio"][value="{value}"]'

# # Example 1. verify default is selected
# default_element = driver.find_element(By.CSS_SELECTOR, locator_by_value.format(value=expected_default_value))
# assert default_element.is_selected(), f"The default value of {expected_default_value} is not selected."

# Ex 2
expected_values = ['21-40','41-60','61-80','81+']
all_radios = driver.find_elements(By.NAME, 'age-group-radio')
assert len(all_radios) == len(expected_values), "the number of radios does not match the expected." \
                                                "Expected: {}, Actual: {}".format(len(expected_values),len(all_radios) )