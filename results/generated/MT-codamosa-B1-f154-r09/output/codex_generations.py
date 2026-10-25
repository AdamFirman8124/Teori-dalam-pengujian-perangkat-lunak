

# Generated at 2026-10-24 05:54:26.626455
# Unit test for function cycpattern_check
def test_cycpattern_check():
    # Exact match
    assert module_0.cycpattern_check("abc", "abc") is True

    # Cyclic rotations: "bca" and "cab"
    assert module_0.cycpattern_check("xxbcayy", "abc") is True
    assert module_0.cycpattern_check("xxcabyy", "abc") is True

    # No cyclic rotation present
    assert module_0.cycpattern_check("abdc", "abc") is False

    # Pattern longer than the searched string
    assert module_0.cycpattern_check("ab", "abc") is False

    # Single-character pattern
    assert module_0.cycpattern_check("hello", "e") is True
    assert module_0.cycpattern_check("hello", "x") is False

    # Empty-string behavior
    assert module_0.cycpattern_check("", "abc") is False
    assert module_0.cycpattern_check("abc", "") is True
    assert module_0.cycpattern_check("", "") is True

# Generated at 2026-10-24 05:54:35.533523
# Unit test for function cycpattern_check
def test_cycpattern_check():
    # Exact pattern
    assert module_0.cycpattern_check("xxabcxx", "abc") is True

    # Cyclic rotations of "abc": "bca" and "cab"
    assert module_0.cycpattern_check("xxbcaxx", "abc") is True
    assert module_0.cycpattern_check("xxcabxx", "abc") is True

    # No cyclic rotation present
    assert module_0.cycpattern_check("xxacbxx", "abc") is False

    # Pattern longer than the searched string
    assert module_0.cycpattern_check("ab", "abc") is False

    # Empty pattern
    assert module_0.cycpattern_check("abc", "") is True

# Generated at 2026-10-24 05:54:44.686305
# Unit test for function cycpattern_check
def test_cycpattern_check():
    # Exact pattern
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

    # Single-character pattern
    assert module_0.cycpattern_check("hello", "e") is True
    assert module_0.cycpattern_check("hello", "z") is False

# Generated at 2026-10-24 05:54:57.556099
# Unit test for function cycpattern_check
def test_cycpattern_check():
    # Exact pattern
    assert module_0.cycpattern_check("xxabcyy", "abc") is True

    # Cyclic rotations of "abc": "bca" and "cab"
    assert module_0.cycpattern_check("xxbcayy", "abc") is True
    assert module_0.cycpattern_check("xxcabyy", "abc") is True

    # Not a cyclic rotation
    assert module_0.cycpattern_check("xxacbyy", "abc") is False

    # Pattern longer than the input
    assert module_0.cycpattern_check("ab", "abc") is False

    # Single-character pattern
    assert module_0.cycpattern_check("hello", "e") is True
    assert module_0.cycpattern_check("hello", "x") is False

    # Empty pattern is considered present
    assert module_0.cycpattern_check("abc", "") is True
    assert module_0.cycpattern_check("", "") is True

# Generated at 2026-10-24 05:55:06.882363
# Unit test for function cycpattern_check
def test_cycpattern_check():
    # Exact match
    assert module_0.cycpattern_check("abcd", "abcd") is True

    # Cyclic rotations
    assert module_0.cycpattern_check("cdab", "abcd") is True
    assert module_0.cycpattern_check("dabc", "abcd") is True

    # Cyclic pattern contained within a longer string
    assert module_0.cycpattern_check("xxcdabyy", "abcd") is True

    # Same characters, but not a cyclic rotation
    assert module_0.cycpattern_check("acbd", "abcd") is False

    # Pattern longer than the searched string
    assert module_0.cycpattern_check("abc", "abcd") is False

    # No matching cyclic pattern
    assert module_0.cycpattern_check("xyzxyz", "abcd") is False