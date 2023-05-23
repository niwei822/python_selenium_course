*** Settings ***
Documentation  This is the documentation for DumentationInTestCaseFiles.robot.
...             We can also break into lines if the documentation is too long.
...             There theree dots (...) represent continuation.
...             ${\n}Also we can add new line.

Library  SeleniumLibrary


*** Test Cases ***
First test case

    [Documentation]  This is documentation for the first test case.
    ...             This is actualy on a second line.
    ...             ${\n}This is a new line break.

    I am user keyword 1

Second test case
    I am user keyword 2

Third test case

    I am user keyword 3




*** Keywords ***
I am user keyword 1

    [Documentation]  This is documentation for user keyword.
    ...             This is the second line of user keyword doc.

    log to console  I just run user keyword 1

I am user keyword 2

    log to console  I just run user keyword 2

I am user keyword 3

    log to console  I just run user keyword 3