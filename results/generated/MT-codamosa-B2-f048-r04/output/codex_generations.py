

# Generated at 2026-11-02 09:58:42.626980
# Unit test for function is_palindrome
def test_is_palindrome():
    # Basic palindromes
    assert module_0.is_palindrome("racecar") == True
    assert module_0.is_palindrome("noon") == True
    assert module_0.is_palindrome("madam") == True
    assert module_0.is_palindrome("level") == True

    # Non-palindromes
    assert module_0.is_palindrome("hello") == False
    assert module_0.is_palindrome("world") == False
    assert module_0.is_palindrome("python") == False

    # Edge cases
    assert module_0.is_palindrome("") == True          # empty string
    assert module_0.is_palindrome("a") == True         # single character
    assert module_0.is_palindrome("ab") == False       # two different chars
    assert module_0.is_palindrome("aa") == True        # two identical chars

    # Even-length palindromes
    assert module_0.is_palindrome("abba") == True
    assert module_0.is_palindrome("12321") == True

    # Odd-length palindromes
    assert module_0.is_palindrome("aba") == True
    assert module_0.is_palindrome("abcba") == True

    # Case sensitivity (implementation is case-sensitive)
    assert module_0.is_palindrome("Racecar") == False
    assert module_0.is_palindrome("Anna") == False
    assert module_0.is_palindrome("ANNA") == True

    # Spaces and punctuation are significant
    assert module_0.is_palindrome("nurses run") == False
    assert module_0.is_palindrome("a b a") == True
    assert module_0.is_palindrome("a man a plan a canal panama") == False
    assert module_0.is_palindrome("!!!") == True
    assert module_0.is_palindrome("!.!") == True

    # Numeric strings
    assert module_0.is_palindrome("12321") == True
    assert module_0.is_palindrome("12345") == False
    assert module_0.is_palindrome("1001") == True

    # Mixed alphanumeric
    assert module_0.is_palindrome("1a1") == True
    assert module_0.is_palindrome("12a21") == True
    assert module_0.is_palindrome("1a2") == False

    # Long palindrome
    assert module_0.is_palindrome("abcdeffedcba") == True
    assert module_0.is_palindrome("abcdefgedcba") == False

    print("All tests passed!")


# Run tests
test_is_palindrome()

# Generated at 2026-11-02 09:59:43.402165
# Unit test for function is_palindrome
def test_is_palindrome():
    # Basic palindromes
    assert module_0.is_palindrome("racecar") is True
    assert module_0.is_palindrome("level") is True
    assert module_0.is_palindrome("noon") is True
    assert module_0.is_palindrome("abba") is True

    # Non-palindromes
    assert module_0.is_palindrome("hello") is False
    assert module_0.is_palindrome("python") is False
    assert module_0.is_palindrome("abcd") is False

    # Single character
    assert module_0.is_palindrome("a") is True
    assert module_0.is_palindrome("z") is True

    # Empty string
    assert module_0.is_palindrome("") is True

    # Two characters
    assert module_0.is_palindrome("aa") is True
    assert module_0.is_palindrome("ab") is False

    # Odd-length palindrome
    assert module_0.is_palindrome("abcba") is True

    # Even-length palindrome
    assert module_0.is_palindrome("abccba") is True

    # Case sensitivity: uppercase vs lowercase are different
    assert module_0.is_palindrome("Abba") is False
    assert module_0.is_palindrome("ABBA") is True

    # Strings with spaces and punctuation (not stripped)
    assert module_0.is_palindrome("a b a") is True
    assert module_0.is_palindrome("ab a") is False

    # Near-palindrome differing by one character at each end
    assert module_0.is_palindrome("xabcay") is False

    # Numeric strings
    assert module_0.is_palindrome("12321") is True
    assert module_0.is_palindrome("12345") is False

    # Repeated identical characters
    assert module_0.is_palindrome("aaaa") is True
    assert module_0.is_palindrome("aaaab") is False

    print("All tests passed!")


# Run tests
test_is_palindrome()

