import unittest
from src import touchscreen_input

class TestTouchscreenInput(unittest.TestCase):

    def setUp(self):
        self.userInput = "Test input"
        self.touchscreen = touchscreen_input.TouchscreenInput()

    def test_handleTouchscreenInput(self):
        result = self.touchscreen.handleTouchscreenInput(self.userInput)
        self.assertEqual(result, self.userInput)

    def test_inputField(self):
        self.touchscreen.inputField = self.userInput
        self.assertEqual(self.touchscreen.inputField, self.userInput)

if __name__ == '__main__':
    unittest.main()