from cmath import exp
import pyautogui
import subprocess
import time

import platform
import ipaddress as ip
import ipaddress 
import sys
# intro

print("===============================================")
print("Starting OP COMMAND CRACK Python script...")
print('===============================================')
time.sleep(0.1)

# WIFI PASSWORD
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
for i in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            print ("{:<30}|  {:<}".format(i, results[0]))
        except IndexError:
            print ("{:<30}|  {:<}".format(i, ""))
    except subprocess.CalledProcessError:
        print ("{:<30}|  {:<}".format(i, "ENCODING ERROR"))
time.sleep(0.7)
print("Completed Stage One, beginning Stage Two")
time.sleep(0.5)
print("================================================")

# PC SPEC VIEWER
xeon = platform.machine()
feetpics = platform.version()
wasdderef = platform.processor()
whyyoubully = platform.python_build()
explosion = platform.system()
fortnitebad = platform.release()
scienceclass = platform.architecture()
lastone = platform.uname()

print(xeon)
print(feetpics)
print(wasdderef)
print(whyyoubully)
print(explosion)
print(fortnitebad)
print(scienceclass)
print(lastone)
print("==================================================")
time.sleep(0.5)
print("Username and PC specs Status...")
time.sleep(0.2)
print("Grabbed!")
time.sleep(0.5)
print("Initiating 3rd stage, SYSTEM GRAB almost completed")

ip = ipaddress.ip_address(sys.argv[1])

print(ip)
