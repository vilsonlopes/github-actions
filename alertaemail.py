import sys
# import os
import smtplib
from email.message import EmailMessage
# from dotenv import load_dotenv

# load_dotenv()

password = sys.argv


def send_mail():

    email_address = 'buscadorcaixa@gmail.com'
    email_password = password[1]

    contacts = ["vilsonlopes@yahoo.com.br", "liandro.sys@gmail.com"]

    msg = EmailMessage()
    msg['Subject'] = "Testes Actions"
    msg['From'] = email_address
    msg['To'] = ','.join(contacts)

    # The email body for recipients with non-HTML email clients.
    body_text = ""
    # The HTML body of the email.
    body_html = """
    <h1>Deu certo</h1>
    <p>Não desista, continue tentando.</a>
    """

    # msg.set_content(body_text)
    # msg.add_alternative(body_text, subtype='text')
    msg.add_alternative(body_html, subtype='html')

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(email_address, email_password)
            # server.send_message(msg)
            server.send_message(msg)
    except Exception as e:
        print(f'Erro ao enviar {e}')
    else:
        print('Email enviado com sucesso!')


send_mail()
