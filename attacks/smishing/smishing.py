from twilio.rest import Client
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO)

# Twilio credentials (Sign up for a Twilio account to get these)
account_sid = os.getenv('TWILIO_ACCOUNT_SID')  # Use environment variable
auth_token = os.getenv('TWILIO_AUTH_TOKEN')  # Use environment variable
twilio_number = os.getenv('TWILIO_NUMBER')  # Use environment variable

client = Client(account_sid, auth_token)

def send_smishing_sms(target_phone):
    """Send fake SMS message for phishing."""
    try:
        message = client.messages.create(
            body="Alert: Your account has been compromised! Click this link to secure your account: http://fake-login-page.com",
            from_=twilio_number,
            to=target_phone
        )
        logging.info(f"Smishing message sent to {target_phone}")
    except Exception as e:
        logging.error(f"Failed to send SMS: {e}")

# Example usage
if __name__ == '__main__':
    send_smishing_sms('+1234567890')  # Replace with a test phone number
