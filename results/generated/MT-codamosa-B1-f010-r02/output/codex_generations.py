

# Generated at 2026-10-24 21:05:53.224598
# Unit test for function is_palindrome
def test_is_palindrome():
    assert module_0.is_palindrome("") is True
    assert module_0.is_palindrome("a") is True
    assert module_0.is_palindrome("abba") is True
    assert module_0.is_palindrome("racecar") is True
    assert module_0.is_palindrome("abc") is False
    assert module_0.is_palindrome("Racecar") is False  # Case-sensitive


# Unit tests for function make_palindrome
def test_make_palindrome():
    assert make_palindrome("") == ""
    assert make_palindrome("a") == "a"
    assert make_palindrome("aba") == "aba"
    assert make_palindrome("ab") == "aba"
    assert make_palindrome("abcd") == "abcdcba"
    assert make_palindrome("abac") == "abacaba"

# Generated at 2026-10-24 21:05:57.663128
# Unit test for function is_palindrome
def test_is_palindrome():
    assert module_0.is_palindrome("") is True
    assert module_0.is_palindrome("a") is True
    assert module_0.is_palindrome("racecar") is True
    assert module_0.is_palindrome("abba") is True
    assert module_0.is_palindrome("hello") is False
    assert module_0.is_palindrome("Racecar") is False

# Generated at 2026-10-24 21:05:59.025867
# Unit test for function make_palindrome
def test_make_palindrome():
    assert module_0.make_palindrome('') == ''
    assert module_0.make_palindrome('a') == 'a'
    assert module_0.make_palindrome('aa') == 'aa'
    assert module_0.make_palindrome('ab') == 'aba'
    assert module_0.make_palindrome('abc') == 'abcba'
    assert module_0.make_palindrome('aab') == 'aabaa'
    assert module_0.make_palindrome('cat') == 'catac'
    assert module_0.make_palindrome('cata') == 'catac'
    assert module_0.make_palindrome('race') == 'racecar'

    # already palindromes stay unchanged
    assert module_0.make_palindrome('aba') == 'aba'
    assert module_0.make_palindrome('abba') == 'abba'
    assert module_0.make_palindrome('racecar') == 'racecar'

    # property: result starts with input and is a palindrome
    for s in ['', 'a', 'ab', 'abc', 'abac', 'abca', 'race', 'hello']:
        result = module_0.make_palindrome(s)
        assert result.startswith(s)
        assert is_palindrome(result)

# Generated at 2026-10-24 21:06:03.770038
# Unit test for function is_palindrome
def test_is_palindrome():
    assert module_0.is_palindrome("") is True
    assert module_0.is_palindrome("a") is True
    assert module_0.is_palindrome("racecar") is True
    assert module_0.is_palindrome("abba") is True
    assert module_0.is_palindrome("hello") is False
    assert module_0.is_palindrome("Racecar") is False

# Generated at 2026-10-24 21:06:06.190231
# Unit test for function is_palindrome

# Generated at 2026-10-24 21:06:08.729518
# Unit test for function is_palindrome

# Generated at 2026-10-24 21:06:11.148995
# Unit test for function is_palindrome