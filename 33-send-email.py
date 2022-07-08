#!/usr/local/bin/python3
import smtplib
from email.mime.text import MIMEText

# Build email headers and body
body = "This is a test email."
msg = MIMEText(body)
msg["From"] = "username@gmail.com"
msg["To"] = "username@gmail.com"
msg["Subject"] = "Python Test"

# Instantiate SMTP with server address and port
server = smtplib.SMTP("smtp.gmail.com", 587)

# Initialize connection, login, send message and exit
server.starttls()
server.login("username", "password")
server.send(msg)
print("Message sent.")
server.quit()
