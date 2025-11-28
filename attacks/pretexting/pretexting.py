import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO)

# Configuration
sender_email = os.getenv('SENDER_EMAIL')  # Use environment variable
sender_password = os.getenv('SENDER_PASSWORD')  # Use environment variable
subject = 'Urgent Request for Information'

body = """
Hello {name},

I need your help with a quick verification process for our company's system. 
Could you provide me with your account number and username?

Best Regards,
HR Department
"""

def send_pretexting_email(receiver_email, name):
    """Send pretexting email."""
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        # Create the body of the email
        message = body.format(name=name)
        msg.attach(MIMEText(message, 'plain'))

        # Set up the server and send the email
        server = smtplib.SMTP('smtp.example.com', 587)  # Replace with a valid SMTP server
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()

        logging.info(f"Pretexting email sent to {receiver_email}")
    except Exception as e:
        logging.error(f"Failed to send pretexting email: {e}")

# Example usage
if __name__ == '__main__':
    send_pretexting_email('victim@example.com', 'John Doe')  # Replace with a test email
