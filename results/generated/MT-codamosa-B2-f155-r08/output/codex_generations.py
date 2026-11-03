

# Generated at 2026-11-03 04:40:38.089626
# Unit test for function even_odd_count
def test_even_odd_count():
    # Test positive number with mixed digits
    assert module_0.even_odd_count(123) == (1, 2)
    # Test negative number (abs should handle sign)
    assert module_0.even_odd_count(-123) == (1, 2)
    # Test zero (0 is even)
    assert module_0.even_odd_count(0) == (1, 0)
    # Test all even digits
    assert module_0.even_odd_count(2468) == (4, 0)
    # Test all odd digits
    assert module_0.even_odd_count(1357) == (0, 4)
    # Test mixed digits
    assert module_0.even_odd_count(1234567) == (3, 4)
    # Test single odd digit
    assert module_0.even_odd_count(7) == (0, 1)
    # Test single even digit
    assert module_0.even_odd_count(8) == (1, 0)
    # Test negative number with even digits
    assert module_0.even_odd_count(-2468) == (4, 0)
    # Test number containing zero digit
    assert module_0.even_odd_count(102) == (2, 1)
    # Test larger number
    assert module_0.even_odd_count(1000000) == (7, 0)
    # Test return type is tuple
    assert isinstance(module_0.even_odd_count(123), tuple)
    # Test tuple length is 2
    assert len(module_0.even_odd_count(123)) == 2
    # Test counts sum equals number of digits
    result = module_0.even_odd_count(98765)
    assert result == (2, 3)
    assert result[0] + result[1] == 5
    print("All test cases passed!")

test_even_odd_count()

# Generated at 2026-11-03 04:42:34.573023
# Unit test for function even_odd_count
def test_even_odd_count():
    # Positive number with mixed digits
    assert module_0.even_odd_count(123) == (1, 2)
    # Negative number with mixed digits
    assert module_0.even_odd_count(-12) == (1, 1)
    # All even digits
    assert module_0.even_odd_count(2468) == (4, 0)
    assert module_0.even_odd_count(-2468) == (4, 0)
    # All odd digits
    assert module_0.even_odd_count(13579) == (0, 5)
    # Zero is even
    assert module_0.even_odd_count(0) == (1, 0)
    # Number with repeated digits
    assert module_0.even_odd_count(100) == (2, 1)
    assert module_0.even_odd_count(-305) == (1, 2)
    # Single digit cases
    assert module_0.even_odd_count(2) == (1, 0)
    assert module_0.even_odd_count(7) == (0, 1)

# Generated at 2026-11-03 04:46:54.256982
# Unit test for function even_odd_count
def test_even_odd_count():
    # Mixed even and odd digits
    assert module_0.even_odd_count(-12) == (1, 1)
    assert module_0.even_odd_count(123) == (1, 2)

    # Zero has one even digit
    assert module_0.even_odd_count(0) == (1, 0)

    # All even digits
    assert module_0.even_odd_count(2468) == (4, 0)

    # All odd digits
    assert module_0.even_odd_count(1357) == (0, 4)

    # Negative numbers use absolute value
    assert module_0.even_odd_count(-2468) == (4, 0)
    assert module_0.even_odd_count(-135) == (0, 3)

    # Single digit numbers
    assert module_0.even_odd_count(7) == (0, 1)
    assert module_0.even_odd_count(8) == (1, 0)

    # Repeated digits
    assert module_0.even_odd_count(1000) == (3, 1)

    # All ten digits, balanced counts
    assert module_0.even_odd_count(1234567890) == (5, 5)

    print("All tests passed!")


test_even_odd_count()