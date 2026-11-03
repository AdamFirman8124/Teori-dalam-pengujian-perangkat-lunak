

# Generated at 2026-11-02 17:06:38.437526
# Unit test for function prime_length
def test_prime_length():
    assert module_0.prime_length("Hello") == True      # length 5 (prime)
    assert module_0.prime_length("ab") == True         # length 2 (prime)
    assert module_0.prime_length("abc") == True        # length 3 (prime)
    assert module_0.prime_length("aaaa") == False      # length 4 (not prime)
    assert module_0.prime_length("") == False          # length 0 (not prime)
    assert module_0.prime_length("a") == False         # length 1 (not prime)
    assert module_0.prime_length("abcdef") == False    # length 6 (not prime)
    assert module_0.prime_length("aabbccdd") == False  # length 8 (not prime)
    assert module_0.prime_length("aabbcc") == False    # length 6 (not prime)
    assert module_0.prime_length("aabbccc") == True    # length 7 (prime)
    assert module_0.prime_length("aaaaaaaaaaa") == True  # length 11 (prime)
    print("All test cases passed!")

# Generated at 2026-11-02 17:07:20.785750
# Unit test for function prime_length
def test_prime_length():import unittest
from solution import prime_length


class TestPrimeLength(unittest.TestCase):

    def test_prime_length_hello(self):
        """'Hello' has length 5, which is prime."""
        self.assertTrue(module_0.prime_length("Hello"))

    def test_prime_length_abcdcba(self):
        """'abcdcba' has length 7, which is prime."""
        self.assertTrue(module_0.prime_length("abcdcba"))

    def test_prime_length_kittens(self):
        """'kittens' has length 7, which is prime."""
        self.assertTrue(module_0.prime_length("kittens"))

    def test_prime_length_orange(self):
        """'orange' has length 6, which is not prime."""
        self.assertFalse(module_0.prime_length("orange"))

    def test_prime_length_empty_string(self):
        """Empty string has length 0, not prime."""
        self.assertFalse(module_0.prime_length(""))

    def test_prime_length_single_char(self):
        """Single character has length 1, not prime."""
        self.assertFalse(module_0.prime_length("a"))

    def test_prime_length_two_chars(self):
        """'ab' has length 2, which is prime."""
        self.assertTrue(module_0.prime_length("ab"))

    def test_prime_length_three_chars(self):
        """'abc' has length 3, which is prime."""
        self.assertTrue(module_0.prime_length("abc"))

    def test_prime_length_four_chars(self):
        """'abcd' has length 4, which is not prime."""
        self.assertFalse(module_0.prime_length("abcd"))

    def test_prime_length_nine_chars(self):
        """Length 9 (3x3) is not prime."""
        self.assertFalse(module_0.prime_length("a" * 9))

    def test_prime_length_eleven_chars(self):
        """Length 11 is prime."""
        self.assertTrue(module_0.prime_length("a" * 11))

    def test_prime_length_large_prime(self):
        """Length 13 is prime."""
        self.assertTrue(module_0.prime_length("a" * 13))

    def test_prime_length_large_composite(self):
        """Length 20 is not prime."""
        self.assertFalse(module_0.prime_length("a" * 20))

    def test_prime_length_with_spaces(self):
        """Spaces count towards length: 'a b' has length 3, prime."""
        self.assertTrue(module_0.prime_length("a b"))


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 17:07:33.284052
# Unit test for function prime_length
def test_prime_length():
    # Test with empty string (length 0 -> not prime)
    assert module_0.prime_length("") == False

    # Test with single character (length 1 -> not prime)
    assert module_0.prime_length("a") == False

    # Test with length 2 (prime)
    assert module_0.prime_length("ab") == True

    # Test with length 3 (prime)
    assert module_0.prime_length("abc") == True

    # Test with length 4 (not prime)
    assert module_0.prime_length("abcd") == False

    # Test with length 5 (prime)
    assert module_0.prime_length("abcde") == True

    # Test with length 6 (not prime)
    assert module_0.prime_length("abcdef") == False

    # Test with length 7 (prime)
    assert module_0.prime_length("abcdefg") == True

    # Test with length 9 (not prime, 9 = 3*3)
    assert module_0.prime_length("a" * 9) == False

    # Test with length 11 (prime)
    assert module_0.prime_length("a" * 11) == True

    # Test with length 13 (prime)
    assert module_0.prime_length("hello world!!") == True

    # Test with length 16 (not prime)
    assert module_0.prime_length("a" * 16) == False

    # Test with spaces and special characters (length matters only)
    assert module_0.prime_length("Hello, World!") == True  # length 13

    # Test with whitespace-only string of prime length
    assert module_0.prime_length("     ") == True  # length 5

    print("All tests passed!")


if __name__ == "__main__":
    test_prime_length()

# Generated at 2026-11-02 17:07:40.050021
# Unit test for function prime_length
def test_prime_length():
    # Non-prime lengths
    assert module_0.prime_length("") == False          # length 0
    assert module_0.prime_length("a") == False         # length 1
    assert module_0.prime_length("abab") == False      # length 4
    assert module_0.prime_length("abcdef") == False    # length 6
    assert module_0.prime_length("aaaaaaaa") == False  # length 8
    assert module_0.prime_length("a" * 9) == False     # length 9
    assert module_0.prime_length("a" * 10) == False    # length 10

    # Prime lengths
    assert module_0.prime_length("ab") == True         # length 2
    assert module_0.prime_length("abc") == True        # length 3
    assert module_0.prime_length("abcde") == True      # length 5
    assert module_0.prime_length("abcdefg") == True    # length 7
    assert module_0.prime_length("a" * 11) == True     # length 11
    assert module_0.prime_length("hello world") == True  # length 11
    assert module_0.prime_length("a" * 13) == True     # length 13
    assert module_0.prime_length("a" * 97) == True     # length 97

    print("All tests passed!")


test_prime_length()

# Generated at 2026-11-02 17:07:55.806159
# Unit test for function prime_length
def test_prime_length():
    # Prime lengths
    assert module_0.prime_length("ab") == True        # length 2 (prime)
    assert module_0.prime_length("abc") == True       # length 3 (prime)
    assert module_0.prime_length("Hello") == True     # length 5 (prime)
    assert module_0.prime_length("abcdcba") == True   # length 7 (prime)
    assert module_0.prime_length("kittens") == True   # length 7 (prime)
    assert module_0.prime_length("a" * 11) == True    # length 11 (prime)
    assert module_0.prime_length("a" * 13) == True    # length 13 (prime)

    # Non-prime lengths
    assert module_0.prime_length("") == False         # length 0
    assert module_0.prime_length("a") == False        # length 1
    assert module_0.prime_length("abcd") == False     # length 4
    assert module_0.prime_length("orange") == False   # length 6
    assert module_0.prime_length("a" * 8) == False    # length 8
    assert module_0.prime_length("a" * 9) == False    # length 9 (3*3)
    assert module_0.prime_length("a" * 10) == False   # length 10
    assert module_0.prime_length("a" * 12) == False   # length 12
    assert module_0.prime_length("a" * 15) == False   # length 15