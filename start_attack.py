import logging
from attacks.phishing.email_phishing import send_email
from attacks.smishing.smishing import send_smishing_sms
from attacks.evil_twin.evil_twin import create_evil_twin_network
from attacks.pretexting.pretexting import send_pretexting_email

logging.basicConfig(level=logging.INFO)

def start_phishing():
    send_email('victim@example.com', 'John Doe')

def start_smishing():
    send_smishing_sms('+1234567890')

def start_evil_twin():
    create_evil_twin_network('wlan0', 'Free_WiFi')

def start_pretexting():
    send_pretexting_email('victim@example.com', 'John Doe')

# Start any attack
if __name__ == '__main__':
    start_phishing()
    start_smishing()
    start_evil_twin()
    start_pretexting()
