import smtplib
import email.message


def enviar_email(emailto='', nome=''):
    corpo_email = """
    <p>Teste1</p> """+nome

    msg = email.message.Message()
    msg['Subject'] = 'Seu amigo Secreto'
    msg['From'] = 'amigosecretornd@outlook.com'
    msg['to'] = emailto
    password = '123456789AB'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.outlook.com: 587')
    s.starttls()

    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['to']], msg.as_string().encode('utf-8'))
    print('Email enviado')


enviar_email(emailto='rodrigoaugusto839@gmail.com', nome="Rodrigo")
