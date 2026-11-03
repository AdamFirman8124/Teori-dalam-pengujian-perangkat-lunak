

# Generated at 2026-11-02 23:53:37.963224
# Unit test for function generate_integers
def test_generate_integers():
    # Both values within range [2, 8]
    assert module_0.generate_integers(2, 8) == [2, 4, 6, 8]

    # Arguments reversed should give same result
    assert module_0.generate_integers(8, 2) == [2, 4, 6, 8]

    # Range partially below the lower bound of 2
    assert module_0.generate_integers(1, 5) == [2, 4]

    # Range partially above the upper bound of 8
    assert module_0.generate_integers(7, 10) == [8]

    # Entire range below 2
    assert module_0.generate_integers(0, 1) == []

    # Entire range above 8
    assert module_0.generate_integers(9, 12) == []

    # Wide range clamped to [2, 8]
    assert module_0.generate_integers(1, 10) == [2, 4, 6, 8]

    # a == b, single even value
    assert module_0.generate_integers(4, 4) == [4]

    # a == b, odd value yields empty result
    assert module_0.generate_integers(3, 3) == []

    # Negative values
    assert module_0.generate_integers(-5, 3) == [2]

    print("All tests passed!")


if __name__ == "__main__":
    test_generate_integers()

# Generated at 2026-11-02 23:54:17.077298
# Unit test for function generate_integers
def test_generate_integers():
    # Both bounds within even range
    assert module_0.generate_integers(2, 8) == [2, 4, 6, 8]
    assert module_0.generate_integers(8, 2) == [2, 4, 6, 8]  # order swapped

    # Partial overlap with [2, 8]
    assert module_0.generate_integers(1, 5) == [2, 4]
    assert module_0.generate_integers(5, 1) == [2, 4]
    assert module_0.generate_integers(3, 7) == [4, 6]
    assert module_0.generate_integers(7, 3) == [4, 6]

    # Range entirely below 2
    assert module_0.generate_integers(0, 1) == []

    # Range entirely above 8
    assert module_0.generate_integers(9, 14) == []
    assert module_0.generate_integers(14, 9) == []

    # Single-value ranges
    assert module_0.generate_integers(2, 2) == [2]
    assert module_0.generate_integers(4, 4) == [4]
    assert module_0.generate_integers(3, 3) == []  # odd value, no evens
    assert module_0.generate_integers(9, 9) == []  # above upper bound

    # Negative inputs clamped
    assert module_0.generate_integers(-5, 3) == [2]
    assert module_0.generate_integers(-10, -1) == []

    # Large values clamped to [2, 8]
    assert module_0.generate_integers(1, 100) == [2, 4, 6, 8]
    assert module_0.generate_integers(100, 1) == [2, 4, 6, 8]

    print("All tests passed!")


if __name__ == "__main__":
    test_generate_integers()

# Generated at 2026-11-02 23:55:11.146967
# Unit test for function generate_integers
def test_generate_integers():
    # Basic case within range
    assert module_0.generate_integers(2, 8) == [2, 4, 6, 8]
    # Arguments reversed — result should be the same
    assert module_0.generate_integers(8, 2) == [2, 4, 6, 8]
    # Range partially below lower bound
    assert module_0.generate_integers(1, 5) == [2, 4]
    # Range fully inside bounds, only evens kept
    assert module_0.generate_integers(3, 7) == [4, 6]
    # Range above upper bound — empty result
    assert module_0.generate_integers(10, 14) == []
    # Single value, odd — empty result
    assert module_0.generate_integers(5, 5) == []
    # Single value, even — singleton list
    assert module_0.generate_integers(2, 2) == [2]
    # Lower bound clamping with zero
    assert module_0.generate_integers(0, 2) == [2]
    # Negative and large values clamped to [2, 8]
    assert module_0.generate_integers(-2, 9) == [2, 4, 6, 8]
    # Upper bound clamping
    assert module_0.generate_integers(4, 100) == [4, 6, 8]

# Generated at 2026-11-02 23:55:42.485768
# Unit test for function generate_integers
def test_generate_integers():
    # Basic ascending range
    assert module_0.generate_integers(2, 8) == [2, 4, 6, 8]
    # Order shouldn't matter
    assert module_0.generate_integers(8, 2) == [2, 4, 6, 8]
    # Range clamped to lower bound of 2
    assert module_0.generate_integers(1, 5) == [2, 4]
    # Range clamped to upper bound of 8
    assert module_0.generate_integers(0, 10) == [2, 4, 6, 8]
    assert module_0.generate_integers(9, 1) == [2, 4, 6, 8]
    # Both bounds clamped
    assert module_0.generate_integers(0, 100) == [2, 4, 6, 8]
    # Partial range with odd start
    assert module_0.generate_integers(3, 7) == [4, 6]
    assert module_0.generate_integers(7, 3) == [4, 6]
    # Single even value
    assert module_0.generate_integers(4, 4) == [4]
    # Single odd value -> no evens
    assert module_0.generate_integers(3, 3) == []
    # Range entirely above 8 -> empty
    assert module_0.generate_integers(10, 20) == []
    assert module_0.generate_integers(20, 10) == []
    # Range entirely below 2 -> empty
    assert module_0.generate_integers(-5, 1) == []
    # Only upper boundary included
    assert module_0.generate_integers(7, 9) == [8]
    # Negative bounds clamped
    assert module_0.generate_integers(-10, -2) == []
    print("All tests passed!")


if __name__ == "__main__":
    test_generate_integers()

# Generated at 2026-11-02 23:56:46.180042
# Unit test for function generate_integers
def test_generate_integers():
    # Typical case: full range 2..8
    assert module_0.generate_integers(2, 8) == [2, 4, 6, 8]
    # Argument order should not matter
    assert module_0.generate_integers(8, 2) == [2, 4, 6, 8]
    # Lower bound clamped to 2
    assert module_0.generate_integers(1, 5) == [2, 4]
    assert module_0.generate_integers(0, 3) == [2]
    # Upper bound clamped to 8
    assert module_0.generate_integers(5, 20) == [6, 8]
    # Mixed range containing only evens in between
    assert module_0.generate_integers(3, 7) == [4, 6]
    # Single-value ranges
    assert module_0.generate_integers(4, 4) == [4]
    assert module_0.generate_integers(3, 3) == []  # odd single value -> no evens
    # Entire range above 8 yields nothing
    assert module_0.generate_integers(10, 14) == []
    # Negative inputs clamped to lower bound of 2
    assert module_0.generate_integers(-2, 4) == [2, 4]
    # Large reversed inputs
    assert module_0.generate_integers(50, 1) == [2, 4, 6, 8]


if __name__ == "__main__":
    test_generate_integers()
    print("All tests passed.")