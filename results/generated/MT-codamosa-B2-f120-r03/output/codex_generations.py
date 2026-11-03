

# Generated at 2026-11-02 18:30:03.747463
# Unit test for function maximum
def test_maximum():
    # Test k == 0 returns empty list
    assert module_0.maximum([1, 2, 3], 0) == []

    # Test basic case: k largest elements in ascending order
    assert module_0.maximum([1, 2, 3, 4, 5], 2) == [4, 5]

    # Test k equals array length
    assert module_0.maximum([3, 1, 2], 3) == [1, 2, 3]

    # Test k greater than array length
    assert module_0.maximum([3, 1, 2], 5) == [1, 2, 3]

    # Test with negative numbers
    assert module_0.maximum([-1, -5, 2, 0], 2) == [0, 2]

    # Test with duplicates
    assert module_0.maximum([5, 5, 5, 5], 2) == [5, 5]

    # Test single element array
    assert module_0.maximum([7], 1) == [7]

    # Test unsorted input returns sorted k largest
    assert module_0.maximum([9, 1, 8, 2, 7, 3], 3) == [7, 8, 9]

    # Test all negative numbers
    assert module_0.maximum([-10, -20, -30], 2) == [-20, -10]

    # Test empty array with k > 0
    assert module_0.maximum([], 3) == []

    print("All tests passed!")


if __name__ == "__main__":
    test_maximum()

# Generated at 2026-11-02 18:32:56.315375
# Unit test for function maximum
def test_maximum():
    # k == 0 should return an empty list
    assert module_0.maximum([1, 2, 3], 0) == []

    # Basic case: returns the k largest elements in ascending order
    assert module_0.maximum([1, 2, 3], 2) == [2, 3]
    assert module_0.maximum([-1, 5, 3, 2], 2) == [3, 5]

    # k equal to array length returns the whole (sorted) array
    assert module_0.maximum([-3, -4, 5], 3) == [-4, -3, 5]

    # k larger than array length returns the whole sorted array
    assert module_0.maximum([1, 2, 3], 5) == [1, 2, 3]

    # Duplicates are preserved
    assert module_0.maximum([4, -4, 4], 2) == [4, 4]

    # Single element result
    assert module_0.maximum([-3, 2, 1, 2, -1, -2, 1], 1) == [2]

    # Negative numbers only
    assert module_0.maximum([-10, -20, -30], 2) == [-20, -10]

    # Unsorted input gets sorted in the result
    assert module_0.maximum([9, 1, 8, 2, 7], 3) == [7, 8, 9]

    # k == 1 on single-element array
    assert module_0.maximum([42], 1) == [42]

    # Empty array with k == 0
    assert module_0.maximum([], 0) == []

    print("All tests passed!")


if __name__ == "__main__":
    test_maximum()

# Generated at 2026-11-02 18:35:08.340809
# Unit test for function maximum
def test_maximum():import unittest


class TestMaximum(unittest.TestCase):

    def test_k_zero_returns_empty(self):
        self.assertEqual(module_0.maximum([1, 2, 3], 0), [])

    def test_basic_case(self):
        self.assertEqual(module_0.maximum([-3, -4, 5], 3), [-4, -3, 5])

    def test_returns_k_largest_sorted(self):
        self.assertEqual(module_0.maximum([4, -4, 4], 2), [-4, 4])

    def test_k_equals_length(self):
        self.assertEqual(module_0.maximum([3, 1, 2], 3), [1, 2, 3])

    def test_k_one_returns_max(self):
        self.assertEqual(module_0.maximum([7, 2, 9, 4], 1), [9])

    def test_k_greater_than_length(self):
        self.assertEqual(module_0.maximum([2, 1], 5), [1, 2])

    def test_duplicates(self):
        self.assertEqual(module_0.maximum([5, 5, 5, 1], 2), [5, 5])

    def test_single_element(self):
        self.assertEqual(module_0.maximum([42], 1), [42])

    def test_negative_numbers(self):
        self.assertEqual(module_0.maximum([-10, -20, -30], 2), [-20, -10])

    def test_empty_array(self):
        self.assertEqual(module_0.maximum([], 3), [])

    def test_result_is_sorted_ascending(self):
        result = module_0.maximum([9, 1, 8, 2, 7, 3], 4)
        self.assertEqual(result, sorted(result))
        self.assertEqual(result, [2, 3, 7, 8])


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 18:36:34.696582
# Unit test for function maximum
def test_maximum():import unittest


class TestMaximum(unittest.TestCase):

    def test_k_zero_returns_empty_list(self):
        self.assertEqual(module_0.maximum([1, 2, 3], 0), [])

    def test_basic_case(self):
        self.assertEqual(module_0.maximum([-3, -4, 5], 1), [5])

    def test_k_equal_length(self):
        self.assertEqual(module_0.maximum([4, -4, 4], 3), [-4, 4, 4])

    def test_k_greater_than_length(self):
        self.assertEqual(module_0.maximum([2, 1], 5), [1, 2])

    def test_single_element(self):
        self.assertEqual(module_0.maximum([7], 1), [7])

    def test_duplicates(self):
        self.assertEqual(module_0.maximum([5, 5, 5, 1], 2), [5, 5])

    def test_negative_numbers(self):
        self.assertEqual(module_0.maximum([-1, -2, -3], 2), [-2, -1])

    def test_result_is_sorted_ascending(self):
        result = module_0.maximum([10, 3, 8, 1, 9], 3)
        self.assertEqual(result, [8, 9, 10])

    def test_already_sorted_input(self):
        self.assertEqual(module_0.maximum([1, 2, 3, 4], 2), [3, 4])

    def test_mixed_values(self):
        self.assertEqual(module_0.maximum([-5, 0, 5, -10, 10], 3), [0, 5, 10])


if __name__ == "__main__":
    unittest.main()