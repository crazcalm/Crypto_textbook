"""
plaintext will be written in lowercase letters and CIPHERTEXT will be
written in capital letters

The letters of the alphabet are assigned numbers (a=0, z=25)

Spaces and punctuation are omitted.
"""

import string

class Caesar_cipher():
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
    def __init__(self, key, plaintext=None, ciphertext=None):
        self.key = key        
        self.plaintext = plaintext
        self.ciphertext = ciiphertext

    
    def _is_string(self, text):
        return isinstance(text, str)
        
    def _no_special_chars(self, text):
        pass

    def _no_spaces(self, text):
        pass

    def _make_lowercase(self, key):
        pass

    def _make_uppercase(self, key):
        pass

    def encrypt(self):
        pass

    def decrypt(self):
