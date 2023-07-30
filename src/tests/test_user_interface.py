import unittest
from src import user_interface

class TestUserInterface(unittest.TestCase):

    def setUp(self):
        self.ui = user_interface.UserInterface()

    def test_handleTouchscreenInput(self):
        userInput = "Test input"
        self.ui.handleTouchscreenInput(userInput)
        self.assertEqual(self.ui.userInput, userInput)

    def test_applyHCI(self):
        self.ui.applyHCI()
        self.assertTrue(self.ui.hciApplied)

    def test_processNaturalLanguage(self):
        naturalLanguageInput = "Test natural language input"
        processedInput = self.ui.processNaturalLanguage(naturalLanguageInput)
        self.assertEqual(processedInput, "Test processed natural language input")

    def test_applyAesthetics(self):
        self.ui.applyAesthetics()
        self.assertTrue(self.ui.aestheticsApplied)

    def test_optimizeUsability(self):
        self.ui.optimizeUsability()
        self.assertTrue(self.ui.usabilityOptimized)

    def test_applyJournalismPrinciples(self):
        self.ui.applyJournalismPrinciples()
        self.assertTrue(self.ui.journalismPrinciplesApplied)

    def test_applyMusicTheory(self):
        self.ui.applyMusicTheory()
        self.assertTrue(self.ui.musicTheoryApplied)

    def test_optimizeForMobile(self):
        self.ui.optimizeForMobile()
        self.assertTrue(self.ui.mobileOptimized)

if __name__ == '__main__':
    unittest.main()