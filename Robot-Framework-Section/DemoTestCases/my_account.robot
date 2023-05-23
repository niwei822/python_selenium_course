*** Settings ***
Library  SeleniumLibrary


*** Test Cases ***
Login attempt with invalid user should show error

    Open Browser                http://demostore.supersqa.com/  Firefox
    Click Element               id=menu-item-157
    Input Text                  id=username     fakeuser
    Input Text                  id=password     fakepassword
    Click Element               css=#post-73 > div > div > form > p:nth-child(3) > input.woocommerce-Button.button
    Element Should Be Visible   css=#content > div > div.woocommerce > ul
    Element Text Should Be      css=#content > div > div.woocommerce > ul  ERROR: Invalid username. Lost your password?
    Close Browser
