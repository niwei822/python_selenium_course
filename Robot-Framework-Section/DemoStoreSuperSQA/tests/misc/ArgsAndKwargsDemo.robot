*** Settings ***
Library  demostore.miscLibraries.ArgsAndKwargs


*** Test Cases ***
Demo of *args


    example of args
    example of args  aa
    example of args  aa  bb  cc  cc

Demo of kwargs

    example of kwargs  aa  bb=two