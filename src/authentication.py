import hashlib
import binascii
import os

def authenticateUser(username, password, db):
    """
    Authenticate user by comparing hashed password in the database with the one user entered.
    """
    # Fetch user data from the database
    user_data = db.get(username)

    if not user_data:
        return False

    # Extract the salt and hashed password from the database
    salt, stored_password = user_data.split(':')

    # Hash the password provided by the user
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('ascii'), 100000)

    # Convert the hashed password to stored password format
    hashed_password = binascii.hexlify(hashed_password).decode('ascii')

    # Compare the hashed password with the stored password
    if hashed_password == stored_password:
        authenticatedUser = username
        return True

    return False

def hash_password(password):
    """
    Hash a password for storing.
    """
    # Generate a random salt
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')

    # Hash the password along with the salt
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

    # Convert the hashed password to stored password format
    hashed_password = binascii.hexlify(hashed_password).decode('ascii')

    # Combine the salt and hashed password
    stored_password = salt.decode('ascii') + ':' + hashed_password

    return stored_password

def store_user(username, password, db):
    """
    Store user data in the database.
    """
    # Hash the password
    stored_password = hash_password(password)

    # Store the username and hashed password in the database
    db[username] = stored_password
