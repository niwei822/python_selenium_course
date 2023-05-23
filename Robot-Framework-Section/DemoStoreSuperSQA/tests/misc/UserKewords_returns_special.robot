

*** Test Cases ***
Demo of user keyword returning 1 value

    ${now}  I get the current datetime
    log to console  ${\n}
    log to console  ${now}



Demo of using Return from keyword if


    ${n1}  I get a number larger than 75  50  100
    log to console  ${n1}



*** Keywords ***
I get the current datetime

    ${cur_time}  get time

    Return From Keyword  ${cur_time}


I get a number larger than 75

    [Arguments]  ${min}  ${max}
    ${num1}  Evaluate  random.randint(${min}, ${max})  modules=random
    log to console  ${\n}
    log to console  Value of num1 is: ${num1}
    return from keyword if  ${num1} > 75  ${num1}
    log to console  Condition is not met
    return from keyword  0