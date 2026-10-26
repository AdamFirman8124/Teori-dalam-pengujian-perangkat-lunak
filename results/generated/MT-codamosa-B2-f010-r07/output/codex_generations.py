

# Generated at 2026-10-25 14:24:39.912972
# Unit test for function is_palindrome
def test_is_palindrome():
    assert module_0.is_palindrome("") is True
    assert module_0.is_palindrome("a") is True
    assert module_0.is_palindrome("abba") is True
    assert module_0.is_palindrome("racecar") is True
    assert module_0.is_palindrome("ab") is False
    assert module_0.is_palindrome("abc") is False
    # case- and space-sensitive by design â pins current behavior
    assert module_0.is_palindrome("Abba") is False
    assert module_0.is_palindrome("ab ba") is False


def test_make_palindrome():
    assert make_palindrome("") == ""
    assert make_palindrome("a") == "a"
    assert make_palindrome("abba") == "abba"    # already a palindrome
    assert make_palindrome("cat") == "catac"
    assert make_palindrome("cata") == "catac"   # longest palindromic suffix wins
    assert make_palindrome("race") == "racecar"
    assert make_palindrome("abab") == "ababa"

    # property: result is always a palindrome and preserves the input as prefix
    for s in ["", "a", "ab", "abc", "abab", "xyzzy", "hello"]:
        p = make_palindrome(s)
        assert module_0.is_palindrome(p), f"not a palindrome: {p!r}"
        assert p.startswith(s)

# Generated at 2026-10-25 14:24:54.556975
# Unit test for function make_palindrome
def test_make_palindrome():
    assert module_0.make_palindrome('') == ''
    assert module_0.make_palindrome('a') == 'a'
    assert module_0.make_palindrome('ab') == 'aba'
    assert module_0.make_palindrome('abc') == 'abcba'
    assert module_0.make_palindrome('race') == 'racecar'
    assert module_0.make_palindrome('racecar') == 'racecar'
    assert module_0.make_palindrome('abba') == 'abba'
    assert module_0.make_palindrome('abca') == 'abcacba'
    assert module_0.make_palindrome('aab') == 'aabaa'

    # property: result starts with input and is a palindrome
    for s in ['', 'a', 'ab', 'abc', 'race', 'racecar', 'abba', 'abca']:
        result = module_0.make_palindrome(s)
        assert result.startswith(s)
        assert is_palindrome(result)

# Generated at 2026-10-25 14:24:59.999042
# Unit test for function is_palindrome

# Generated at 2026-10-25 14:25:02.419034
# Unit test for function is_palindrome

# Generated at 2026-10-25 14:25:04.839763
# Unit test for function is_palindrome

# Generated at 2026-10-25 14:25:10.331049
# Unit test for function is_palindrome

# Generated at 2026-10-25 14:25:12.747109
# Unit test for function is_palindrome

# Generated at 2026-10-25 14:25:15.161860
# Unit test for function is_palindrome

# Generated at 2026-10-25 14:25:17.577722
# Unit test for function make_palindrome

# Generated at 2026-10-25 14:25:19.991691
# Unit test for function make_palindrome

# Generated at 2026-10-25 14:25:22.405061
# Unit test for function make_palindrome