import logging

def simulate_webpage():
    print("\n--- SIMULATED PHISHING PAGE ---")
    print("Fake login page would be hosted here.")
    print("URL: http://example-login.com")
    print("-------------------------------\n")

def run(config):
    mode = config.get("mode", "simulation")

    logging.info(f"Web phishing module started | Mode: {mode}")

    if mode == "simulation":
        simulate_webpage()
    else:
        print("[!] Web server hosting not implemented in lab mode yet.")
