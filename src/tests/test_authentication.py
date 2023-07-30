import unittest
from src.authentication import authenticateUser, UserDataSchema

class TestAuthentication(unittest.TestCase):

    def setUp(self):
        self.user_data = {
            "username": "test_user",
            "password": "test_password"
        }
        self.user_data_schema = UserDataSchema()

    def test_authenticate_user(self):
        authenticated_user = authenticateUser(self.user_data)
        self.assertEqual(authenticated_user, self.user_data)

    def test_user_data_schema(self):
        data, errors = self.user_data_schema.load(self.user_data)
        self.assertFalse(errors)
        self.assertEqual(data, self.user_data)

if __name__ == '__main__':
    unittest.main()