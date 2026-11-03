

# Generated at 2026-11-01 20:56:16.192001
# Unit test for function even_odd_count
def test_even_odd_count():
    # nonce:9dc6f073
    assert module_0.even_odd_count(-12) == (1, 1)
    assert module_0.even_odd_count(123) == (1, 2)
    assert module_0.even_odd_count(0) == (1, 0)
    assert module_0.even_odd_count(-123) == (1, 2)
    assert module_0.even_odd_count(123456789) == (4, 5)
    assert module_0.even_odd_count(2468) == (4, 0)
    assert module_0.even_odd_count(13579) == (0, 5)
    assert module_0.even_odd_count(-2468) == (4, 0)
    assert module_0.even_odd_count(100) == (2, 1)
    assert module_0.even_odd_count(-7) == (0, 1)
    assert module_0.even_odd_count(7) == (0, 1)
    assert module_0.even_odd_count(222222) == (6, 0)

# Generated at 2026-11-01 20:56:32.113502
# Unit test for function even_odd_count
def test_even_odd_count():
    # Test with a positive number containing both even and odd digits
    assert module_0.even_odd_count(123456) == (3, 3)
    
    # Test with a number containing only even digits
    assert module_0.even_odd_count(2468) == (4, 0)
    
    # Test with a number containing only odd digits
    assert module_0.even_odd_count(1357) == (0, 4)
    
    # Test with zero (0 is even)
    assert module_0.even_odd_count(0) == (1, 0)
    
    # Test with a negative number (abs value should be used)
    assert module_0.even_odd_count(-123456) == (3, 3)
    
    # Test with a single even digit
    assert module_0.even_odd_count(4) == (1, 0)
    
    # Test with a single odd digit
    assert module_0.even_odd_count(7) == (0, 1)
    
    # Test with a negative single digit
    assert module_0.even_odd_count(-9) == (0, 1)
    
    # Test with a large number
    assert module_0.even_odd_count(1234567890) == (5, 5)
    
    # Test with repeated digits
    assert module_0.even_odd_count(2222) == (4, 0)
    assert module_0.even_odd_count(1111) == (0, 4)
    
    # Test with a negative number with only even digits
    assert module_0.even_odd_count(-8642) == (4, 0)
    
    # Test with a negative number with only odd digits
    assert module_0.even_odd_count(-9753) == (0, 4)
    
    # Test with mixed digits including zero
    assert module_0.even_odd_count(105) == (2, 1)
    
    print("All tests passed!")


test_even_odd_count()

# Generated at 2026-11-01 20:56:58.139804
# Unit test for function even_odd_count
def test_even_odd_count():
    assert module_0.even_odd_count(-12) == (1, 1)
    assert module_0.even_odd_count(123) == (1, 2)
    assert module_0.even_odd_count(0) == (1, 0)
    assert module_0.even_odd_count(2468) == (4, 0)
    assert module_0.even_odd_count(1357) == (0, 4)
    assert module_0.even_odd_count(-2468) == (4, 0)
    assert module_0.even_odd_count(1000000) == (7, 0)
    assert module_0.even_odd_count(-999) == (0, 3)
    assert module_0.even_odd_count(5050) == (3, 1)

# Generated at 2026-11-01 20:57:25.339999
# Unit test for function even_odd_count
def test_even_odd_count():
    # Mixed even and odd digits
    assert module_0.even_odd_count(123) == (1, 2)
    assert module_0.even_odd_count(-12) == (1, 1)   # negative number handled via abs
    assert module_0.even_odd_count(5023) == (2, 2)

    # All even digits
    assert module_0.even_odd_count(2468) == (4, 0)
    assert module_0.even_odd_count(0) == (1, 0)     # zero counts as even

    # All odd digits
    assert module_0.even_odd_count(1357) == (0, 4)
    assert module_0.even_odd_count(-111) == (0, 3)

    # Single digit cases
    assert module_0.even_odd_count(4) == (1, 0)
    assert module_0.even_odd_count(7) == (0, 1)
    assert module_0.even_odd_count(-8) == (1, 0)

    # Larger numbers
    assert module_0.even_odd_count(1000000) == (7, 0)
    assert module_0.even_odd_count(9876543210) == (5, 5)

    print("All tests passed!")

test_even_odd_count()

# Generated at 2026-11-01 20:58:04.930359
# Unit test for function even_odd_count
def test_even_odd_count():
    # Mixed even and odd digits
    assert module_0.even_odd_count(123456) == (3, 3)
    assert module_0.even_odd_count(12) == (1, 1)
    assert module_0.even_odd_count(123) == (1, 2)

    # Negative numbers (sign should be ignored)
    assert module_0.even_odd_count(-12) == (1, 1)
    assert module_0.even_odd_count(-123456) == (3, 3)

    # Zero (single even digit)
    assert module_0.even_odd_count(0) == (1, 0)

    # All even digits
    assert module_0.even_odd_count(2468) == (4, 0)
    assert module_0.even_odd_count(-246) == (3, 0)

    # All odd digits
    assert module_0.even_odd_count(1357) == (0, 4)
    assert module_0.even_odd_count(-135) == (0, 3)

    # Large number
    assert module_0.even_odd_count(1000000) == (7, 0)

    # Result should be a tuple
    result = module_0.even_odd_count(1234)
    assert isinstance(result, tuple)
    assert len(result) == 2

    print("All test_even_odd_count tests passed!")


if __name__ == "__main__":
    test_even_odd_count()