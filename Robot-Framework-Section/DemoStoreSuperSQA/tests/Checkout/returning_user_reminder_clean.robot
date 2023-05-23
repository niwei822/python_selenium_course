*** Settings ***
Library  SeleniumLibrary  implicit_wait=30

Resource  ../resources/checkout_page_resources.robot


*** Test Cases ***
Checkout page should prompt returning users to login

    Go to home page
    Add item to cart and navigate to checkout
    Notice for returning user to log in should be displayed
    Close Browser


