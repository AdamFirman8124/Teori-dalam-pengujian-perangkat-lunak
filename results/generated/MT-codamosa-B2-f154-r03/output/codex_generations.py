

# Generated at 2026-11-02 18:38:04.182274
# Unit test for function cycpattern_check
def test_cycpattern_check():
    # Basic cases
    assert module_0.cycpattern_check("abcd", "abd") == False
    assert module_0.cycpattern_check("hello", "ell") == True
    assert module_0.cycpattern_check("whassup", "psus") == False
    assert module_0.cycpattern_check("abab", "baa") == True
    assert module_0.cycpattern_check("efef", "eeff") == False
    assert module_0.cycpattern_check("himenss", "simen") == True

    # Rotation matching
    assert module_0.cycpattern_check("abcd", "dabc") == True   # rotation of abcd
    assert module_0.cycpattern_check("abcd", "cdab") == True   # rotation of abcd
    assert module_0.cycpattern_check("abcde", "eabcd") == True # rotation of abcde

    # b longer than a -> impossible
    assert module_0.cycpattern_check("ab", "abc") == False
    assert module_0.cycpattern_check("", "a") == False

    # Empty pattern matches trivially
    assert module_0.cycpattern_check("abc", "") == True
    assert module_0.cycpattern_check("", "") == True

    # Identical strings
    assert module_0.cycpattern_check("same", "same") == True

    # Repeated characters
    assert module_0.cycpattern_check("aabbcc", "bcaa") == True
    assert module_0.cycpattern_check("aaaa", "aa") == True

    # Single characters
    assert module_0.cycpattern_check("a", "a") == True
    assert module_0.cycpattern_check("a", "b") == False

    print("All cycpattern_check tests passed!")

test_cycpattern_check()

# Generated at 2026-11-02 18:40:14.768355
# Unit test for function cycpattern_check
def test_cycpattern_check():
    # Basic true cases: b is a substring of a
    assert module_0.cycpattern_check("hello", "ell") == True
    assert module_0.cycpattern_check("whassup", "psus") == False
    assert module_0.cycpattern_check("abab", "baa") == True
    assert module_0.cycpattern_check("efef", "eeff") == False
    assert module_0.cycpattern_check("himenssos", "simenssos") == True
    assert module_0.cycpattern_check("aaaa", "aa") == True
    assert module_0.cycpattern_check("abcdef", "defabc") == True

    # Empty pattern should always match
    assert module_0.cycpattern_check("anything", "") == True
    assert module_0.cycpattern_check("", "") == True

    # Pattern longer than a cannot match
    assert module_0.cycpattern_check("ab", "abc") == False

    # Pattern equal in length to a: must be rotation of a
    assert module_0.cycpattern_check("abcd", "cdab") == True
    assert module_0.cycpattern_check("abcd", "dcba") == False

    # Rotations that are substrings
    assert module_0.cycpattern_check("xyzw", "zwxy") == False
    assert module_0.cycpattern_check("xyzwxyz", "wxyz") == True

    # Repeated characters
    assert module_0.cycpattern_check("aaaa", "aaaa") == True
    assert module_0.cycpattern_check("aab", "baa") == True

# Generated at 2026-11-02 18:42:11.949687
# Unit test for function cycpattern_check
def test_cycpattern_check():
    # nonce:5220e2d4
    # Basic cases
    assert module_0.cycpattern_check('abcd', 'abd') == False
    assert module_0.cycpattern_check('hello', 'ell') == True
    assert module_0.cycpattern_check('whassup', 'psus') == False
    assert module_0.cycpattern_check('abab', 'baa') == True
    assert module_0.cycpattern_check('efef', 'eeff') == False
    assert module_0.cycpattern_check('himenss', 'simen') == True

    # Edge cases
    assert module_0.cycpattern_check('aaaa', 'aa') == True
    assert module_0.cycpattern_check('aaaa', 'aaaaa') == False
    assert module_0.cycpattern_check('', '') == True
    assert module_0.cycpattern_check('abc', '') == True
    assert module_0.cycpattern_check('', 'a') == False
    assert module_0.cycpattern_check('abc', 'abc') == True

    # Rotation-specific cases
    assert module_0.cycpattern_check('xabc', 'abcx') == True   # rotation of b found in a
    assert module_0.cycpattern_check('xabc', 'abxc') == False  # no rotation matches
    assert module_0.cycpattern_check('ab', 'ba') == True       # two-char rotation
    assert module_0.cycpattern_check('efef', 'ef') == True

# Generated at 2026-11-02 18:44:00.928974
# Unit test for function cycpattern_check
def test_cycpattern_check():
    # Basic cases
    assert module_0.cycpattern_check("abcd", "abd") == False
    assert module_0.cycpattern_check("hello", "ell") == True
    assert module_0.cycpattern_check("whassup", "psus") == False
    assert module_0.cycpattern_check("abab", "baa") == True
    assert module_0.cycpattern_check("efef", "eeff") == False
    assert module_0.cycpattern_check("himenss", "simen") == True

    # Rotations that match
    assert module_0.cycpattern_check("abab", "ab") == True
    assert module_0.cycpattern_check("abab", "ba") == True
    assert module_0.cycpattern_check("xyzab", "abyz") == True  # rotation "yzab" in a
    assert module_0.cycpattern_check("abcdef", "cde") == True

    # Exact match
    assert module_0.cycpattern_check("abc", "abc") == True

    # b longer than a
    assert module_0.cycpattern_check("ab", "abc") == False

    # Empty strings
    assert module_0.cycpattern_check("", "a") == False
    assert module_0.cycpattern_check("a", "") == True
    assert module_0.cycpattern_check("", "") == True

    # Repeated characters
    assert module_0.cycpattern_check("aaaa", "aa") == True
    assert module_0.cycpattern_check("aaa", "aaaa") == False

    # No match at all
    assert module_0.cycpattern_check("xyz", "zyx") == False
    assert module_0.cycpattern_check("cat", "dog") == False

# Generated at 2026-11-02 18:44:59.680778
# Unit test for function cycpattern_check
def test_cycpattern_check():
    # Basic cases from problem specification
    assert module_0.cycpattern_check("abcd", "abd") == False
    assert module_0.cycpattern_check("hello", "ell") == True
    assert module_0.cycpattern_check("whassup", "psus") == False
    assert module_0.cycpattern_check("abab", "baa") == True
    assert module_0.cycpattern_check("efef", "eeff") == False
    assert module_0.cycpattern_check("himenss", "simen") == True

    # Exact match
    assert module_0.cycpattern_check("abcd", "abcd") == True

    # Rotation of b present in a
    assert module_0.cycpattern_check("abcdef", "cdefab") == True
    assert module_0.cycpattern_check("abcde", "deabc") == True

    # Rotation not present
    assert module_0.cycpattern_check("abcdef", "facdab") == False

    # b longer than a
    assert module_0.cycpattern_check("ab", "abc") == False
    assert module_0.cycpattern_check("", "abc") == False

    # Empty b is a substring of any a
    assert module_0.cycpattern_check("abc", "") == True
    assert module_0.cycpattern_check("", "") == True

    # Repeated characters
    assert module_0.cycpattern_check("aaaa", "aa") == True
    assert module_0.cycpattern_check("abab", "ab") == True

    # Single characters
    assert module_0.cycpattern_check("x", "x") == True
    assert module_0.cycpattern_check("x", "y") == False

    # Case sensitivity
    assert module_0.cycpattern_check("Hello", "ell") == True
    assert module_0.cycpattern_check("hello", "ELL") == False

    print("All tests passed!")


if __name__ == "__main__":
    test_cycpattern_check()