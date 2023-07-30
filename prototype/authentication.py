```python
import hashlib
import binascii
import os
from prototype.cyber_security import userDataSchema

def authenticateUser(username, password):
    """
    Verify a stored password against one provided by user
    """
    stored_password = userDataSchema.find_one({"username": username})['password']
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password

def login():
    """
    Handle user login
    """
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if authenticateUser(username, password):
        print("User authenticated successfully.")
        return True
    else:
        print("Authentication failed. Please try again.")
        return False

loginButton = input("Press any key to login: ")
if loginButton:
    login()
```