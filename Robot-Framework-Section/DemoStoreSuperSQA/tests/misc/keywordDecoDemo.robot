*** Settings ***
Library  demostore.miscLibraries.TheKeywordDecorator


*** Test Cases ***
Refun calculated correctly

#    user requests full refund
    The user have requested a refund
    the order should be refunded fully