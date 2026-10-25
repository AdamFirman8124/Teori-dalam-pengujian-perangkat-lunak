

# Generated at 2026-10-24 22:57:43.321796
# Unit test for function cycpattern_check
def test_cycpattern_check():
    # Exact pattern
    assert module_0.cycpattern_check("xxabcxx", "abc") is True

    # Cyclic rotations of "abc": "bca" and "cab"
    assert module_0.cycpattern_check("xxbcaxx", "abc") is True
    assert module_0.cycpattern_check("xxcabxx", "abc") is True

    # No matching cyclic pattern
    assert module_0.cycpattern_check("xxacbxx", "abc") is False

    # Pattern longer than the searched string
    assert module_0.cycpattern_check("ab", "abc") is False

    # Match at string boundaries
    assert module_0.cycpattern_check("cabxyz", "abc") is True
    assert module_0.cycpattern_check("xyabca", "abc") is True

    # Single-character pattern
    assert module_0.cycpattern_check("hello", "e") is True
    assert module_0.cycpattern_check("hello", "z") is False

# Generated at 2026-10-24 22:57:50.590021
# Unit test for function cycpattern_check
def test_cycpattern_check():
    # Exact pattern
    assert module_0.cycpattern_check("abcdef", "abc") is True

    # Cyclic rotations of "abc": "bca" and "cab"
    assert module_0.cycpattern_check("xxbcaxx", "abc") is True
    assert module_0.cycpattern_check("xxcabxx", "abc") is True

    # No cyclic rotation is present
    assert module_0.cycpattern_check("abcdef", "acb") is False

    # Source string is shorter than the pattern
    assert module_0.cycpattern_check("ab", "abc") is False

    # Empty pattern (current implementation treats it as a match)
    assert module_0.cycpattern_check("abc", "") is True

# Generated at 2026-10-24 22:58:05.029517
# Unit test for function cycpattern_check
def test_cycpattern_check():
    # Exact pattern
    assert module_0.cycpattern_check("abcdef", "abc") is True

    # Cyclic rotations of "abc": "bca" and "cab"
    assert module_0.cycpattern_check("xxbcayy", "abc") is True
    assert module_0.cycpattern_check("xxcabyy", "abc") is True

    # No cyclic rotation is present
    assert module_0.cycpattern_check("xxacbyy", "abc") is False

    # Source string is shorter than the pattern
    assert module_0.cycpattern_check("ab", "abc") is False

    # Empty pattern is considered a match by the current implementation
    assert module_0.cycpattern_check("anything", "") is True

# Generated at 2026-10-24 22:58:12.401414
# Unit test for function cycpattern_check
def test_cycpattern_check():
    # Exact match
    assert module_0.cycpattern_check("abc", "abc") is True

    # Cyclic rotations of "abc"
    assert module_0.cycpattern_check("xxbcayy", "abc") is True
    assert module_0.cycpattern_check("xxcabyy", "abc") is True

    # No cyclic rotation present
    assert module_0.cycpattern_check("axbycz", "abc") is False

    # First string is shorter than the pattern
    assert module_0.cycpattern_check("ab", "abc") is False

    # Repeated characters
    assert module_0.cycpattern_check("zzaaazz", "aaa") is True

# Generated at 2026-10-24 22:58:22.335425
# Unit test for function cycpattern_check
def test_cycpattern_check():
    # Exact pattern
    assert module_0.cycpattern_check("xxabcxx", "abc") is True

    # Cyclic rotations: "bca" and "cab"
    assert module_0.cycpattern_check("xxbcaxx", "abc") is True
    assert module_0.cycpattern_check("xxcabxx", "abc") is True

    # No cyclic rotation is present
    assert module_0.cycpattern_check("xxacbxx", "abc") is False

    # Pattern is longer than the searched string
    assert module_0.cycpattern_check("ab", "abc") is False

    # Single-character pattern
    assert module_0.cycpattern_check("xyz", "y") is True
    assert module_0.cycpattern_check("xyz", "a") is False