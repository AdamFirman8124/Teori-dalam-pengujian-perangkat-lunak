

# Generated at 2026-10-24 19:40:35.815890
# Unit test for function cycpattern_check
def test_cycpattern_check():
    # Exact pattern
    assert module_0.cycpattern_check("abcdef", "abc") is True

    # Cyclic rotations of "abc": "bca" and "cab"
    assert module_0.cycpattern_check("xxbcayy", "abc") is True
    assert module_0.cycpattern_check("xxcabyy", "abc") is True

    # No cyclic rotation is present
    assert module_0.cycpattern_check("xxacbyy", "abc") is False

    # Pattern is longer than the searched string
    assert module_0.cycpattern_check("ab", "abc") is False

    # Single-character pattern
    assert module_0.cycpattern_check("hello", "e") is True
    assert module_0.cycpattern_check("hello", "z") is False

# Generated at 2026-10-24 19:40:44.363031
# Unit test for function cycpattern_check
def test_cycpattern_check():
    # Exact match
    assert module_0.cycpattern_check("abcd", "abcd") is True

    # Cyclic rotation appears in a
    assert module_0.cycpattern_check("xxcdabyy", "abcd") is True

    # Entire string is a cyclic rotation
    assert module_0.cycpattern_check("hello", "lohel") is True

    # No cyclic rotation appears
    assert module_0.cycpattern_check("abdc", "abcd") is False

    # Pattern is longer than the searched string
    assert module_0.cycpattern_check("abc", "abcd") is False

    # Single-character pattern
    assert module_0.cycpattern_check("xyz", "y") is True
    assert module_0.cycpattern_check("xyz", "a") is False

# Generated at 2026-10-24 19:40:52.964192
# Unit test for function cycpattern_check
def test_cycpattern_check():
    # Direct match
    assert module_0.cycpattern_check("xxabcxx", "abc") is True

    # Cyclic rotations of "abc": "bca" and "cab"
    assert module_0.cycpattern_check("xxbcaxx", "abc") is True
    assert module_0.cycpattern_check("xxcabxx", "abc") is True

    # No cyclic rotation is present
    assert module_0.cycpattern_check("xxacbxx", "abc") is False

    # Pattern is longer than the searched string
    assert module_0.cycpattern_check("ab", "abc") is False

    # Empty searched string
    assert module_0.cycpattern_check("", "abc") is False

# Generated at 2026-10-24 19:40:55.386229
# Unit test for function cycpattern_check

# Generated at 2026-10-24 19:40:57.809447
# Unit test for function cycpattern_check

# Generated at 2026-10-24 19:41:00.221535
# Unit test for function cycpattern_check

# Generated at 2026-10-24 19:41:02.638288
# Unit test for function cycpattern_check

# Generated at 2026-10-24 19:41:05.054280
# Unit test for function cycpattern_check

# Generated at 2026-10-24 19:41:07.638784
# Unit test for function cycpattern_check