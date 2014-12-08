import unittest
import shift_ciphers

class Test_Basic_crypto_checks(unittest.TestCase):
    def setUp(self):
        self.check = shift_ciphers.Basic_cryto_checks()
        self.text = "123 abc XYZ !@#"
        self.alph = "abcdefghijklmnopqrstuvwxyz"
        self.num = list(range(26))

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

    def test_char_to_num(self):
        result = []
        for num in self.check._char_to_num(self.alph):
            result.append(num)

        answer = list(range(26))
        self.assertEqual(result, answer)

    def test_num_to_char(self):
        result = ""
        for char in self.check._num_to_char(self.num):
            result = result + char

        answer = self.alph
        self.assertEqual(result, answer) 

class Test_Caesar_cipher(unittest.TestCase):
    
    def setUp(self):
        pass

    def test__init__(self):
        pass

    def test__format_plaintext(self):
        pass

    def test_shift(self):
        pass

    def test_encrypt(self):
        pass

    def test_decrypt(self):
        pass

if __name__=="__main__":
    unittest.main()
