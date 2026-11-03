

# Generated at 2026-11-02 08:48:23.036437
# Unit test for function is_palindrome
def test_is_palindrome():
    # Simple palindromes
    assert module_0.is_palindrome("racecar") is True
    assert module_0.is_palindrome("level") is True
    assert module_0.is_palindrome("noon") is True
    assert module_0.is_palindrome("abba") is True
    assert module_0.is_palindrome("abcba") is True
    assert module_0.is_palindrome("abccba") is True

    # Non-palindromes
    assert module_0.is_palindrome("hello") is False
    assert module_0.is_palindrome("python") is False
    assert module_0.is_palindrome("abca") is False

    # Edge cases
    assert module_0.is_palindrome("") is True        # empty string
    assert module_0.is_palindrome("a") is True       # single character
    assert module_0.is_palindrome("aa") is True      # two identical characters
    assert module_0.is_palindrome("ab") is False     # two different characters

    # Case sensitivity (function is case-sensitive)
    assert module_0.is_palindrome("Racecar") is False
    assert module_0.is_palindrome("Anna") is False

    # Spaces are not normalized
    assert module_0.is_palindrome("race car") is False
    assert module_0.is_palindrome("nurses run") is False
    assert module_0.is_palindrome("a man a plan a canal panama") is False

    # Numeric strings
    assert module_0.is_palindrome("12321") is True
    assert module_0.is_palindrome("12345") is False

    # Special characters
    assert module_0.is_palindrome("!!") is True
    assert module_0.is_palindrome("!a!") is True
    assert module_0.is_palindrome("!@#!@#") is False

    print("All tests passed!")


test_is_palindrome()

# Generated at 2026-11-02 08:48:28.868343
# Unit test for function is_palindrome
def test_is_palindrome():
    # Basic palindromes
    assert module_0.is_palindrome("racecar") == True
    assert module_0.is_palindrome("aba") == True
    assert module_0.is_palindrome("abba") == True
    assert module_0.is_palindrome("madam") == True

    # Edge cases
    assert module_0.is_palindrome("") == True          # empty string
    assert module_0.is_palindrome("a") == True         # single character
    assert module_0.is_palindrome("aa") == True        # two identical chars
    assert module_0.is_palindrome("ab") == False       # two different chars

    # Non-palindromes
    assert module_0.is_palindrome("hello") == False
    assert module_0.is_palindrome("abc") == False
    assert module_0.is_palindrome("abca") == False

    # Case sensitivity (function is case-sensitive)
    assert module_0.is_palindrome("Racecar") == False
    assert module_0.is_palindrome("AbBa") == False

    # Strings with spaces/punctuation (not normalized by function)
    assert module_0.is_palindrome("a b a") == True
    assert module_0.is_palindrome("ab a") == False

    # Even-length palindromes
    assert module_0.is_palindrome("abba") == True
    assert module_0.is_palindrome("noon") == True
    assert module_0.is_palindrome("abcba") == True     # odd-length palindrome

    # Numeric-like strings
    assert module_0.is_palindrome("12321") == True
    assert module_0.is_palindrome("12345") == False

    print("All tests passed!")


test_is_palindrome()

# Generated at 2026-11-02 08:48:52.624039
# Unit test for function is_palindrome
def test_is_palindrome():
    # Empty string is a palindrome
    assert module_0.is_palindrome("") is True

    # Single character is a palindrome
    assert module_0.is_palindrome("a") is True

    # Odd-length palindromes
    assert module_0.is_palindrome("aba") is True
    assert module_0.is_palindrome("racecar") is True
    assert module_0.is_palindrome("madam") is True

    # Even-length palindromes
    assert module_0.is_palindrome("abba") is True
    assert module_0.is_palindrome("noon") is True
    assert module_0.is_palindrome("abccba") is True

    # Non-palindromes
    assert module_0.is_palindrome("ab") is False
    assert module_0.is_palindrome("hello") is False
    assert module_0.is_palindrome("race a car") is False

    # Case sensitivity: comparison is case-sensitive
    assert module_0.is_palindrome("Racecar") is False
    assert module_0.is_palindrome("AbBa") is False

    # Spaces and punctuation are not ignored
    assert module_0.is_palindrome("a man a plan a canal panama") is False
    assert module_0.is_palindrome("amanaplanacanalpanama") is True

    # Repeated characters
    assert module_0.is_palindrome("aaaa") is True
    assert module_0.is_palindrome("aaab") is False

    # Numbers and symbols as characters
    assert module_0.is_palindrome("12321") is True
    assert module_0.is_palindrome("12345") is False
    assert module_0.is_palindrome("!!@@!!") is True

    # First/last character mismatch detected early
    assert module_0.is_palindrome("x...a") is False

    print("All tests passed!")


test_is_palindrome()

# Generated at 2026-11-02 08:49:02.490673
# Unit test for function is_palindrome
def test_is_palindrome():
    # Basic palindromes
    assert module_0.is_palindrome("") is True          # empty string
    assert module_0.is_palindrome("a") is True         # single character
    assert module_0.is_palindrome("aa") is True        # even-length palindrome
    assert module_0.is_palindrome("aba") is True       # odd-length palindrome
    assert module_0.is_palindrome("racecar") is True
    assert module_0.is_palindrome("abba") is True
    assert module_0.is_palindrome("noon") is True

    # Non-palindromes
    assert module_0.is_palindrome("ab") is False
    assert module_0.is_palindrome("abc") is False
    assert module_0.is_palindrome("abca") is False
    assert module_0.is_palindrome("hello") is False
    assert module_0.is_palindrome("race a car") is False

    # Case sensitivity: function is case-sensitive
    assert module_0.is_palindrome("Aba") is False
    assert module_0.is_palindrome("Abba") is False

    # Strings with spaces/punctuation (character-level check only)
    assert module_0.is_palindrome("a a") is True
    assert module_0.is_palindrome("!!") is True
    assert module_0.is_palindrome("a!a") is True
    assert module_0.is_palindrome("ab!") is False

    # Numeric strings
    assert module_0.is_palindrome("12321") is True
    assert module_0.is_palindrome("1231") is False

    # Unicode characters
    assert module_0.is_palindrome("абба") is True
    assert module_0.is_palindrome("абв") is False

# Generated at 2026-11-02 08:49:31.429981
# Unit test for function is_palindrome
def test_is_palindrome():
    # Basic palindromes
    assert module_0.is_palindrome("racecar") == True
    assert module_0.is_palindrome("madam") == True
    assert module_0.is_palindrome("aba") == True
    assert module_0.is_palindrome("abba") == True

    # Non-palindromes
    assert module_0.is_palindrome("hello") == False
    assert module_0.is_palindrome("world") == False
    assert module_0.is_palindrome("ab") == False

    # Edge cases
    assert module_0.is_palindrome("") == True          # empty string
    assert module_0.is_palindrome("a") == True         # single character
    assert module_0.is_palindrome("aa") == True        # two identical characters

    # Case sensitivity (function is case-sensitive)
    assert module_0.is_palindrome("Racecar") == False
    assert module_0.is_palindrome("Madam") == False

    # Strings containing spaces
    assert module_0.is_palindrome("a b a") == True
    assert module_0.is_palindrome("ab a") == False

    # Numeric strings
    assert module_0.is_palindrome("12321") == True
    assert module_0.is_palindrome("12345") == False

    # Longer palindromes
    assert module_0.is_palindrome("amanaplanacanalpanama") == True
    assert module_0.is_palindrome("wasitacaroracatisaw") == True