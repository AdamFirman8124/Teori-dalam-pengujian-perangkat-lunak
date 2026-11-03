

# Generated at 2026-11-02 08:36:48.853970
# Unit test for function maximum
def test_maximum():
    # k == 0 returns empty list
    assert module_0.maximum([1, 2, 3], 0) == []

    # Basic case: k largest elements in ascending order
    assert module_0.maximum([1, 2, 3, 4, 5], 2) == [4, 5]
    assert module_0.maximum([5, 1, 3, 2, 4], 3) == [3, 4, 5]

    # k equal to array length returns all elements sorted
    assert module_0.maximum([3, 1, 2], 3) == [1, 2, 3]

    # k greater than array length returns all elements sorted
    assert module_0.maximum([2, 1], 5) == [1, 2]

    # Single element array
    assert module_0.maximum([7], 1) == [7]

    # Array with duplicates
    assert module_0.maximum([4, 4, 4, 4], 2) == [4, 4]
    assert module_0.maximum([1, 3, 3, 2, 3], 3) == [3, 3, 3]

    # Negative numbers
    assert module_0.maximum([-1, -5, -3], 2) == [-3, -1]
    assert module_0.maximum([-2, 5, -1, 0], 2) == [0, 5]

    # Mixed positive/negative with zero
    assert module_0.maximum([0, -10, 10], 1) == [10]

    # Unsorted input with floats
    assert module_0.maximum([2.5, 1.1, 3.3], 2) == [2.5, 3.3]

    # Empty array with k == 0
    assert module_0.maximum([], 0) == []

    # Result is sorted ascending even from unsorted input
    result = module_0.maximum([9, 1, 8, 2, 7], 4)
    assert result == sorted(result)
    assert result == [2, 7, 8, 9]

# Generated at 2026-11-02 08:37:43.225642
# Unit test for function maximum
def test_maximum():
    # nonce:2ff8a550
    assert module_0.maximum([-10, -8, -6, -4, -2], 3) == [-6, -4, -2]
    assert module_0.maximum([2, 4, 1, 3, 5], 2) == [4, 5]
    assert module_0.maximum([0, 0, 0, 0], 2) == [0, 0]
    assert module_0.maximum([1], 1) == [1]
    assert module_0.maximum([3, 1, 2], 0) == []
    assert module_0.maximum([1, 2, 3], 3) == [1, 2, 3]
    assert module_0.maximum([5, 5, 5, 5], 3) == [5, 5, 5]
    assert module_0.maximum([7, 1, 9, 3, 8], 4) == [3, 7, 8, 9]
    assert module_0.maximum([-1, -5, -3], 1) == [-1]

test_maximum()
print("All tests passed!")

# Generated at 2026-11-02 08:38:38.627586
# Unit test for function maximum
def test_maximum():
    # k == 0 returns empty list
    assert module_0.maximum([1, 2, 3], 0) == []
    assert module_0.maximum([], 0) == []

    # basic cases
    assert module_0.maximum([-1, 15, 12, 17, -18], 3) == [12, 15, 17]
    assert module_0.maximum([1, 2, 3], 2) == [2, 3]
    assert module_0.maximum([5, 1, 3, 4, 2], 1) == [5]
    assert module_0.maximum([3, 1, 2], 3) == [1, 2, 3]

    # k larger than array length returns all elements sorted
    assert module_0.maximum([4, -4, 6], 5) == [-4, 4, 6]
    assert module_0.maximum([], 3) == []

    # duplicates
    assert module_0.maximum([2, 2, 2, 2], 2) == [2, 2]
    assert module_0.maximum([1, 3, 3, 2], 2) == [3, 3]

    # negative numbers
    assert module_0.maximum([-5, -1, -3], 2) == [-3, -1]

    # single element arrays
    assert module_0.maximum([7], 1) == [7]

    # result is sorted ascending
    result = module_0.maximum([10, 9, 8, 7, 6], 3)
    assert result == sorted(result) == [8, 9, 10]

    print("All tests passed!")


test_maximum()

# Generated at 2026-11-02 08:39:46.422704
# Unit test for function maximum
def test_maximum():
# nonce:de0bd8d8
    # k == 0 returns empty list
    assert module_0.maximum([1, 2, 3, 4, 5], 0) == []

    # Basic case: top k elements in ascending order
    assert module_0.maximum([1, 2, 3, 4, 5], 2) == [4, 5]
    assert module_0.maximum([1, 2, 3, 4, 5], 3) == [3, 4, 5]

    # k equals array length: returns fully sorted array
    assert module_0.maximum([5, 1, 3, 2, 4], 5) == [1, 2, 3, 4, 5]

    # Unsorted input with negatives
    assert module_0.maximum([-5, 3, 0, -1, 8], 3) == [0, 3, 8]

    # Duplicates
    assert module_0.maximum([7, 7, 7, 7], 2) == [7, 7]
    assert module_0.maximum([4, -4, 4, 0], 2) == [0, 4]

    # Single element array
    assert module_0.maximum([10], 1) == [10]

    # k larger than array length: returns all elements sorted
    assert module_0.maximum([3, 1, 2], 10) == [1, 2, 3]

    # k == 1 returns the single maximum element
    assert module_0.maximum([5, -2, 9, 1], 1) == [9]

    # All negative numbers
    assert module_0.maximum([-10, -3, -7, -1], 2) == [-3, -1]

    # Input with mixed positives and zero
    assert module_0.maximum([0, -1, 2, -3, 4], 4) == [-1, 0, 2, 4]

# Generated at 2026-11-02 08:40:19.805298
# Unit test for function maximum
def test_maximum():import unittest


class TestMaximum(unittest.TestCase):

    def test_k_zero_returns_empty(self):
        self.assertEqual(module_0.maximum([1, 2, 3], 0), [])

    def test_k_equals_length(self):
        self.assertEqual(module_0.maximum([-3, -4, 5], 3), [-4, -3, 5])

    def test_returns_k_largest_sorted(self):
        self.assertEqual(module_0.maximum([4, -4, 5], 2), [4, 5])

    def test_single_largest(self):
        self.assertEqual(module_0.maximum([-3, 2, 1, 4], 1), [4])

    def test_negative_numbers(self):
        self.assertEqual(module_0.maximum([-5, -1, -3], 2), [-3, -1])

    def test_duplicates(self):
        self.assertEqual(module_0.maximum([3, 3, 3], 2), [3, 3])

    def test_single_element_array(self):
        self.assertEqual(module_0.maximum([7], 1), [7])

    def test_k_larger_than_length(self):
        self.assertEqual(module_0.maximum([1, 2], 5), [1, 2])

    def test_result_is_ascending(self):
        result = module_0.maximum([10, 2, 8, 4, 6], 3)
        self.assertEqual(result, sorted(result))
        self.assertEqual(result, [6, 8, 10])


if __name__ == "__main__":
    unittest.main()