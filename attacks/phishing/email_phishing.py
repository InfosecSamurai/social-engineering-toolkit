import smtplib
import logging
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# -------------------------------
# Configurable Defaults
# -------------------------------
DEFAULT_SUBJECT = "Important Security Update"
DEFAULT_BODY = """
Hello {name},

Please log in immediately to your account to secure it.
Click the link below to access your account:

http://example-login.com

Regards,
Security Team
"""

SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.example.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")

# -------------------------------
# Core Email Function
# -------------------------------
def send_email(receiver_email, name, subject=DEFAULT_SUBJECT, body=DEFAULT_BODY):
    """Send an email (used in lab mode only)."""
    try:
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = receiver_email
        msg["Subject"] = subject

        message = body.format(name=name)
        msg.attach(MIMEText(message, "plain"))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email, msg.as_string())
        server.quit()

        logging.info(f"[SUCCESS] Email sent to {receiver_email}")

    except Exception as e:
        logging.error(f"[ERROR] Failed to send email: {e}")

# -------------------------------
# Simulation Mode
# -------------------------------
def simulate_email(receiver_email, name, subject=DEFAULT_SUBJECT, body=DEFAULT_BODY):
    """Simulate sending an email (safe mode)."""
    message = body.format(name=name)

    logging.info(f"[SIMULATION] Email would be sent to: {receiver_email}")
    logging.info(f"Subject: {subject}")
    logging.info(f"Body:\n{message}")

    print("\n--- SIMULATED EMAIL ---")
    print(f"To: {receiver_email}")
    print(f"Subject: {subject}")
    print(message)
    print("------------------------\n")

# -------------------------------
# Required Framework Entry Point
# -------------------------------
def run(config):
    """
    Standard entry point for the attack framework.
    Expects:
        config = {
            "target": "...",
            "mode": "simulation" | "lab"
        }
    """
    target = config.get("target")
    mode = config.get("mode", "simulation")

    if not target:
        logging.error("No target provided.")
        print("[!] No target specified.")
        return

    name = "Target User"

    logging.info(f"Phishing module started | Target: {target} | Mode: {mode}")

    if mode == "simulation":
        simulate_email(target, name)
    elif mode == "lab":
        if not SENDER_EMAIL or not SENDER_PASSWORD:
            logging.error("Missing email credentials in environment variables.")
            print("[!] Missing SENDER_EMAIL or SENDER_PASSWORD.")
            return

        send_email(target, name)
    else:
        logging.warning(f"Unknown mode: {mode}")
        print(f"[!] Unknown mode: {mode}")

# -------------------------------
# Optional Direct Run (Testing)
# -------------------------------
if __name__ == "__main__":
    test_config = {
        "target": "test@example.com",
        "mode": "simulation"
    }
    run(test_config)
