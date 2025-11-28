#!/bin/bash
# Triggers EDR alerts safely

echo "[+] Simulating EDR detection triggers:"

if touch /etc/.test_edr_alert; then
    echo "[+] Test EDR alert file created."
else
    echo "[!] Failed to create test EDR alert file. Please run as root." >&2
fi

# Checking network availability before running curl
if curl -s http://example.com/edr_test >/dev/null; then
    echo "[+] EDR test request sent successfully."
else
    echo "[!] Failed to reach EDR test URL. Check your network connection." >&2
fi

if echo "* * * * * echo 'EDR Test'" | crontab -; then
    echo "[+] Cron job for EDR test created."
else
    echo "[!] Failed to set up the cron job." >&2
fi

echo "[+] Check your EDR console for alerts."
