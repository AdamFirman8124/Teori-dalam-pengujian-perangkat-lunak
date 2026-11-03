

# Generated at 2026-11-02 22:16:53.163944
# Unit test for function is_palindrome
def test_is_palindrome():
    # Edge cases: empty and single-character strings
    assert module_0.is_palindrome("") == True
    assert module_0.is_palindrome("a") == True

    # Simple palindromes (even and odd length)
    assert module_0.is_palindrome("aa") == True
    assert module_0.is_palindrome("aba") == True
    assert module_0.is_palindrome("abba") == True
    assert module_0.is_palindrome("racecar") == True
    assert module_0.is_palindrome("madamimadam") == True

    # Non-palindromes
    assert module_0.is_palindrome("ab") == False
    assert module_0.is_palindrome("abc") == False
    assert module_0.is_palindrome("abca") == False
    assert module_0.is_palindrome("hello") == False

    # Case sensitivity: the function does not normalize case
    assert module_0.is_palindrome("Aba") == False
    assert module_0.is_palindrome("AbBa") == False
    assert module_0.is_palindrome("ABBA") == True  # same case on both ends

    # Spaces and punctuation are not filtered out
    assert module_0.is_palindrome("nurses run") == False
    assert module_0.is_palindrome("nursesrun") == True
    assert module_0.is_palindrome("A man, a plan, a canal: Panama") == False
    assert module_0.is_palindrome("amanaplanacanalpanama") == True

    # Numeric strings
    assert module_0.is_palindrome("12321") == True
    assert module_0.is_palindrome("1231") == False

# Generated at 2026-11-02 22:18:50.207055
# Unit test for function is_palindrome
def test_is_palindrome():
    # Empty string is a palindrome
    assert module_0.is_palindrome("") == True

    # Single character is a palindrome
    assert module_0.is_palindrome("a") == True

    # Odd-length palindromes
    assert module_0.is_palindrome("aba") == True
    assert module_0.is_palindrome("racecar") == True
    assert module_0.is_palindrome("level") == True

    # Even-length palindromes
    assert module_0.is_palindrome("abba") == True
    assert module_0.is_palindrome("noon") == True

    # Non-palindromes
    assert module_0.is_palindrome("abc") == False
    assert module_0.is_palindrome("hello") == False
    assert module_0.is_palindrome("abca") == False

    # Case-sensitive check
    assert module_0.is_palindrome("Aa") == False
    assert module_0.is_palindrome("AbBa") == False

    # Strings with spaces (spaces are treated as characters)
    assert module_0.is_palindrome("a b a") == False
    assert module_0.is_palindrome("aba") == True

# Generated at 2026-11-02 22:20:16.125247
# Unit test for function is_palindrome
def test_is_palindrome():
    # Simple palindromes
    assert module_0.is_palindrome("racecar") == True
    assert module_0.is_palindrome("level") == True
    assert module_0.is_palindrome("noon") == True
    assert module_0.is_palindrome("madam") == True

    # Non-palindromes
    assert module_0.is_palindrome("hello") == False
    assert module_0.is_palindrome("world") == False
    assert module_0.is_palindrome("python") == False

    # Edge cases
    assert module_0.is_palindrome("") == True          # empty string
    assert module_0.is_palindrome("a") == True         # single character
    assert module_0.is_palindrome("ab") == False       # two different chars
    assert module_0.is_palindrome("aa") == True        # two same chars

    # Odd-length palindrome
    assert module_0.is_palindrome("abcba") == True
    assert module_0.is_palindrome("abcda") == False

    # Even-length palindrome
    assert module_0.is_palindrome("abba") == True
    assert module_0.is_palindrome("abca") == False

    # Case sensitivity (function is case-sensitive)
    assert module_0.is_palindrome("Racecar") == False
    assert module_0.is_palindrome("RaceCar") == False

    # Strings with spaces (not stripped by function)
    assert module_0.is_palindrome("a b a") == True
    assert module_0.is_palindrome("a  b a") == False

    # Numeric strings
    assert module_0.is_palindrome("12321") == True
    assert module_0.is_palindrome("12345") == False

    # Special characters
    assert module_0.is_palindrome("!@#@!") == True
    assert module_0.is_palindrome("!@#") == False

    # Longer palindromes
    assert module_0.is_palindrome("amanaplanacanalpanama") == True
    assert module_0.is_palindrome("wasitacaroracatisaw") == True

    print("All tests passed!")


# Run tests
if __name__ == "__main__":
    test_is_palindrome()

# Generated at 2026-11-02 22:21:49.487138
# Unit test for function is_palindrome
def test_is_palindrome():
# nonce:a1e5b436
    # Empty string is a palindrome
    assert module_0.is_palindrome("") is True

    # Single character is a palindrome
    assert module_0.is_palindrome("a") is True

    # Odd-length palindrome
    assert module_0.is_palindrome("aba") is True
    assert module_0.is_palindrome("racecar") is True
    assert module_0.is_palindrome("madam") is True

    # Even-length palindrome
    assert module_0.is_palindrome("abba") is True
    assert module_0.is_palindrome("noon") is True

    # Non-palindromes
    assert module_0.is_palindrome("ab") is False
    assert module_0.is_palindrome("abc") is False
    assert module_0.is_palindrome("hello") is False

    # Case sensitivity: comparison is case-sensitive
    assert module_0.is_palindrome("Abba") is False
    assert module_0.is_palindrome("AbBa") is False

    # Strings with spaces are compared literally
    assert module_0.is_palindrome("a b a") is True
    assert module_0.is_palindrome("a ba") is False

    # Numbers-as-strings
    assert module_0.is_palindrome("12321") is True
    assert module_0.is_palindrome("12345") is False

    # Long palindrome
    assert module_0.is_palindrome("amanaplanacanalpanama") is True

    print("All tests passed!")


if __name__ == "__main__":
    test_is_palindrome()

# Generated at 2026-11-02 22:22:43.067891
# Unit test for function is_palindrome
def test_is_palindrome():
    # Basic palindromes
    assert module_0.is_palindrome("racecar") is True
    assert module_0.is_palindrome("level") is True
    assert module_0.is_palindrome("madam") is True

    # Even-length palindromes
    assert module_0.is_palindrome("abba") is True
    assert module_0.is_palindrome("noon") is True

    # Non-palindromes
    assert module_0.is_palindrome("hello") is False
    assert module_0.is_palindrome("world") is False
    assert module_0.is_palindrome("ab") is False

    # Edge cases
    assert module_0.is_palindrome("") is True          # empty string
    assert module_0.is_palindrome("a") is True         # single character
    assert module_0.is_palindrome("aa") is True        # two identical chars
    assert module_0.is_palindrome("ab") is False       # two different chars

    # Case sensitivity (function is case-sensitive)
    assert module_0.is_palindrome("Racecar") is False

    # Strings with spaces/punctuation (not ignored)
    assert module_0.is_palindrome("a man a plan a canal panama") is False
    assert module_0.is_palindrome("amanaplanacanalpanama") is True

    # Numeric-like strings
    assert module_0.is_palindrome("12321") is True
    assert module_0.is_palindrome("12345") is False

    print("All tests passed!")


test_is_palindrome()