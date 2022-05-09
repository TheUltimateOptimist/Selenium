import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from credentials import Credentials

def get_email():
    with open("sales_email.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        email = ""
        for line in lines:
            email+=line   
    return email

def send(address, subject):
    # connect to server
    server = smtplib.SMTP(host=Credentials.HOST_ADDRESS, port=Credentials.HOST_PORT)
    server.starttls()
    server.login(Credentials.MY_ADDRESS, Credentials.MY_PASSWORD)

    #creation of MIMEMultipart Object
    message = MIMEMultipart()
    message["From"] = Credentials.MY_ADDRESS
    message["To"] = address
    message["Subject"] = subject

    # creation of MIMEText Part
    textPart = MIMEText(get_email())

    # part attachment
    message.attach(textPart)

    # send email and close connection
    server.send_message(message)
    server.quit()