import smtplib
import logging
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# -------------------------------
# Environment Config
# -------------------------------
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.example.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
EMAIL_USERNAME = os.getenv("EMAIL_USERNAME")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# -------------------------------
# Email Service
# -------------------------------
class EmailService:
    def __init__(self):
        self.server = SMTP_SERVER
        self.port = SMTP_PORT
        self.username = EMAIL_USERNAME
        self.password = EMAIL_PASSWORD

    def validate(self):
        """Ensure required credentials exist."""
        if not self.username or not self.password:
            raise ValueError("Missing EMAIL_USERNAME or EMAIL_PASSWORD")

    def send(self, to_email, subject, body):
        """Send an email (lab mode only)."""
        try:
            self.validate()

            msg = MIMEMultipart()
            msg["From"] = self.username
            msg["To"] = to_email
            msg["Subject"] = subject
            msg.attach(MIMEText(body, "plain"))

            with smtplib.SMTP(self.server, self.port) as server:
                server.starttls()
                server.login(self.username, self.password)
                server.sendmail(self.username, to_email, msg.as_string())

            logging.info(f"[SUCCESS] Email sent to {to_email}")

        except Exception as e:
            logging.error(f"[ERROR] Failed to send email: {e}")

    def simulate(self, to_email, subject, body):
        """Simulate sending email safely."""
        logging.info(f"[SIMULATION] Email would be sent to: {to_email}")
        logging.info(f"Subject: {subject}")
        logging.info(f"Body:\n{body}")

        print("\n--- SIMULATED EMAIL ---")
        print(f"To: {to_email}")
        print(f"Subject: {subject}")
        print(body)
        print("------------------------\n")


# -------------------------------
# Optional Direct Test
# -------------------------------
if __name__ == "__main__":
    service = EmailService()
    service.simulate(
        "test@example.com",
        "Test Subject",
        "This is a simulated email."
    )
