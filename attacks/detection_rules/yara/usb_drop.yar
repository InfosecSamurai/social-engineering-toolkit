rule usb_drop_attack {
  meta:
    description = "Detects USB drop attack scripts"
    author = "Your Name"
  strings:
    $crontab = "* * * * *" nocase
    $ncat = "ncat" nocase
    $dev_shm = "/dev/shm/" nocase
  condition:
    any of them
}
