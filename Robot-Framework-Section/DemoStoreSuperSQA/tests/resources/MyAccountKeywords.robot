*** Settings ***
Library  SeleniumLibrary
Resource  ./MyAccountVariables.robot

*** Keywords ***
I go to my account page

    Open browser  about:blank  Chrome
    Go to  ${my_account_home_url}