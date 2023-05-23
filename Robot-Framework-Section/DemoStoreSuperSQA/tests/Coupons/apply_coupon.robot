*** Settings ***
Library  SeleniumLibrary  implicit_wait=30
Library  demostore.coupons.Coupons


*** Test Cases ***
Valid coupon should show success message

    Open Browser  http://demostore.supersqa.com  Chrome
    Click Link  xpath=//*[@id="main"]/div[2]/ul/li[1]/a[2]
    sleep  1
    Go To  http://demostore.supersqa.com/cart/
    ${valid coupon}  Get a valid coupon
    Log  The valid coupon is: ${valid coupon}  console=True
    ${code}=  evaluate  ${valid coupon}.get("code")
    ${discount percent}=  evaluate  ${valid coupon}.get("discount")

    Input text  id=coupon_code  ${code}
    Press key  id=coupon_code  \\13

    ${success message}  Get text  class=woocommerce-message
    should be equal  ${success message}  Coupon code applied successfully1.
    close browser