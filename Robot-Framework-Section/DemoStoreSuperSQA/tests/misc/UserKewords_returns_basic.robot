

*** Test Cases ***
Demo of user keyword returning 1 value

    ${now}  I get the current datetime
    log to console  Returned is: ${now}

Demo of user keyword returning multiple values

    ${r1}  ${r2}  ${r3}  I get 3 random numbers
    log to console  ${\n}
    log to console  ${r1}
    log to console  ${r2}
    log to console  ${r3}


Demo of user keyword returning multiple values and takes arguments

    ${r1}  ${r2}  ${r3}  I get 3 random numbers with upper and lower limit  50  100
    log to console  ${\n}
    log to console  ${r1}
    log to console  ${r2}
    log to console  ${r3}

*** Keywords ***
I get the current datetime

    ${current_time}  get time
    log to console  ${\n}
    log to console  The current time is ${current_time}
    [Return]  ${current_time}


I get 3 random numbers

    ${num1}  Evaluate  random.randint(0, 20)  modules=random
    ${num2}  Evaluate  random.randint(0, 20)  modules=random
    ${num3}  Evaluate  random.randint(0, 20)  modules=random

    [Return]  ${num1}  ${num2}  ${num3}

I get 3 random numbers with upper and lower limit

    [Arguments]  ${min}  ${max}

    ${num1}  Evaluate  random.randint(${min}, ${max})  modules=random
    ${num2}  Evaluate  random.randint(${min}, ${max})  modules=random
    ${num3}  Evaluate  random.randint(${min}, ${max})  modules=random

    [Return]  ${num1}  ${num2}  ${num3}