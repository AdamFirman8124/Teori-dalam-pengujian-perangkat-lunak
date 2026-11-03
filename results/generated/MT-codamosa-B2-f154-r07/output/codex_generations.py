

# Generated at 2026-11-01 23:20:07.203626
# Unit test for function cycpattern_check
def test_cycpattern_check():
    # No rotation of b present in a
    assert module_0.cycpattern_check("abcd", "abd") == False
    # b appears directly in a
    assert module_0.cycpattern_check("hello", "ell") == True
    # No rotation matches
    assert module_0.cycpattern_check("whassup", "psus") == False
    # Rotation "aba" of "baa" appears in "abab"
    assert module_0.cycpattern_check("abab", "baa") == True
    # No rotation of "eeff" in "efef"
    assert module_0.cycpattern_check("efef", "eeff") == False
    # Rotation "imens" of "simen" appears in "himenss"
    assert module_0.cycpattern_check("himenss", "simen") == True
    # No rotation of "zyx" equals a substring of "xyz"
    assert module_0.cycpattern_check("xyz", "zyx") == False
    # Rotation "abcd" of "dabc" matches a itself
    assert module_0.cycpattern_check("abcd", "dabc") == True
    # b longer than a
    assert module_0.cycpattern_check("ab", "abc") == False
    # a equals b
    assert module_0.cycpattern_check("abc", "abc") == True
    # Single characters
    assert module_0.cycpattern_check("a", "a") == True
    assert module_0.cycpattern_check("a", "b") == False
    # Two-character rotation
    assert module_0.cycpattern_check("ab", "ba") == True
    # Empty pattern matches trivially
    assert module_0.cycpattern_check("abc", "") == True
    assert module_0.cycpattern_check("", "") == True
    # Empty a with non-empty b
    assert module_0.cycpattern_check("", "abc") == False
    # Repeated characters
    assert module_0.cycpattern_check("aaa", "aa") == True
    assert module_0.cycpattern_check("aab", "baa") == True

test_cycpattern_check()
print("All tests passed!")

# Generated at 2026-11-01 23:21:10.261654
# Unit test for function cycpattern_check
def test_cycpattern_check():
    # Substring found without needing rotation
    assert module_0.cycpattern_check("abcd", "abd") == False
    assert module_0.cycpattern_check("hello", "ell") == True
    assert module_0.cycpattern_check("whassup", "psus") == False

    # Cases where a rotation of b must be matched
    assert module_0.cycpattern_check("abab", "baa") == True
    assert module_0.cycpattern_check("efef", "eeff") == False
    assert module_0.cycpattern_check("himenss", "simen") == True
    assert module_0.cycpattern_check("abcdef", "cdefab") == True
    assert module_0.cycpattern_check("abc", "cab") == True

    # Identical strings
    assert module_0.cycpattern_check("xyz", "xyz") == True

    # Pattern longer than source string
    assert module_0.cycpattern_check("hi", "hims") == False

    # Single character cases
    assert module_0.cycpattern_check("a", "a") == True
    assert module_0.cycpattern_check("a", "b") == False

    # Empty string / empty pattern edge cases
    assert module_0.cycpattern_check("", "") == True
    assert module_0.cycpattern_check("abc", "") == True
    assert module_0.cycpattern_check("", "a") == False

    # Repeated characters
    assert module_0.cycpattern_check("aaaa", "aa") == True
    assert module_0.cycpattern_check("abbba", "bab") == True
    assert module_0.cycpattern_check("abcde", "aced") == False

