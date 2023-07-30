import unittest
from src import human_computer_interaction as hci

class TestHumanComputerInteraction(unittest.TestCase):

    def setUp(self):
        self.userInput = "Test input"
        self.dataSet = {"key": "value"}

    def test_applyHCI(self):
        result = hci.applyHCI(self.userInput, self.dataSet)
        self.assertIsNotNone(result)

    def test_handleTouchscreenInput(self):
        result = hci.handleTouchscreenInput(self.userInput)
        self.assertEqual(result, self.userInput)

    def test_optimizeForMobile(self):
        result = hci.optimizeForMobile(self.dataSet)
        self.assertEqual(result, self.dataSet)

if __name__ == '__main__':
    unittest.main()