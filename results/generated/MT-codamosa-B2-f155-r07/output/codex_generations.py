

# Generated at 2026-11-01 20:24:44.052874
# Unit test for function even_odd_count
def test_even_odd_count():
# nonce:63e7b410
    # Test positive number with mixed even/odd digits
    assert module_0.even_odd_count(123) == (1, 2)
    assert module_0.even_odd_count(1230) == (2, 2)

    # Test negative number (abs should be applied)
    assert module_0.even_odd_count(-12) == (1, 1)
    assert module_0.even_odd_count(-3456) == (2, 2)

    # Test all even digits
    assert module_0.even_odd_count(2468) == (4, 0)
    assert module_0.even_odd_count(-246) == (3, 0)

    # Test all odd digits
    assert module_0.even_odd_count(1357) == (0, 4)
    assert module_0.even_odd_count(-135) == (0, 3)

    # Test zero (single even digit)
    assert module_0.even_odd_count(0) == (1, 0)
    assert module_0.even_odd_count(-0) == (1, 0)

    # Test single digit numbers
    assert module_0.even_odd_count(4) == (1, 0)
    assert module_0.even_odd_count(7) == (0, 1)

    # Test number with repeated digits
    assert module_0.even_odd_count(1000) == (3, 1)
    assert module_0.even_odd_count(111) == (0, 3)

    # Test large number
    assert module_0.even_odd_count(1234567890) == (5, 5)

    # Verify return type is a tuple
    result = module_0.even_odd_count(123)
    assert isinstance(result, tuple)
    assert len(result) == 2

    print("All test cases passed!")


if __name__ == "__main__":
    test_even_odd_count()

# Generated at 2026-11-01 20:24:55.653260
# Unit test for function even_odd_count
def test_even_odd_count():
    # Test with positive numbers
    assert module_0.even_odd_count(123) == (1, 2), "Expected (1, 2) for input 123"
    assert module_0.even_odd_count(2468) == (4, 0), "Expected (4, 0) for input 2468"
    assert module_0.even_odd_count(13579) == (0, 5), "Expected (0, 5) for input 13579"

    # Test with negative numbers (abs value used)
    assert module_0.even_odd_count(-12) == (1, 1), "Expected (1, 1) for input -12"
    assert module_0.even_odd_count(-3456) == (2, 2), "Expected (2, 2) for input -3456"

    # Test with zero
    assert module_0.even_odd_count(0) == (1, 0), "Expected (1, 0) for input 0"

    # Test with single digit numbers
    assert module_0.even_odd_count(7) == (0, 1), "Expected (0, 1) for input 7"
    assert module_0.even_odd_count(8) == (1, 0), "Expected (1, 0) for input 8"

    # Test with mixed digits including zeros
    assert module_0.even_odd_count(105) == (2, 1), "Expected (2, 1) for input 105"
    assert module_0.even_odd_count(-100) == (2, 1), "Expected (2, 1) for input -100"

    print("All tests passed!")

# Generated at 2026-11-01 20:25:03.249426
# Unit test for function even_odd_count
def test_even_odd_count():
    assert module_0.even_odd_count(123) == (1, 2)
    assert module_0.even_odd_count(-12) == (1, 1)
    assert module_0.even_odd_count(0) == (1, 0)
    assert module_0.even_odd_count(2468) == (4, 0)
    assert module_0.even_odd_count(13579) == (0, 5)
    assert module_0.even_odd_count(-1357) == (0, 4)
    assert module_0.even_odd_count(100) == (3, 0)
    assert module_0.even_odd_count(7) == (0, 1)

# Generated at 2026-11-01 20:25:10.792368
# Unit test for function even_odd_count
def test_even_odd_count():
    # Mixed even and odd digits
    assert module_0.even_odd_count(123) == (1, 2)
    assert module_0.even_odd_count(4321) == (2, 2)
    assert module_0.even_odd_count(5024) == (3, 1)

    # Negative numbers (abs applied)
    assert module_0.even_odd_count(-123) == (1, 2)
    assert module_0.even_odd_count(-2468) == (4, 0)

    # All even digits
    assert module_0.even_odd_count(2468) == (4, 0)
    assert module_0.even_odd_count(0) == (1, 0)

    # All odd digits
    assert module_0.even_odd_count(1357) == (0, 4)
    assert module_0.even_odd_count(111) == (0, 3)

    # Single digits
    assert module_0.even_odd_count(4) == (1, 0)
    assert module_0.even_odd_count(5) == (0, 1)

    # Large number
    assert module_0.even_odd_count(1000000) == (7, 0)

    # Returns a tuple
    assert isinstance(module_0.even_odd_count(12), tuple)

    print("All tests passed!")


test_even_odd_count()

# Generated at 2026-11-01 20:25:18.461757
# Unit test for function even_odd_count
def test_even_odd_count():
    # Mixed even and odd digits
    assert module_0.even_odd_count(123456) == (3, 3)
    assert module_0.even_odd_count(-12) == (1, 1)
    assert module_0.even_odd_count(1000) == (4, 0)
    assert module_0.even_odd_count(-1357) == (0, 4)
    # Zero has one even digit
    assert module_0.even_odd_count(0) == (1, 0)
    # Single digits
    assert module_0.even_odd_count(4) == (1, 0)
    assert module_0.even_odd_count(7) == (0, 1)
    # Negative of same value gives same result (abs applied)
    assert module_0.even_odd_count(-2468) == (4, 0)
    assert module_0.even_odd_count(-97531) == (0, 5)
    # Large number
    assert module_0.even_odd_count(1029384756) == (5, 5)