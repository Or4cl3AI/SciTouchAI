import unittest
from src import music_theory

class TestMusicTheory(unittest.TestCase):

    def setUp(self):
        self.music_theory = music_theory.applyMusicTheory()

    def test_music_theory_application(self):
        result = self.music_theory.apply()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)
        self.assertIn('harmony', result)
        self.assertIn('rhythm', result)
        self.assertIn('melody', result)

    def test_music_theory_optimization(self):
        result = self.music_theory.optimize()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)
        self.assertIn('optimizedHarmony', result)
        self.assertIn('optimizedRhythm', result)
        self.assertIn('optimizedMelody', result)

if __name__ == '__main__':
    unittest.main()