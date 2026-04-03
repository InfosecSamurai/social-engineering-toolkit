import logging
import os
from twilio.rest import Client

# -------------------------------
# Configurable Defaults
# -------------------------------
DEFAULT_MESSAGE = (
    "Alert: Your account has been compromised! "
    "Visit the link below to secure it:\n"
    "http://example-login.com"
)

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")

# -------------------------------
# Core SMS Function (Lab Mode)
# -------------------------------
def send_sms(target_phone, message=DEFAULT_MESSAGE):
    """Send SMS (lab mode only)."""
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        msg = client.messages.create(
            body=message,
            from_=TWILIO_NUMBER,
            to=target_phone
        )

        logging.info(f"[SUCCESS] SMS sent to {target_phone} | SID: {msg.sid}")

    except Exception as e:
        logging.error(f"[ERROR] Failed to send SMS: {e}")

# -------------------------------
# Simulation Mode
# -------------------------------
def simulate_sms(target_phone, message=DEFAULT_MESSAGE):
    """Simulate sending SMS (safe mode)."""
    logging.info(f"[SIMULATION] SMS would be sent to: {target_phone}")
    logging.info(f"Message:\n{message}")

    print("\n--- SIMULATED SMS ---")
    print(f"To: {target_phone}")
    print(message)
    print("----------------------\n")

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
        logging.error("No target phone number provided.")
        print("[!] No target specified.")
        return

    logging.info(f"Smishing module started | Target: {target} | Mode: {mode}")

    if mode == "simulation":
        simulate_sms(target)

    elif mode == "lab":
        if not all([TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_NUMBER]):
            logging.error("Missing Twilio credentials in environment variables.")
            print("[!] Missing Twilio configuration.")
            return

        send_sms(target)

    else:
        logging.warning(f"Unknown mode: {mode}")
        print(f"[!] Unknown mode: {mode}")

# -------------------------------
# Optional Direct Run (Testing)
# -------------------------------
if __name__ == "__main__":
    test_config = {
        "target": "+1234567890",
        "mode": "simulation"
    }
    run(test_config)
