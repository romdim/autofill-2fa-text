#!/usr/bin/env python3
import fileinput
import pyotp
import os
import time
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env', verbose=True)

secret = os.getenv('SECRET')
totp = pyotp.TOTP(secret)

def replace_code_to_file():
  newCode = totp.now()
  # Read in the file
  with open('ovpn-creds.txt', 'r') as file :
    filedata = file.read()

  lastCode = filedata[-6:]
  # Replace the target string
  filedata = filedata.replace(lastCode, newCode)

  # Write the file out again
  with open('ovpn-creds.txt', 'w') as file:
    file.write(filedata)

# Replace the code for the first time
replace_code_to_file()
print('Script is running. You can connect to VPN.')

# Wait until new code is out (exact or half minute)
while (time.localtime().tm_sec != 0 and time.localtime().tm_sec != 30 ):
  time.sleep(1)

# Every 30 seconds run replacement of code
while True:
    replace_code_to_file()
    time.sleep(30)