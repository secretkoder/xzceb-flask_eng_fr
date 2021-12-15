import unittest
from translator import englishToFrench, frenchToEnglish

class EnglishToFrenchTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
    
    def test2(self):
        self.assertEqual(englishToFrench(""), "")


class FrenchToEnglishTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
    
    def test2(self):
        self.assertEqual(frenchToEnglish(""), "")

if __name__ == "__main__":
    unittest.main()