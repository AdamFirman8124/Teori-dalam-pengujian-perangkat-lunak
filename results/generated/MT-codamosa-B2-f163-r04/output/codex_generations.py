

# Generated at 2026-11-02 17:07:48.991369
# Unit test for function generate_integers
def test_generate_integers():
    # Both bounds within [2, 8], full even range
    assert module_0.generate_integers(2, 8) == [2, 4, 6, 8]

    # Arguments reversed, same result
    assert module_0.generate_integers(8, 2) == [2, 4, 6, 8]

    # Range partially below lower clamp of 2
    assert module_0.generate_integers(1, 5) == [2, 4]
    assert module_0.generate_integers(0, 7) == [2, 4, 6]

    # Range partially above upper clamp of 8
    assert module_0.generate_integers(6, 18) == [6, 8]
    assert module_0.generate_integers(10, 3) == [4, 6, 8]

    # Range entirely outside [2, 8] yields empty list
    assert module_0.generate_integers(10, 14) == []
    assert module_0.generate_integers(0, 0) == []
    assert module_0.generate_integers(9, 20) == []

    # Single-value ranges
    assert module_0.generate_integers(2, 2) == [2]
    assert module_0.generate_integers(4, 4) == [4]
    assert module_0.generate_integers(3, 3) == []  # odd value filtered out

    # Only odd numbers in range
    assert module_0.generate_integers(3, 5) == []

    # Negative bounds clamped to 2
    assert module_0.generate_integers(-5, 4) == [2, 4]

# Generated at 2026-11-02 17:08:06.591158
# Unit test for function generate_integers
def test_generate_integers():
    # Both values within range, a < b
    assert module_0.generate_integers(2, 8) == [2, 4, 6, 8]
    # Both values within range, a > b (order shouldn't matter)
    assert module_0.generate_integers(8, 2) == [2, 4, 6, 8]
    # Range clamped at lower bound 2
    assert module_0.generate_integers(1, 5) == [2, 4]
    assert module_0.generate_integers(5, 1) == [2, 4]
    # Range clamped at upper bound 8
    assert module_0.generate_integers(7, 20) == [8]
    # Both values above 8 -> empty list
    assert module_0.generate_integers(10, 14) == []
    assert module_0.generate_integers(14, 10) == []
    # Both values below 2 -> clamped to 2
    assert module_0.generate_integers(0, 1) == [2]
    # Single even value
    assert module_0.generate_integers(4, 4) == [4]
    # Single odd value -> empty list
    assert module_0.generate_integers(3, 3) == []
    # Boundary: only even numbers included
    assert module_0.generate_integers(3, 7) == [4, 6]
    # Negative values clamped to 2
    assert module_0.generate_integers(-5, 3) == [2]

    print("All tests passed!")


if __name__ == "__main__":
    test_generate_integers()

# Generated at 2026-11-02 17:08:22.924137
# Unit test for function generate_integers
def test_generate_integers():
    assert module_0.generate_integers(2, 8) == [2, 4, 6, 8]
    assert module_0.generate_integers(8, 2) == [2, 4, 6, 8]
    assert module_0.generate_integers(10, 14) == []
    assert module_0.generate_integers(14, 10) == []
    assert module_0.generate_integers(1, 5) == [2, 4]
    assert module_0.generate_integers(5, 1) == [2, 4]
    assert module_0.generate_integers(3, 3) == []
    assert module_0.generate_integers(4, 4) == [4]
    assert module_0.generate_integers(2, 2) == [2]
    assert module_0.generate_integers(7, 7) == []
    assert module_0.generate_integers(9, 9) == []
    assert module_0.generate_integers(0, 2) == [2]
    assert module_0.generate_integers(0, 10) == [2, 4, 6, 8]
    assert module_0.generate_integers(-2, 3) == [2]

# Generated at 2026-11-02 17:08:40.861269
# Unit test for function generate_integers
def test_generate_integers():
    # Both bounds within range, ordered
    assert module_0.generate_integers(2, 8) == [2, 4, 6, 8]
    
    # Reversed arguments should give same result
    assert module_0.generate_integers(8, 2) == [2, 4, 6, 8]
    
    # Partially below lower bound of 2
    assert module_0.generate_integers(1, 5) == [2, 4]
    
    # Partially above upper bound of 8
    assert module_0.generate_integers(7, 15) == [8]
    
    # Both bounds above 8 -> empty
    assert module_0.generate_integers(10, 20) == []
    
    # Both bounds below 2 -> empty
    assert module_0.generate_integers(-3, 1) == []
    
    # Single value, even
    assert module_0.generate_integers(4, 4) == [4]
    
    # Single value, odd -> empty
    assert module_0.generate_integers(3, 3) == []
    assert module_0.generate_integers(5, 5) == []
    
    # Single value at boundary
    assert module_0.generate_integers(2, 2) == [2]
    assert module_0.generate_integers(8, 8) == [8]
    
    # No even numbers in interval
    assert module_0.generate_integers(3, 3) == []
    
    # Interval with one even number
    assert module_0.generate_integers(5, 7) == [6]
    
    # Negative inputs clamped
    assert module_0.generate_integers(-10, -5) == []
    
    print("All tests passed!")


if __name__ == "__main__":
    test_generate_integers()

# Generated at 2026-11-02 17:09:09.714204
# Unit test for function generate_integers
def test_generate_integers():
    assert module_0.generate_integers(2, 8) == [2, 4, 6, 8]
    assert module_0.generate_integers(8, 2) == [2, 4, 6, 8]
    assert module_0.generate_integers(1, 5) == [2, 4]
    assert module_0.generate_integers(3, 3) == []
    assert module_0.generate_integers(10, 14) == []
    assert module_0.generate_integers(0, 0) == []
    assert module_0.generate_integers(-2, 5) == [2, 4]
    print("All tests passed!")