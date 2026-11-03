

# Generated at 2026-11-02 06:31:15.067373
# Unit test for function count_up_to
def test_count_up_to():assert module_0.count_up_to(0) == []

# Generated at 2026-11-02 06:31:25.176374
# Unit test for function count_up_to
def test_count_up_to():import unittest


class TestCountUpTo(unittest.TestCase):

    def test_count_up_to_zero(self):
        self.assertEqual(module_0.count_up_to(0), [])

    def test_count_up_to_one(self):
        self.assertEqual(module_0.count_up_to(1), [])

    def test_count_up_to_two(self):
        self.assertEqual(module_0.count_up_to(2), [])

    def test_count_up_to_three(self):
        self.assertEqual(module_0.count_up_to(3), [2])

    def test_count_up_to_ten(self):
        self.assertEqual(module_0.count_up_to(10), [2, 3, 5, 7])

    def test_count_up_to_eleven(self):
        self.assertEqual(module_0.count_up_to(11), [2, 3, 5, 7])

    def test_count_up_to_twenty(self):
        self.assertEqual(module_0.count_up_to(20), [2, 3, 5, 7, 11, 13, 17, 19])

    def test_result_is_list(self):
        self.assertIsInstance(module_0.count_up_to(10), list)

    def test_primes_are_sorted(self):
        result = module_0.count_up_to(30)
        self.assertEqual(result, sorted(result))

    def test_no_duplicates(self):
        result = module_0.count_up_to(30)
        self.assertEqual(len(result), len(set(result)))


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 06:31:32.844294
# Unit test for function count_up_to
def test_count_up_to():
    # n <= 2 yields no primes
    assert module_0.count_up_to(0) == []
    assert module_0.count_up_to(1) == []
    assert module_0.count_up_to(2) == []

    # smallest prime only
    assert module_0.count_up_to(3) == [2]

    # typical ranges
    assert module_0.count_up_to(10) == [2, 3, 5, 7]
    assert module_0.count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert module_0.count_up_to(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    # result excludes n itself even when n is prime
    assert module_0.count_up_to(11) == [2, 3, 5, 7]

    # boundary: primes strictly less than n
    assert module_0.count_up_to(13) == [2, 3, 5, 7, 11]

# Generated at 2026-11-02 06:31:37.648010
# Unit test for function count_up_to
def test_count_up_to():
    assert module_0.count_up_to(0) == []
    assert module_0.count_up_to(1) == []
    assert module_0.count_up_to(2) == []
    assert module_0.count_up_to(3) == [2]
    assert module_0.count_up_to(5) == [2, 3]
    assert module_0.count_up_to(10) == [2, 3, 5, 7]
    assert module_0.count_up_to(11) == [2, 3, 5, 7]
    assert module_0.count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert module_0.count_up_to(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert module_0.count_up_to(-5) == []

# Generated at 2026-11-02 06:31:48.523770
# Unit test for function count_up_to
def test_count_up_to():
# nonce:17cbed3b
    # n < 2 should return an empty list (no primes exist below 2)
    assert module_0.count_up_to(0) == []
    assert module_0.count_up_to(1) == []
    assert module_0.count_up_to(-10) == []

    # n = 2: range(2, 2) is empty, so no primes
    assert module_0.count_up_to(2) == []

    # n = 3: only prime below 3 is 2
    assert module_0.count_up_to(3) == [2]

    # Small known cases
    assert module_0.count_up_to(10) == [2, 3, 5, 7]
    assert module_0.count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert module_0.count_up_to(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    # Edge: n is itself prime — it should NOT be included (strictly below n)
    assert module_0.count_up_to(13) == [2, 3, 5, 7, 11]

    # Results must be strictly increasing and unique
    result = module_0.count_up_to(50)
    assert result == sorted(result)
    assert len(result) == len(set(result))

    # Every returned value must actually be prime
    for p in result:
        assert all(p % j != 0 for j in range(2, p)), f"{p} is not prime"

    # No primes should be missed below 50 (compare against independent check)
    expected = [p for p in range(2, 50) if all(p % j != 0 for j in range(2, p))]
    assert module_0.count_up_to(50) == expected

    print("All tests passed!")


if __name__ == "__main__":
    test_count_up_to()

# Generated at 2026-11-02 06:32:21.679997
# Unit test for function count_up_to
def test_count_up_to():
    assert module_0.count_up_to(0) == []
    assert module_0.count_up_to(1) == []
    assert module_0.count_up_to(2) == []
    assert module_0.count_up_to(3) == [2]
    assert module_0.count_up_to(5) == [2, 3]
    assert module_0.count_up_to(10) == [2, 3, 5, 7]
    assert module_0.count_up_to(11) == [2, 3, 5, 7]
    assert module_0.count_up_to(12) == [2, 3, 5, 7, 11]
    assert module_0.count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert module_0.count_up_to(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# nonce:37115e33