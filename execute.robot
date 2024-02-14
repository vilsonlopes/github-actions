*** Settings ***
Documentation        Enviar email em pipeline.

Library         alertaemail.py

*** Variables ***

*** Keywords ***
Send Email By Pipeline
    [Arguments]           ${email1}         ${email2}
    Send Email            ${email1}        ${email2}

*** Test Cases ***
Send Email By Pipeline
    Send Email By Pipeline    'elainyr.s@gmail.com'    'liandro.arq@gmail.com'
