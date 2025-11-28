import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import logging

def send_email(receiver_email, subject, message):
    """Send an email using SMTP."""
    sender_email = os.getenv('EMAIL_USERNAME')  # Use environment variable
    sender_password = os.getenv('EMAIL_PASSWORD')  # Use environment variable
    
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # Connect to SMTP server
        server = smtplib.SMTP('smtp.example.com', 587)  # Consider making this configurable
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()

        logging.info(f"Email sent to {receiver_email}")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")

# Example usage
if __name__ == '__main__':
    send_email('victim@example.com', 'Security Alert', 'Click the link: http://fake-login.com')
