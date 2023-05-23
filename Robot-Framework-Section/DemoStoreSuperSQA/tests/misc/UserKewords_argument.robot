

*** Test Cases ***
50% coupon should discount total by half

    I add 2 items to cart  xpath=/foo/bar  class=dummy_class
    I apply 50% off coupon  id=fake_id  AAA





*** Keywords ***
I add 2 items to cart

    [Arguments]  ${item1 locator}  ${item2locator}

#    Click link  ${item1 locator}
#    Click link  ${item2 locator}
    log to console  ${item1 locator}
    log to console  ${item2 locator}

I apply 50% off coupon

    [Arguments]  ${coupon_locator}  ${coupon code}=XYZ50off

    log to console  ${coupon_locator}
    log to console  ${coupon code}