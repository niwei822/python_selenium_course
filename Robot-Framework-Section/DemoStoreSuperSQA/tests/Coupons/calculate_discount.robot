*** Settings ***
Library  SeleniumLibrary  implicit_wait=30
Library  demostore.coupons.Coupons


*** Variables ***
${first item add to cart locator}  //*[@id="main"]/div[2]/ul/li[1]/a[2]
${second item add to cart locator}  //*[@id="main"]/div[2]/ul/li[2]/a[2]
${to to cart button locator}  //*[@id="menu-item-159"]/a
${coupon field locator}  id=coupon_code
${cart total locator}  css=#post-71 > div > div > div > div > table > tbody > tr.order-total > td


*** Test Cases ***
Coupon should be applied correctly

    # go to homepage
    Open Browser  http://demostore.supersqa.com  Chrome

    # add the first two items on the page to cart
    Click Link  ${first item add to cart locator}
    sleep  1
    Click Link  ${second item add to cart locator}
    sleep  1

    # go to the cart page
    Click Link  ${to to cart button locator}

    # get a valid coupon code and apply the coupon
    ${valid coupon}  Get a valid coupon
    ${code}=  evaluate  ${valid coupon}.get("code")
    ${discount percent}=  evaluate  ${valid coupon}.get("discount")

    # get the total amount displayed
    ${total before coupon}  Get Text  ${cart total locator}
    Log  Total before coupon is: ${total before coupon}  console=true

    # apply the coupon and verify success
    Input Text  ${coupon field locator}  ${code}
    Press key  ${coupon field locator}  \\13
    ${success message}  Get Text  class=woocommerce-message
    Should Be Equal  ${success message}  Coupon code applied successfully.

    # get the new total price after the coupon is applied
    sleep  1
    ${total after coupon}  Get Text  ${cart total locator}
    Log  Total after coupon is: ${total after coupon}  console=true

    # verify coupon is applied correctly
    Discount should be calculated correctly  ${total before coupon}  ${total after coupon}  ${discount percent}

    Close Browser