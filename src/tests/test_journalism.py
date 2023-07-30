import unittest
from src import journalism

class TestJournalismPrinciples(unittest.TestCase):

    def setUp(self):
        self.journalism = journalism.applyJournalismPrinciples()

    def test_journalism_principles(self):
        self.assertEqual(self.journalism, True, "Journalism principles not applied correctly")

    def test_visual_appeal(self):
        visual_appeal = self.journalism.check_visual_appeal()
        self.assertEqual(visual_appeal, True, "Visual appeal not up to the mark")

    def test_content_clarity(self):
        content_clarity = self.journalism.check_content_clarity()
        self.assertEqual(content_clarity, True, "Content clarity is not satisfactory")

    def test_user_engagement(self):
        user_engagement = self.journalism.check_user_engagement()
        self.assertEqual(user_engagement, True, "User engagement is not satisfactory")

if __name__ == '__main__':
    unittest.main()