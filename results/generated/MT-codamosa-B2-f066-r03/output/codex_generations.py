

# Generated at 2026-11-02 09:57:33.165110
# Unit test for function digitSum
def test_digitSum():
    assert module_0.digitSum("") == 0
    assert module_0.digitSum("abAB") == 131
    assert module_0.digitSum("abcCd") == 67
    assert module_0.digitSum("helloE") == 69
    assert module_0.digitSum("woArBld") == 131
    assert module_0.digitSum("aAaaaXa") == 153
    assert module_0.digitSum("123!@#") == 0
    assert module_0.digitSum("A") == 65

# Generated at 2026-11-02 09:58:19.935632
# Unit test for function digitSum
def test_digitSum():
    assert module_0.digitSum("") == 0
    assert module_0.digitSum("abAB") == 131
    assert module_0.digitSum("abcCd") == 67
    assert module_0.digitSum("helloE") == 69
    assert module_0.digitSum("woArBld") == 131
    assert module_0.digitSum("aAaaaXa") == 153
    assert module_0.digitSum("abc") == 0
    assert module_0.digitSum("ABC") == 198
    assert module_0.digitSum("aBCdEf") == 202
    assert module_0.digitSum("1234!") == 0
    assert module_0.digitSum("Z") == 90
    assert module_0.digitSum("z") == 0
    print("All test cases passed!")

# Generated at 2026-11-02 09:59:30.078643
# Unit test for function digitSum
def test_digitSum():
    # Empty string returns 0
    assert module_0.digitSum("") == 0
    # String with no uppercase letters returns 0
    assert module_0.digitSum("abc") == 0
    assert module_0.digitSum("hello world") == 0
    # String with only uppercase letters
    assert module_0.digitSum("ABC") == ord('A') + ord('B') + ord('C')  # 65 + 66 + 67 = 198
    assert module_0.digitSum("HELLO") == ord('H') + ord('E') + ord('L') + ord('L') + ord('O')  # 372
    # Mixed case: only uppercase letters contribute
    assert module_0.digitSum("abAB") == ord('A') + ord('B')  # 131
    assert module_0.digitSum("abcCd") == ord('C')  # 67
    assert module_0.digitSum("aAaaaXa") == ord('A') + ord('X')  # 65 + 88 = 153
    # Uppercase with digits/symbols (digits are not uppercase)
    assert module_0.digitSum("A1!") == ord('A')  # 65
    # Single uppercase character
    assert module_0.digitSum("Z") == ord('Z')  # 90
    print("All tests passed!")

test_digitSum()

# Generated at 2026-11-02 10:00:30.089519
# Unit test for function digitSum
def test_digitSum():
    # Empty string returns 0
    assert module_0.digitSum("") == 0
    # All lowercase characters contribute 0
    assert module_0.digitSum("abcde") == 0
    # Only uppercase characters are summed
    assert module_0.digitSum("aBCde") == ord('B') + ord('C')  # 133
    assert module_0.digitSum("aBCdEf") == ord('B') + ord('C') + ord('F')  # 203
    # Single uppercase character
    assert module_0.digitSum("E") == 69
    # All uppercase characters
    assert module_0.digitSum("AB") == ord('A') + ord('B')  # 131
    assert module_0.digitSum("ABC") == ord('A') + ord('B') + ord('C')  # 198
    # Mixed case with digits and symbols (non-letters contribute 0)
    assert module_0.digitSum("aB1cD!") == ord('B') + ord('D')
    # String with spaces
    assert module_0.digitSum("a B c") == ord('B')
    # Repeated uppercase characters
    assert module_0.digitSum("AaAa") == ord('A') + ord('A')  # 130

# Generated at 2026-11-02 10:01:43.181291
# Unit test for function digitSum
def test_digitSum():
    # Empty string
    assert module_0.digitSum("") == 0
    # Single uppercase letter
    assert module_0.digitSum("A") == 65
    # Single lowercase letter
    assert module_0.digitSum("a") == 0
    # All uppercase letters
    assert module_0.digitSum("AB") == 131  # 65 + 66
    # All lowercase letters
    assert module_0.digitSum("abc") == 0
    # Mixed case letters
    assert module_0.digitSum("aBC") == 133  # 66 + 67
    # Uppercase and lowercase combined
    assert module_0.digitSum("Hello World") == 159  # H(72) + W(87)
    # Digits are not uppercase
    assert module_0.digitSum("1aA2") == 65
    # String with spaces and punctuation
    assert module_0.digitSum("a b!C") == 67  # C(67)
    # Long mixed string
    assert module_0.digitSum("You aRe thE Best") == 323  # Y(89) R(82) E(69) B(66) = 306... verify below


# Corrected check for the long string case
def test_digitSum_long_string():
    expected = ord('Y') + ord('R') + ord('E') + ord('B')
    assert module_0.digitSum("You aRe thE Best") == expected


class TestDigitSum(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(module_0.digitSum(""), 0)

    def test_single_upper(self):
        self.assertEqual(module_0.digitSum("A"), 65)

    def test_single_lower(self):
        self.assertEqual(module_0.digitSum("a"), 0)

    def test_all_upper(self):
        self.assertEqual(module_0.digitSum("AB"), 131)

    def test_all_lower(self):
        self.assertEqual(module_0.digitSum("abc"), 0)

    def test_mixed(self):
        self.assertEqual(module_0.digitSum("aBC"), 133)

    def test_sentence(self):
        self.assertEqual(module_0.digitSum("Hello World"), 159)

    def test_digits_ignored(self):
        self.assertEqual(module_0.digitSum("1aA2"), 65)


if __name__ == "__main__":
    test_digitSum()
    test_digitSum_long_string()
    unittest.main()