

# Generated at 2026-11-03 03:25:32.881571
# Unit test for function maximum
def test_maximum():
    # k == 0 returns an empty list
    assert module_0.maximum([1, 2, 3], 0) == []

    # k largest elements returned in ascending order
    assert module_0.maximum([1, 2, 3, 4, 5], 3) == [3, 4, 5]

    # k equals length of array (entire array sorted)
    assert module_0.maximum([5, 1, 3], 3) == [1, 3, 5]

    # array with duplicates
    assert module_0.maximum([4, -4, 4], 2) == [4, 4]

    # all negative numbers
    assert module_0.maximum([-5, -1, -3], 2) == [-3, -1]

    # single element array
    assert module_0.maximum([7], 1) == [7]

    # k = 1 returns the single largest element
    assert module_0.maximum([10, 2, 8], 1) == [10]

    # unsorted input with mixed values
    assert module_0.maximum([9, 1, 5, 7, 3], 4) == [3, 5, 7, 9]

    print("All tests passed!")


test_maximum()

# Generated at 2026-11-03 03:27:24.092681
# Unit test for function maximum
def test_maximum():import unittest


def module_0.maximum(arr, k):
    if k == 0:
        return []
    arr.sort()
    ans = arr[-k:]
    return ans


class TestMaximum(unittest.TestCase):

    def test_k_zero_returns_empty_list(self):
        self.assertEqual(module_0.maximum([1, 2, 3], 0), [])

    def test_basic_case(self):
        self.assertEqual(module_0.maximum([1, 2, 3, 4, 5], 3), [3, 4, 5])

    def test_k_equals_length(self):
        self.assertEqual(module_0.maximum([1, 2, 3], 3), [1, 2, 3])

    def test_k_one(self):
        self.assertEqual(module_0.maximum([5, 1, 9, 3], 1), [9])

    def test_unsorted_input(self):
        self.assertEqual(module_0.maximum([-10, 7, 3, 20, 4], 2), [7, 20])

    def test_with_duplicates(self):
        self.assertEqual(module_0.maximum([4, -4, 4, 1, 2], 2), [4, 4])

    def test_all_negative_numbers(self):
        self.assertEqual(module_0.maximum([-5, -2, -8, -1], 2), [-2, -1])

    def test_empty_array(self):
        self.assertEqual(module_0.maximum([], 1), [])

    def test_k_larger_than_array(self):
        # arr[-k:] with k > len returns whole sorted array
        self.assertEqual(module_0.maximum([3, 1, 2], 5), [1, 2, 3])

    def test_single_element_array(self):
        self.assertEqual(module_0.maximum([42], 1), [42])

    def test_result_is_sorted_ascending(self):
        result = module_0.maximum([9, 3, 7, 1, 8], 3)
        self.assertEqual(result, sorted(result))

    def test_input_array_is_modified_in_place(self):
        arr = [3, 1, 2]
        module_0.maximum(arr, 2)
        self.assertEqual(arr, [1, 2, 3])  # sort() mutates input


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-03 03:29:16.640751
# Unit test for function maximum
def test_maximum():
    # k == 0 returns an empty list
    assert module_0.maximum([1, 2, 3], 0) == []

    # Canonical cases: k largest elements returned in ascending order
    assert module_0.maximum([-3, -4, 5], 3) == [-4, -3, 5]
    assert module_0.maximum([4, -4, 4], 2) == [4, 4]
    assert module_0.maximum([-3, 2, 1, 2, -1, -2, 1], 1) == [2]

    # Unsorted input, k < len(arr)
    assert module_0.maximum([5, 1, 3, 2, 4], 3) == [3, 4, 5]

    # k equals len(arr): all elements returned, sorted
    assert module_0.maximum([3, 1, 2], 3) == [1, 2, 3]

    # k = 1 returns the single maximum element
    assert module_0.maximum([10, 20, 30], 1) == [30]

    # Duplicates are preserved
    assert module_0.maximum([1, 1, 1], 2) == [1, 1]

    # Single-element array
    assert module_0.maximum([7], 1) == [7]

    # All negative numbers
    assert module_0.maximum([-5, -1, -3], 2) == [-3, -1]

    # Mixed positive/negative with k = 2
    assert module_0.maximum([-1, 15, 0, -8, 7], 2) == [7, 15]

    print("All tests passed!")


if __name__ == "__main__":
    test_maximum()

# Generated at 2026-11-03 03:31:03.348246
# Unit test for function maximum
def test_maximum():
    # k == 0 should return an empty list
    assert module_0.maximum([-10, 9, 20, 3, 4, -3], 0) == []

    # k equal to length of array returns all elements sorted ascending
    assert module_0.maximum([-3, -4, 5], 3) == [-4, -3, 5]

    # k largest elements returned in ascending order
    assert module_0.maximum([4, -4, 3], 2) == [3, 4]

    # larger array, k = 3
    assert module_0.maximum([-10, 9, 20, 3, 4, -3], 3) == [4, 9, 20]

    # single element array
    assert module_0.maximum([7], 1) == [7]

    # duplicates handled correctly
    assert module_0.maximum([5, 5, 5, 5], 2) == [5, 5]

    # negative numbers only
    assert module_0.maximum([-5, -2, -9, -1], 2) == [-2, -1]

    # k larger than array length returns all elements sorted
    assert module_0.maximum([4, -4, 3], 5) == [-4, 3, 4]

    # mixed positive/negative with k = 1 returns the single largest
    assert module_0.maximum([10, -10, 0], 1) == [10]

# Generated at 2026-11-03 03:32:48.055542
# Unit test for function maximum
def test_maximum():import unittest


class TestMaximum(unittest.TestCase):
    def test_k_zero_returns_empty(self):
        self.assertEqual(module_0.maximum([-3, -4, 5], 0), [])

    def test_basic_case(self):
        self.assertEqual(module_0.maximum([-3, -4, 5], 3), [-4, -3, 5])

    def test_k_smaller_than_length(self):
        self.assertEqual(module_0.maximum([1, 2, 3, 4, 5], 2), [4, 5])

    def test_k_equals_length(self):
        self.assertEqual(module_0.maximum([10, 20, 30], 3), [10, 20, 30])

    def test_single_element(self):
        self.assertEqual(module_0.maximum([7], 1), [7])

    def test_duplicates(self):
        self.assertEqual(module_0.maximum([5, 5, 3, 5], 2), [5, 5])

    def test_negative_numbers(self):
        self.assertEqual(module_0.maximum([-10, -5, -1], 2), [-5, -1])

    def test_result_is_sorted_ascending(self):
        result = module_0.maximum([9, 1, 8, 2, 7], 3)
        self.assertEqual(result, sorted(result))
        self.assertEqual(result, [7, 8, 9])


if __name__ == "__main__":
    unittest.main()