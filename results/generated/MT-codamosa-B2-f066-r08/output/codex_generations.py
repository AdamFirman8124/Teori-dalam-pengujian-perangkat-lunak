

# Generated at 2026-11-02 10:29:18.572661
# Unit test for function digitSum
def test_digitSum():import unittest

class TestDigitSum(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(module_0.digitSum(""), 0)

    def test_all_lowercase(self):
        self.assertEqual(module_0.digitSum("abcde"), 0)

    def test_mixed_case(self):
        self.assertEqual(module_0.digitSum("aBCde"), 133)  # ord('B') + ord('C') = 66 + 67

    def test_uppercase_only(self):
        self.assertEqual(module_0.digitSum("ABC"), 198)  # 65 + 66 + 67

    def test_single_uppercase(self):
        self.assertEqual(module_0.digitSum("aA"), 65)

    def test_single_lowercase(self):
        self.assertEqual(module_0.digitSum("a"), 0)

    def test_string_with_digits(self):
        self.assertEqual(module_0.digitSum("4A"), 65)  # digits are not uppercase

    def test_string_with_spaces(self):
        self.assertEqual(module_0.digitSum("A B"), 65)  # space is not uppercase

    def test_long_mixed_string(self):
        self.assertEqual(module_0.digitSum("Hello World"), 0)  # no uppercase-only sum (H=72? no, H is uppercase)
        # Correction: 'H' and 'W' are uppercase
        self.assertEqual(module_0.digitSum("Hello World"), 72 + 87)  # 159

if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 10:30:29.588040
# Unit test for function digitSum
def test_digitSum():
    # Empty string returns 0
    assert module_0.digitSum("") == 0
    
    # Single uppercase character
    assert module_0.digitSum("A") == 65
    
    # Single lowercase character contributes 0
    assert module_0.digitSum("a") == 0
    
    # All uppercase characters
    assert module_0.digitSum("ABC") == 65 + 66 + 67  # 198
    
    # All lowercase characters
    assert module_0.digitSum("abc") == 0
    
    # Mixed case: only uppercase counted
    assert module_0.digitSum("aBcD") == 66 + 68  # 134
    
    # Example from spec
    assert module_0.digitSum("aA") == 65
    assert module_0.digitSum("Hello") == 72
    
    # Digits and special chars are not uppercase, contribute 0
    assert module_0.digitSum("123!@#") == 0
    
    # Mixed with digits and uppercase
    assert module_0.digitSum("1A2B") == 65 + 66  # 131
    
    # Whitespace is not uppercase
    assert module_0.digitSum(" A ") == 65
    
    # Long string with repeated chars
    assert module_0.digitSum("ZZZ") == 90 * 3  # 270
    
    # Uppercase letters at various positions
    assert module_0.digitSum("aBcDeF") == 66 + 68 + 70  # 204
    
    print("All test_digitSum tests passed!")

# Generated at 2026-11-02 10:31:31.846313
# Unit test for function digitSum
def test_digitSum():
    # Empty string returns 0
    assert module_0.digitSum("") == 0
    # Single uppercase character
    assert module_0.digitSum("A") == 65
    # All uppercase characters
    assert module_0.digitSum("ABC") == ord('A') + ord('B') + ord('C')  # 65 + 66 + 67 = 198
    # All lowercase characters contribute 0
    assert module_0.digitSum("abc") == 0
    # Mixed case: only uppercase counted
    assert module_0.digitSum("aBcD") == ord('B') + ord('D')  # 66 + 68 = 134
    # Digits and special characters contribute 0
    assert module_0.digitSum("123!@#") == 0
    # Mixed with digits, specials, and uppercase
    assert module_0.digitSum("aA1!") == 65
    # String with only whitespace contributes 0
    assert module_0.digitSum("   ") == 0
    # Longer mixed string
    assert module_0.digitSum("Hello World") == ord('H') + ord('W')  # 72 + 87 = 159
    # Uppercase letters repeated
    assert module_0.digitSum("ZZ") == 2 * ord('Z')  # 2 * 90 = 180
    print("All test_digitSum tests passed!")

test_digitSum()

# Generated at 2026-11-02 10:32:42.612746
# Unit test for function digitSum
def test_digitSum():
    # Test empty string
    assert module_0.digitSum("") == 0

    # Test string with only uppercase letters
    assert module_0.digitSum("aBCde") == ord('B') + ord('C')

    # Test string with all uppercase letters
    assert module_0.digitSum("ABC") == ord('A') + ord('B') + ord('C')

    # Test string with all lowercase letters
    assert module_0.digitSum("abc") == 0

    # Test string with digits and symbols (non-alpha chars are not upper)
    assert module_0.digitSum("a1b2C3") == ord('C')

    # Test single uppercase character
    assert module_0.digitSum("A") == 65

    # Test single lowercase character
    assert module_0.digitSum("a") == 0

    # Test string with spaces
    assert module_0.digitSum("Hello World") == ord('H') + ord('W')

    # Test string with mixed case
    assert module_0.digitSum("aAa") == ord('A')

    # Test string with punctuation
    assert module_0.digitSum("!@# $%^") == 0

    # Test long string
    assert module_0.digitSum("aBcDeFgHiJ") == ord('B') + ord('D') + ord('F') + ord('H') + ord('J')

    print("All tests passed!")


test_digitSum()

# Generated at 2026-11-02 10:33:49.158189
# Unit test for function digitSum
def test_digitSum():
    # Empty string returns 0
    assert module_0.digitSum("") == 0

    # Single uppercase character
    assert module_0.digitSum("A") == 65

    # All uppercase characters
    assert module_0.digitSum("abcde") == 0
    assert module_0.digitSum("ABCDE") == 65 + 66 + 67 + 68 + 69

    # Lowercase only contributes nothing
    assert module_0.digitSum("aBcD") == 66 + 68

    # Mixed case with digits and spaces (non-letters contribute 0)
    assert module_0.digitSum("Hello World") == ord('H') + ord('W')

    # String with numbers and punctuation
    assert module_0.digitSum("123!@#") == 0

    # Uppercase with special characters
    assert module_0.digitSum("aA1!Z") == ord('A') + ord('Z')

    # Repeated uppercase characters
    assert module_0.digitSum("ZZZ") == 3 * ord('Z')

    print("All tests passed!")