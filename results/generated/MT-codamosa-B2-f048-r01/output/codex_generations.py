

# Generated at 2026-11-02 12:25:02.751719
# Unit test for function is_palindrome
def test_is_palindrome():
    # Single character strings are palindromes
    assert module_0.is_palindrome("a") == True
    assert module_0.is_palindrome("z") == True

    # Empty string is a palindrome
    assert module_0.is_palindrome("") == True

    # Even-length palindromes
    assert module_0.is_palindrome("abba") == True
    assert module_0.is_palindrome("noon") == True
    assert module_0.is_palindrome("123321") == True

    # Odd-length palindromes
    assert module_0.is_palindrome("aba") == True
    assert module_0.is_palindrome("racecar") == True
    assert module_0.is_palindrome("level") == True

    # Non-palindromes
    assert module_0.is_palindrome("ab") == False
    assert module_0.is_palindrome("abc") == False
    assert module_0.is_palindrome("hello") == False
    assert module_0.is_palindrome("palindrome") == False

    # Case sensitivity: function is case-sensitive
    assert module_0.is_palindrome("Abba") == False
    assert module_0.is_palindrome("Aba") == False

    # Strings with spaces (no special handling)
    assert module_0.is_palindrome("a b a") == True
    assert module_0.is_palindrome("a  ba") == False

    # Longer palindromes
    assert module_0.is_palindrome("amanaplanacanalpanama") == False  # spaces/case not ignored
    assert module_0.is_palindrome("amanaplanacanalpanama"[::]) == True  # same string reversed check
    assert module_0.is_palindrome("abccba") == True
    assert module_0.is_palindrome("abcba") == True

    # Mixed alphanumeric
    assert module_0.is_palindrome("1a1") == True
    assert module_0.is_palindrome("1a2") == False

    print("All tests passed!")


test_is_palindrome()

# Generated at 2026-11-02 12:26:35.217689
# Unit test for function is_palindrome
def test_is_palindrome():
    # Basic palindromes
    assert module_0.is_palindrome("racecar") == True
    assert module_0.is_palindrome("level") == True
    assert module_0.is_palindrome("noon") == True

    # Non-palindromes
    assert module_0.is_palindrome("hello") == False
    assert module_0.is_palindrome("world") == False

    # Edge cases
    assert module_0.is_palindrome("") == True          # empty string is a palindrome
    assert module_0.is_palindrome("a") == True         # single character
    assert module_0.is_palindrome("aa") == True        # two identical characters
    assert module_0.is_palindrome("ab") == False       # two different characters

    # Case sensitivity (function is case-sensitive)
    assert module_0.is_palindrome("Racecar") == False
    assert module_0.is_palindrome("Abba") == False

    # Numeric strings
    assert module_0.is_palindrome("12321") == True
    assert module_0.is_palindrome("12345") == False

    # Strings with spaces (strict comparison, spaces count)
    assert module_0.is_palindrome("nurses run") == False
    assert module_0.is_palindrome("a b a") == True

    print("All tests passed!")


test_is_palindrome()

# Generated at 2026-11-02 12:27:36.604461
# Unit test for function is_palindrome
def test_is_palindrome():
    # Odd-length palindromes
    assert module_0.is_palindrome("racecar") is True
    assert module_0.is_palindrome("level") is True
    assert module_0.is_palindrome("madam") is True
    assert module_0.is_palindrome("radar") is True

    # Even-length palindromes
    assert module_0.is_palindrome("abba") is True
    assert module_0.is_palindrome("noon") is True
    assert module_0.is_palindrome("deed") is True

    # Non-palindromes
    assert module_0.is_palindrome("hello") is False
    assert module_0.is_palindrome("world") is False
    assert module_0.is_palindrome("python") is False
    assert module_0.is_palindrome("test") is False

    # Single character strings are palindromes
    assert module_0.is_palindrome("a") is True
    assert module_0.is_palindrome("z") is True
    assert module_0.is_palindrome("7") is True

    # Empty string is a palindrome
    assert module_0.is_palindrome("") is True

    # Two-character strings
    assert module_0.is_palindrome("aa") is True
    assert module_0.is_palindrome("ab") is False

    # Strings with mixed content
    assert module_0.is_palindrome("12321") is True
    assert module_0.is_palindrome("12345") is False
    assert module_0.is_palindrome("ab1ba") is True
    assert module_0.is_palindrome("a b a") is True
    assert module_0.is_palindrome("a b c") is False

    # Case sensitivity (function is case-sensitive)
    assert module_0.is_palindrome("Aa") is False
    assert module_0.is_palindrome("aa") is True

