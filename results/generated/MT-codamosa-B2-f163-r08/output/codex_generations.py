

# Generated at 2026-11-02 16:09:07.899249
# Unit test for function generate_integers
def test_generate_integers():
    # Both values within even-producing range
    assert module_0.generate_integers(2, 8) == [2, 4, 6, 8]
    assert module_0.generate_integers(8, 2) == [2, 4, 6, 8]

    # Arguments given in reverse order
    assert module_0.generate_integers(7, 3) == [4, 6]

    # Clamped by lower bound of 2
    assert module_0.generate_integers(1, 5) == [2, 4]
    assert module_0.generate_integers(9, 1) == [2, 4, 6, 8]

    # Clamped by upper bound of 8
    assert module_0.generate_integers(5, 12) == [6, 8]

    # No even numbers in range
    assert module_0.generate_integers(10, 14) == []
    assert module_0.generate_integers(1, 1) == []

    # Single-value ranges
    assert module_0.generate_integers(4, 4) == [4]
    assert module_0.generate_integers(2, 2) == [2]
    assert module_0.generate_integers(3, 3) == []

# Generated at 2026-11-02 16:10:07.235361
# Unit test for function generate_integers
def test_generate_integers():
    # Basic case: full valid range
    assert module_0.generate_integers(2, 8) == [2, 4, 6, 8]
    # Arguments in reverse order should yield same result
    assert module_0.generate_integers(8, 2) == [2, 4, 6, 8]
    # Range clamped to lower bound of 2
    assert module_0.generate_integers(1, 5) == [2, 4]
    assert module_0.generate_integers(5, 1) == [2, 4]
    # Range clamped to upper bound of 8
    assert module_0.generate_integers(6, 15) == [6, 8]
    assert module_0.generate_integers(15, 6) == [6, 8]
    # Both values below the valid range
    assert module_0.generate_integers(0, 1) == []
    # Both values above the valid range
    assert module_0.generate_integers(10, 14) == []
    # Partial overlap with valid range
    assert module_0.generate_integers(3, 7) == [4, 6]
    assert module_0.generate_integers(7, 3) == [4, 6]
    # Single value ranges
    assert module_0.generate_integers(2, 2) == [2]
    assert module_0.generate_integers(4, 4) == [4]
    assert module_0.generate_integers(5, 5) == []  # odd number, no evens
    assert module_0.generate_integers(9, 9) == []  # above upper clamp
    # Negative values
    assert module_0.generate_integers(-10, -5) == []
    assert module_0.generate_integers(-5, 3) == [2]
    # Boundary values of the clamp
    assert module_0.generate_integers(1, 8) == [2, 4, 6, 8]
    assert module_0.generate_integers(2, 9) == [2, 4, 6, 8]
    assert module_0.generate_integers(1, 9) == [2, 4, 6, 8]

    print("All tests passed!")


if __name__ == "__main__":
    test_generate_integers()

# Generated at 2026-11-02 16:10:30.265731
# Unit test for function generate_integers
def test_generate_integers():
    # Both bounds within [2, 8], ascending
    assert module_0.generate_integers(2, 8) == [2, 4, 6, 8]

    # Arguments reversed — order shouldn't matter
    assert module_0.generate_integers(8, 2) == [2, 4, 6, 8]

    # Lower bound below 2 gets clamped to 2
    assert module_0.generate_integers(1, 5) == [2, 4]
    assert module_0.generate_integers(0, 4) == [2, 4]

    # Upper bound above 8 gets clamped to 8
    assert module_0.generate_integers(6, 10) == [6, 8]

    # Both bounds outside range entirely
    assert module_0.generate_integers(10, 14) == []
    assert module_0.generate_integers(-5, 1) == []

    # Single value range
    assert module_0.generate_integers(2, 2) == [2]
    assert module_0.generate_integers(3, 3) == []
    assert module_0.generate_integers(4, 4) == [4]

    # Partial range containing mixed parity
    assert module_0.generate_integers(4, 7) == [4, 6]
    assert module_0.generate_integers(3, 9) == [4, 6, 8]

    print("All tests passed!")


test_generate_integers()

# Generated at 2026-11-02 16:10:50.767581
# Unit test for function generate_integers
def test_generate_integers():
    # Both values within the even range 2-8
    assert module_0.generate_integers(2, 8) == [2, 4, 6, 8]
    assert module_0.generate_integers(8, 2) == [2, 4, 6, 8]

    # Partial overlap with range
    assert module_0.generate_integers(1, 5) == [2, 4]
    assert module_0.generate_integers(5, 1) == [2, 4]

    # Clamped at both bounds
    assert module_0.generate_integers(1, 10) == [2, 4, 6, 8]
    assert module_0.generate_integers(0, 100) == [2, 4, 6, 8]

    # Range entirely above 8 -> empty
    assert module_0.generate_integers(10, 14) == []
    assert module_0.generate_integers(9, 9) == []

    # Range entirely below 2 -> empty
    assert module_0.generate_integers(0, 1) == []
    assert module_0.generate_integers(-5, 1) == []

    # Single value cases
    assert module_0.generate_integers(4, 4) == [4]
    assert module_0.generate_integers(2, 2) == [2]
    assert module_0.generate_integers(3, 3) == []  # odd single value
    assert module_0.generate_integers(7, 7) == []  # odd single value

    # Odd bounds: only evens in between
    assert module_0.generate_integers(3, 7) == [4, 6]
    assert module_0.generate_integers(7, 3) == [4, 6]

    # Negative and mixed bounds
    assert module_0.generate_integers(-10, -5) == []
    assert module_0.generate_integers(-2, 3) == [2]

    print("All tests passed!")


if __name__ == "__main__":
    test_generate_integers()

# Generated at 2026-11-02 16:11:01.590881
# Unit test for function generate_integers
def test_generate_integers():
    # Basic case: full valid range
    assert module_0.generate_integers(2, 8) == [2, 4, 6, 8]
    
    # Arguments in reverse order
    assert module_0.generate_integers(8, 2) == [2, 4, 6, 8]
    
    # Range clipped at upper bound (8)
    assert module_0.generate_integers(4, 12) == [4, 6, 8]
    assert module_0.generate_integers(12, 4) == [4, 6, 8]
    
    # Range clipped at lower bound (2)
    assert module_0.generate_integers(0, 5) == [2, 4]
    assert module_0.generate_integers(5, 0) == [2, 4]
    
    # Range entirely above 8 — empty result
    assert module_0.generate_integers(10, 14) == []
    
    # Range entirely below 2 — empty result
    assert module_0.generate_integers(0, 1) == []
    
    # Single valid even number
    assert module_0.generate_integers(2, 2) == [2]
    
    # Single valid odd number — empty result
    assert module_0.generate_integers(3, 3) == []
    
    # Mixed range with odd bounds
    assert module_0.generate_integers(3, 7) == [4, 6]
    assert module_0.generate_integers(7, 3) == [4, 6]
    
    # Negative bounds clipped to 2
    assert module_0.generate_integers(-5, 3) == [2]
    
    # Wide range fully covering bounds
    assert module_0.generate_integers(-10, 100) == [2, 4, 6, 8]
    
    print("All tests passed!")


if __name__ == "__main__":
    test_generate_integers()