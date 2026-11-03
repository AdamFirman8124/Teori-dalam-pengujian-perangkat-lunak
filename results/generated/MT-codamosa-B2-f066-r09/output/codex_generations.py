

# Generated at 2026-11-02 17:41:46.029758
# Unit test for function digitSum
def test_digitSum():
    assert module_0.digitSum("") == 0
    assert module_0.digitSum("abAB") == 131
    assert module_0.digitSum("abcCd") == 67
    assert module_0.digitSum("ignore") == 0
    assert module_0.digitSum("aA") == 65
    assert module_0.digitSum("Z") == 90
    assert module_0.digitSum("1234") == 0
    assert module_0.digitSum("HelloWorld") == 338

# Generated at 2026-11-02 17:44:02.829309
# Unit test for function digitSum
def test_digitSum():
    # Empty string returns 0
    assert module_0.digitSum("") == 0

    # All uppercase letters
    assert module_0.digitSum("A") == 65
    assert module_0.digitSum("ABC") == ord('A') + ord('B') + ord('C')  # 65 + 66 + 67 = 198
    assert module_0.digitSum("Z") == 90

    # All lowercase letters contribute 0
    assert module_0.digitSum("abc") == 0
    assert module_0.digitSum("z") == 0

    # Mixed case
    assert module_0.digitSum("aA") == 65
    assert module_0.digitSum("Ab") == 65
    assert module_0.digitSum("Hello World") == ord('H') + ord('W')  # 72 + 87 = 159

    # Digits and special characters are not uppercase, contribute 0
    assert module_0.digitSum("123!@#") == 0
    assert module_0.digitSum("a1B2") == ord('B')  # 66

    # Whitespace is not uppercase
    assert module_0.digitSum(" A ") == 65

    # Unicode uppercase characters
    assert module_0.digitSum("É") == ord('É')

    # Long mixed string
    assert module_0.digitSum("The Quick Brown Fox") == (
        ord('T') + ord('Q') + ord('B') + ord('F')
    )  # 84 + 81 + 66 + 70 = 301

    print("All tests passed!")

# Generated at 2026-11-02 17:46:31.880615
# Unit test for function digitSum
def test_digitSum():
    # Empty string returns 0
    assert module_0.digitSum("") == 0
    # Only uppercase chars contribute their ord values
    assert module_0.digitSum("abAB") == 131   # A(65) + B(66)
    assert module_0.digitSum("abcCd") == 67   # C(67)
    assert module_0.digitSum("helloE") == 69  # E(69)
    assert module_0.digitSum("woArBjt") == 131  # A(65) + B(66)
    assert module_0.digitSum("aAaaaXa") == 153  # A(65) + X(88)
    assert module_0.digitSum(" You are verySmart!") == 172  # Y(89) + S(83)
    # String with no uppercase characters
    assert module_0.digitSum("aaaa") == 0
    assert module_0.digitSum("12345!@#") == 0
    # All uppercase
    assert module_0.digitSum("ABC") == 198  # 65 + 66 + 67
    assert module_0.digitSum("ZZZ") == 270  # 90 * 3

# Generated at 2026-11-02 17:48:22.563112
# Unit test for function digitSum
def test_digitSum():
    # Empty string returns 0
    assert module_0.digitSum("") == 0

    # All uppercase letters
    assert module_0.digitSum("ABC") == 65 + 66 + 67  # 198

    # Mixed case: only uppercase contribute
    assert module_0.digitSum("abAB") == ord('A') + ord('B')  # 131
    assert module_0.digitSum("abcCd") == ord('C')  # 67
    assert module_0.digitSum("aAaaaXa") == ord('A') + ord('X')  # 153
    assert module_0.digitSum("aBCde") == ord('B') + ord('C')  # 133

    # All lowercase returns 0
    assert module_0.digitSum("abcdef") == 0

    # Single uppercase character
    assert module_0.digitSum("Z") == ord('Z')  # 90

    # Non-letter characters (not uppercase) contribute 0
    assert module_0.digitSum(" ") == 0
    assert module_0.digitSum("123") == 0
    assert module_0.digitSum("!@#") == 0

    # Mixed letters, digits, and symbols
    assert module_0.digitSum("a1B!cD") == ord('B') + ord('D')  # 134

    # String with only one uppercase among many chars
    assert module_0.digitSum("hello World") == ord('W')  # 87

    print("All test_digitSum tests passed!")


if __name__ == "__main__":
    test_digitSum()

# Generated at 2026-11-02 17:50:04.648565
# Unit test for function digitSum
def test_digitSum():
    # Empty string returns 0
    assert module_0.digitSum("") == 0
    # All lowercase letters contribute 0
    assert module_0.digitSum("abc") == 0
    # All uppercase letters contribute their ord values
    assert module_0.digitSum("ABC") == ord('A') + ord('B') + ord('C')  # 65 + 66 + 67 = 198
    # Mixed case: only uppercase counted
    assert module_0.digitSum("aBcD") == ord('B') + ord('D')  # 66 + 68 = 134
    # Single uppercase character
    assert module_0.digitSum("A") == 65
    # Single lowercase character
    assert module_0.digitSum("a") == 0
    # String with digits and symbols (not uppercase, contribute 0)
    assert module_0.digitSum("a1!A") == 65
    # Repeated uppercase characters
    assert module_0.digitSum("AA") == 130
    # Long mixed string
    assert module_0.digitSum("Hello World") == ord('H') + ord('W')  # 72 + 87 = 159
    print("All tests passed!")