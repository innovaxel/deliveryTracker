import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, sender, recipients, password):
    try:
        # Create a MIMEText object for HTML
        msg = MIMEMultipart("alternative")

        html_body = MIMEText(body, "html")
        msg.attach(html_body)

        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = ", ".join(recipients)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp_server:
            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, recipients, msg.as_string())

        print("Email sent successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

