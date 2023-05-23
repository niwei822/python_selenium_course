*** Settings ***
Library  SeleniumLibrary  implicit_wait=30


*** Variables ***
${homepage}  http://demostore.supersqa.com
${first item locator}  xpath=//*[@id="main"]/div[2]/ul/li[1]/a[2]
${cart button locator}  xpath=//*[@id="menu-item-159"]/a
${checkout button locator}  xpath=//*[@id="post-71"]/div/div/div/div/div/a
${login notice locator}  xpath=//*[@id="post-72"]/div/div/div[1]


*** Test Cases ***
Checkout page should prompt returning users to login

    # go to the omepage
    Open browser  about:blank  Firefox
    Go to  ${homepage}

    # add item to the cart and navigate to checkout
    Click link  ${first item locator}
    sleep  1
    Click link  ${cart button locator}
    Click link  ${checkout button locator}

    # verify there is notice for returning users to login
    ${login notice text}  Get text  ${login notice locator}
    Should be equal  ${login notice text}  Returning customer? Click here to login
    Close Browser