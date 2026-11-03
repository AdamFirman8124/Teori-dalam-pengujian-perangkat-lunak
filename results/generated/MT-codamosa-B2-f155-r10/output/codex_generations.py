

# Generated at 2026-11-02 21:13:45.619858
# Unit test for function even_odd_count
def test_even_odd_count():
    # Mixed even and odd digits
    assert module_0.even_odd_count(123456) == (3, 3)
    assert module_0.even_odd_count(-123456) == (3, 3)  # negative number handled via abs

    # All even digits
    assert module_0.even_odd_count(2468) == (4, 0)
    assert module_0.even_odd_count(-24680) == (5, 0)

    # All odd digits
    assert module_0.even_odd_count(1357) == (0, 4)
    assert module_0.even_odd_count(-13579) == (0, 5)

    # Single digit cases
    assert module_0.even_odd_count(0) == (1, 0)
    assert module_0.even_odd_count(2) == (1, 0)
    assert module_0.even_odd_count(3) == (0, 1)
    assert module_0.even_odd_count(-7) == (0, 1)

    # Numbers with zeros
    assert module_0.even_odd_count(1001) == (3, 1)
    assert module_0.even_odd_count(-2000) == (4, 0)

    # Large number
    assert module_0.even_odd_count(9876543210) == (5, 5)

    print("All test cases passed!")


if __name__ == "__main__":
    test_even_odd_count()

# Generated at 2026-11-02 21:14:26.846185
# Unit test for function even_odd_count
def test_even_odd_count():
    # Positive number with mixed even and odd digits
    assert module_0.even_odd_count(123) == (1, 2)          # digits: 1(odd), 2(even), 3(odd)
    assert module_0.even_odd_count(2468) == (4, 0)         # all even digits
    assert module_0.even_odd_count(1357) == (0, 4)         # all odd digits
    
    # Negative number (absolute value should be used)
    assert module_0.even_odd_count(-12) == (1, 1)          # digits: 1(odd), 2(even)
    assert module_0.even_odd_count(-1357) == (0, 4)
    assert module_0.even_odd_count(-246) == (3, 0)
    
    # Zero is even
    assert module_0.even_odd_count(0) == (1, 0)
    
    # Single digit numbers
    assert module_0.even_odd_count(2) == (1, 0)
    assert module_0.even_odd_count(7) == (0, 1)
    
    # Larger numbers
    assert module_0.even_odd_count(1020304) == (4, 3)      # evens: 0,2,0,4; odds: 1,3
    assert module_0.even_odd_count(-9876543210) == (5, 5)  # evens: 8,6,4,2,0; odds: 9,7,5,3,1
    
    # Repeated digits
    assert module_0.even_odd_count(111) == (0, 3)
    assert module_0.even_odd_count(222) == (3, 0)
    
    print("All test cases passed!")


test_even_odd_count()

# Generated at 2026-11-02 21:15:24.468348
# Unit test for function even_odd_count
def test_even_odd_count():
    # Mixed even and odd digits
    assert module_0.even_odd_count(123) == (1, 2)
    assert module_0.even_odd_count(1234) == (2, 2)

    # Negative numbers (abs applied)
    assert module_0.even_odd_count(-12) == (1, 1)
    assert module_0.even_odd_count(-2468) == (4, 0)

    # All even digits
    assert module_0.even_odd_count(2468) == (4, 0)

    # All odd digits
    assert module_0.even_odd_count(1357) == (0, 4)

    # Zero (0 is even)
    assert module_0.even_odd_count(0) == (1, 0)

    # Single digit numbers
    assert module_0.even_odd_count(7) == (0, 1)
    assert module_0.even_odd_count(8) == (1, 0)

    # Negative zero edge case
    assert module_0.even_odd_count(-0) == (1, 0)

    print("All tests passed!")


if __name__ == "__main__":
    test_even_odd_count()

# Generated at 2026-11-02 21:16:35.346396
# Unit test for function even_odd_count
def test_even_odd_count():
    # Test with a mixed even/odd digit number
    assert module_0.even_odd_count(-12) == (1, 1)
    assert module_0.even_odd_count(123) == (1, 2)
    assert module_0.even_odd_count(1230) == (2, 2)

    # Test with negative numbers (abs should be applied)
    assert module_0.even_odd_count(-123) == (1, 2)
    assert module_0.even_odd_count(-2468) == (4, 0)

    # Test with all even digits
    assert module_0.even_odd_count(2468) == (4, 0)
    assert module_0.even_odd_count(0) == (1, 0)

    # Test with all odd digits
    assert module_0.even_odd_count(1357) == (0, 4)
    assert module_0.even_odd_count(-135) == (0, 3)

    # Test with single digit numbers
    assert module_0.even_odd_count(2) == (1, 0)
    assert module_0.even_odd_count(7) == (0, 1)
    assert module_0.even_odd_count(-9) == (0, 1)

    # Test with large numbers
    assert module_0.even_odd_count(1029384756) == (5, 5)

    print("All tests passed!")


if __name__ == "__main__":
    test_even_odd_count()

# Generated at 2026-11-02 21:17:21.831678
# Unit test for function even_odd_count
def test_even_odd_count():
    # Positive number with mixed digits
    assert module_0.even_odd_count(123) == (1, 2)  # 1 is odd, 2 is even, 3 is odd... wait: evens: 2 -> 1; odds: 1,3 -> 2
    # Actually: digits 1,2,3 -> even: 1 (the digit 2), odd: 2 (digits 1 and 3)
    assert module_0.even_odd_count(123) == (1, 2)

    # Negative number - abs should be applied
    assert module_0.even_odd_count(-12) == (1, 1)  # digits 1 (odd), 2 (even)

    # Zero is even
    assert module_0.even_odd_count(0) == (1, 0)

    # All even digits
    assert module_0.even_odd_count(2468) == (4, 0)
    assert module_0.even_odd_count(-2468) == (4, 0)

    # All odd digits
    assert module_0.even_odd_count(1357) == (0, 4)
    assert module_0.even_odd_count(-13579) == (0, 5)

    # Repeated digits including zero
    assert module_0.even_odd_count(1000) == (3, 1)  # 1 odd, three 0s even

    # Single digit
    assert module_0.even_odd_count(7) == (0, 1)
    assert module_0.even_odd_count(8) == (1, 0)

    # Larger mixed number
    assert module_0.even_odd_count(4829130) == (4, 3)  # evens: 4,8,2,0 ; odds: 9,1,3

    # Result is a tuple
    result = module_0.even_odd_count(1234)
    assert isinstance(result, tuple)
    assert len(result) == 2