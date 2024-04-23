*** Settings ***

Resource    ../resources/resource.robot

*** Test Cases ***

Open Google Search Page
    Open Browser To view Google Page
    [Teardown]    Close Browser