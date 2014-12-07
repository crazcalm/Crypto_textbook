import unittest
import shift_ciphers

class Test_Basic_crypto_checks(unittest.TestCase):
    def setUp(self):
        self.check = shift_ciphers.Basic_cryto_checks()
        self.text = "123 abc XYZ !@#"

    def test_is_string(self):
        result = self.check._is_string(self.text)
        self.assertTrue(result)
        
    def test_no_special_chars(self):
        result = self.check._no_special_chars(self.text)
        answer = "123 abc XYZ "
        self.assertEqual(result, answer)

    def test_no_spaces(self):
        results = self.check._no_spaces(self.text)
        answer = "123abcXYZ!@#"
        self.assertEqual(results, answer)

    def test_make_lowercase(self):
        result = self.check._make_lowercase(self.text)
        answer = "123 abc xyz !@#"
        self.assertEqual(result, answer)

    def test_make_uppercase(self):
        result = self.check._make_uppercase(self.text)
        answer = "123 ABC XYZ !@#"
        self.assertEqual(result, answer)

if __name__=="__main__":
    unittest.main()
