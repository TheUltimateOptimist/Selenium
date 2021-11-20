import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
class EmailData:
    MY_ADDRESS = "jonathan.dueck@digital-confidence.de"
    MY_PASSWORD = "A1a1B2b2C3c3D4d4"
    HOST_ADDRESS = "smtp.1und1.de"
    HOST_PORT = 587

def send(address, subject, text):
    # connect to server
    server = smtplib.SMTP(host=EmailData.HOST_ADDRESS, port=EmailData.HOST_PORT)
    server.starttls()
    server.login(EmailData.MY_ADDRESS, EmailData.MY_PASSWORD)

    #creation of MIMEMultipart Object
    message = MIMEMultipart()
    message["From"] = EmailData.MY_ADDRESS
    message["To"] = address
    message["Subject"] = subject

    # creation of MIMEText Part
    textPart = MIMEText(text)

    # part attachment
    message.attach(textPart)

    # send email and close connection
    server.send_message(message)
    server.quit()