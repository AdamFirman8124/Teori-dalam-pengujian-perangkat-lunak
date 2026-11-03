

# Generated at 2026-11-02 22:56:16.825488
# Unit test for function count_up_to
def test_count_up_to():import unittest


class TestCountUpTo(unittest.TestCase):

    def test_count_up_to(self):
        # Basic cases
        self.assertEqual(module_0.count_up_to(10), [2, 3, 5, 7])
        self.assertEqual(module_0.count_up_to(20), [2, 3, 5, 7, 11, 13, 17, 19])

        # Edge cases: n too small to contain primes
        self.assertEqual(module_0.count_up_to(0), [])
        self.assertEqual(module_0.count_up_to(1), [])
        self.assertEqual(module_0.count_up_to(2), [])

        # Smallest prime boundary
        self.assertEqual(module_0.count_up_to(3), [2])
        self.assertEqual(module_0.count_up_to(4), [2, 3])

        # Negative input should yield no primes
        self.assertEqual(module_0.count_up_to(-5), [])

        # Verify all returned values are prime and strictly less than n
        result = module_0.count_up_to(50)
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        self.assertEqual(result, expected)
        for p in result:
            self.assertLess(p, 50)
            self.assertTrue(all(p % j != 0 for j in range(2, p)))


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 22:59:32.511435
# Unit test for function count_up_to
def test_count_up_to():
# nonce:bc43a364
    # n less than 2 yields no primes
    assert module_0.count_up_to(0) == []
    assert module_0.count_up_to(-5) == []
    assert module_0.count_up_to(1) == []

    # n = 2: range(2, 2) is empty, so no primes
    assert module_0.count_up_to(2) == []

    # n = 3: only prime below 3 is 2
    assert module_0.count_up_to(3) == [2]

    # n = 5: primes below 5
    assert module_0.count_up_to(5) == [2, 3]

    # n = 10: primes below 10
    assert module_0.count_up_to(10) == [2, 3, 5, 7]

    # n = 11: primes below 11 (11 itself excluded)
    assert module_0.count_up_to(11) == [2, 3, 5, 7]

    # n = 20: primes below 20
    assert module_0.count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]

    # n = 30: primes below 30
    assert module_0.count_up_to(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    # Verify result elements are strictly increasing primes
    result = module_0.count_up_to(50)
    assert result == sorted(result)
    assert len(result) == len(set(result))
    for p in result:
        assert all(p % j != 0 for j in range(2, p))

    print("All tests passed!")