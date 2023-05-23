*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${homepage_url}               http://demostore.supersqa.com/
${missing_username_error}     Error: Username is required.
${missing_password_error}     ERROR: The password field is empty.


*** Test Cases ***
Login attempt with invalid user should show error
    Open Browser                ${homepage_url}  Chrome
    Click Element               id=menu-item-157
    Input Text                  id=username     fakeuser
    Input Text                  id=password     fakepassword
    Click Element               css=#post-73 > div > div > form > p:nth-child(3) > input.woocommerce-Button.button
    Element Should Be Visible   css=#content > div > div.woocommerce > ul
    Element Text Should Be      css=#content > div > div.woocommerce > ul  ERROR: Invalid username. Lost your password?
    Close Browser


Login attempt with empty password should show "Empty Password" error message
    Open Browser                    ${homepage_url}  Chrome
    Click Element                   id=menu-item-157
    Input Text                      id=username     fakeuser
    Wait Until Element Is Visible   css=#post-73 > div > div > form > p:nth-child(3) > input.woocommerce-Button.button
    Click Element                   css=#post-73 > div > div > form > p:nth-child(3) > input.woocommerce-Button.button
    Element Should Be Visible       css=#content > div > div.woocommerce > ul
    Element Text Should Be          css=#content > div > div.woocommerce > ul  ${missing_password_error}
    Close Browser


Login attempt with empty username should show "Empty Password" error message
    Open Browser                    ${homepage_url}  Chrome
    Click Element                   id=menu-item-157
    Input Text                      id=password     fakepassword
    Wait Until Element Is Visible   css=#post-73 > div > div > form > p:nth-child(3) > input.woocommerce-Button.button
    Click Element                   css=#post-73 > div > div > form > p:nth-child(3) > input.woocommerce-Button.button
    Element Should Be Visible       css=#content > div > div.woocommerce > ul
    Element Text Should Be          css=#content > div > div.woocommerce > ul  ${missing_username_error}
    Close Browser
