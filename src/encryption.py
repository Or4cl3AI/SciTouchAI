```python
from cryptography.fernet import Fernet

class EncryptionService:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

    def encrypt_data(self, dataSet):
        encryptedData = self.cipher_suite.encrypt(dataSet)
        return encryptedData

    def decrypt_data(self, encryptedData):
        decryptedData = self.cipher_suite.decrypt(encryptedData)
        return decryptedData

def encryptData(dataSet):
    encryption_service = EncryptionService()
    encryptedData = encryption_service.encrypt_data(dataSet)
    return encryptedData
```