

# Generated at 2026-10-24 11:55:00.095912
# Unit test for function is_palindrome
def test_is_palindrome():
    assert module_0.is_palindrome("") is True
    assert module_0.is_palindrome("a") is True
    assert module_0.is_palindrome("racecar") is True
    assert module_0.is_palindrome("abba") is True

    assert module_0.is_palindrome("hello") is False
    assert module_0.is_palindrome("ab") is False
    assert module_0.is_palindrome("Racecar") is False  # case-sensitive


# Unit tests for make_palindrome
def test_make_palindrome():
    assert make_palindrome("") == ""
    assert make_palindrome("a") == "a"
    assert make_palindrome("race") == "racecar"
    assert make_palindrome("abcd") == "abcdcba"
    assert make_palindrome("aacecaaa") == "aacecaaa"

# Generated at 2026-10-24 11:55:02.317141
# Unit test for function is_palindrome
def test_is_palindrome():
    # True cases - reads the same forwards and backwards
    assert module_0.is_palindrome("") is True
    assert module_0.is_palindrome("a") is True
    assert module_0.is_palindrome("abba") is True
    assert module_0.is_palindrome("racecar") is True
    assert module_0.is_palindrome("madam") is True

    # False cases
    assert module_0.is_palindrome("hello") is False
    assert module_0.is_palindrome("ab") is False
    assert module_0.is_palindrome("racecars") is False
    assert module_0.is_palindrome("Racecar") is False  # case-sensitive

# Generated at 2026-10-24 11:55:19.304239
# Unit test for function is_palindrome
def test_is_palindrome():
    # Basic true cases
    assert module_0.is_palindrome('') == True
    assert module_0.is_palindrome('a') == True
    assert module_0.is_palindrome('aba') == True
    assert module_0.is_palindrome('racecar') == True
    assert module_0.is_palindrome('aaaa') == True

    # False cases
    assert module_0.is_palindrome('ab') == False
    assert module_0.is_palindrome('abc') == False
    assert module_0.is_palindrome('abab') == False

    # Case sensitivity: 'A' != 'a', so this is NOT a palindrome
    assert module_0.is_palindrome('Aba') == False

    print("test_is_palindrome passed")


def test_make_palindrome():
    # Empty string
    assert make_palindrome('') == ''

    # Already a palindrome â returned unchanged
    assert make_palindrome('') == ''
    assert make_palindrome('x') == 'x'
    assert make_palindrome('aba') == 'aba'
    assert make_palindrome('racecar') == 'racecar'

    # Needs appending (from HumanEval-style examples)
    assert make_palindrome('cat') == 'catac'
    assert make_palindrome('cata') == 'catac'

    # Result must itself be a palindrome and start with the original
    for s in ['cat', 'cata', 'hello', 'ab', 'abcd']:
        result = make_palindrome(s)
        assert module_0.is_palindrome(result), f"{result} is not a palindrome"
        assert result.startswith(s), f"{result} does not start with {s}"

    print("test_make_palindrome passed")


if __name__ == '__main__':
    test_is_palindrome()
    test_make_palindrome()

# Generated at 2026-10-24 11:55:21.841462
# Unit test for function is_palindrome

# Generated at 2026-10-24 11:55:30.906472
# Unit test for function is_palindrome
def test_is_palindrome():assert module_0.is_palindrome("racecar") == True

# Generated at 2026-10-24 11:55:41.962240
# Unit test for function is_palindrome
def test_is_palindrome():
    assert module_0.is_palindrome("") is True
    assert module_0.is_palindrome("a") is True
    assert module_0.is_palindrome("racecar") is True
    assert module_0.is_palindrome("abba") is True

    assert module_0.is_palindrome("hello") is False
    assert module_0.is_palindrome("ab") is False