# Generated at 2026-11-02 12:28:05.440962
# Unit test for function is_palindrome
def test_is_palindrome():
    # Basic palindromes
    assert module_0.is_palindrome("racecar") == True
    assert module_0.is_palindrome("aba") == True
    assert module_0.is_palindrome("abba") == True
    assert module_0.is_palindrome("madam") == True

    # Non-palindromes
    assert module_0.is_palindrome("hello") == False
    assert module_0.is_palindrome("abc") == False
    assert module_0.is_palindrome("abca") == False

    # Edge cases
    assert module_0.is_palindrome("") == True          # empty string
    assert module_0.is_palindrome("a") == True         # single character
    assert module_0.is_palindrome("aa") == True        # two identical chars
    assert module_0.is_palindrome("ab") == False       # two different chars

    # Case sensitivity (function is case-sensitive)
    assert module_0.is_palindrome("Racecar") == False
    assert module_0.is_palindrome("Aba") == False

    # Strings with spaces and punctuation (character-based check)
    assert module_0.is_palindrome("a b a") == True
    assert module_0.is_palindrome("ab a") == False

    # Numeric strings
    assert module_0.is_palindrome("12321") == True
    assert module_0.is_palindrome("12345") == False

    print("All tests passed!")


if __name__ == "__main__":
    test_is_palindrome()

# Generated at 2026-11-02 12:29:30.741621
# Unit test for function is_palindrome
def test_is_palindrome():
    # Empty string is a palindrome
    assert module_0.is_palindrome("") == True

    # Single character is a palindrome
    assert module_0.is_palindrome("a") == True
    assert module_0.is_palindrome("z") == True

    # Simple odd-length palindromes
    assert module_0.is_palindrome("racecar") == True
    assert module_0.is_palindrome("madam") == True
    assert module_0.is_palindrome("level") == True

    # Even-length palindromes
    assert module_0.is_palindrome("abba") == True
    assert module_0.is_palindrome("noon") == True
    assert module_0.is_palindrome("deed") == True

    # Non-palindromes
    assert module_0.is_palindrome("hello") == False
    assert module_0.is_palindrome("world") == False
    assert module_0.is_palindrome("python") == False
    assert module_0.is_palindrome("ab") == False
    assert module_0.is_palindrome("abca") == False

    # Almost-palindromes (one character off)
    assert module_0.is_palindrome("racecars") == False
    assert module_0.is_palindrome("abcdba") == False

    # Case sensitivity matters
    assert module_0.is_palindrome("Racecar") == False
    assert module_0.is_palindrome("Abba") == False

    # Spaces and punctuation are not ignored
    assert module_0.is_palindrome("a man a plan") == False
    assert module_0.is_palindrome("nurses run") == False

    # Numeric palindromes
    assert module_0.is_palindrome("12321") == True
    assert module_0.is_palindrome("123321") == True
    assert module_0.is_palindrome("12345") == False

    # Strings with special characters
    assert module_0.is_palindrome("!@!!@!") == True
    assert module_0.is_palindrome("!!") == True
    assert module_0.is_palindrome("!@") == False

    # Repeated identical characters
    assert module_0.is_palindrome("aaaa") == True
    assert module_0.is_palindrome("aaabaaa") == True