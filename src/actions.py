#!/usr/bin/env python3
import os
import sys
import subprocess

if os.getuid() != 0:
    subprocess.run(["/usr/bin/pkexec", __file__])

import ctypes
libc = ctypes.cdll['libc.so.6']
RB_POWER_OFF = 0x4321fedc
RB_AUTOBOOT  = 0x01234567

#https://github.com/systemd/systemd/blob/main/src/shutdown/shutdown.c#L653
#https://unix.stackexchange.com/questions/83049/rolling-your-own-init-how-to-shutdown-restart#83053

def poweroff():
    os.sync()
    libc.reboot(RB_POWER_OFF)

def reboot():
    os.sync()
    libc.reboot(RB_AUTOBOOT)

if "poweroff" in sys.argv:
    poweroff()

if "reboot" in sys.argv:
    reboot()
