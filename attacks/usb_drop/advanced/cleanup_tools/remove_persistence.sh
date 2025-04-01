#!/bin/bash
# Removes persistence mechanisms
crontab -r
systemctl stop malicious-service 2>/dev/null
rm -f /etc/systemd/system/malicious-service.service
