*** Settings ***
Library  Selenium2Library



*** Variables ***
${HOME PAGE URL}  http://demostore.supersqa.com
${SEARCH FIELD ID}  woocommerce-product-search-field-0
${EXISTING ITEM SEARCH TERM}  Flying Ninja
${EXPECTED URL TEXT}  /product/flying-ninja/
${ASCI CODE FOR ENTER}  \\13

${MSG BOX CLASS}  woocommerce-info
${NOT FOUND MSG}  No products were found matching your selection.



*** Test Cases ***
User should be able to search for an existing product

    Open browser  about:blank  Chrome
    Go To  ${HOME PAGE URL}
    Input Text  ${SEARCH FIELD ID}  ${EXISTING ITEM SEARCH TERM}
    Press Key  ${SEARCH FIELD ID}  ${ASCI CODE FOR ENTER}
    Location Should Contain  ${EXPECTED URL TEXT}
    Close Browser


User should see correct message when searching none existing item

    Open Browser  about:blank  Chrome
    Go To  ${HOME PAGE URL}
    Input Text  ${SEARCH FIELD ID}  abc
    Press Key  ${SEARCH FIELD ID}  ${ASCI CODE FOR ENTER}
    Element Text Should Be  class=${MSG BOX CLASS}  ${NOT FOUND MSG}
    Close Browser