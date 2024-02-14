*** Settings ***
Documentation        Enviar email em pipeline.

Library         alertaemail.py

*** Variables ***

*** Keywords ***
Send Email By Pipeline
    Send Email

*** Test Cases ***
Send Email
    Send Email By Pipeline
