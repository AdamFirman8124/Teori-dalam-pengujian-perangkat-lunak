

# Generated at 2026-11-03 02:24:58.681536
# Unit test for function generate_integers
def test_generate_integers():
    # Basic case: both values within [2, 8]
    assert module_0.generate_integers(2, 8) == [2, 4, 6, 8]
    assert module_0.generate_integers(8, 2) == [2, 4, 6, 8]

    # Order of arguments should not matter
    assert module_0.generate_integers(1, 5) == [2, 4]
    assert module_0.generate_integers(5, 1) == [2, 4]

    # Values outside the [2, 8] range are clamped
    assert module_0.generate_integers(10, 14) == []  # lower > upper -> empty
    assert module_0.generate_integers(0, 20) == [2, 4, 6, 8]
    assert module_0.generate_integers(-5, 3) == [2]

    # Single value ranges
    assert module_0.generate_integers(2, 2) == [2]
    assert module_0.generate_integers(4, 4) == [4]
    assert module_0.generate_integers(3, 3) == []  # 3 is odd
    assert module_0.generate_integers(7, 7) == []  # 7 is odd
    assert module_0.generate_integers(8, 8) == [8]

    # Both bounds clamped to same odd value
    assert module_0.generate_integers(9, 9) == []

    print("All tests passed!")


if __name__ == "__main__":
    test_generate_integers()

# Generated at 2026-11-03 02:26:38.302633
# Unit test for function generate_integers
def test_generate_integers():
    # Basic case: range fully within [2, 8]
    assert module_0.generate_integers(2, 8) == [2, 4, 6, 8]

    # Reversed arguments should give same result
    assert module_0.generate_integers(8, 2) == [2, 4, 6, 8]

    # Partial range within bounds
    assert module_0.generate_integers(1, 5) == [2, 4]
    assert module_0.generate_integers(5, 1) == [2, 4]

    # Both arguments below lower bound of 2
    assert module_0.generate_integers(1, 1) == []

    # Both arguments above upper bound of 8
    assert module_0.generate_integers(10, 14) == []

    # Single even value in range
    assert module_0.generate_integers(3, 4) == [4]

    # Single value input
    assert module_0.generate_integers(2, 2) == [2]
    assert module_0.generate_integers(3, 3) == []

    # Mixed bounds where clamping kicks in on both sides
    assert module_0.generate_integers(7, 3) == [4, 6]

    # One value below 2, one above 8
    assert module_0.generate_integers(1, 9) == [2, 4, 6, 8]

    # Negative values get clamped to 2
    assert module_0.generate_integers(-5, 4) == [2, 4]

    print("All tests passed!")


test_generate_integers()

# Generated at 2026-11-03 02:28:43.794434
# Unit test for function generate_integers
def test_generate_integers():
    # Both values within range, a < b
    assert module_0.generate_integers(2, 8) == [2, 4, 6, 8]
    # Both values within range, a > b
    assert module_0.generate_integers(8, 2) == [2, 4, 6, 8]
    # Values below range boundary
    assert module_0.generate_integers(1, 5) == [2, 4]
    assert module_0.generate_integers(5, 1) == [2, 4]
    # Values above range boundary
    assert module_0.generate_integers(10, 14) == []
    assert module_0.generate_integers(14, 10) == []
    # Mixed: one below, one above
    assert module_0.generate_integers(1, 10) == [2, 4, 6, 8]
    assert module_0.generate_integers(10, 1) == [2, 4, 6, 8]
    # Odd numbers only in range
    assert module_0.generate_integers(3, 7) == [4, 6]
    assert module_0.generate_integers(7, 3) == [4, 6]
    # Single even number
    assert module_0.generate_integers(2, 2) == [2]
    # Single odd number
    assert module_0.generate_integers(3, 3) == []
    # Boundary at 8
    assert module_0.generate_integers(6, 9) == [6, 8]
    # Equal values both even and in range
    assert module_0.generate_integers(4, 4) == [4]
    # Large odd values
    assert module_0.generate_integers(9, 11) == []

    print("All tests passed!")

test_generate_integers()

# Generated at 2026-11-03 02:30:37.419769
# Unit test for function generate_integers
def test_generate_integers():
    # Basic case: even numbers between 2 and 8
    assert module_0.generate_integers(2, 8) == [2, 4, 6, 8]
    assert module_0.generate_integers(8, 2) == [2, 4, 6, 8]  # order of args shouldn't matter

    # Range clamped below at 2
    assert module_0.generate_integers(1, 5) == [2, 4]
    assert module_0.generate_integers(0, 7) == [2, 4, 6]
    assert module_0.generate_integers(-3, 6) == [2, 4, 6]

    # Range clamped above at 8
    assert module_0.generate_integers(5, 15) == [6, 8]
    assert module_0.generate_integers(9, 20) == []
    assert module_0.generate_integers(10, 10) == []

    # Single-value ranges
    assert module_0.generate_integers(2, 2) == [2]
    assert module_0.generate_integers(4, 4) == [4]
    assert module_0.generate_integers(3, 3) == []  # odd value yields nothing
    assert module_0.generate_integers(7, 7) == []

    # Empty ranges (upper < lower after clamping)
    assert module_0.generate_integers(0, 0) == []
    assert module_0.generate_integers(-5, 1) == []
    assert module_0.generate_integers(9, 9) == []

    # Larger spans, still clamped to [2, 8]
    assert module_0.generate_integers(-10, 100) == [2, 4, 6, 8]
    assert module_0.generate_integers(100, -10) == [2, 4, 6, 8]

    # Negative bounds
    assert module_0.generate_integers(-8, -2) == []
    assert module_0.generate_integers(-2, 3) == [2]

    print("All tests passed!")


if __name__ == "__main__":
    test_generate_integers()