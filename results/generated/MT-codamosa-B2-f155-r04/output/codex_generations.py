

# Generated at 2026-11-02 11:42:54.440193
# Unit test for function even_odd_count
def test_even_odd_count():
    # Basic mixed digits
    assert module_0.even_odd_count(123456) == (3, 3)
    assert module_0.even_odd_count(12) == (1, 1)
    assert module_0.even_odd_count(101) == (2, 1)

    # Negative numbers (uses abs)
    assert module_0.even_odd_count(-12) == (1, 1)
    assert module_0.even_odd_count(-135) == (0, 3)
    assert module_0.even_odd_count(-2468) == (4, 0)

    # Zero
    assert module_0.even_odd_count(0) == (1, 0)
    assert module_0.even_odd_count(-0) == (1, 0)

    # All even digits
    assert module_0.even_odd_count(2468) == (4, 0)
    assert module_0.even_odd_count(0) == (1, 0)

    # All odd digits
    assert module_0.even_odd_count(13579) == (0, 5)

    # Single digit
    assert module_0.even_odd_count(7) == (0, 1)
    assert module_0.even_odd_count(8) == (1, 0)

    # Large numbers
    assert module_0.even_odd_count(1029384756) == (5, 5)
    assert module_0.even_odd_count(9876543210) == (5, 5)

    # Return type check
    result = module_0.even_odd_count(1234)
    assert isinstance(result, tuple)
    assert len(result) == 2

    print("All tests passed!")

test_even_odd_count()

# Generated at 2026-11-02 11:44:25.110606
# Unit test for function even_odd_count
def test_even_odd_count():
    # Basic positive number
    assert module_0.even_odd_count(123) == (1, 2)      # digits: 1(odd), 2(even), 3(odd)
    
    # Negative number (abs should be applied)
    assert module_0.even_odd_count(-12) == (1, 1)      # digits: 1(odd), 2(even)
    
    # Zero case
    assert module_0.even_odd_count(0) == (1, 0)        # digit: 0(even)
    
    # All even digits
    assert module_0.even_odd_count(2468) == (4, 0)
    
    # All odd digits
    assert module_0.even_odd_count(1357) == (0, 4)
    
    # Negative number with all even digits
    assert module_0.even_odd_count(-8642) == (4, 0)
    
    # Single digit
    assert module_0.even_odd_count(5) == (0, 1)
    assert module_0.even_odd_count(-4) == (1, 0)
    
    # Number with repeated digits
    assert module_0.even_odd_count(111) == (0, 3)
    assert module_0.even_odd_count(222) == (3, 0)
    
    # Mixed digits with zeros
    assert module_0.even_odd_count(100) == (2, 1)      # digits: 1(odd), 0(even), 0(even)
    assert module_0.even_odd_count(-305) == (1, 2)     # digits: 3(odd), 0(even), 5(odd)
    
    print("All tests passed!")

# Run the tests
if __name__ == "__main__":
    test_even_odd_count()

# Generated at 2026-11-02 11:45:32.385307
# Unit test for function even_odd_count
def test_even_odd_count():
    # Test with positive number
    assert module_0.even_odd_count(123) == (1, 2)      # even: 2, odd: 1,3
    assert module_0.even_odd_count(2468) == (4, 0)     # all even digits
    assert module_0.even_odd_count(1357) == (0, 4)     # all odd digits
    
    # Test with negative number (should use absolute value)
    assert module_0.even_odd_count(-12) == (1, 1)
    assert module_0.even_odd_count(-2468) == (4, 0)
    assert module_0.even_odd_count(-1357) == (0, 4)
    
    # Test with zero
    assert module_0.even_odd_count(0) == (1, 0)        # 0 is even
    
    # Test with repeated digits
    assert module_0.even_odd_count(1000) == (3, 1)
    assert module_0.even_odd_count(111) == (0, 3)
    
    # Test with mixed digits
    assert module_0.even_odd_count(50239) == (2, 3)    # even: 5->no, 0,2 yes; odd: 5,3,9
    assert module_0.even_odd_count(9876543210) == (5, 5)
    
    # Test result type
    result = module_0.even_odd_count(42)
    assert isinstance(result, tuple)
    assert len(result) == 2
    
    print("All tests passed!")

test_even_odd_count()

# Generated at 2026-11-02 11:47:59.796476
# Unit test for function even_odd_count
def test_even_odd_count():
    # Mixed even and odd digits
    assert module_0.even_odd_count(123) == (1, 2)
    assert module_0.even_odd_count(1234) == (2, 2)
    assert module_0.even_odd_count(12) == (1, 1)

    # Negative numbers (abs applied)
    assert module_0.even_odd_count(-12) == (1, 1)
    assert module_0.even_odd_count(-1234) == (2, 2)
    assert module_0.even_odd_count(-135) == (0, 3)

    # Zero is even
    assert module_0.even_odd_count(0) == (1, 0)
    assert module_0.even_odd_count(-0) == (1, 0)

    # All even digits
    assert module_0.even_odd_count(2468) == (4, 0)
    assert module_0.even_odd_count(-8642) == (4, 0)

    # All odd digits
    assert module_0.even_odd_count(1357) == (0, 4)
    assert module_0.even_odd_count(-97531) == (0, 5)

    # Single digit
    assert module_0.even_odd_count(2) == (1, 0)
    assert module_0.even_odd_count(7) == (0, 1)
    assert module_0.even_odd_count(-5) == (0, 1)

    # Larger numbers
    assert module_0.even_odd_count(1000000) == (7, 0)
    assert module_0.even_odd_count(9876543210) == (5, 5)

    # Return type is a tuple
    assert isinstance(module_0.even_odd_count(123), tuple)

# Generated at 2026-11-02 11:49:46.643132
# Unit test for function even_odd_count
def test_even_odd_count():
    # Mixed even and odd digits
    assert module_0.even_odd_count(-12) == (1, 1)      # digits: 1(odd), 2(even)
    assert module_0.even_odd_count(123) == (1, 2)      # digits: 1(odd), 2(even), 3(odd)

    # Negative numbers (abs should be applied)
    assert module_0.even_odd_count(-123) == (1, 2)
    assert module_0.even_odd_count(-2468) == (4, 0)

    # All even digits
    assert module_0.even_odd_count(2468) == (4, 0)
    assert module_0.even_odd_count(0) == (1, 0)        # 0 is even

    # All odd digits
    assert module_0.even_odd_count(1357) == (0, 4)
    assert module_0.even_odd_count(-13579) == (0, 5)

    # Single digit inputs
    assert module_0.even_odd_count(2) == (1, 0)
    assert module_0.even_odd_count(7) == (0, 1)

    print("All test cases passed!")

test_even_odd_count()