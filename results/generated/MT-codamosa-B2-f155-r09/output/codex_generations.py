

# Generated at 2026-11-02 00:37:14.920849
# Unit test for function even_odd_count
def test_even_odd_count():
    # Basic positive numbers
    assert module_0.even_odd_count(123) == (1, 2), "Expected (1, 2) for 123"
    assert module_0.even_odd_count(4567) == (2, 2), "Expected (2, 2) for 4567"

    # Negative numbers (abs should be applied)
    assert module_0.even_odd_count(-12) == (1, 1), "Expected (1, 1) for -12"
    assert module_0.even_odd_count(-2468) == (4, 0), "Expected (4, 0) for -2468"

    # All even digits
    assert module_0.even_odd_count(2468) == (4, 0), "Expected (4, 0) for 2468"
    assert module_0.even_odd_count(0) == (1, 0), "Expected (1, 0) for 0"

    # All odd digits
    assert module_0.even_odd_count(1357) == (0, 4), "Expected (0, 4) for 1357"
    assert module_0.even_odd_count(111) == (0, 3), "Expected (0, 3) for 111"

    # Single digit numbers
    assert module_0.even_odd_count(5) == (0, 1), "Expected (0, 1) for 5"
    assert module_0.even_odd_count(8) == (1, 0), "Expected (1, 0) for 8"
    assert module_0.even_odd_count(-9) == (0, 1), "Expected (0, 1) for -9"

    # Mixed with zero
    assert module_0.even_odd_count(105) == (1, 2), "Expected (1, 2) for 105"
    assert module_0.even_odd_count(-3050) == (2, 2), "Expected (2, 2) for -3050"

    # Large number
    assert module_0.even_odd_count(9876543210) == (5, 5), "Expected (5, 5) for 9876543210"

    # Verify return type is a tuple
    result = module_0.even_odd_count(1234)
    assert isinstance(result, tuple), "Result should be a tuple"
    assert len(result) == 2, "Tuple should have exactly two elements"

    print("All tests passed!")


if __name__ == "__main__":
    test_even_odd_count()

# Generated at 2026-11-02 00:38:40.401338
# Unit test for function even_odd_count
def test_even_odd_count():import unittest


class TestEvenOddCount(unittest.TestCase):

    def test_positive_mixed(self):
        self.assertEqual(module_0.even_odd_count(123), (2, 1))  # even: 2, odd: 1,3

    def test_negative_mixed(self):
        self.assertEqual(module_0.even_odd_count(-12), (1, 1))  # abs(-12) -> 1,2

    def test_all_even(self):
        self.assertEqual(module_0.even_odd_count(2468), (4, 0))

    def test_all_odd(self):
        self.assertEqual(module_0.even_odd_count(1357), (0, 4))

    def test_zero(self):
        self.assertEqual(module_0.even_odd_count(0), (1, 0))

    def test_negative_zero(self):
        self.assertEqual(module_0.even_odd_count(-0), (1, 0))

    def test_single_even_digit(self):
        self.assertEqual(module_0.even_odd_count(8), (1, 0))

    def test_single_odd_digit(self):
        self.assertEqual(module_0.even_odd_count(7), (0, 1))

    def test_negative_with_zeros(self):
        self.assertEqual(module_0.even_odd_count(-101), (1, 2))  # digits: 1,0,1

    def test_large_number(self):
        self.assertEqual(module_0.even_odd_count(1000000), (6, 1))

    def test_returns_tuple(self):
        result = module_0.even_odd_count(42)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 00:39:33.734104
# Unit test for function even_odd_count
def test_even_odd_count():assert module_0.even_odd_count(-12) == (1, 1)

# Generated at 2026-11-02 00:40:21.773384
# Unit test for function even_odd_count
def test_even_odd_count():
    # Basic positive number
    assert module_0.even_odd_count(123) == (1, 2), "Test case 123 failed"
    
    # Negative number (should use absolute value)
    assert module_0.even_odd_count(-12) == (1, 1), "Test case -12 failed"
    
    # Zero (single even digit)
    assert module_0.even_odd_count(0) == (1, 0), "Test case 0 failed"
    
    # All even digits
    assert module_0.even_odd_count(2468) == (4, 0), "Test case 2468 failed"
    
    # All odd digits
    assert module_0.even_odd_count(13579) == (0, 5), "Test case 13579 failed"
    
    # Negative number with all even digits
    assert module_0.even_odd_count(-246) == (3, 0), "Test case -246 failed"
    
    # Number with repeated digits
    assert module_0.even_odd_count(1000) == (3, 1), "Test case 1000 failed"
    
    # Large mixed number
    assert module_0.even_odd_count(9876543210) == (5, 5), "Test case 9876543210 failed"
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_even_odd_count()

# Generated at 2026-11-02 00:41:24.488660
# Unit test for function even_odd_count
def test_even_odd_count():
    # Test with mixed even and odd digits
    assert module_0.even_odd_count(123) == (1, 2)
    assert module_0.even_odd_count(4567) == (2, 2)

    # Test with negative numbers (should use absolute value)
    assert module_0.even_odd_count(-12) == (1, 1)
    assert module_0.even_odd_count(-1357) == (0, 4)

    # Test with zero (0 is even)
    assert module_0.even_odd_count(0) == (1, 0)

    # Test with all even digits
    assert module_0.even_odd_count(2468) == (4, 0)
    assert module_0.even_odd_count(-2468) == (4, 0)

    # Test with all odd digits
    assert module_0.even_odd_count(1357) == (0, 4)

    # Test with repeated digits
    assert module_0.even_odd_count(100) == (2, 1)
    assert module_0.even_odd_count(-111) == (0, 3)

    # Test with single digit numbers
    assert module_0.even_odd_count(2) == (1, 0)
    assert module_0.even_odd_count(7) == (0, 1)
    assert module_0.even_odd_count(-9) == (0, 1)

    # Test return type is a tuple
    result = module_0.even_odd_count(123)
    assert isinstance(result, tuple)
    assert len(result) == 2

    print("All tests passed!")


if __name__ == "__main__":
    test_even_odd_count()