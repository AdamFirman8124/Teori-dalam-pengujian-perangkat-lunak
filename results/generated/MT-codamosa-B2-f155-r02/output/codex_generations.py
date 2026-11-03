

# Generated at 2026-11-02 21:45:43.511454
# Unit test for function even_odd_count
def test_even_odd_count():
    # Test with positive number
    assert module_0.even_odd_count(123) == (1, 2), "Failed for positive number 123"
    # Test with negative number
    assert module_0.even_odd_count(-12) == (1, 1), "Failed for negative number -12"
    # Test with zero
    assert module_0.even_odd_count(0) == (1, 0), "Failed for zero"
    # Test with all even digits
    assert module_0.even_odd_count(2468) == (4, 0), "Failed for all even digits 2468"
    # Test with all odd digits
    assert module_0.even_odd_count(1357) == (0, 4), "Failed for all odd digits 1357"
    # Test with negative number containing zero
    assert module_0.even_odd_count(-102) == (2, 1), "Failed for -102"
    # Test with single digit
    assert module_0.even_odd_count(7) == (0, 1), "Failed for single odd digit"
    assert module_0.even_odd_count(8) == (1, 0), "Failed for single even digit"
    # Test with large number
    assert module_0.even_odd_count(1000000) == (7, 0), "Failed for 1000000"
    print("All tests passed!")

test_even_odd_count()

# Generated at 2026-11-02 21:47:36.491351
# Unit test for function even_odd_count
def test_even_odd_count():
    # Test positive number with mixed digits
    assert module_0.even_odd_count(123) == (1, 2), "Expected (1, 2) for 123"
    
    # Test negative number with mixed digits
    assert module_0.even_odd_count(-1234) == (2, 2), "Expected (2, 2) for -1234"
    
    # Test zero
    assert module_0.even_odd_count(0) == (1, 0), "Expected (1, 0) for 0"
    
    # Test negative zero
    assert module_0.even_odd_count(-0) == (1, 0), "Expected (1, 0) for -0"
    
    # Test all even digits
    assert module_0.even_odd_count(2468) == (4, 0), "Expected (4, 0) for 2468"
    
    # Test all odd digits
    assert module_0.even_odd_count(1357) == (0, 4), "Expected (0, 4) for 1357"
    
    # Test negative number with all odd digits
    assert module_0.even_odd_count(-135) == (0, 3), "Expected (0, 3) for -135"
    
    # Test single even digit
    assert module_0.even_odd_count(2) == (1, 0), "Expected (1, 0) for 2"
    
    # Test single odd digit
    assert module_0.even_odd_count(7) == (0, 1), "Expected (0, 1) for 7"
    
    # Test negative single digit
    assert module_0.even_odd_count(-8) == (1, 0), "Expected (1, 0) for -8"
    
    # Test larger number
    assert module_0.even_odd_count(1029384756) == (5, 5), "Expected (5, 5) for 1029384756"
    
    # Test that result is a tuple
    result = module_0.even_odd_count(1234)
    assert isinstance(result, tuple), "Result should be a tuple"
    assert len(result) == 2, "Result tuple should have 2 elements"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_even_odd_count()

# Generated at 2026-11-02 21:48:44.778423
# Unit test for function even_odd_count
def test_even_odd_count():
    # Basic positive number with mixed digits
    assert module_0.even_odd_count(123) == (1, 2)
    assert module_0.even_odd_count(123456) == (3, 3)
    
    # Negative numbers (abs applied)
    assert module_0.even_odd_count(-12) == (1, 1)
    assert module_0.even_odd_count(-123) == (1, 2)
    
    # Zero is even
    assert module_0.even_odd_count(0) == (1, 0)
    
    # All even digits
    assert module_0.even_odd_count(2468) == (4, 0)
    assert module_0.even_odd_count(-246) == (3, 0)
    
    # All odd digits
    assert module_0.even_odd_count(1357) == (0, 4)
    assert module_0.even_odd_count(-135) == (0, 3)
    
    # Digits with zeros
    assert module_0.even_odd_count(1000) == (3, 1)
    assert module_0.even_odd_count(105) == (2, 1)
    
    # Single digit numbers
    assert module_0.even_odd_count(7) == (0, 1)
    assert module_0.even_odd_count(8) == (1, 0)
    assert module_0.even_odd_count(-9) == (0, 1)
    
    # Result is a tuple
    assert isinstance(module_0.even_odd_count(123), tuple)
    
    print("All tests passed!")

test_even_odd_count()

# Generated at 2026-11-02 21:50:06.711261
# Unit test for function even_odd_count
def test_even_odd_count():
    # Test with mixed even and odd positive number
    assert module_0.even_odd_count(123) == (1, 2)
    
    # Test with negative number (abs handles sign)
    assert module_0.even_odd_count(-12) == (1, 1)
    
    # Test with all even digits
    assert module_0.even_odd_count(2468) == (4, 0)
    
    # Test with all odd digits
    assert module_0.even_odd_count(13579) == (0, 5)
    
    # Test with zero
    assert module_0.even_odd_count(0) == (1, 0)
    
    # Test with negative number containing only even digits
    assert module_0.even_odd_count(-2046) == (4, 0)
    
    # Test with single odd digit
    assert module_0.even_odd_count(7) == (0, 1)
    
    # Test with single even digit
    assert module_0.even_odd_count(8) == (1, 0)
    
    # Test with negative single odd digit
    assert module_0.even_odd_count(-3) == (0, 1)
    
    # Test with larger multi-digit number
    assert module_0.even_odd_count(1029384756) == (5, 5)
    
    print("All test cases passed!")

# Run the tests
test_even_odd_count()

# Generated at 2026-11-02 21:51:43.672668
# Unit test for function even_odd_count
def test_even_odd_count():
    assert module_0.even_odd_count(-12) == (1, 1)
    assert module_0.even_odd_count(123) == (1, 2)
    assert module_0.even_odd_count(0) == (1, 0)
    assert module_0.even_odd_count(-2468) == (4, 0)
    assert module_0.even_odd_count(1357) == (0, 4)
    assert module_0.even_odd_count(100) == (2, 1)
    assert module_0.even_odd_count(7) == (0, 1)
    assert module_0.even_odd_count(-8) == (1, 0)
    assert module_0.even_odd_count(24680) == (5, 0)
    assert module_0.even_odd_count(-13579) == (0, 5)