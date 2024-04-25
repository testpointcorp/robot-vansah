*** Settings ***

Resource    ../resources/resource.robot

*** Test Cases ***

Open Google Search Page 1
    Open Browser To view Google Page
    [Teardown]    Close Browser
    Set Test Variable    ${TestCaseKey}    Test-C10
    Set Test Variable    ${AssetKey}    Test-3

Open Google Search Page 2
    Open Browser To view Google Page
    [Teardown]    Close Browser
    Set Test Variable    ${TestCaseKey}    Test-C6
    Set Test Variable    ${AssetKey}    b97fe80b-0b6a-11ee-8e52-5658ef8eadd5