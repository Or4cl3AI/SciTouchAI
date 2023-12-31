```python
import hashlib
import binascii
import os
from prototype.cyber_security import authSuccess

# User data schema
userDataSchema = {
    "username": "",
    "password": ""
}

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

def authenticateUser(userInput):
    """Authenticate user based on input"""
    username = userInput.get('username')
    password = userInput.get('password')
    stored_password = userDataSchema.get('password')
    if username == userDataSchema.get('username') and verify_password(stored_password, password):
        authSuccess.emit()
        return True
    return False
```