

# Generated at 2026-11-03 05:18:22.822353
# Unit test for function generate_integers
def test_generate_integers():
    # Both bounds within range
    assert module_0.generate_integers(2, 8) == [2, 4, 6, 8]
    assert module_0.generate_integers(8, 2) == [2, 4, 6, 8]

    # Arguments swapped / unordered
    assert module_0.generate_integers(5, 1) == [2, 4]
    assert module_0.generate_integers(1, 5) == [2, 4]

    # Bounds outside [2, 8]
    assert module_0.generate_integers(10, 14) == []
    assert module_0.generate_integers(9, 9) == []
    assert module_0.generate_integers(-2, 4) == [2, 4]
    assert module_0.generate_integers(0, 20) == [2, 4, 6, 8]

    # Equal arguments
    assert module_0.generate_integers(2, 2) == [2]
    assert module_0.generate_integers(3, 3) == []
    assert module_0.generate_integers(4, 4) == [4]

    # Partial overlap with the [2, 8] window
    assert module_0.generate_integers(7, 8) == [8]
    assert module_0.generate_integers(6, 100) == [6, 8]

    print("All test_generate_integers tests passed!")


test_generate_integers()

# Generated at 2026-11-03 05:20:59.096085
# Unit test for function generate_integers
def test_generate_integers():
    # Basic case: even numbers between 2 and 8
    assert module_0.generate_integers(2, 8) == [2, 4, 6, 8]

    # Reversed arguments should yield the same result
    assert module_0.generate_integers(8, 2) == [2, 4, 6, 8]

    # Range clamped to [2, 8]
    assert module_0.generate_integers(1, 10) == [2, 4, 6, 8]
    assert module_0.generate_integers(0, 100) == [2, 4, 6, 8]

    # Partial clamping: lower bound raised to 2
    assert module_0.generate_integers(1, 4) == [2, 4]

    # Partial clamping: upper bound capped at 8
    assert module_0.generate_integers(6, 10) == [6, 8]

    # Range with no even numbers after clamping (upper < lower)
    assert module_0.generate_integers(9, 10) == []
    assert module_0.generate_integers(10, 20) == []

    # Negative inputs: lower clamped to 2, upper below lower -> empty
    assert module_0.generate_integers(-2, -1) == []
    assert module_0.generate_integers(-10, 0) == []

    # Single-value ranges
    assert module_0.generate_integers(4, 4) == [4]   # even single value
    assert module_0.generate_integers(3, 3) == []    # odd single value
    assert module_0.generate_integers(7, 7) == []

    # Small ranges containing one even number
    assert module_0.generate_integers(1, 3) == [2]
    assert module_0.generate_integers(2, 3) == [2]
    assert module_0.generate_integers(3, 6) == [4, 6]
    assert module_0.generate_integers(5, 6) == [6]

    # Overlapping ranges around the clamp boundaries
    assert module_0.generate_integers(2, 2) == [2]
    assert module_0.generate_integers(8, 8) == [8]
    assert module_0.generate_integers(1, 2) == [2]
    assert module_0.generate_integers(8, 9) == [8]

    print("All tests passed!")


if __name__ == "__main__":
    test_generate_integers()

# Generated at 2026-11-03 05:23:10.824917
# Unit test for function generate_integers
def test_generate_integers():
    # Basic ascending range
    assert module_0.generate_integers(2, 8) == [2, 4, 6, 8]
    # Descending order should yield the same result
    assert module_0.generate_integers(8, 2) == [2, 4, 6, 8]
    # Range partially below bounds
    assert module_0.generate_integers(1, 5) == [2, 4]
    assert module_0.generate_integers(5, 1) == [2, 4]
    # Range partially above bounds
    assert module_0.generate_integers(6, 10) == [6, 8]
    assert module_0.generate_integers(10, 6) == [6, 8]
    # Fully outside valid bounds -> empty
    assert module_0.generate_integers(10, 14) == []
    assert module_0.generate_integers(14, 10) == []
    assert module_0.generate_integers(0, 0) == []
    # Single even value in range
    assert module_0.generate_integers(4, 4) == [4]
    # Single odd value in range -> empty
    assert module_0.generate_integers(3, 3) == []
    # Narrow range with one even value
    assert module_0.generate_integers(3, 5) == [4]
    assert module_0.generate_integers(5, 3) == [4]
    # Range with no even numbers after clamping
    assert module_0.generate_integers(9, 9) == []
    assert module_0.generate_integers(1, 1) == []

    print("All test cases passed!")


if __name__ == "__main__":
    test_generate_integers()

# Generated at 2026-11-03 05:24:57.080011
# Unit test for function generate_integers
def test_generate_integers():
    # Both bounds within [2, 8]
    assert module_0.generate_integers(2, 8) == [2, 4, 6, 8]
    # Reversed order arguments
    assert module_0.generate_integers(8, 2) == [2, 4, 6, 8]
    # Bounds outside the range, no valid even numbers
    assert module_0.generate_integers(10, 14) == []
    # Only one even number in range
    assert module_0.generate_integers(1, 3) == [2]
    # Narrow range with a single even number
    assert module_0.generate_integers(3, 5) == [4]
    # Single number inputs
    assert module_0.generate_integers(4, 4) == [4]
    assert module_0.generate_integers(5, 5) == []
    # Lower bound below 2, clamped to 2
    assert module_0.generate_integers(0, 4) == [2, 4]
    # Upper bound above 8, clamped to 8
    assert module_0.generate_integers(6, 20) == [6, 8]