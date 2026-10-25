

# Generated at 2026-10-25 01:45:14.973878
# Unit test for function cycpattern_check

# Generated at 2026-10-25 01:45:17.388721
# Unit test for function cycpattern_check

# Generated at 2026-10-25 01:45:19.804243
# Unit test for function cycpattern_check

# Generated at 2026-10-25 01:45:22.218585
# Unit test for function cycpattern_check

# Generated at 2026-10-25 01:45:24.632938
# Unit test for function cycpattern_check

# Generated at 2026-10-25 01:45:27.047734
# Unit test for function cycpattern_check

# Generated at 2026-10-25 01:45:29.464546
# Unit test for function cycpattern_check

# Generated at 2026-10-25 01:45:31.880545
# Unit test for function cycpattern_check

# Generated at 2026-10-25 01:45:38.193044
# Unit test for function cycpattern_check
def test_cycpattern_check():assert module_0.cycpattern_check("xxcabyy", "abc") is True

# Generated at 2026-10-25 01:45:45.974438
# Unit test for function cycpattern_check
def test_cycpattern_check():
    # b itself is a substring of a
    assert module_0.cycpattern_check("abcd", "abd") == False
    assert module_0.cycpattern_check("hello", "ell") == True

    # rotation of b appears in a
    assert module_0.cycpattern_check("whassup", "psus") == False
    assert module_0.cycpattern_check("whassup", "ssup") == True
    assert module_0.cycpattern_check("abab", "baa") == True   # "aab" isn't in "abab", but rotation "aba" is
    assert module_0.cycpattern_check("efef", "eeff") == False
    assert module_0.cycpattern_check("himenss", "simen") == True  # rotation "imenss" matches

    # b longer than a -> impossible
    assert module_0.cycpattern_check("ab", "aba") == False

    # empty b -> trivially found
    assert module_0.cycpattern_check("abc", "") == True
    assert module_0.cycpattern_check("", "") == True

    # empty a, non-empty b
    assert module_0.cycpattern_check("", "a") == False

    print("All tests passed.")

test_cycpattern_check()

# Generated at 2026-10-25 01:45:47.306863
# Unit test for function cycpattern_check
def test_cycpattern_check():
    # b itself is a substring of a
    assert module_0.cycpattern_check("abcd", "abd") == False
    assert module_0.cycpattern_check("hello", "ell") == True

    # rotation of b appears in a
    assert module_0.cycpattern_check("whassup", "psus") == False
    assert module_0.cycpattern_check("whassup", "ssup") == True
    assert module_0.cycpattern_check("abab", "baa") == True   # "aab" isn't in "abab", but rotation "aba" is
    assert module_0.cycpattern_check("efef", "eeff") == False
    assert module_0.cycpattern_check("himenss", "simen") == True  # rotation "imenss" matches

    # b longer than a -> impossible
    assert module_0.cycpattern_check("ab", "aba") == False

    # empty b -> trivially found
    assert module_0.cycpattern_check("abc", "") == True
    assert module_0.cycpattern_check("", "") == True

    # empty a, non-empty b
    assert module_0.cycpattern_check("", "a") == False

    print("All tests passed.")

test_cycpattern_check()