

# Generated at 2026-11-01 21:38:42.357735
# Unit test for function is_palindrome
def test_is_palindrome():
    # Odd-length palindromes
    assert module_0.is_palindrome("aba") == True
    assert module_0.is_palindrome("racecar") == True
    assert module_0.is_palindrome("madam") == True

    # Even-length palindromes
    assert module_0.is_palindrome("abba") == True
    assert module_0.is_palindrome("noon") == True
    assert module_0.is_palindrome("abccba") == True

    # Non-palindromes
    assert module_0.is_palindrome("abc") == False
    assert module_0.is_palindrome("hello") == False
    assert module_0.is_palindrome("abca") == False

    # Edge cases
    assert module_0.is_palindrome("") == True          # empty string
    assert module_0.is_palindrome("a") == True         # single character
    assert module_0.is_palindrome("ab") == False       # two different chars
    assert module_0.is_palindrome("aa") == True        # two same chars

    # Case sensitivity (function is case-sensitive)
    assert module_0.is_palindrome("Abba") == False
    assert module_0.is_palindrome("ABBA") == True

    # Strings with spaces/punctuation are NOT normalized
    assert module_0.is_palindrome("nurses run") == False
    assert module_0.is_palindrome("nursesrun") == True

    # Numeric-like strings
    assert module_0.is_palindrome("12321") == True
    assert module_0.is_palindrome("12345") == False

    print("All test_is_palindrome tests passed!")


test_is_palindrome()

# Generated at 2026-11-01 21:39:41.505184
# Unit test for function is_palindrome
def test_is_palindrome():
    # Basic palindromes
    assert module_0.is_palindrome("racecar") == True
    assert module_0.is_palindrome("madam") == True
    assert module_0.is_palindrome("abba") == True
    assert module_0.is_palindrome("noon") == True

    # Non-palindromes
    assert module_0.is_palindrome("hello") == False
    assert module_0.is_palindrome("world") == False
    assert module_0.is_palindrome("abcd") == False

    # Edge cases
    assert module_0.is_palindrome("") == True          # empty string
    assert module_0.is_palindrome("a") == True         # single character
    assert module_0.is_palindrome("aa") == True        # two identical chars
    assert module_0.is_palindrome("ab") == False       # two different chars

    # Even-length palindrome
    assert module_0.is_palindrome("abccba") == True

    # Odd-length palindrome
    assert module_0.is_palindrome("abcba") == True

    # Case sensitivity check
    assert module_0.is_palindrome("Abba") == False     # 'A' != 'a'
    assert module_0.is_palindrome("ABBA") == True

    # Strings with digits and symbols
    assert module_0.is_palindrome("12321") == True
    assert module_0.is_palindrome("12a21") == False
    assert module_0.is_palindrome("!@!") == True

    # Strings with spaces (spaces count as characters)
    assert module_0.is_palindrome("a b a") == True
    assert module_0.is_palindrome("ab ba") == False

    print("All tests passed!")

# Generated at 2026-11-01 21:40:21.696974
# Unit test for function is_palindrome
def test_is_palindrome():
    # Typical palindromes
    assert module_0.is_palindrome("racecar") is True
    assert module_0.is_palindrome("level") is True
    assert module_0.is_palindrome("madam") is True
    assert module_0.is_palindrome("noon") is True
    assert module_0.is_palindrome("abba") is True

    # Non-palindromes
    assert module_0.is_palindrome("hello") is False
    assert module_0.is_palindrome("world") is False
    assert module_0.is_palindrome("python") is False

    # Edge cases
    assert module_0.is_palindrome("") is True          # empty string is a palindrome
    assert module_0.is_palindrome("a") is True         # single character
    assert module_0.is_palindrome("ab") is False       # two different characters
    assert module_0.is_palindrome("aa") is True        # two identical characters

    # Case sensitivity (function is case-sensitive)
    assert module_0.is_palindrome("Racecar") is False
    assert module_0.is_palindrome("Madam") is False

    # Repeated characters and longer strings
    assert module_0.is_palindrome("aaaa") is True
    assert module_0.is_palindrome("abcba") is True
    assert module_0.is_palindrome("abccba") is True
    assert module_0.is_palindrome("abcabc") is False

    # Strings with spaces/punctuation are treated literally
    assert module_0.is_palindrome("a b a") is True
    assert module_0.is_palindrome("ab a") is False

# Generated at 2026-11-01 21:40:47.384205
# Unit test for function is_palindrome
def test_is_palindrome():
# nonce:7ee52ba5
    # Empty string is a palindrome
    assert module_0.is_palindrome("") == True

    # Single character is a palindrome
    assert module_0.is_palindrome("a") == True
    assert module_0.is_palindrome("x") == True

    # Odd-length palindromes
    assert module_0.is_palindrome("aba") == True
    assert module_0.is_palindrome("racecar") == True
    assert module_0.is_palindrome("madam") == True

    # Even-length palindromes
    assert module_0.is_palindrome("abba") == True
    assert module_0.is_palindrome("noon") == True

    # Non-palindromes
    assert module_0.is_palindrome("abc") == False
    assert module_0.is_palindrome("ab") == False
    assert module_0.is_palindrome("hello") == False

    # Case sensitivity: comparison is case-sensitive
    assert module_0.is_palindrome("Abba") == False
    assert module_0.is_palindrome("Aa") == True

    # Digits and mixed characters
    assert module_0.is_palindrome("12321") == True
    assert module_0.is_palindrome("1231") == False
    assert module_0.is_palindrome("ab!ba") == True

    # Phrases with spaces are not normalized
    assert module_0.is_palindrome("a man a plan a canal panama") == False
    assert module_0.is_palindrome("step on no pets") == False

# Generated at 2026-11-01 21:41:15.716218
# Unit test for function is_palindrome
def test_is_palindrome():
    # Simple palindromes
    assert module_0.is_palindrome("racecar") is True
    assert module_0.is_palindrome("madam") is True
    assert module_0.is_palindrome("level") is True
    assert module_0.is_palindrome("noon") is True

    # Non-palindromes
    assert module_0.is_palindrome("hello") is False
    assert module_0.is_palindrome("world") is False
    assert module_0.is_palindrome("python") is False

    # Edge cases
    assert module_0.is_palindrome("") is True          # empty string
    assert module_0.is_palindrome("a") is True         # single character
    assert module_0.is_palindrome("ab") is False       # two different chars
    assert module_0.is_palindrome("aa") is True        # two same chars

    # Case sensitivity — the function does not normalize case
    assert module_0.is_palindrome("Racecar") is False
    assert module_0.is_palindrome("rAcecar") is False

    # Even-length palindromes
    assert module_0.is_palindrome("abba") is True
    assert module_0.is_palindrome("abca") is False

    # Strings with spaces / punctuation (no normalization)
    assert module_0.is_palindrome("a b a") is True
    assert module_0.is_palindrome("ab a") is False

    # Numeric strings
    assert module_0.is_palindrome("12321") is True
    assert module_0.is_palindrome("12345") is False