

# Generated at 2026-10-24 20:24:19.979136
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

# Generated at 2026-10-24 20:24:22.402549
# Unit test for function make_palindrome

# Generated at 2026-10-24 20:24:28.181299
# Unit test for function make_palindrome
def test_make_palindrome():assert module_0.make_palindrome("race") == "racecar"

# Generated at 2026-10-24 20:24:33.493562
# Unit test for function is_palindrome
def test_is_palindrome():
    assert module_0.is_palindrome("") is True
    assert module_0.is_palindrome("a") is True
    assert module_0.is_palindrome("racecar") is True
    assert module_0.is_palindrome("abba") is True
    assert module_0.is_palindrome("hello") is False
    assert module_0.is_palindrome("Racecar") is False  # Case-sensitive

# Generated at 2026-10-24 20:24:38.113998
# Unit test for function is_palindrome
def test_is_palindrome():
    assert module_0.is_palindrome("")
    assert module_0.is_palindrome("a")
    assert module_0.is_palindrome("aba")
    assert module_0.is_palindrome("abba")
    assert not module_0.is_palindrome("abc")
    assert not module_0.is_palindrome("Palindrome")
    assert not module_0.is_palindrome("Racecar")  # Case-sensitive


# Unit test for function make_palindrome
def test_make_palindrome():
    assert make_palindrome("") == ""
    assert make_palindrome("a") == "a"
    assert make_palindrome("aba") == "aba"
    assert make_palindrome("ab") == "aba"
    assert make_palindrome("abcd") == "abcdcba"
    assert make_palindrome("abac") == "abacaba"

# Generated at 2026-10-24 20:24:39.534546
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