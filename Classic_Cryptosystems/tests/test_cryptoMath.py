import unittest
import cryptoMath

class Testing(unittest.TestCase):
    def test_testing(self):
        self.assertEqual(1,1)

class Test_CryptoMath(unittest.TestCase):
    def setUp(self):    
        self.math = cryptoMath
        self.case1 = (5,9)
        self.case2 = (50, 90)
        self.prime = 7

    def test_gcd(self):
        # Case 1
        result1 = self.math.gcd(self.case1[0], self.case1[1])
        answer1 = 1
    
        # Case 2
        result2 = self.math.gcd(self.case2[0], self.case2[1])
        answer2 = 10

        # Running tests
        self.assertEqual(result1, answer1)
        self.assertEqual(result2, answer2)


    def test_ext_gcd(self):
        # Case 1
        result1 = self.math.ext_gcd(self.case1[0], self.case1[1])
        answer1 = (1, 2, -1)

        # Case 2
        result2 = self.math.ext_gcd(self.case2[0], self.case2[1])
        answer2 = (10, 2, -1)

        # Running tests
        self.assertEqual(result1, answer1)
        self.assertEqual(result2, answer2)

    def test_modexp(self):
        result1 = self.math.modexp(self.case1[0], self.case1[1], self.prime)
        answer1 = 6

        result2 = self.math.modexp(self.case2[0], self.case2[1], self.prime)
        answer2 = 1

        self.assertEqual(result1, answer1)
        self.assertEqual(result2, answer2)

if __name__ == "__main__":
    unittest.main()
