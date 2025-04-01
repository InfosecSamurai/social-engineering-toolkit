#!/bin/bash
# Triggers EDR alerts safely
echo "[+] Simulating EDR detection triggers:"
touch /etc/.test_edr_alert 2>/dev/null
curl -s http://example.com/edr_test >/dev/null
echo "* * * * * echo 'EDR Test'" | crontab - 2>/dev/null
echo "[+] Check your EDR console for alerts."
