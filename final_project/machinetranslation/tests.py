import unittest
from translator import english_to_french, french_to_english

french = 'Bonjour'
f2e_text = french_to_english(french)
english = 'Hello'
e2f_text = english_to_french(english)

class Test_Translator(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(f2e_text, 'Hello')
        self.assertNotEqual(french_to_english(''), 'Hello')

        self.assertEqual(e2f_text, 'Bonjour')
        self.assertNotEqual(english_to_french(''), 'Bonjour')  

unittest.main()