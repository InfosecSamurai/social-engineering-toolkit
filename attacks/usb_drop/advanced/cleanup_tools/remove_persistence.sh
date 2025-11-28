#!/bin/bash
# Removes persistence mechanisms

# Remove all cron jobs (use with caution)
# Use specific command to target malicious jobs if possible
crontab -r

# Check if the malicious service is running before stopping it
if systemctl is-active --quiet malicious-service; then
    systemctl stop malicious-service
fi

# Remove the service file if it exists
if [ -f /etc/systemd/system/malicious-service.service ]; then
    rm -f /etc/systemd/system/malicious-service.service
fi
