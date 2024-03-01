import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from trackingapp.settings import *

def send_email(subject, body, sender, recipients, password):

    print("Sending email...")
    print("Recipient: ", recipients)
    print("Subject: ", subject)
    print("Sender: ", sender)
    print("Password: ", password)
    try:
        # Create a MIMEText object for HTML
        msg = MIMEMultipart("alternative")

        html_body = MIMEText(body, "html")
        msg.attach(html_body)

        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = ", ".join(recipients)

        with smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT) as smtp_server:
            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, recipients, msg.as_string())

        print("Email sent successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

