import logging
import os
from attacks.phishing.email_phishing import send_email
from attacks.smishing.smishing import send_smishing_sms
from attacks.evil_twin.evil_twin import create_evil_twin_network
from attacks.pretexting.pretexting import send_pretexting_email

logging.basicConfig(level=logging.INFO)

def start_phishing():
    email = os.getenv("ATTACK_EMAIL", "default_victim@example.com")
    send_email(email, 'John Doe')

def start_smishing():
    phone = os.getenv("ATTACK_PHONE", "+1234567890")
    send_smishing_sms(phone)

def start_evil_twin():