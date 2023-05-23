from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn


def verify_12_producs_are_displayed():
    """

    Returns:

    """

    selenium_lib = BuiltIn().get_library_instance('SeleniumLibrary')
    browser = selenium_lib._current_browser()

    # get the container element that contains all products
    all_products_element = browser.find_element_by_class_name('products')

    # get all list items or products in the container
    products_elements_list = all_products_element.find_elements_by_tag_name('li')

    number_of_products = len(products_elements_list)
    if number_of_products != 12:
        raise Exception("Number of products in the page is not 12. Actual: {}".format(number_of_products))

    # step further and check if the products are visible
    logger.info("Checking if products are visible on page.")
    for product_element in products_elements_list:
        if not product_element.is_displayed():
            raise Exception("One more products on the page is/are not visible.")

    logger.console("PASS. Correct number of products are displayed.")