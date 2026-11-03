

# Generated at 2026-11-02 14:00:37.270305
# Unit test for function is_palindrome
def test_is_palindrome():
    # Basic palindromes
    assert module_0.is_palindrome("racecar") is True
    assert module_0.is_palindrome("madam") is True
    assert module_0.is_palindrome("abba") is True

    # Basic non-palindromes
    assert module_0.is_palindrome("hello") is False
    assert module_0.is_palindrome("abc") is False
    assert module_0.is_palindrome("ab") is False

    # Edge cases
    assert module_0.is_palindrome("") is True          # empty string
    assert module_0.is_palindrome("a") is True         # single character
    assert module_0.is_palindrome("aa") is True        # two identical chars
    assert module_0.is_palindrome("ab") is False       # two different chars

    # Odd and even length palindromes
    assert module_0.is_palindrome("abcba") is True
    assert module_0.is_palindrome("abccba") is True
    assert module_0.is_palindrome("abcdba") is False

    # Case sensitivity and spaces are NOT handled (exact char comparison)
    assert module_0.is_palindrome("Racecar") is False
    assert module_0.is_palindrome("a man a plan") is False

    # Numeric and mixed strings
    assert module_0.is_palindrome("12321") is True
    assert module_0.is_palindrome("1231") is False
    assert module_0.is_palindrome("1a1") is True

    # Strings with special characters
    assert module_0.is_palindrome("!@!") is True
    assert module_0.is_palindrome("!@#") is False

    # Verify return type is bool
    assert isinstance(module_0.is_palindrome("noon"), bool)
    assert isinstance(module_0.is_palindrome("nope"), bool)

    print("All tests passed!")

# Generated at 2026-11-02 14:02:56.012846
# Unit test for function is_palindrome
def test_is_palindrome():
    # Simple palindromes
    assert module_0.is_palindrome("aba") == True
    assert module_0.is_palindrome("racecar") == True
    assert module_0.is_palindrome("abba") == True

    # Single character is a palindrome
    assert module_0.is_palindrome("a") == True

    # Empty string is a palindrome
    assert module_0.is_palindrome("") == True

    # Non-palindromes
    assert module_0.is_palindrome("abc") == False
    assert module_0.is_palindrome("hello") == False
    assert module_0.is_palindrome("abca") == False

    # Two-character strings
    assert module_0.is_palindrome("aa") == True
    assert module_0.is_palindrome("ab") == False

    # Case sensitivity: uppercase vs lowercase are not equal
    assert module_0.is_palindrome("Aba") == False

    # Strings with spaces (spaces count as characters)
    assert module_0.is_palindrome("a a") == False
    assert module_0.is_palindrome("a aa a") == True

    # Numeric string palindrome
    assert module_0.is_palindrome("12321") == True
    assert module_0.is_palindrome("12345") == False

    print("All tests passed!")


if __name__ == "__main__":
    test_is_palindrome()

# Generated at 2026-11-02 14:05:12.146574
# Unit test for function is_palindrome
def test_is_palindrome():
    # Basic palindrome
    assert module_0.is_palindrome("racecar") == True
    assert module_0.is_palindrome("madam") == True
    assert module_0.is_palindrome("noon") == True

    # Even-length palindrome
    assert module_0.is_palindrome("abba") == True
    assert module_0.is_palindrome("abccba") == True

    # Not a palindrome
    assert module_0.is_palindrome("hello") == False
    assert module_0.is_palindrome("python") == False
    assert module_0.is_palindrome("ab") == False

    # Edge cases
    assert module_0.is_palindrome("") == True        # empty string
    assert module_0.is_palindrome("a") == True       # single character
    assert module_0.is_palindrome("aa") == True      # two identical characters
    assert module_0.is_palindrome("ab") == False     # two different characters

    # Case sensitivity
    assert module_0.is_palindrome("Aba") == False    # case-sensitive comparison

    # Spaces and punctuation are not ignored
    assert module_0.is_palindrome("nurses run") == False
    assert module_0.is_palindrome("nursesrun") == True

    # Numeric strings
    assert module_0.is_palindrome("12321") == True
    assert module_0.is_palindrome("12345") == False

    print("All test cases passed!")


# Run the tests
if __name__ == "__main__":
    test_is_palindrome()

# Generated at 2026-11-02 14:06:48.051698
# Unit test for function is_palindrome
def test_is_palindrome():
    # Empty string is a palindrome
    assert module_0.is_palindrome("") == True

    # Single character is a palindrome
    assert module_0.is_palindrome("a") == True

    # Simple odd-length palindrome
    assert module_0.is_palindrome("racecar") == True

    # Even-length palindrome
    assert module_0.is_palindrome("abba") == True

    # Two identical characters
    assert module_0.is_palindrome("aa") == True

    # Two different characters
    assert module_0.is_palindrome("ab") == False

    # Numeric palindrome
    assert module_0.is_palindrome("12321") == True

    # Numeric non-palindrome
    assert module_0.is_palindrome("12345") == False

    # Common word that is a palindrome
    assert module_0.is_palindrome("level") == True
    assert module_0.is_palindrome("noon") == True

    # Non-palindrome words
    assert module_0.is_palindrome("hello") == False
    assert module_0.is_palindrome("world") == False

    # Case sensitivity: comparison is case-sensitive
    assert module_0.is_palindrome("Racecar") == False
    assert module_0.is_palindrome("AbBa") == False

    # Palindrome with repeated pattern
    assert module_0.is_palindrome("abcba") == True
    assert module_0.is_palindrome("abccba") == True

    # Longer palindrome sentence (exact characters)
    assert module_0.is_palindrome("was it a car or a cat i saw".replace(" ", "")) == True

    # String with spaces (spaces count as characters)
    assert module_0.is_palindrome("a b a") == True
    assert module_0.is_palindrome("ab a") == False

    # Palindrome with punctuation
    assert module_0.is_palindrome("!!!!") == True
    assert module_0.is_palindrome("a!a") == True

    print("All tests passed!")


if __name__ == "__main__":
    test_is_palindrome()

# Generated at 2026-11-02 14:08:20.709258
# Unit test for function is_palindrome
def test_is_palindrome():
    # nonce:bf3bfd57

    # Simple palindromes
    assert module_0.is_palindrome("racecar") == True
    assert module_0.is_palindrome("madam") == True
    assert module_0.is_palindrome("level") == True
    assert module_0.is_palindrome("noon") == True

    # Non-palindromes
    assert module_0.is_palindrome("hello") == False
    assert module_0.is_palindrome("world") == False
    assert module_0.is_palindrome("python") == False

    # Edge cases
    assert module_0.is_palindrome("") == True          # empty string
    assert module_0.is_palindrome("a") == True         # single character
    assert module_0.is_palindrome("ab") == False       # two different chars
    assert module_0.is_palindrome("aa") == True        # two same chars

    # Even-length palindromes
    assert module_0.is_palindrome("abba") == True
    assert module_0.is_palindrome("abccba") == True

    # Odd-length palindromes
    assert module_0.is_palindrome("aba") == True
    assert module_0.is_palindrome("abcba") == True

    # Case sensitivity (function is case-sensitive)
    assert module_0.is_palindrome("Anna") == False
    assert module_0.is_palindrome("Anna".lower()) == True

    # Strings with spaces / punctuation (treated literally)
    assert module_0.is_palindrome("a b a") == True
    assert module_0.is_palindrome("a man") == False

    # Numbers as strings
    assert module_0.is_palindrome("12321") == True
    assert module_0.is_palindrome("12345") == False

    print("All tests passed!")


test_is_palindrome()