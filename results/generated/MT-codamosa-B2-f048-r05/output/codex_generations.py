

# Generated at 2026-11-02 14:09:03.842899
# Unit test for function is_palindrome
def test_is_palindrome():
    # nonce:1b665144
    # Basic palindromes
    assert module_0.is_palindrome("racecar") == True
    assert module_0.is_palindrome("level") == True
    assert module_0.is_palindrome("madam") == True
    assert module_0.is_palindrome("noon") == True

    # Basic non-palindromes
    assert module_0.is_palindrome("hello") == False
    assert module_0.is_palindrome("world") == False
    assert module_0.is_palindrome("palindrome") == False

    # Edge cases
    assert module_0.is_palindrome("") == True          # empty string is a palindrome
    assert module_0.is_palindrome("a") == True         # single character
    assert module_0.is_palindrome("ab") == False       # two different characters
    assert module_0.is_palindrome("aa") == True        # two same characters
    assert module_0.is_palindrome("abba") == True      # even-length palindrome
    assert module_0.is_palindrome("abca") == False     # even-length non-palindrome

    # Case sensitivity (function is case-sensitive)
    assert module_0.is_palindrome("Racecar") == False
    assert module_0.is_palindrome("Anna") == False

    # Strings with spaces and punctuation (not normalized by function)
    assert module_0.is_palindrome("a b a") == True
    assert module_0.is_palindrome("abc ba") == False
    assert module_0.is_palindrome("ab ba") == True

    # Numeric strings
    assert module_0.is_palindrome("12321") == True
    assert module_0.is_palindrome("12345") == False
    assert module_0.is_palindrome("1001") == True

    print("All tests passed!")


if __name__ == "__main__":
    test_is_palindrome()

# Generated at 2026-11-02 14:10:50.584181
# Unit test for function is_palindrome
def test_is_palindrome():
    # Simple palindromes
    assert module_0.is_palindrome("racecar") == True
    assert module_0.is_palindrome("level") == True
    assert module_0.is_palindrome("madam") == True
    assert module_0.is_palindrome("noon") == True

    # Non-palindromes
    assert module_0.is_palindrome("hello") == False
    assert module_0.is_palindrome("world") == False
    assert module_0.is_palindrome("python") == False

    # Edge cases
    assert module_0.is_palindrome("") == True          # empty string is a palindrome
    assert module_0.is_palindrome("a") == True         # single character
    assert module_0.is_palindrome("ab") == False       # two different characters
    assert module_0.is_palindrome("aa") == True        # two identical characters

    # Case sensitivity (function is case-sensitive)
    assert module_0.is_palindrome("Racecar") == False
    assert module_0.is_palindrome("Madam") == False

    # Even-length palindromes
    assert module_0.is_palindrome("abba") == True
    assert module_0.is_palindrome("abca") == False

    # Strings with spaces/punctuation (no normalization in function)
    assert module_0.is_palindrome("a b a") == True
    assert module_0.is_palindrome("a man a plan") == False

    # Numeric-like strings
    assert module_0.is_palindrome("12321") == True
    assert module_0.is_palindrome("12345") == False

    print("All tests passed!")


# Run the test
if __name__ == "__main__":
    test_is_palindrome()

# Generated at 2026-11-02 14:12:35.631081
# Unit test for function is_palindrome
def test_is_palindrome():
# nonce:6452a9e7
    # Odd-length palindrome
    assert module_0.is_palindrome("racecar") is True
    # Even-length palindrome
    assert module_0.is_palindrome("abba") is True
    # Non-palindrome
    assert module_0.is_palindrome("hello") is False
    # Empty string is a palindrome
    assert module_0.is_palindrome("") is True
    # Single character
    assert module_0.is_palindrome("a") is True
    # Two identical characters
    assert module_0.is_palindrome("aa") is True
    # Two different characters
    assert module_0.is_palindrome("ab") is False
    # Numeric palindrome
    assert module_0.is_palindrome("12321") is True
    # Case-sensitive: 'R' != 'r'
    assert module_0.is_palindrome("Racecar") is False
    # Spaces are not ignored
    assert module_0.is_palindrome("nurses run") is False
    assert module_0.is_palindrome("nursesrun") is True
    # Near-palindrome differing in one position
    assert module_0.is_palindrome("abcdba") is False
    # Symmetric string with mixed characters
    assert module_0.is_palindrome("a.b:a") is True
    # First/last mismatch only
    assert module_0.is_palindrome("abcba" + "x") is False

# Generated at 2026-11-02 14:14:14.838578
# Unit test for function is_palindrome
def test_is_palindrome():
    # Basic palindromes
    assert module_0.is_palindrome("racecar") == True
    assert module_0.is_palindrome("level") == True
    assert module_0.is_palindrome("madam") == True

    # Even-length palindromes
    assert module_0.is_palindrome("abba") == True
    assert module_0.is_palindrome("noon") == True

    # Non-palindromes
    assert module_0.is_palindrome("hello") == False
    assert module_0.is_palindrome("python") == False
    assert module_0.is_palindrome("palindrome") == False

    # Edge cases
    assert module_0.is_palindrome("") == True          # empty string
    assert module_0.is_palindrome("a") == True         # single character
    assert module_0.is_palindrome("ab") == False       # two different characters
    assert module_0.is_palindrome("aa") == True        # two identical characters

    # Case sensitivity (comparison is case-sensitive)
    assert module_0.is_palindrome("Racecar") == False
    assert module_0.is_palindrome("AbBa") == False

    # Strings with spaces
    assert module_0.is_palindrome("a b a") == True
    assert module_0.is_palindrome("ab a") == False

    # Numeric strings
    assert module_0.is_palindrome("12321") == True
    assert module_0.is_palindrome("12345") == False

# Generated at 2026-11-02 14:16:06.312685
# Unit test for function is_palindrome
def test_is_palindrome():
    # Typical palindromes
    assert module_0.is_palindrome("racecar")
    assert module_0.is_palindrome("abba")
    assert module_0.is_palindrome("aba")
    assert module_0.is_palindrome("aa")

    # Typical non-palindromes
    assert not module_0.is_palindrome("hello")
    assert not module_0.is_palindrome("ab")
    assert not module_0.is_palindrome("abca")

    # Edge cases
    assert module_0.is_palindrome("")            # empty string
    assert module_0.is_palindrome("a")           # single character
    assert not module_0.is_palindrome("ab")

    # No normalization: case-sensitive and whitespace-aware
    assert not module_0.is_palindrome("Racecar")  # 'R' != 'r'
    assert not module_0.is_palindrome("ab ba")    # space is compared too

    print("test_is_palindrome passed")