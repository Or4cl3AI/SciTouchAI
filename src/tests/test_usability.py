import unittest
from src import usability

class TestUsability(unittest.TestCase):

    def setUp(self):
        self.userInput = "Test input"
        self.optimizedUserInput = usability.optimizeUsability(self.userInput)

    def test_optimizeUsability(self):
        self.assertNotEqual(self.userInput, self.optimizedUserInput,
                            "The optimized user input should not be the same as the original input.")

    def test_optimizeUsability_type(self):
        self.assertIsInstance(self.optimizedUserInput, str,
                              "The optimized user input should be a string.")

    def test_optimizeUsability_content(self):
        self.assertTrue(" " not in self.optimizedUserInput,
                        "The optimized user input should not contain any spaces.")

if __name__ == '__main__':
    unittest.main()