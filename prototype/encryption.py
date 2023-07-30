```python
from cryptography.fernet import Fernet

# Shared variable
data_set = None

def generate_key():
    """
    This function generates a new encryption key.
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    This function loads the encryption key from a file.
    """
    return open("secret.key", "rb").read()

def encrypt_data():
    """
    This function encrypts the global data_set using the loaded encryption key.
    """
    global data_set
    key = load_key()
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data_set)
    data_set = encrypted_data

def decrypt_data():
    """
    This function decrypts the global data_set using the loaded encryption key.
    """
    global data_set
    key = load_key()
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(data_set)
    data_set = decrypted_data
```