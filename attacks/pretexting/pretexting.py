import logging
from utils.email_utils import EmailService

# -------------------------------
# Default Message
# -------------------------------
DEFAULT_SUBJECT = "Quick Request"
DEFAULT_BODY = """
Hi {name},

I need your help with something urgent. Can you take a look at the link below and get back to me?

http://example-link.com

Thanks,
Admin
"""

# -------------------------------
# Core Logic
# -------------------------------
def execute(target, name="User", subject=DEFAULT_SUBJECT, body=DEFAULT_BODY, mode="simulation"):
    service = EmailService()
    message = body.format(name=name)

    if mode == "simulation":
        service.simulate(target, subject, message)
    elif mode == "lab":
        service.send(target, subject, message)
    else:
        logging.warning(f"Unknown mode: {mode}")
        print(f"[!] Unknown mode: {mode}")

# -------------------------------
# Framework Entry
# -------------------------------
def run(config):
    target = config.get("target")
    mode = config.get("mode", "simulation")

    if not target:
        logging.error("No target provided.")
        print("[!] No target specified.")
        return

    logging.info(f"Pretexting module started | Target: {target} | Mode: {mode}")

    execute(target, mode=mode)

# -------------------------------
# Direct Test
# -------------------------------
if __name__ == "__main__":
    test_config = {
        "target": "test@example.com",
        "mode": "simulation"
    }
    run(test_config)
