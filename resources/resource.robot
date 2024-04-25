*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${TEST_URL}    https://google.com
${BROWSER}    chrome
${AssetKey}    Test-3
${TestCaseKey}
${SprintName}    SM Sprint 1
${ReleaseName}    Release 24
${EnvironmentName}    UAT

*** Keywords ***   
Open Browser To view Google Page
    Open Browser    ${TEST_URL}    ${BROWSER}
    Maximize Browser Window  
