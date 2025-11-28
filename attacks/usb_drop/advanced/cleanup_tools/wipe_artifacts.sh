#!/bin/bash
# Securely removes artifacts

# Ensure these files exist before shredding
if [ -f /tmp/.stolen_data.tgz ]; then
    shred -zu /tmp/.stolen_data.tgz
fi

if [ -f /dev/shm/.log ]; then
    shred -zu /dev/shm/.log
fi

# Clear command history
history -c
