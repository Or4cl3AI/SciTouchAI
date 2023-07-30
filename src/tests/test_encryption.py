import unittest
from src import encryption

class TestEncryption(unittest.TestCase):

    def setUp(self):
        self.dataSet = "This is some scientific data"
        self.encryptedData = None

    def test_encryptData(self):
        self.encryptedData = encryption.encryptData(self.dataSet)
        self.assertNotEqual(self.dataSet, self.encryptedData)

    def test_decryptData(self):
        decryptedData = encryption.decryptData(self.encryptedData)
        self.assertEqual(self.dataSet, decryptedData)

if __name__ == '__main__':
    unittest.main()