from twilio.rest import Client

def send_sms(account_sid, auth_token, twilio_number, target_number, message):
    """Send an SMS using Twilio."""
    try:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=message,
            from_=twilio_number,
            to=target_number
        )
        print(f"SMS sent to {target_number}: {message.sid}")
    except Exception as e:
        print(f"Failed to send SMS: {e}")

# Example usage
if __name__ == '__main__':
    send_sms('your_account_sid', 'your_auth_token', 'your_twilio_number', '+1234567890', 'Phishing Alert! Click the link: http://fake-login.com')
