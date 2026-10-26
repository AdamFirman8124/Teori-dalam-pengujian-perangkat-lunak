

# Generated at 2026-10-25 12:32:26.257859
# Unit test for function is_palindrome
def test_is_palindrome():
    assert module_0.is_palindrome("") is True
    assert module_0.is_palindrome("a") is True
    assert module_0.is_palindrome("aa") is True
    assert module_0.is_palindrome("ab") is False
    assert module_0.is_palindrome("aba") is True
    assert module_0.is_palindrome("abba") is True
    assert module_0.is_palindrome("racecar") is True
    assert module_0.is_palindrome("hello") is False
    assert module_0.is_palindrome("abca") is False
    assert module_0.is_palindrome("12321") is True
    assert module_0.is_palindrome("12345") is False
    assert module_0.is_palindrome("Racecar") is False
    assert module_0.is_palindrome("madam") is True
    assert module_0.is_palindrome("madam ") is False

# Generated at 2026-10-25 12:32:36.087504
# Unit test for function is_palindrome
def test_is_palindrome():
    # True cases - palindromes
    assert module_0.is_palindrome("") is True
    assert module_0.is_palindrome("a") is True
    assert module_0.is_palindrome("abba") is True
    assert module_0.is_palindrome("racecar") is True
    assert module_0.is_palindrome("madam") is True

    # False cases - not palindromes
    assert module_0.is_palindrome("hello") is False
    assert module_0.is_palindrome("abca") is False
    assert module_0.is_palindrome("racecars") is False
    assert module_0.is_palindrome("Racecar") is False  # case-sensitive

# Generated at 2026-10-25 12:32:37.626749
# Unit test for function is_palindrome
def test_is_palindrome():
    # True cases - palindromes
    assert module_0.is_palindrome("") is True
    assert module_0.is_palindrome("a") is True
    assert module_0.is_palindrome("abba") is True
    assert module_0.is_palindrome("racecar") is True
    assert module_0.is_palindrome("madam") is True

    # False cases - not palindromes
    assert module_0.is_palindrome("hello") is False
    assert module_0.is_palindrome("abca") is False
    assert module_0.is_palindrome("racecars") is False
    assert module_0.is_palindrome("Racecar") is False  # case-sensitive

# Generated at 2026-10-25 12:32:39.120603
# Unit test for function is_palindrome
def test_is_palindrome():
    # True cases - palindromes
    assert module_0.is_palindrome("") is True
    assert module_0.is_palindrome("a") is True
    assert module_0.is_palindrome("abba") is True
    assert module_0.is_palindrome("racecar") is True
    assert module_0.is_palindrome("madam") is True

    # False cases - not palindromes
    assert module_0.is_palindrome("hello") is False
    assert module_0.is_palindrome("abca") is False
    assert module_0.is_palindrome("racecars") is False
    assert module_0.is_palindrome("Racecar") is False  # case-sensitive

# Generated at 2026-10-25 12:32:41.209186
# Unit test for function is_palindrome
def test_is_palindrome():
    # True cases - palindromes
    assert module_0.is_palindrome("") is True
    assert module_0.is_palindrome("a") is True
    assert module_0.is_palindrome("abba") is True
    assert module_0.is_palindrome("racecar") is True
    assert module_0.is_palindrome("madam") is True

    # False cases - not palindromes
    assert module_0.is_palindrome("hello") is False
    assert module_0.is_palindrome("abca") is False
    assert module_0.is_palindrome("racecars") is False
    assert module_0.is_palindrome("Racecar") is False  # case-sensitive