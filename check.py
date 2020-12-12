from pyotp import *
from config import keys
import os


# Returns an authentication code using your auth key that is good for 30 seconds.
def totp_code():
    totp = TOTP(keys['auth_key'])
    print(totp.now())
    return totp.now()
