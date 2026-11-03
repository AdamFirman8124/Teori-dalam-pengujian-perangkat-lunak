

# Generated at 2026-11-02 05:56:01.365153
# Unit test for function make_a_pile
def test_make_a_pile():
    # Test basic case: n=3 should return [3, 5, 7]
    assert module_0.make_a_pile(3) == [3, 5, 7]

    # Test smallest non-trivial case: n=1
    assert module_0.make_a_pile(1) == [1]

    # Test n=2
    assert module_0.make_a_pile(2) == [2, 4]

    # Test n=0 returns an empty list
    assert module_0.make_a_pile(0) == []

    # Test a larger case: n=5 should return [5, 7, 9, 11, 13]
    assert module_0.make_a_pile(5) == [5, 7, 9, 11, 13]

    # Verify structure: each level increases by 2, starting at n
    result = module_0.make_a_pile(6)
    assert result[0] == 6
    assert all(result[i + 1] - result[i] == 2 for i in range(len(result) - 1))
    assert len(result) == 6

    # Verify all elements have correct parity (same parity as n)
    assert all(x % 2 == 6 % 2 for x in result)

# Generated at 2026-11-02 05:56:04.635021
# Unit test for function make_a_pile
def test_make_a_pile():import unittest


class TestMakeAPile(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(module_0.make_a_pile(3), [3, 5, 7])

    def test_one(self):
        self.assertEqual(module_0.make_a_pile(1), [1])

    def test_zero(self):
        self.assertEqual(module_0.make_a_pile(0), [])

    def test_five(self):
        self.assertEqual(module_0.make_a_pile(5), [5, 7, 9, 11, 13])

    def test_length(self):
        result = module_0.make_a_pile(10)
        self.assertEqual(len(result), 10)

    def test_increasing(self):
        result = module_0.make_a_pile(4)
        self.assertTrue(all(b > a for a, b in zip(result, result[1:])))


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 05:56:07.091511
# Unit test for function make_a_pile
def test_make_a_pile():
    assert module_0.make_a_pile(1) == [1]
    assert module_0.make_a_pile(2) == [2, 4]
    assert module_0.make_a_pile(3) == [3, 5, 7]
    assert module_0.make_a_pile(4) == [4, 6, 8, 10]
    assert module_0.make_a_pile(5) == [5, 7, 9, 11, 13]
    assert module_0.make_a_pile(0) == []

# Generated at 2026-11-02 05:56:13.555792
# Unit test for function make_a_pile
def test_make_a_pile():
    # Basic expected-value checks
    assert module_0.make_a_pile(1) == [1]
    assert module_0.make_a_pile(2) == [2, 4]
    assert module_0.make_a_pile(3) == [3, 5, 7]
    assert module_0.make_a_pile(4) == [4, 6, 8, 10]
    assert module_0.make_a_pile(5) == [5, 7, 9, 11, 13]
    assert module_0.make_a_pile(0) == []

    # Property-based checks
    for n in range(10):
        pile = module_0.make_a_pile(n)
        assert len(pile) == n  # length equals n
        if n > 0:
            assert pile[0] == n  # first level is n
            assert all(pile[i + 1] - pile[i] == 2 for i in range(n - 1))  # step of 2
            assert all(x % 2 == n % 2 for x in pile)  # parity matches n

# Generated at 2026-11-02 05:56:18.151275
# Unit test for function make_a_pile
def test_make_a_pile():
    assert module_0.make_a_pile(1) == [1]
    assert module_0.make_a_pile(2) == [2, 4]
    assert module_0.make_a_pile(3) == [3, 5, 7]
    assert module_0.make_a_pile(4) == [4, 6, 8, 10]
    assert module_0.make_a_pile(5) == [5, 7, 9, 11, 13]
    assert module_0.make_a_pile(0) == []
    assert module_0.make_a_pile(6) == [6, 8, 10, 12, 14, 16]
    assert len(module_0.make_a_pile(10)) == 10
    result = module_0.make_a_pile(7)
    assert all(result[i + 1] - result[i] == 2 for i in range(len(result) - 1))