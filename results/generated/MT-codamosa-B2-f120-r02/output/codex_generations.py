

# Generated at 2026-11-03 03:34:30.281644
# Unit test for function maximum
def test_maximum():
    # k == 0 should return an empty list
    assert module_0.maximum([1, 2, 3], 0) == []

    # Basic case: k largest elements in ascending order
    assert module_0.maximum([1, 2, 3, 4, 5], 3) == [3, 4, 5]

    # k equals array length
    assert module_0.maximum([5, 1, 3], 3) == [1, 3, 5]

    # k larger than array length returns all elements sorted
    assert module_0.maximum([5, 1, 3], 10) == [1, 3, 5]

    # Array with negative numbers
    assert module_0.maximum([-1, -5, -3, 2], 2) == [-3, 2]

    # Array with duplicates
    assert module_0.maximum([4, 4, 4, 1], 2) == [4, 4]

    # Single element array
    assert module_0.maximum([7], 1) == [7]

    # Unsorted input with mixed values
    assert module_0.maximum([10, -2, 8, 0, 15, 3], 4) == [3, 8, 10, 15]

    # Two elements, k = 1
    assert module_0.maximum([100, 50], 1) == [100]

    # Empty array with k > 0
    assert module_0.maximum([], 2) == []

# Generated at 2026-11-03 03:37:06.341177
# Unit test for function maximum
def test_maximum():import unittest


class TestMaximum(unittest.TestCase):
    def test_k_zero_returns_empty(self):
        self.assertEqual(module_0.maximum([1, 2, 3], 0), [])

    def test_basic_case(self):
        self.assertEqual(module_0.maximum([-3, -4, 5], 3), [-4, -3, 5])

    def test_k_one(self):
        self.assertEqual(module_0.maximum([4, -4, 4], 2), [-4, 4])

    def test_k_larger_than_length(self):
        self.assertEqual(module_0.maximum([1, 2], 5), [1, 2])

    def test_duplicates(self):
        self.assertEqual(module_0.maximum([5, 5, 5, 1], 2), [5, 5])

    def test_negative_numbers(self):
        self.assertEqual(module_0.maximum([-1, -5, -3], 2), [-3, -1])

    def test_empty_array(self):
        self.assertEqual(module_0.maximum([], 3), [])

    def test_sorted_result_ascending(self):
        self.assertEqual(module_0.maximum([9, 1, 8, 2, 7, 3], 3), [7, 8, 9])

    def test_single_element(self):
        self.assertEqual(module_0.maximum([42], 1), [42])

    def test_mixed_values(self):
        self.assertEqual(module_0.maximum([10, -10, 0, 7, -3], 3), [0, 7, 10])


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-03 03:38:24.283688
# Unit test for function maximum
def test_maximum():import unittest


class TestMaximum(unittest.TestCase):

    def test_k_zero_returns_empty(self):
        self.assertEqual(module_0.maximum([3, 1, 2], 0), [])

    def test_k_equals_full_array(self):
        self.assertEqual(module_0.maximum([5, 2, 8, 1], 4), [1, 2, 5, 8])

    def test_returns_k_largest_ascending(self):
        self.assertEqual(module_0.maximum([4, -4, 2, 0, 10], 3), [2, 4, 10])

    def test_single_element(self):
        self.assertEqual(module_0.maximum([7], 1), [7])

    def test_duplicates(self):
        self.assertEqual(module_0.maximum([3, 3, 3, 3], 2), [3, 3])

    def test_negative_numbers(self):
        self.assertEqual(module_0.maximum([-10, -5, -1, -20], 2), [-5, -1])

    def test_k_one_returns_max(self):
        self.assertEqual(module_0.maximum([9, 12, 4, 8], 1), [12])

    def test_input_is_sorted_in_place(self):
        arr = [3, 1, 2]
        module_0.maximum(arr, 2)
        self.assertEqual(arr, [1, 2, 3])

    def test_empty_array_k_zero(self):
        self.assertEqual(module_0.maximum([], 0), [])

    def test_result_is_list(self):
        self.assertIsInstance(module_0.maximum([1, 2, 3], 2), list)


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-03 03:39:50.181327
# Unit test for function maximum
def test_maximum():import unittest


def module_0.maximum(arr, k):
    if k == 0:
        return []
    arr.sort()
    ans = arr[-k:]
    return ans


class TestMaximum(unittest.TestCase):

    def test_k_zero_returns_empty(self):
        self.assertEqual(module_0.maximum([1, 2, 3], 0), [])

    def test_basic_case(self):
        self.assertEqual(module_0.maximum([-3, -4, 5], 3), [-4, -3, 5])

    def test_k_smaller_than_length(self):
        self.assertEqual(module_0.maximum([4, -4, 4], 2), [4, 4])

    def test_k_equals_length(self):
        self.assertEqual(module_0.maximum([1, 2, 3], 3), [1, 2, 3])

    def test_k_larger_than_length(self):
        self.assertEqual(module_0.maximum([2, 1], 5), [1, 2])

    def test_single_element(self):
        self.assertEqual(module_0.maximum([7], 1), [7])

    def test_duplicates(self):
        self.assertEqual(module_0.maximum([5, 5, 5, 5], 2), [5, 5])

    def test_negative_numbers(self):
        self.assertEqual(module_0.maximum([-1, -5, -3], 2), [-5, -3])

    def test_empty_array(self):
        self.assertEqual(module_0.maximum([], 1), [])

    def test_result_is_sorted_ascending(self):
        result = module_0.maximum([9, 1, 8, 2, 7], 3)
        self.assertEqual(result, sorted(result))
        self.assertEqual(result, [7, 8, 9])

    def test_modifies_original_arr(self):
        arr = [3, 1, 2]
        module_0.maximum(arr, 2)
        self.assertEqual(arr, [1, 2, 3])  # sort is in-place


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-03 03:40:56.536373
# Unit test for function maximum
def test_maximum():
    # k == 0 returns an empty list
    assert module_0.maximum([1, 2, 3], 0) == []

    # k equals array length: returns sorted full array
    assert module_0.maximum([-3, -4, 5], 3) == [-4, -3, 5]

    # k less than array length: returns k largest in ascending order
    assert module_0.maximum([4, -4, 5], 2) == [4, 5]

    # k == 1 returns single largest element
    assert module_0.maximum([1, 2, 3, 4, 5], 1) == [5]

    # k == full length returns entire sorted array
    assert module_0.maximum([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]

    # duplicates are preserved
    assert module_0.maximum([5, 5, 3], 2) == [5, 5]

    # all negative numbers
    assert module_0.maximum([-1, -5, -3], 2) == [-3, -1]

    # single-element array
    assert module_0.maximum([7], 1) == [7]

    # unsorted input with mixed values
    assert module_0.maximum([10, 2, 8, 4, 6], 3) == [6, 8, 10]

    # k exceeding array length returns all elements sorted
    assert module_0.maximum([1, 2], 3) == [1, 2]