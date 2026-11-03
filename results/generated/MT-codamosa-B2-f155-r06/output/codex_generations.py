

# Generated at 2026-11-02 17:54:03.725757
# Unit test for function even_odd_count
def test_even_odd_count():
    # Test with mixed even and odd digits
    assert module_0.even_odd_count(123) == (1, 2)  # 1 odd, 2 even, 3 odd
    assert module_0.even_odd_count(-12) == (1, 1)  # negative number: 1 odd, 2 even
    
    # Test with zero
    assert module_0.even_odd_count(0) == (1, 0)  # 0 is even
    
    # Test with all even digits
    assert module_0.even_odd_count(2468) == (4, 0)
    assert module_0.even_odd_count(-24680) == (5, 0)  # includes 0 as even
    
    # Test with all odd digits
    assert module_0.even_odd_count(1357) == (0, 4)
    assert module_0.even_odd_count(-999) == (0, 3)
    
    # Test with single digits
    assert module_0.even_odd_count(7) == (0, 1)
    assert module_0.even_odd_count(8) == (1, 0)
    
    # Test with repeated digits
    assert module_0.even_odd_count(1000) == (3, 1)  # 1 odd, three 0s even
    
    # Test with large numbers
    assert module_0.even_odd_count(1234567890) == (5, 5)
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_even_odd_count()

# Generated at 2026-11-02 17:55:19.034277
# Unit test for function even_odd_count
def test_even_odd_count():
    assert module_0.even_odd_count(-12) == (1, 1)
    assert module_0.even_odd_count(123) == (1, 2)
    assert module_0.even_odd_count(0) == (1, 0)
    assert module_0.even_odd_count(2468) == (4, 0)
    assert module_0.even_odd_count(1357) == (0, 4)
    assert module_0.even_odd_count(-2468) == (4, 0)
    assert module_0.even_odd_count(-13579) == (0, 5)
    assert module_0.even_odd_count(100) == (2, 1)
    assert module_0.even_odd_count(7) == (0, 1)
    assert module_0.even_odd_count(-8) == (1, 0)
    assert module_0.even_odd_count(1029384756) == (5, 5)

# Generated at 2026-11-02 17:56:49.533804
# Unit test for function even_odd_count
def test_even_odd_count():
    # Mixed even and odd digits
    assert module_0.even_odd_count(-12) == (1, 1)
    assert module_0.even_odd_count(123) == (1, 2)
    assert module_0.even_odd_count(1230) == (2, 2)

    # Zero is even
    assert module_0.even_odd_count(0) == (1, 0)

    # All even digits
    assert module_0.even_odd_count(2468) == (4, 0)
    assert module_0.even_odd_count(-2468) == (4, 0)

    # All odd digits
    assert module_0.even_odd_count(1357) == (0, 4)
    assert module_0.even_odd_count(-1357) == (0, 4)

    # Single digit
    assert module_0.even_odd_count(2) == (1, 0)
    assert module_0.even_odd_count(7) == (0, 1)
    assert module_0.even_odd_count(-7) == (0, 1)

    # Negative numbers use absolute value
    assert module_0.even_odd_count(-1000) == (3, 1)
    assert module_0.even_odd_count(-505) == (2, 1)

    print("All tests passed!")


test_even_odd_count()

# Generated at 2026-11-02 17:58:21.492178
# Unit test for function even_odd_count
def test_even_odd_count():
    assert module_0.even_odd_count(-12) == (1, 1)
    assert module_0.even_odd_count(123) == (1, 2)
    assert module_0.even_odd_count(0) == (1, 0)
    assert module_0.even_odd_count(2468) == (4, 0)
    assert module_0.even_odd_count(1357) == (0, 4)
    assert module_0.even_odd_count(-1357) == (0, 4)
    assert module_0.even_odd_count(100) == (2, 1)
    assert module_0.even_odd_count(-100) == (2, 1)
    assert module_0.even_odd_count(7) == (0, 1)
    assert module_0.even_odd_count(1020304) == (4, 3)

# Generated at 2026-11-02 17:59:57.664490
# Unit test for function even_odd_count
def test_even_odd_count():
    # Mixed even and odd digits
    assert module_0.even_odd_count(-12) == (1, 1)
    assert module_0.even_odd_count(123) == (1, 2)
    assert module_0.even_odd_count(1230) == (2, 2)

    # Negative numbers (abs should be applied)
    assert module_0.even_odd_count(-123) == (1, 2)
    assert module_0.even_odd_count(-2468) == (4, 0)

    # All even digits
    assert module_0.even_odd_count(2468) == (4, 0)
    assert module_0.even_odd_count(0) == (1, 0)

    # All odd digits
    assert module_0.even_odd_count(1357) == (0, 4)
    assert module_0.even_odd_count(1) == (0, 1)

    # Single digits
    assert module_0.even_odd_count(2) == (1, 0)
    assert module_0.even_odd_count(3) == (0, 1)
    assert module_0.even_odd_count(-7) == (0, 1)

    # Large numbers
    assert module_0.even_odd_count(9876543210) == (5, 5)

    print("All tests passed!")


test_even_odd_count()