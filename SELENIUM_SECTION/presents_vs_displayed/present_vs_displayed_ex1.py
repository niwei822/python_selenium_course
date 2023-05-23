

from selenium import webdriver


driver = webdriver.Chrome()
driver.implicitly_wait(5)

url = 'file:///Users/admas/Google%20Drive/PROJECTS/SuperSQA/Courses/MegaCourses/SeleniumPython/course-code/course-code-py-selenium-video/course-selenium-and-python/SELENIUM_SECTION/presents_vs_displayed/present_vs_displayed.html'

driver.get(url)

my_btn1 = driver.find_element('id', 'btn1')
my_btn1_txt = my_btn1.text
print("First button text: {}".format(my_btn1_txt))

my_btn2 = driver.find_element('id', 'btn2')
print("Second button text: {}".format(my_btn2.text))

my_btn3 = driver.find_element('id', 'btn3')
print("Third button text: {}".format(my_btn3.text))

my_btn4 = driver.find_element('id', 'btn4')
print("Fourth button text: {}".format(my_btn4.text))

if my_btn4.is_displayed():
    my_btn4.click()
else:
    raise Exception("Button 4 is not displayed")
import pdb; pdb.set_trace()