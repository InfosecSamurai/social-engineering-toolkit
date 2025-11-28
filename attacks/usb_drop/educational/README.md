# USB Drop Attack Simulations (Educational)

**Legal Use Only.** These scripts simulate attack patterns for defensive research.

## Files
- `usb_payload.sh`: Basic USB attack simulation
- `edr_detection_demo.sh`: Safe EDR alert triggers

## Usage
1. Run the following command to make the scripts executable:
   ```bash
   chmod +x *.sh
   ```

2. Execute the EDR detection demo:
   ```bash
   ./edr_detection_demo.sh  # Monitor your EDR console for alerts
   ```
   You should expect to see alerts triggered in your EDR console due to the actions simulated by this script.