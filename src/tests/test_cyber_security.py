import unittest
from src import cyber_security

class TestCyberSecurity(unittest.TestCase):

    def setUp(self):
        self.dataSet = "test_data"
        self.userInput = "test_user"
        self.encryptedData = None
        self.authenticatedUser = None

    def test_encryptData(self):
        self.encryptedData = cyber_security.encryptData(self.dataSet)
        self.assertNotEqual(self.encryptedData, self.dataSet)

    def test_authenticateUser(self):
        self.authenticatedUser = cyber_security.authenticateUser(self.userInput)
        self.assertEqual(self.authenticatedUser, self.userInput)

    def test_applyCyberSecurityMeasures(self):
        secure_data = cyber_security.applyCyberSecurityMeasures(self.dataSet)
        self.assertNotEqual(secure_data, self.dataSet)

if __name__ == '__main__':
    unittest.main()