# Generated at 2026-11-02 10:01:01.300783
# Unit test for function is_palindrome
def test_is_palindrome():
    # Basic palindromes
    assert module_0.is_palindrome("racecar") is True
    assert module_0.is_palindrome("level") is True
    assert module_0.is_palindrome("noon") is True

    # Non-palindromes
    assert module_0.is_palindrome("hello") is False
    assert module_0.is_palindrome("world") is False
    assert module_0.is_palindrome("python") is False

    # Empty string is a palindrome
    assert module_0.is_palindrome("") is True

    # Single character is a palindrome
    assert module_0.is_palindrome("a") is True
    assert module_0.is_palindrome("z") is True

    # Two-character strings
    assert module_0.is_palindrome("aa") is True
    assert module_0.is_palindrome("ab") is False

    # Odd-length palindromes
    assert module_0.is_palindrome("aba") is True
    assert module_0.is_palindrome("abcba") is True

    # Even-length palindromes
    assert module_0.is_palindrome("abba") is True
    assert module_0.is_palindrome("abccba") is True

    # Case sensitivity: function is case-sensitive
    assert module_0.is_palindrome("Racecar") is False
    assert module_0.is_palindrome("Aa") is False

    # Spaces and punctuation are not ignored
    assert module_0.is_palindrome("a man a plan a canal panama") is False
    assert module_0.is_palindrome("nurses run") is False

    # Strings that are palindromes with special characters
    assert module_0.is_palindrome("!!") is True
    assert module_0.is_palindrome("a!a") is True
    assert module_0.is_palindrome("12321") is True
    assert module_0.is_palindrome("123321") is True
    assert module_0.is_palindrome("12345") is False

    # Near-palindromes (single character difference)
    assert module_0.is_palindrome("abca") is False
    assert module_0.is_palindrome("abcda") is False

    print("All tests passed!")


if __name__ == "__main__":
    test_is_palindrome()

# Generated at 2026-11-02 10:02:06.549137
# Unit test for function is_palindrome
def test_is_palindrome():
    # Typical palindromes
    assert module_0.is_palindrome("racecar") == True
    assert module_0.is_palindrome("abba") == True
    assert module_0.is_palindrome("noon") == True
    assert module_0.is_palindrome("level") == True

    # Non-palindromes
    assert module_0.is_palindrome("hello") == False
    assert module_0.is_palindrome("python") == False
    assert module_0.is_palindrome("abca") == False

    # Edge cases
    assert module_0.is_palindrome("") == True        # empty string
    assert module_0.is_palindrome("a") == True       # single character
    assert module_0.is_palindrome("ab") == False     # two different chars
    assert module_0.is_palindrome("aa") == True      # two same chars

    # Case sensitivity (no normalization in the function)
    assert module_0.is_palindrome("Racecar") == False

    # Spaces and punctuation are NOT ignored
    assert module_0.is_palindrome("nurses run") == False
    assert module_0.is_palindrome("a man a plan a canal panama") == False

    # Numeric strings
    assert module_0.is_palindrome("12321") == True
    assert module_0.is_palindrome("12345") == False

    # Even-length palindromes
    assert module_0.is_palindrome("abccba") == True
    assert module_0.is_palindrome("abcba") == True   # odd-length palindrome

    print("All is_palindrome tests passed!")

# Generated at 2026-11-02 10:02:42.083323
# Unit test for function is_palindrome
def test_is_palindrome():
    # Empty string is a palindrome
    assert module_0.is_palindrome("") == True
    # Single character is a palindrome
    assert module_0.is_palindrome("a") == True
    assert module_0.is_palindrome("x") == True
    # Simple palindromes
    assert module_0.is_palindrome("aba") == True
    assert module_0.is_palindrome("abba") == True
    assert module_0.is_palindrome("racecar") == True
    assert module_0.is_palindrome("level") == True
    # Even-length palindrome
    assert module_0.is_palindrome("noon") == True
    # Numeric string palindrome
    assert module_0.is_palindrome("12321") == True
    assert module_0.is_palindrome("1") == True
    # Non-palindromes
    assert module_0.is_palindrome("ab") == False
    assert module_0.is_palindrome("abc") == False
    assert module_0.is_palindrome("abab") == False
    assert module_0.is_palindrome("hello") == False
    assert module_0.is_palindrome("palindrome") == False
    assert module_0.is_palindrome("12345") == False
    # Near-palindrome (one char off)
    assert module_0.is_palindrome("abca") == False
    assert module_0.is_palindrome("abcda") == False
    # Case and whitespace sensitivity
    assert module_0.is_palindrome("Aba") == False
    assert module_0.is_palindrome("a ba") == False
    # Palindrome with repeated characters
    assert module_0.is_palindrome("aaaa") == True
    assert module_0.is_palindrome("aaabaaa") == True