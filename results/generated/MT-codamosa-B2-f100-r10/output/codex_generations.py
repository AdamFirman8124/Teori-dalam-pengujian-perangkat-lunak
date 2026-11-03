

# Generated at 2026-11-02 08:57:53.503878
# Unit test for function make_a_pile
def test_make_a_pile():
    # Basic cases
    assert module_0.make_a_pile(1) == [1]
    assert module_0.make_a_pile(2) == [2, 4]
    assert module_0.make_a_pile(3) == [3, 5, 7]
    assert module_0.make_a_pile(4) == [4, 6, 8, 10]
    assert module_0.make_a_pile(5) == [5, 7, 9, 11, 13]

    # Edge case: n = 0 returns an empty list
    assert module_0.make_a_pile(0) == []

    # Larger input
    assert module_0.make_a_pile(8) == [8, 10, 12, 14, 16, 18, 20, 22]

    # Property checks for a general n
    n = 7
    result = module_0.make_a_pile(n)
    assert len(result) == n                      # list has exactly n levels
    assert result[0] == n                        # starts at n
    assert result[-1] == n + 2 * (n - 1)         # ends at n + 2*(n-1)
    for i in range(1, n):
        assert result[i] - result[i - 1] == 2    # each level adds 2 stones

    # All elements share the parity of n
    assert all(x % 2 == n % 2 for x in result)

# Generated at 2026-11-02 08:58:50.735224
# Unit test for function make_a_pile
def test_make_a_pile():import unittest


def module_0.make_a_pile(n):
    return [n + 2*i for i in range(n)]


class TestMakeAPile(unittest.TestCase):

    def test_basic_case(self):
        self.assertEqual(module_0.make_a_pile(3), [3, 5, 7])

    def test_single_element(self):
        self.assertEqual(module_0.make_a_pile(1), [1])

    def test_zero(self):
        self.assertEqual(module_0.make_a_pile(0), [])

    def test_even_n(self):
        self.assertEqual(module_0.make_a_pile(4), [4, 6, 8, 10])

    def test_larger_n(self):
        self.assertEqual(module_0.make_a_pile(6), [6, 8, 10, 12, 14, 16])

    def test_first_element_equals_n(self):
        self.assertEqual(module_0.make_a_pile(5)[0], 5)

    def test_odd_elements(self):
        result = module_0.make_a_pile(5)
        for value in result:
            self.assertEqual(value % 2, 5 % 2)

    def test_length(self):
        self.assertEqual(len(module_0.make_a_pile(7)), 7)


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 09:01:01.409497
# Unit test for function make_a_pile
def test_make_a_pile():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestMakeAPile)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return result.wasSuccessful()


if __name__ == "__main__":
    test_make_a_pile()

# Generated at 2026-11-02 09:04:04.196055
# Unit test for function make_a_pile
def test_make_a_pile():
    # Test with n = 3: levels should be [3, 5, 7]
    assert module_0.make_a_pile(3) == [3, 5, 7]
    
    # Test with n = 1: single level
    assert module_0.make_a_pile(1) == [1]
    
    # Test with n = 0: empty pile
    assert module_0.make_a_pile(0) == []
    
    # Test with n = 5: levels should be [5, 7, 9, 11, 13]
    assert module_0.make_a_pile(5) == [5, 7, 9, 11, 13]
    
    # Test with n = 2: even number of levels
    assert module_0.make_a_pile(2) == [2, 4]
    
    # Verify all elements are odd when n is odd
    result = module_0.make_a_pile(7)
    assert all(x % 2 == 1 for x in result)
    assert len(result) == 7
    
    # Verify each level increases by 2
    result = module_0.make_a_pile(6)
    for i in range(1, len(result)):
        assert result[i] - result[i-1] == 2
    
    # Verify first element equals n
    assert result[0] == 6
    
    print("All tests passed!")

if __name__ == "__main__":
    test_make_a_pile()

# Generated at 2026-11-02 09:04:38.209325
# Unit test for function make_a_pile
def test_make_a_pile():
    # Test with a typical value
    assert module_0.make_a_pile(3) == [3, 5, 7]
    assert module_0.make_a_pile(1) == [1]
    assert module_0.make_a_pile(5) == [5, 7, 9, 11, 13]

    # Test edge case: zero
    assert module_0.make_a_pile(0) == []

    # Test with a larger value
    assert module_0.make_a_pile(10) == [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]

    # Test that each element is exactly 2 more than the previous
    result = module_0.make_a_pile(6)
    assert len(result) == 6
    for i in range(1, len(result)):
        assert result[i] - result[i - 1] == 2

    # Test first element equals n
    assert result[0] == 6

    print("All tests passed!")

test_make_a_pile()