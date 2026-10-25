

# Generated at 2026-10-24 05:00:32.079668
# Unit test for function cycpattern_check
def test_cycpattern_check():
    # Exact pattern
    assert module_0.cycpattern_check("abcdef", "abc") is True

    # Cyclic rotations of "abc"
    assert module_0.cycpattern_check("xxbcayy", "abc") is True
    assert module_0.cycpattern_check("xxcabyy", "abc") is True

    # Pattern not present
    assert module_0.cycpattern_check("abcdef", "acb") is False

    # Pattern longer than searched string
    assert module_0.cycpattern_check("ab", "abc") is False

    # Single-character pattern
    assert module_0.cycpattern_check("hello", "e") is True
    assert module_0.cycpattern_check("hello", "z") is False

    # Entire string is a cyclic rotation
    assert module_0.cycpattern_check("dabc", "abcd") is True

# Generated at 2026-10-24 05:00:39.874076
# Unit test for function cycpattern_check
def test_cycpattern_check():
    # Exact pattern
    assert module_0.cycpattern_check("xxabcxx", "abc") is True

    # Cyclic rotations of "abc": "bca" and "cab"
    assert module_0.cycpattern_check("xxbcaxx", "abc") is True
    assert module_0.cycpattern_check("xxcabxx", "abc") is True

    # No cyclic rotation is present
    assert module_0.cycpattern_check("xxacbxx", "abc") is False

    # Input is shorter than the pattern
    assert module_0.cycpattern_check("ab", "abc") is False

    # Single-character pattern
    assert module_0.cycpattern_check("hello", "e") is True
    assert module_0.cycpattern_check("hello", "z") is False

# Generated at 2026-10-24 05:00:53.771454
# Unit test for function cycpattern_check
def test_cycpattern_check():
    assert module_0.cycpattern_check("abcd", "abcd") is True       # Exact match
    assert module_0.cycpattern_check("abcd", "dabc") is True       # Cyclic rotation
    assert module_0.cycpattern_check("xxcabyy", "abc") is True     # Rotation within a
    assert module_0.cycpattern_check("xxabcxx", "bca") is True     # Another rotation
    assert module_0.cycpattern_check("abx", "abc") is False        # No cyclic match
    assert module_0.cycpattern_check("ab", "abc") is False         # Pattern is longer
    assert module_0.cycpattern_check("", "abc") is False           # Empty search string
    assert module_0.cycpattern_check("abc", "") is True            # Empty pattern
    assert module_0.cycpattern_check("x", "x") is True             # Single character
    assert module_0.cycpattern_check("x", "y") is False

# Generated at 2026-10-24 05:01:03.219634
# Unit test for function cycpattern_check
def test_cycpattern_check():
    # Exact pattern
    assert module_0.cycpattern_check("xxabcxx", "abc") is True

    # Cyclic rotations: "bca" and "cab"
    assert module_0.cycpattern_check("xxbcaxx", "abc") is True
    assert module_0.cycpattern_check("xxcabxx", "abc") is True

    # Not a cyclic rotation
    assert module_0.cycpattern_check("xxacbxx", "abc") is False

    # Pattern longer than the input
    assert module_0.cycpattern_check("ab", "abc") is False

    # Single-character pattern
    assert module_0.cycpattern_check("hello", "e") is True
    assert module_0.cycpattern_check("hello", "z") is False

    # The current implementation considers an empty pattern a match
    assert module_0.cycpattern_check("", "") is True
    assert module_0.cycpattern_check("abc", "") is True

# Generated at 2026-10-24 05:01:12.230605
# Unit test for function cycpattern_check
def test_cycpattern_check():
    # Direct pattern match
    assert module_0.cycpattern_check("xxabcxx", "abc") is True

    # Cyclic rotations of "abc": "bca" and "cab"
    assert module_0.cycpattern_check("xxbcaxx", "abc") is True
    assert module_0.cycpattern_check("xxcabxx", "abc") is True

    # No cyclic pattern present
    assert module_0.cycpattern_check("xxacbxx", "abc") is False

    # Pattern longer than the input
    assert module_0.cycpattern_check("ab", "abc") is False

    # Single-character pattern
    assert module_0.cycpattern_check("hello", "e") is True
    assert module_0.cycpattern_check("hello", "z") is False