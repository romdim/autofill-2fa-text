#!/usr/bin/env python3
import fileinput
import pyotp
import os
import time
import base64
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env', verbose=True)

secret = base64.b32encode(os.getenv('SECRET'))
totp = pyotp.TOTP(secret)
while True:
  newCode = totp.now()
  print(newCode)
  
  # Read in the file
  with open('ovpn-creds.txt', 'r') as file :
    filedata = file.read()

  lastCode = filedata[-6:]
  # Replace the target string
  filedata = filedata.replace(lastCode, newCode)

  # Write the file out again
  with open('ovpn-creds.txt', 'w') as file:
    file.write(filedata)

  print('Sth else')
  time.sleep(1)