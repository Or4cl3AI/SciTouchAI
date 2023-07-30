```python
import hashlib
import binascii
import os
from prototype.cyber_security import UserSchema

def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf-8'), salt.encode('ascii'), 100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password

def authenticate_user(user_input):
    user_data = UserSchema.load(user_input)
    stored_password = user_data.password
    provided_password = user_input.get('password')

    if verify_password(stored_password, provided_password):
        print("User_Authenticated")
        return True
    else:
        print("Authentication failed")
        return False
```