import unittest
from src import responsive_design

class TestResponsiveDesign(unittest.TestCase):

    def setUp(self):
        self.dataSet = "test_data"
        self.userInput = "test_input"
        self.responsive_design = responsive_design.applyResponsiveDesign(self.dataSet, self.userInput)

    def test_applyResponsiveDesign(self):
        self.assertEqual(self.responsive_design.dataSet, self.dataSet)
        self.assertEqual(self.responsive_design.userInput, self.userInput)

    def test_optimizeForMobile(self):
        optimized_data = self.responsive_design.optimizeForMobile()
        self.assertIsNotNone(optimized_data)

    def test_handleTouchscreenInput(self):
        handled_input = self.responsive_design.handleTouchscreenInput(self.userInput)
        self.assertEqual(handled_input, self.userInput)

if __name__ == '__main__':
    unittest.main()