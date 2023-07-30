```python
from cryptography.fernet import Fernet

def generate_key():
    """
    This function generates a key for encryption and decryption
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    This function loads the key named secret.key from current directory
    """
    return open("secret.key", "rb").read()

def encryptData(dataSet):
    """
    This function encrypts the data
    """
    key = load_key()
    f = Fernet(key)
    encryptedData = f.encrypt(dataSet)
    return encryptedData

def decryptData(encryptedData):
    """
    This function decrypts the data
    """
    key = load_key()
    f = Fernet(key)
    decryptedData = f.decrypt(encryptedData)
    return decryptedData
```