import argparse
import importlib
import logging
import os
import sys

# -------------------------------
# Logging Setup
# -------------------------------
log_file = os.path.join(os.path.dirname(__file__), "attack.log")
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
console = logging.StreamHandler(sys.stdout)
console.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console.setFormatter(formatter)
logging.getLogger().addHandler(console)

# -------------------------------
# Module Loader
# -------------------------------
def load_module(module_name):
    """
    Dynamically load an attack module from attacks/<module_name>/<module_name>.py
    """
    try:
        module_path = f"attacks.{module_name}.{module_name}"
        module = importlib.import_module(module_path)
        return module
    except ModuleNotFoundError:
        logging.error(f"Module '{module_name}' not found at path: {module_path}")
        return None
    except Exception as e:
        logging.error(f"Error loading module '{module_name}': {e}")
        return None

# -------------------------------
# Attack Runner
# -------------------------------
def run_attack(module_name, config):
    module = load_module(module_name)
    if not module:
        print(f"[!] Module '{module_name}' could not be loaded.")
        return

    if hasattr(module, "run"):
        logging.info(f"Running attack module: {module_name} with config: {config}")
        try:
            module.run(config)
        except Exception as e:
            logging.error(f"Error executing module '{module_name}': {e}")
    else:
        print(f"[!] Module '{module_name}' does not implement a run(config) function.")
        logging.warning(f"Module '{module_name}' missing run() interface.")

# -------------------------------
# Main CLI Entry
# -------------------------------
def main():
    parser = argparse.ArgumentParser(description="Red Team Attack Framework Controller")
    parser.add_argument("--module", required=True, help="Attack module to run (e.g., phishing, smishing, evil_twin)")
    parser.add_argument("--target", help="Target identifier (email, phone, etc.)")
    parser.add_argument("--mode", choices=["simulation", "lab"], default="simulation", help="Execution mode")
    args = parser.parse_args()

    # Central config dictionary
    config = {
        "target": args.target,
        "mode": args.mode
    }

    run_attack(args.module, config)

if __name__ == "__main__":
    main()
