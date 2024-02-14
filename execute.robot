*** Settings ***
Documentation        Enviar email em pipeline.

Library    alertaemail.py

*** Variables ***

*** Keywords ***
Send Email By Pipeline
    [Arguments]                      ${attribute}
    ${SORT_BOLEAN}    Send Email     ${attribute}
    IF    ${SORT_BOLEAN} == $True
        Pass Execution    ''
    ELSE
        Fail
    END

*** Test Cases ***
Send Email Using Python
    Send Email By Pipeline      senha