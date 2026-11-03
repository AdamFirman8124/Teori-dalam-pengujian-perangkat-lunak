

# Generated at 2026-11-01 22:49:03.792223
# Unit test for function count_up_to
def test_count_up_to():import unittest


class TestCountUpTo(unittest.TestCase):

    def test_small_numbers(self):
        self.assertEqual(module_0.count_up_to(5), [2, 3])
        self.assertEqual(module_0.count_up_to(6), [2, 3, 5])

    def test_larger_number(self):
        self.assertEqual(module_0.count_up_to(11), [2, 3, 5, 7])
        self.assertEqual(module_0.count_up_to(20), [2, 3, 5, 7, 11, 13, 17, 19])

    def test_edge_cases(self):
        # n too small to contain any primes
        self.assertEqual(module_0.count_up_to(0), [])
        self.assertEqual(module_0.count_up_to(1), [])
        self.assertEqual(module_0.count_up_to(2), [])

    def test_n_is_prime_boundary(self):
        # n itself is excluded (range goes up to n-1)
        self.assertEqual(module_0.count_up_to(7), [2, 3, 5])
        self.assertEqual(module_0.count_up_to(8), [2, 3, 5, 7])

    def test_negative_input(self):
        self.assertEqual(module_0.count_up_to(-5), [])


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-01 22:49:15.463811
# Unit test for function count_up_to
def test_count_up_to():
    # Edge cases: no primes expected
    assert module_0.count_up_to(0) == []
    assert module_0.count_up_to(1) == []
    assert module_0.count_up_to(2) == []

    # Small values
    assert module_0.count_up_to(3) == [2]
    assert module_0.count_up_to(4) == [2, 3]

    # Typical cases
    assert module_0.count_up_to(10) == [2, 3, 5, 7]
    assert module_0.count_up_to(11) == [2, 3, 5, 7]
    assert module_0.count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert module_0.count_up_to(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    # Verify all returned values are prime and correctly ordered
    result = module_0.count_up_to(50)
    expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    assert result == expected
    assert all(
        all(p % d != 0 for d in range(2, int(p ** 0.5) + 1))
        for p in result
    )

    print("All tests passed!")


if __name__ == "__main__":
    test_count_up_to()

# Generated at 2026-11-01 22:49:48.029067
# Unit test for function count_up_to
def test_count_up_to():
    # Test with n less than 2 (no primes possible)
    assert module_0.count_up_to(0) == []
    assert module_0.count_up_to(1) == []
    
    # Test with n = 2 (range is empty, no primes below 2)
    assert module_0.count_up_to(2) == []
    
    # Test with small values
    assert module_0.count_up_to(3) == [2]
    assert module_0.count_up_to(4) == [2, 3]
    assert module_0.count_up_to(5) == [2, 3]
    assert module_0.count_up_to(6) == [2, 3, 5]
    
    # Test with n = 10
    assert module_0.count_up_to(10) == [2, 3, 5, 7]
    
    # Test with n = 20
    assert module_0.count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    
    # Test with n = 30
    assert module_0.count_up_to(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    
    # Verify result is a list
    assert isinstance(module_0.count_up_to(10), list)
    
    # Verify all returned values are primes
    primes = module_0.count_up_to(50)
    for p in primes:
        assert all(p % j != 0 for j in range(2, p))
    
    # Verify primes are strictly increasing
    assert primes == sorted(set(primes))
    
    print("All tests passed!")


if __name__ == "__main__":
    test_count_up_to()

# Generated at 2026-11-01 22:49:58.483113
# Unit test for function count_up_to
def test_count_up_to():import unittest


class TestCountUpTo(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(module_0.count_up_to(0), [])

    def test_one(self):
        self.assertEqual(module_0.count_up_to(1), [])

    def test_two(self):
        self.assertEqual(module_0.count_up_to(2), [])

    def test_three(self):
        self.assertEqual(module_0.count_up_to(3), [2])

    def test_five(self):
        self.assertEqual(module_0.count_up_to(5), [2, 3])

    def test_ten(self):
        self.assertEqual(module_0.count_up_to(10), [2, 3, 5, 7])

    def test_eleven(self):
        # 11 is excluded since range goes up to n-1
        self.assertEqual(module_0.count_up_to(11), [2, 3, 5, 7])

    def test_twelve(self):
        self.assertEqual(module_0.count_up_to(12), [2, 3, 5, 7, 11])

    def test_twenty(self):
        self.assertEqual(module_0.count_up_to(20), [2, 3, 5, 7, 11, 13, 17, 19])

    def test_thirty(self):
        self.assertEqual(module_0.count_up_to(30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

    def test_negative(self):
        self.assertEqual(module_0.count_up_to(-5), [])

    def test_large(self):
        result = module_0.count_up_to(50)
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
# nonce:b5f68fc8

# Generated at 2026-11-01 22:50:08.286742
# Unit test for function count_up_to
def test_count_up_to():
    # n less than 2 yields no primes
    assert module_0.count_up_to(0) == []
    assert module_0.count_up_to(1) == []
    assert module_0.count_up_to(2) == []
    # smallest prime
    assert module_0.count_up_to(3) == [2]
    # typical cases
    assert module_0.count_up_to(5) == [2, 3]
    assert module_0.count_up_to(10) == [2, 3, 5, 7]
    assert module_0.count_up_to(11) == [2, 3, 5, 7]
    assert module_0.count_up_to(12) == [2, 3, 5, 7, 11]
    assert module_0.count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    # larger range includes primes and excludes composites
    assert module_0.count_up_to(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    # result contains only primes
    primes = module_0.count_up_to(50)
    assert all(all(p % j != 0 for j in range(2, p)) for p in primes)
    # result is strictly increasing
    assert primes == sorted(primes)
    # negative input returns empty list
    assert module_0.count_up_to(-5) == []
    print("All tests passed!")


if __name__ == "__main__":
    test_count_up_to()