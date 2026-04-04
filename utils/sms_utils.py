import logging
import os
from twilio.rest import Client

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")

class SMSService:
    def __init__(self):
        self.sid = TWILIO_ACCOUNT_SID
        self.token = TWILIO_AUTH_TOKEN
        self.number = TWILIO_NUMBER

    def validate(self):
        if not all([self.sid, self.token, self.number]):
            raise ValueError("Missing Twilio credentials")

    def send(self, target, message):
        try:
            self.validate()
            client = Client(self.sid, self.token)

            msg = client.messages.create(
                body=message,
                from_=self.number,
                to=target
            )

            logging.info(f"[SUCCESS] SMS sent to {target} | SID: {msg.sid}")

        except Exception as e:
            logging.error(f"[ERROR] SMS failed: {e}")

    def simulate(self, target, message):
        logging.info(f"[SIMULATION] SMS to: {target}")
        logging.info(f"Message:\n{message}")

        print("\n--- SIMULATED SMS ---")
        print(f"To: {target}")
        print(message)
        print("----------------------\n")


if __name__ == "__main__":
    service = SMSService()
    service.simulate("+1234567890", "Test message")
