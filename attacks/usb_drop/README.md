# USB Drop Attack Simulation Research

**Author**: InfosecSamurai  
**Purpose**: Educational research into USB-based attack vectors and EDR/XDR detection capabilities.  
**Disclaimer**:  
⚠️ **For authorized security research only.**  
⚠️ **Never use against systems without explicit permission.**  

---

## Contents
- [`usb_payload.sh`](./usb_payload.sh) - Basic USB attack simulation (safe for labs)  
- [`usb_attack_simulation_edr_demo.sh`](./usb_attack_simulation_edr_demo.sh) - EDR/XDR detection testing script  
- [`cleanup.sh`](./cleanup.sh) - Artifact removal tool (if needed)  

---

## Lab Setup Instructions

### Requirements
- Linux VM (Kali/Ubuntu)  
- EDR/XDR tools (e.g., Elastic EDR, CrowdStrike)  
- Isolated network for C2 simulation  

### Execution
```bash
# Make scripts executable
chmod +x *.sh

# Run simulation (monitor EDR console)
./usb_attack_simulation_edr_demo.sh
```

---

## Research Objectives

### Attack Simulation
1. **Initial Access**: USB auto-execution simulation  
2. **Persistence**: User-level systemd service creation  
3. **Exfiltration**: Simulated data collection and C2 callbacks  

### Detection Testing
- Process tree anomalies  
- File integrity monitoring (FIM) alerts  
- Network traffic analysis  

---

## Expected EDR/XDR Alerts
| Alert Type               | Triggered By                          |
|--------------------------|---------------------------------------|
| Suspicious Process Tree  | `nohup` + nested `bash -c` execution  |
| File Tampering           | `/etc/passwd` modification attempt    |
| Unusual Network Traffic  | `curl` POST to test C2 server         |

---

## Ethical Usage Guidelines
1. **Legal Compliance**  
   - Only execute in owned/controlled environments  
   - Document all activity for research purposes  

2. **Cleanup**  
   ```bash
   ./cleanup.sh  # Removes test artifacts
   ```

3. **Reporting**  
   - Document EDR detection gaps  
   - Share findings responsibly with vendors  

---

## References
- [MITRE ATT&CK: T1091](https://attack.mitre.org/techniques/T1091/) 
- [NIST USB Threat Guidelines](https://csrc.nist.gov/)
