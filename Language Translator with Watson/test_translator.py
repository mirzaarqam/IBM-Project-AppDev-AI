import unittest
from translator import english_to_french, french_to_english


class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('I want to tell you something but I can not'),
                         'Je veux vous dire quelque chose, mais je ne peux pas')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('I want to tell you something but I can not'), 'Bonjour')


class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('Je veux vous dire quelque chose, mais je ne peux pas'),
                         'I want to tell you something but I can not')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Je veux vous dire quelque chose, mais je ne peux pas'), 'Hello')


unittest.main()