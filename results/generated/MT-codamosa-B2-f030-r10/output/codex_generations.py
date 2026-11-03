

# Generated at 2026-11-03 01:43:38.212784
# Unit test for function get_positive
def test_get_positive():
    # Basic mixed list
    assert module_0.get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    # All positive numbers
    assert module_0.get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
    # All negative numbers
    assert module_0.get_positive([-1, -2, -4, -5, -6]) == []
    # Empty list
    assert module_0.get_positive([]) == []
    # Includes zero (zero is not positive)
    assert module_0.get_positive([0, 1, 0, -1]) == [1]
    # Floats and ints mixed
    assert module_0.get_positive([-1.5, 2.5, 3, -0.1]) == [2.5, 3]
    # Single positive element
    assert module_0.get_positive([42]) == [42]
    # Duplicates preserved
    assert module_0.get_positive([1, 1, 2, -2, 1]) == [1, 1, 2, 1]
    # Order preserved
    assert module_0.get_positive([-5, 10, -15, 20]) == [10, 20]

# Generated at 2026-11-03 01:44:57.587665
# Unit test for function get_positive
def test_get_positive():
    # Basic case: mixed positive and negative numbers
    assert module_0.get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]

    # Only positive numbers
    assert module_0.get_positive([1, 2, 3]) == [1, 2, 3]

    # Only negative numbers
    assert module_0.get_positive([-1, -2, -3]) == []

    # Empty list
    assert module_0.get_positive([]) == []

    # Zero is not positive
    assert module_0.get_positive([0, 1, -1]) == [1]

    # Floats included
    assert module_0.get_positive([-1.5, 2.5, 0.0, 3.1]) == [2.5, 3.1]

    # Duplicates preserved
    assert module_0.get_positive([3, -3, 3]) == [3, 3]

    # Order preserved
    assert module_0.get_positive([5, -2, 1, -7, 4]) == [5, 1, 4]

    print("All tests passed!")

# Generated at 2026-11-03 01:46:12.020331
# Unit test for function get_positive
def test_get_positive():
    # Basic case with mixed positive and negative integers
    assert module_0.get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]

    # All positive numbers
    assert module_0.get_positive([1, 2, 3, 4]) == [1, 2, 3, 4]

    # All negative numbers
    assert module_0.get_positive([-1, -2, -3]) == []

    # Empty list
    assert module_0.get_positive([]) == []

    # Zero is not positive
    assert module_0.get_positive([0, 1, -1]) == [1]

    # Mixed with floats
    assert module_0.get_positive([-1.5, 2.5, 0.0, 3]) == [2.5, 3]

    # Duplicates preserved
    assert module_0.get_positive([5, -5, 5]) == [5, 5]

    # Single element cases
    assert module_0.get_positive([7]) == [7]
    assert module_0.get_positive([-7]) == []

    print("All tests passed!")


if __name__ == "__main__":
    test_get_positive()

# Generated at 2026-11-03 01:47:49.607743
# Unit test for function get_positive
def test_get_positive():
    # Basic mixed case
    assert module_0.get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert module_0.get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]

    # Empty list
    assert module_0.get_positive([]) == []

    # All negative numbers
    assert module_0.get_positive([-1, -2, -3, -4]) == []

    # All positive numbers
    assert module_0.get_positive([1, 2, 3, 4]) == [1, 2, 3, 4]

    # Zero is not positive
    assert module_0.get_positive([0, 0, 0]) == []
    assert module_0.get_positive([0, 1, -1, 0]) == [1]

    # Single element lists
    assert module_0.get_positive([7]) == [7]
    assert module_0.get_positive([-7]) == []

    # Floats
    assert module_0.get_positive([-1.5, 2.5, 3.0, -0.1]) == [2.5, 3.0]
    assert module_0.get_positive([0.1]) == [0.1]

    # Duplicates preserved
    assert module_0.get_positive([2, 2, -2, 2]) == [2, 2, 2]

    # Order is preserved
    assert module_0.get_positive([-5, 10, -3, 20, -1, 30]) == [10, 20, 30]

# Generated at 2026-11-03 01:49:26.068263
# Unit test for function get_positive
def test_get_positive():
    assert module_0.get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert module_0.get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
    assert module_0.get_positive([-1, -2, -4, -5, -6]) == []
    assert module_0.get_positive([]) == []
    assert module_0.get_positive([0]) == []
    assert module_0.get_positive([1, 2, 3]) == [1, 2, 3]
    assert module_0.get_positive([-5, 0, 5]) == [5]
    assert module_0.get_positive([1.5, -2.5, 3.7]) == [1.5, 3.7]


class TestGetPositive(unittest.TestCase):
    def test_mixed_values(self):
        self.assertEqual(module_0.get_positive([-1, 2, -4, 5, 6]), [2, 5, 6])

    def test_all_negative(self):
        self.assertEqual(module_0.get_positive([-1, -2, -4, -5, -6]), [])

    def test_empty_list(self):
        self.assertEqual(module_0.get_positive([]), [])

    def test_zero_excluded(self):
        self.assertEqual(module_0.get_positive([0, -3, 7]), [7])

    def test_all_positive(self):
        self.assertEqual(module_0.get_positive([1, 2, 3]), [1, 2, 3])

    def test_floats(self):
        self.assertEqual(module_0.get_positive([1.5, -2.5, 3.7]), [1.5, 3.7])


if __name__ == "__main__":
    unittest.main()