# Generated at 2026-11-01 23:21:44.157643
# Unit test for function cycpattern_check
def test_cycpattern_check():
    assert module_0.cycpattern_check("abcd", "abd") == False
    assert module_0.cycpattern_check("hello", "ell") == True
    assert module_0.cycpattern_check("whassup", "psus") == False
    assert module_0.cycpattern_check("abab", "baa") == True
    assert module_0.cycpattern_check("efef", "eeff") == False
    assert module_0.cycpattern_check("himenss", "simen") == True
    assert module_0.cycpattern_check("aaaa", "aa") == True
    assert module_0.cycpattern_check("ab", "ab") == True
    assert module_0.cycpattern_check("abc", "abcd") == False  # b longer than a
    assert module_0.cycpattern_check("", "a") == False  # empty a
    assert module_0.cycpattern_check("abc", "") == True  # empty b
    assert module_0.cycpattern_check("xyz", "zyx") == True  # full rotation match
    assert module_0.cycpattern_check("abcde", "deab") == True  # rotation across wrap

# Generated at 2026-11-01 23:22:07.510186
# Unit test for function cycpattern_check
def test_cycpattern_check():
    # Canonical cases
    assert module_0.cycpattern_check("abcd", "abd") == False
    assert module_0.cycpattern_check("hello", "ell") == True
    assert module_0.cycpattern_check("whassup", "psus") == False
    assert module_0.cycpattern_check("abab", "baa") == True
    assert module_0.cycpattern_check("efef", "eeff") == False
    assert module_0.cycpattern_check("himenss", "simen") == True

    # Rotation of b found in a
    assert module_0.cycpattern_check("abcd", "dabc") == True
    assert module_0.cycpattern_check("abcd", "cdab") == True
    assert module_0.cycpattern_check("xyzw", "wxyz") == True

    # No match cases
    assert module_0.cycpattern_check("xyz", "abc") == False
    assert module_0.cycpattern_check("a", "b") == False

    # Length edge cases
    assert module_0.cycpattern_check("", "a") == False
    assert module_0.cycpattern_check("ab", "abc") == False
    assert module_0.cycpattern_check("abc", "abc") == True

    # Empty pattern is a substring of anything
    assert module_0.cycpattern_check("abc", "") == True
    assert module_0.cycpattern_check("", "") == True

    # Single characters
    assert module_0.cycpattern_check("a", "a") == True

    # Case sensitivity
    assert module_0.cycpattern_check("ABC", "abc") == False

# Generated at 2026-11-01 23:22:18.561780
# Unit test for function cycpattern_check
def test_cycpattern_check():
    # Direct substring matches
    assert module_0.cycpattern_check("hello", "ell") == True
    assert module_0.cycpattern_check("abcd", "abc") == True
    assert module_0.cycpattern_check("abcd", "bcd") == True

    # Rotation matches
    assert module_0.cycpattern_check("abab", "baa") == True      # "aba" is rotation of "baa"
    assert module_0.cycpattern_check("himenss", "simen") == True # rotation of "simen" found
    assert module_0.cycpattern_check("abcabc", "cab") == True    # "cab" rotation appears

    # No match cases
    assert module_0.cycpattern_check("abcd", "abd") == False
    assert module_0.cycpattern_check("whassup", "psus") == False
    assert module_0.cycpattern_check("efef", "eeff") == False
    assert module_0.cycpattern_check("xyz", "abc") == False

    # Pattern longer than string
    assert module_0.cycpattern_check("ab", "abc") == False

    # Exact match (same string)
    assert module_0.cycpattern_check("abc", "abc") == True
    assert module_0.cycpattern_check("a", "a") == True

    # Empty pattern is always a substring
    assert module_0.cycpattern_check("abc", "") == True
    assert module_0.cycpattern_check("", "") == True

    # Empty string with non-empty pattern
    assert module_0.cycpattern_check("", "abc") == False

    # Single character cases
    assert module_0.cycpattern_check("aaa", "a") == True
    assert module_0.cycpattern_check("aaa", "b") == False

    # Repeated characters / rotations
    assert module_0.cycpattern_check("aaaa", "aa") == True
    assert module_0.cycpattern_check("ababab", "ba") == True
    assert module_0.cycpattern_check("ababab", "bb") == False