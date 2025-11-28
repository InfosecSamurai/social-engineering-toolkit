from twilio.rest import Client
import os
import logging

def send_sms(target_number, message):
    """Send an SMS using Twilio."""
    account_sid = os.getenv('TWILIO_SID')  # Use environment variable
    auth_token = os.getenv('TWILIO_AUTH')  # Use environment variable
    twilio_number = os.getenv('TWILIO_PHONE')  # Use environment variable
    
    try:
        client = Client(account_sid, auth_token)
        sms_message = client.messages.create(
            body=message,
            from_=twilio_number,
            to=target_number
        )
        logging.info(f"SMS sent to {target_number}: {sms_message.sid}")
    except Exception as e:
        logging.error(f"Failed to send SMS: {e}")

# Example usage
if __name__ == '__main__':
    send_sms('+1234567890', 'Phishing Alert! Click the link: http://fake-login.com')
