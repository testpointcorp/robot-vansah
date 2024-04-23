*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${TEST_URL}    https://google.com
${BROWSER}    chrome
*** Keywords ***
Open Browser To view Google Page
    Open Browser    ${TEST_URL}    ${BROWSER}
    Maximize Browser Window
