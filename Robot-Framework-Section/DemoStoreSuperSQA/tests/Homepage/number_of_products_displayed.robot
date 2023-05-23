*** Settings ***
Library  SeleniumLibrary
Library  demostore.homepage.homepage


*** Test Cases ***
Home page should have 12 items displayed

    Open browser  about:blank  Chrome
    Go to  http://demostore.supersqa.com
    Verify 12 producs are displayed
    Close browser