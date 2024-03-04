#!/usr/bin/env python3
import pyotp

key = '37OZZ74PX5BT5WHXAG2HCO7WJJBBO34M'
totp = pyotp.TOTP(key)
print(totp.now())