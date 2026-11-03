

# Generated at 2026-11-02 18:11:54.659292
# Unit test for function largest_divisor
def test_largest_divisor():
    # Composite numbers
    assert module_0.largest_divisor(15) == 5, "module_0.largest_divisor(15) should be 5"
    assert module_0.largest_divisor(12) == 6, "module_0.largest_divisor(12) should be 6"
    assert module_0.largest_divisor(10) == 5, "module_0.largest_divisor(10) should be 5"
    assert module_0.largest_divisor(100) == 50, "module_0.largest_divisor(100) should be 50"

    # Prime numbers: largest divisor is 1
    assert module_0.largest_divisor(2) == 1, "module_0.largest_divisor(2) should be 1"
    assert module_0.largest_divisor(3) == 1, "module_0.largest_divisor(3) should be 1"
    assert module_0.largest_divisor(7) == 1, "module_0.largest_divisor(7) should be 1"
    assert module_0.largest_divisor(13) == 1, "module_0.largest_divisor(13) should be 1"

    # Even numbers
    assert module_0.largest_divisor(4) == 2, "module_0.largest_divisor(4) should be 2"
    assert module_0.largest_divisor(8) == 4, "module_0.largest_divisor(8) should be 4"

    # Perfect squares
    assert module_0.largest_divisor(9) == 3, "module_0.largest_divisor(9) should be 3"
    assert module_0.largest_divisor(49) == 7, "module_0.largest_divisor(49) should be 7"

    # Larger composite
    assert module_0.largest_divisor(360) == 180, "module_0.largest_divisor(360) should be 180"

    print("All tests passed!")


if __name__ == "__main__":
    test_largest_divisor()

# Generated at 2026-11-02 18:12:49.302052
# Unit test for function largest_divisor
def test_largest_divisor():
    assert module_0.largest_divisor(3) == 1
    assert module_0.largest_divisor(10) == 5
    assert module_0.largest_divisor(15) == 5
    assert module_0.largest_divisor(7) == 1
    assert module_0.largest_divisor(2) == 1
    assert module_0.largest_divisor(100) == 50
    assert module_0.largest_divisor(49) == 7
    assert module_0.largest_divisor(36) == 18
    assert module_0.largest_divisor(1) is None  # no divisor found for n=1


if __name__ == "__main__":
    test_largest_divisor()
    print("All tests passed!")

# Generated at 2026-11-02 18:13:37.223586
# Unit test for function largest_divisor
def test_largest_divisor():
# nonce:cd39b8a4
    # Basic cases
    assert module_0.largest_divisor(3) == 1
    assert module_0.largest_divisor(10) == 5
    assert module_0.largest_divisor(15) == 5
    # Primes: largest proper divisor is 1
    assert module_0.largest_divisor(2) == 1
    assert module_0.largest_divisor(7) == 1
    assert module_0.largest_divisor(13) == 1
    # Perfect squares
    assert module_0.largest_divisor(4) == 2
    assert module_0.largest_divisor(49) == 7
    # Composite numbers
    assert module_0.largest_divisor(12) == 6
    assert module_0.largest_divisor(28) == 14
    assert module_0.largest_divisor(36) == 18
    assert module_0.largest_divisor(100) == 50
    # Property checks: result divides n, is < n, and is maximal
    for n in (2, 3, 10, 15, 28, 49, 97, 100, 128, 1024):
        d = module_0.largest_divisor(n)
        assert n % d == 0 and d < n
        assert all(n % k != 0 for k in range(d + 1, n))


if __name__ == "__main__":
    test_largest_divisor()
    print("All tests passed!")

# Generated at 2026-11-02 18:14:01.587516
# Unit test for function largest_divisor
def test_largest_divisor():
    # Test with a composite number
    assert module_0.largest_divisor(10) == 5, "Expected 5 for input 10"
    
    # Test with an even number
    assert module_0.largest_divisor(4) == 2, "Expected 2 for input 4"
    
    # Test with a prime number (largest divisor is 1)
    assert module_0.largest_divisor(13) == 1, "Expected 1 for input 13"
    
    # Test with a perfect square
    assert module_0.largest_divisor(49) == 7, "Expected 7 for input 49"
    
    # Test with a large composite number
    assert module_0.largest_divisor(100) == 50, "Expected 50 for input 100"
    
    # Test with a number whose largest divisor is a small prime
    assert module_0.largest_divisor(15) == 5, "Expected 5 for input 15"
    
    # Test with smallest meaningful input
    assert module_0.largest_divisor(3) == 1, "Expected 1 for input 3"
    
    # Test with a power of two
    assert module_0.largest_divisor(64) == 32, "Expected 32 for input 64"
    
    # Test with a product of two primes
    assert module_0.largest_divisor(21) == 7, "Expected 7 for input 21"
    
    # Test with a larger number
    assert module_0.largest_divisor(1000) == 500, "Expected 500 for input 1000"
    
    print("All tests passed!")

# Generated at 2026-11-02 18:14:15.975332
# Unit test for function largest_divisor
def test_largest_divisor():
    # nonce:1c58aeb1
    # Composite numbers
    assert module_0.largest_divisor(15) == 5, "module_0.largest_divisor(15) should be 5"
    assert module_0.largest_divisor(12) == 6, "module_0.largest_divisor(12) should be 6"
    assert module_0.largest_divisor(100) == 50, "module_0.largest_divisor(100) should be 50"
    assert module_0.largest_divisor(49) == 7, "module_0.largest_divisor(49) should be 7"

    # Prime numbers: largest divisor is 1
    assert module_0.largest_divisor(7) == 1, "module_0.largest_divisor(7) should be 1"
    assert module_0.largest_divisor(13) == 1, "module_0.largest_divisor(13) should be 1"

    # Smallest valid input
    assert module_0.largest_divisor(2) == 1, "module_0.largest_divisor(2) should be 1"

    # Even numbers
    assert module_0.largest_divisor(10) == 5, "module_0.largest_divisor(10) should be 5"
    assert module_0.largest_divisor(8) == 4, "module_0.largest_divisor(8) should be 4"

    print("All tests passed!")


class TestLargestDivisor(unittest.TestCase):
    def test_composite_numbers(self):
        self.assertEqual(module_0.largest_divisor(15), 5)
        self.assertEqual(module_0.largest_divisor(12), 6)
        self.assertEqual(module_0.largest_divisor(100), 50)

    def test_prime_numbers(self):
        self.assertEqual(module_0.largest_divisor(7), 1)
        self.assertEqual(module_0.largest_divisor(13), 1)

    def test_small_inputs(self):
        self.assertEqual(module_0.largest_divisor(2), 1)
        self.assertEqual(module_0.largest_divisor(3), 1)

    def test_perfect_squares(self):
        self.assertEqual(module_0.largest_divisor(49), 7)
        self.assertEqual(module_0.largest_divisor(36), 18)


if __name__ == "__main__":
    test_largest_divisor()
    unittest.main()