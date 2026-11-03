

# Generated at 2026-11-03 03:06:33.985216
# Unit test for function digitSum
def test_digitSum():
    assert module_0.digitSum("") == 0
    assert module_0.digitSum("abAB") == 131
    assert module_0.digitSum("abcCd") == 67
    assert module_0.digitSum("helloE") == 69
    assert module_0.digitSum("woArBld") == 131
    assert module_0.digitSum("aAaaaXa") == 153
    assert module_0.digitSum("a b C d") == 67
    assert module_0.digitSum("ZZZZZ") == sum(ord(c) for c in "ZZZZZ")
    assert module_0.digitSum("1234") == 0
    assert module_0.digitSum("aBcD") == ord('B') + ord('D')
    print("All tests passed!")

# Generated at 2026-11-03 03:08:47.004470
# Unit test for function digitSum
def test_digitSum():
    # Test empty string
    assert module_0.digitSum("") == 0

    # Test string with all lowercase characters
    assert module_0.digitSum("abcde") == 0

    # Test string with all uppercase characters
    assert module_0.digitSum("ABCDE") == ord('A') + ord('B') + ord('C') + ord('D') + ord('E')

    # Test mixed case string
    assert module_0.digitSum("aBCde") == ord('B') + ord('C')
    assert module_0.digitSum("abAB") == ord('A') + ord('B')
    assert module_0.digitSum("abcE") == ord('E')

    # Test string with digits and special characters (non-letters count as 0)
    assert module_0.digitSum("aB1c!") == ord('B')

    # Test single uppercase character
    assert module_0.digitSum("Z") == ord('Z')

    # Test single lowercase character
    assert module_0.digitSum("z") == 0

    # Test string with spaces (space is not uppercase, so counts as 0)
    assert module_0.digitSum("A B") == ord('A') + ord('B')

    print("All tests passed!")

test_digitSum()

# Generated at 2026-11-03 03:10:55.305873
# Unit test for function digitSum
def test_digitSum():
    # Empty string returns 0
    assert module_0.digitSum("") == 0
    # Lowercase only contributes 0
    assert module_0.digitSum("abc") == 0
    assert module_0.digitSum("a") == 0
    # Uppercase letters contribute their ord values
    assert module_0.digitSum("A") == 65
    assert module_0.digitSum("abAB") == 131  # 65 + 66
    assert module_0.digitSum("abcCd") == 67  # only 'C'
    assert module_0.digitSum("helloE") == 69  # only 'E'
    assert module_0.digitSum("woArBld") == 131  # 65 + 66
    assert module_0.digitSum("aAaaaXa") == 153  # 65 + 88
    # Mixed with digits and symbols (non-upper contribute 0)
    assert module_0.digitSum("123") == 0
    assert module_0.digitSum("!@#") == 0
    assert module_0.digitSum("A1!") == 65
    assert module_0.digitSum("Hello World") == 159  # 72 + 87
    # All uppercase
    assert module_0.digitSum("ABC") == 198  # 65 + 66 + 67
    print("All tests passed!")

test_digitSum()

# Generated at 2026-11-03 03:12:52.805986
# Unit test for function digitSum
def test_digitSum():
    # Empty string returns 0
    assert module_0.digitSum("") == 0
    # No uppercase characters
    assert module_0.digitSum("abc") == 0
    assert module_0.digitSum("hello") == 0
    assert module_0.digitSum("123") == 0
    assert module_0.digitSum("!@# ") == 0
    # Single uppercase characters
    assert module_0.digitSum("A") == 65
    assert module_0.digitSum("Z") == 90
    # Mixed case strings
    assert module_0.digitSum("abAB") == 131      # 65 + 66
    assert module_0.digitSum("abcCd") == 67      # ord('C') = 67
    assert module_0.digitSum("helloE") == 69     # ord('E') = 69
    assert module_0.digitSum("woArBld") == 131   # 65 + 66
    assert module_0.digitSum("aAaaaXa") == 153   # 65 + 88
    assert module_0.digitSum("aBcDeF") == 204    # 66 + 68 + 70
    # All uppercase
    assert module_0.digitSum("ABC") == 198       # 65 + 66 + 67
    assert module_0.digitSum("XYZ") == 267       # 88 + 89 + 90
    # Uppercase mixed with digits and special chars
    assert module_0.digitSum("A1B2") == 131      # 65 + 66
    assert module_0.digitSum(" a A ") == 65      # only 'A' counts
    print("All tests passed!")

test_digitSum()

# Generated at 2026-11-03 03:13:29.765702
# Unit test for function digitSum
def test_digitSum():
    # Empty string returns 0
    assert module_0.digitSum("") == 0
    # No uppercase characters
    assert module_0.digitSum("abc") == 0
    assert module_0.digitSum("a1b2c3") == 0
    # Single uppercase character
    assert module_0.digitSum("A") == 65
    assert module_0.digitSum("Z") == 90
    # Mixed case string
    assert module_0.digitSum("abAB") == ord('A') + ord('B')  # 65 + 66 = 131
    assert module_0.digitSum("abcCd") == ord('C')  # 67
    assert module_0.digitSum("aAaaaXa") == ord('A') + ord('X')  # 65 + 88 = 153
    # All uppercase
    assert module_0.digitSum("HELLO") == ord('H') + ord('E') + ord('L') + ord('L') + ord('O')
    # Lowercase and digits contribute nothing
    assert module_0.digitSum("123abc") == 0
    # String with spaces and punctuation (not uppercase)
    assert module_0.digitSum("a B!") == ord('B')  # 66
    print("All tests passed!")

test_digitSum()