```python
from cryptography.fernet import Fernet

class EncryptionModule:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

    def encrypt_data(self, data):
        encrypted_data = self.cipher_suite.encrypt(data)
        return encrypted_data

    def decrypt_data(self, encrypted_data):
        decrypted_data = self.cipher_suite.decrypt(encrypted_data)
        return decrypted_data

if __name__ == "__main__":
    encryption_module = EncryptionModule()
    data = b"Sensitive data that needs to be encrypted"
    encrypted_data = encryption_module.encrypt_data(data)
    print("Encrypted data: ", encrypted_data)
    decrypted_data = encryption_module.decrypt_data(encrypted_data)
    print("Decrypted data: ", decrypted_data)
```