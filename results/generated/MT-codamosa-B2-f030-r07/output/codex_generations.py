

# Generated at 2026-11-03 04:09:16.575429
# Unit test for function get_positive
def test_get_positive():
    assert module_0.get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert module_0.get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
    assert module_0.get_positive([-1, -2, -4, -5, -6]) == []
    assert module_0.get_positive([]) == []
    assert module_0.get_positive([1, 2, 3]) == [1, 2, 3]
    assert module_0.get_positive([0, 0, 0]) == []
    assert module_0.get_positive([0.5, -0.5, 1.5]) == [0.5, 1.5]

# Generated at 2026-11-03 04:11:13.569093
# Unit test for function get_positive
def test_get_positive():
    assert module_0.get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert module_0.get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
    assert module_0.get_positive([-1, -2, -4, -5, -6]) == []
    assert module_0.get_positive([]) == []
    assert module_0.get_positive([1, 2, 3]) == [1, 2, 3]
    assert module_0.get_positive([0, 0, 0]) == []
    assert module_0.get_positive([-1.5, 2.5, -3.7, 4.2]) == [2.5, 4.2]
    assert module_0.get_positive([7]) == [7]
    assert module_0.get_positive([-7]) == []
    print("All tests passed!")


class TestGetPositive(unittest.TestCase):

    def test_mixed_values(self):
        self.assertEqual(module_0.get_positive([-1, 2, -4, 5, 6]), [2, 5, 6])

    def test_mixed_with_zero(self):
        self.assertEqual(
            module_0.get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]),
            [5, 3, 2, 3, 9, 123, 1]
        )

    def test_all_negative(self):
        self.assertEqual(module_0.get_positive([-1, -2, -4, -5, -6]), [])

    def test_empty_list(self):
        self.assertEqual(module_0.get_positive([]), [])

    def test_all_positive(self):
        self.assertEqual(module_0.get_positive([1, 2, 3]), [1, 2, 3])

    def test_all_zeros(self):
        self.assertEqual(module_0.get_positive([0, 0, 0]), [])

    def test_floats(self):
        self.assertEqual(module_0.get_positive([-1.5, 2.5, -3.7, 4.2]), [2.5, 4.2])

    def test_single_positive(self):
        self.assertEqual(module_0.get_positive([7]), [7])

    def test_single_negative(self):
        self.assertEqual(module_0.get_positive([-7]), [])

    def test_preserves_order(self):
        self.assertEqual(module_0.get_positive([3, -1, 1, -2, 2]), [3, 1, 2])

    def test_returns_list_type(self):
        self.assertIsInstance(module_0.get_positive([1, -1]), list)


if __name__ == "__main__":
    test_get_positive()
    unittest.main()

# Generated at 2026-11-03 04:12:33.924708
# Unit test for function get_positive
def test_get_positive():
    # Mixed positive and negative numbers
    assert module_0.get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert module_0.get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]

    # Only positive numbers
    assert module_0.get_positive([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # Only negative numbers
    assert module_0.get_positive([-1, -2, -3, -4, -5]) == []

    # Zero is not positive
    assert module_0.get_positive([0, 0, 0]) == []
    assert module_0.get_positive([-1, 0, 1]) == [1]

    # Empty list
    assert module_0.get_positive([]) == []

    # Single element lists
    assert module_0.get_positive([7]) == [7]
    assert module_0.get_positive([-7]) == []

    # Floats and mixed types
    assert module_0.get_positive([-1.5, 2.5, 0.0, 3.14]) == [2.5, 3.14]

    # Duplicates preserved
    assert module_0.get_positive([3, 3, -3, 3]) == [3, 3, 3]

    # Order preserved
    assert module_0.get_positive([10, -20, 30, -40, 50]) == [10, 30, 50]

    # Original list is not modified
    original = [-1, 2, -3, 4]
    copy_of_original = list(original)
    module_0.get_positive(original)
    assert original == copy_of_original

# Generated at 2026-11-03 04:13:31.232975
# Unit test for function get_positive
def test_get_positive():
    # Test with mixed positive, negative, and zero values
    assert module_0.get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    # Test with all positive numbers
    assert module_0.get_positive([1, 2, 3]) == [1, 2, 3]
    # Test with all negative numbers
    assert module_0.get_positive([-1, -2, -3]) == []
    # Test with empty list
    assert module_0.get_positive([]) == []
    # Test with zero (zero is not positive)
    assert module_0.get_positive([0, 1, -1]) == [1]
    # Test with floats
    assert module_0.get_positive([-1.5, 2.5, 0.0, 3.7]) == [2.5, 3.7]
    # Test with duplicates
    assert module_0.get_positive([3, -3, 3, 0, 3]) == [3, 3, 3]

# Generated at 2026-11-03 04:15:40.595925
# Unit test for function get_positive
def test_get_positive():
    # Mixed positive and negative numbers
    assert module_0.get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    # Mixed with zero (zero is not positive, should be excluded)
    assert module_0.get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
    # All negative numbers
    assert module_0.get_positive([-1, -2, -4, -5, -6]) == []
    # Empty list
    assert module_0.get_positive([]) == []
    # Single zero
    assert module_0.get_positive([0]) == []
    # All positive numbers
    assert module_0.get_positive([1, 2, 3]) == [1, 2, 3]
    # Floats
    assert module_0.get_positive([-1.5, 2.5, -3.3, 4.4]) == [2.5, 4.4]
    # Duplicates preserved
    assert module_0.get_positive([-2, 7, 7, -7, 7]) == [7, 7, 7]