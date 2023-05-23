*** Settings ***
Library  SeleniumLibrary
Resource  ../resources/MyAccountVariables.robot
Resource  ../resources/MyAccountKeywords.robot

Test Setup  Run Keywords  Open browser  about:blank  Chrome  AND  Go to  ${my_account_home_url}
Test Teardown  close browser


*** Test Cases ***
Login without username and password should show correct error


    Click button  ${login_button}
    ${act_msg}  Get Text  ${error_msg_box}
    should be equal  ${act_msg}  Error: Username is required.


Login with username but without password should show correct error


    Input Text  ${user_name_field}  fakename
    Click button  ${login_button}
    ${err msg}  Get text  ${error_msg_box}
    should be equal  ${err msg}  ERROR: The password field is empty.

Login with invalid username and invalid password should show correct error


    Input Text  ${user_name_field}  fakename
    Input Text  ${passw_field}  fakepassword
    Click button  ${login_button}
    ${err msg}  Get text  ${error_msg_box}
    should be equal  ${err msg}  ERROR: Invalid username. Lost your password?
