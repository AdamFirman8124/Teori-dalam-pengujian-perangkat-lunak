

# Generated at 2026-10-24 21:37:04.185111
# Unit test for function is_palindrome
def test_is_palindrome():
    # Basic true cases
    assert module_0.is_palindrome("racecar") is True
    assert module_0.is_palindrome("a") is True
    assert module_0.is_palindrome("") is True          # empty string is a palindrome
    assert module_0.is_palindrome("aa") is True
    assert module_0.is_palindrome("abba") is True
    assert module_0.is_palindrome("abcba") is True

    # Basic false cases
    assert module_0.is_palindrome("ab") is False
    assert module_0.is_palindrome("hello") is False
    assert module_0.is_palindrome("racecars") is False

    # Edge cases
    assert module_0.is_palindrome("Aa") is False        # case-sensitive
    assert module_0.is_palindrome("a man a plan") is False  # spaces count as chars
    assert module_0.is_palindrome("01210") is True      # digits work too
    assert module_0.is_palindrome("abca") is False      # mismatch in the middle

    print("All tests passed!")


test_is_palindrome()

# Generated at 2026-10-24 21:37:06.739570
# Unit test for function is_palindrome

# Generated at 2026-10-24 21:37:09.271906
# Unit test for function is_palindrome

# Generated at 2026-10-24 21:37:11.816787
# Unit test for function is_palindrome

# Generated at 2026-10-24 21:37:14.236429
# Unit test for function is_palindrome

# Generated at 2026-10-24 21:37:16.821102
# Unit test for function is_palindrome

# Generated at 2026-10-24 21:37:19.242613
# Unit test for function is_palindrome

# Generated at 2026-10-24 21:37:21.663601
# Unit test for function is_palindrome

# Generated at 2026-10-24 21:37:24.085788
# Unit test for function is_palindrome

# Generated at 2026-10-24 21:37:26.499981
# Unit test for function is_palindrome

# Generated at 2026-10-24 21:37:28.934943
# Unit test for function is_palindrome

# Generated at 2026-10-24 21:37:31.342986
# Unit test for function is_palindrome

# Generated at 2026-10-24 21:37:38.097047
# Unit test for function is_palindrome
def test_is_palindrome():assert module_0.is_palindrome("racecar") is True