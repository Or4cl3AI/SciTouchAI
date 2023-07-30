```python
from cryptography.fernet import Fernet

# Function to generate a key for encryption
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Function to load the key
def load_key():
    return open("key.key", "rb").read()

# Function to encrypt the data
def encrypt_data(data_set):
    key = load_key()
    f = Fernet(key)
    encrypted_data = f.encrypt(data_set)
    return encrypted_data

# Function to decrypt the data
def decrypt_data(encrypted_data):
    key = load_key()
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data)
    return decrypted_data
```