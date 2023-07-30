import unittest
from src import natural_language_processing as nlp

class TestNaturalLanguageProcessing(unittest.TestCase):

    def setUp(self):
        self.userInput = "This is a test input"
        self.processedInput = nlp.processNaturalLanguage(self.userInput)

    def test_processNaturalLanguage(self):
        self.assertIsNotNone(self.processedInput, "Processed input should not be None")

    def test_processedInputType(self):
        self.assertIsInstance(self.processedInput, str, "Processed input should be a string")

    def test_processedInputContent(self):
        self.assertNotEqual(self.processedInput, self.userInput, "Processed input should not be the same as the original input")

if __name__ == '__main__':
    unittest.main()