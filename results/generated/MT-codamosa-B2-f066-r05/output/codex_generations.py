

# Generated at 2026-11-03 00:18:54.759153
# Unit test for function digitSum
def test_digitSum():
    assert module_0.digitSum("") == 0
    assert module_0.digitSum("a") == 0
    assert module_0.digitSum("A") == 65
    assert module_0.digitSum("abAB") == 65 + 66
    assert module_0.digitSum("abcCd") == 67
    assert module_0.digitSum("aAaaaXa") == 65 + 88
    assert module_0.digitSum("") == 0
    assert module_0.digitSum("aBCdEf") == 66 + 67 + 70
    assert module_0.digitSum("1234") == 0
    assert module_0.digitSum("Z") == 90
    assert module_0.digitSum("!!@#") == 0
    assert module_0.digitSum("HELLO") == sum(ord(c) for c in "HELLO")
    assert module_0.digitSum("hello") == 0
    assert module_0.digitSum("aBcDeF") == 66 + 68 + 70

# Generated at 2026-11-03 00:20:53.960535
# Unit test for function digitSum
def test_digitSum():
    # Empty string returns 0
    assert module_0.digitSum("") == 0
    # Lowercase characters contribute 0
    assert module_0.digitSum("abcde") == 0
    # Uppercase characters contribute their ASCII values
    assert module_0.digitSum("aAaaaXa") == 153  # ord('A')=65, ord('X')=88
    assert module_0.digitSum("abAB") == 131     # ord('A')=65, ord('B')=66
    assert module_0.digitSum("abcCd") == 67     # ord('C')=67
    assert module_0.digitSum("helloE") == 69    # ord('E')=69
    assert module_0.digitSum("woArBld") == 131  # ord('A')=65, ord('B')=66
    # Non-letter characters contribute 0
    assert module_0.digitSum(" ") == 0
    assert module_0.digitSum("123") == 0
    assert module_0.digitSum("a1b2C3") == 67    # only 'C' counts
    # Mixed content
    assert module_0.digitSum("You aRe a Very Smart Person") == 89 + 82 + 86 + 83 + 80  # Y+R+V+S+P = 400
    assert module_0.digitSum("ZzZz") == 90 + 90  # ord('Z')=90
    print("All tests passed!")

test_digitSum()

# Generated at 2026-11-03 00:22:44.819398
# Unit test for function digitSum
def test_digitSum():import unittest


class TestDigitSum(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(module_0.digitSum(""), 0)

    def test_all_lowercase(self):
        self.assertEqual(module_0.digitSum("abc"), 0)

    def test_all_uppercase(self):
        self.assertEqual(module_0.digitSum("ABC"), 65 + 66 + 67)  # 198

    def test_mixed_case(self):
        self.assertEqual(module_0.digitSum("aBCde"), 66 + 67)  # 133

    def test_single_uppercase(self):
        self.assertEqual(module_0.digitSum("A"), 65)

    def test_single_lowercase(self):
        self.assertEqual(module_0.digitSum("a"), 0)

    def test_mixed_with_digits(self):
        # Digits are not uppercase, so contribute 0
        self.assertEqual(module_0.digitSum("aB1cD2"), ord("B") + ord("D"))  # 66 + 68

    def test_repeated_uppercase(self):
        self.assertEqual(module_0.digitSum("ZZ"), ord("Z") * 2)  # 90 * 2 = 180

    def test_string_with_spaces(self):
        # Space is not uppercase
        self.assertEqual(module_0.digitSum("A B"), ord("A") + ord("B"))  # 65 + 66

    def test_special_characters(self):
        self.assertEqual(module_0.digitSum("!@#"), 0)


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-03 00:24:59.886156
# Unit test for function digitSum
def test_digitSum():
    # Empty string returns 0
    assert module_0.digitSum("") == 0

    # Single uppercase character
    assert module_0.digitSum("A") == 65

    # Single lowercase character contributes 0
    assert module_0.digitSum("a") == 0

    # Mixed case string
    assert module_0.digitSum("abAB") == 131  # 65 + 66

    # All uppercase
    assert module_0.digitSum("ABC") == 198  # 65 + 66 + 67

    # All lowercase
    assert module_0.digitSum("abc") == 0

    # String with digits (digits are not uppercase)
    assert module_0.digitSum("aA1") == 65

    # String with spaces
    assert module_0.digitSum(" A") == 65

    # Known example: "aBcDe" -> B(66) + D(68) = 134
    assert module_0.digitSum("aBcDe") == 134

    # Known example: "You ARE the best" -> Y(89) + A(65) + R(82) + E(69) = 305
    assert module_0.digitSum("You ARE the best") == 305

    # Special characters (not uppercase)
    assert module_0.digitSum("!@#") == 0

    # Unicode uppercase character
    assert module_0.digitSum("É") == 201

    # Longer mixed string
    assert module_0.digitSum("Hello World") == 72 + 87  # H + W = 159