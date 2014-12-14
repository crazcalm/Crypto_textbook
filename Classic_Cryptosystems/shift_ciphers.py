"""
plaintext will be written in lowercase letters and CIPHERTEXT will be
written in capital letters

The letters of the alphabet are assigned numbers (a=0, z=25)

Spaces and punctuation are omitted.
"""

import string

alphabet = "abcdefghijklmnopqrstuvwxyz"
numbers = [1,2,3,4,5,6,7,8,9,0]


class Basic_cryto_checks():
    """
    Class of basic checks needed for all of these ciphers
    """
    def _is_string(self, text):
        return isinstance(text, str)
        
    def _no_special_chars(self, text):
        """
        Removes special characters
        """
        wanted_chars = string.letters + string.digits + string.whitespace
        results = "".join([char for char in text if char in wanted_chars])
        return results

    def _no_spaces(self, text):
        results = "".join([char for char in text if char not in string.whitespace])
        return results

    def _make_lowercase(self, text):
        return text.lower()

    def _make_uppercase(self, text):
        return text.upper()

    def _char_to_num(self, text):
        for char in text:
            if char.lower() in alphabet:
                yield alphabet.index(char.lower())

    def _num_to_char(self, num_list):
        for num in num_list:
            try:
                index = num % 26
                yield alphabet[index]
            except:
                yield str(num)

class Caesar_cipher(Basic_cryto_checks):
    """
    One of the earliest cryptosystems is often attributed to Julius Caesar.
    Suppose he wanted to send a plaintext such as

        'gual is divided into three parts'

    but he didn't want Brutus to read it. He shifted each letter by three
    places, so a became D, b became E, c became F, etc. The end of the
    alphabet wrapped around to the beginning, so x becames A, y became B,
    and z became C. The ciphertext was then

        'JDXOLVGLYLGHGLQWRWKUHHSDUWV'

    Decryption was accomplished by shifting back by three spaces
    """
    def __init__(self, key=None, plaintext=None, ciphertext=None, formated_plaintext=None,
                    shifted_plain_nums=None, plain_nums=[], key_shift=0,
                    cipher_nums=[]):
        self.key = key        
        self.plaintext = plaintext
        self.ciphertext = ciphertext
        self.formated_plaintext = formated_plaintext
        self.shifted_plain_nums = shifted_plain_nums
        self.plain_nums = plain_nums
        self.key_shift = key_shift
        self.cipher_nums = cipher_nums

    def encrypt(self):
        """
        Steps:
            1. convert key to num
            2. convert plaintext to numbers
            3. apply shift.
            4. convert numbers to ciphertext
        """
        # Key shift value
        for num in self._char_to_num(self.key):
            self.key_shift = num

        # convert plaintext to numbers
        self.plain_nums=[]
        self.formated_plaintext = self._format_plaintext()
        for num in self._char_to_num(self.formated_plaintext):
            self.plain_nums.append(num)

        # Shift plaintext numbers
        self.cipher_nums=[]
        for num in self.shift(self.plain_nums):
            self.cipher_nums.append(num)

        # obtain ciphertext
        self.ciphertext = ""
        for char in self._num_to_char(self.cipher_nums):
            self.ciphertext = self.ciphertext + char

        self.ciphertext = self._make_uppercase(self.ciphertext)
        return self.ciphertext

    def _format_plaintext(self):
        """
        Makes sure that there are not spaces, special characters or whitespace
        """
        plaintext = self.plaintext
        plaintext = self._make_lowercase(plaintext)
        plaintext = self._no_special_chars(plaintext)
        plaintext = self._no_spaces(plaintext)
        return plaintext

    def shift(self, nums):
        for num in nums:
            yield num + self.key_shift

    def decrypt(self):
        pass
