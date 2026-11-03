

# Generated at 2026-11-02 06:41:48.265532
# Unit test for function maximum
def test_maximum():
    # k == 0 returns empty list
    assert module_0.maximum([1, 2, 3], 0) == []
    # basic case: k largest elements in ascending order
    assert module_0.maximum([-1, 2, -4, 5, 6], 3) == [2, 5, 6]
    assert module_0.maximum([5, -2, 3, 4, -1], 2) == [4, 5]
    # all negative numbers
    assert module_0.maximum([-1, -2, -3], 1) == [-1]
    assert module_0.maximum([-1, -2, -3], 2) == [-2, -1]
    # k equals array length
    assert module_0.maximum([3, 1, 2], 3) == [1, 2, 3]
    # k larger than array length returns all elements sorted
    assert module_0.maximum([3, 1, 2], 5) == [1, 2, 3]
    # single element
    assert module_0.maximum([7], 1) == [7]
    # duplicates
    assert module_0.maximum([4, 4, 4], 2) == [4, 4]
    # empty array with k > 0
    assert module_0.maximum([], 2) == []

if __name__ == "__main__":
    test_maximum()
    print("All tests passed!")

# Generated at 2026-11-02 06:43:30.152750
# Unit test for function maximum
def test_maximum():import unittest


class TestMaximum(unittest.TestCase):

    def test_k_zero_returns_empty(self):
        self.assertEqual(module_0.maximum([1, 2, 3], 0), [])

    def test_basic_case(self):
        self.assertEqual(module_0.maximum([-3, -4, 5], 3), [-4, -3, 5])

    def test_k_larger_than_array(self):
        # arr[-k:] with k > len returns whole sorted array
        self.assertEqual(module_0.maximum([4, -4, 4], 2), [-4, 4])

    def test_k_equal_length(self):
        self.assertEqual(module_0.maximum([1, 2, 3], 3), [1, 2, 3])

    def test_k_one_returns_largest(self):
        self.assertEqual(module_0.maximum([5, 1, 9, 3], 1), [9])

    def test_duplicates(self):
        self.assertEqual(module_0.maximum([2, 2, 2, 2], 2), [2, 2])

    def test_negative_numbers(self):
        self.assertEqual(module_0.maximum([-1, -5, -3], 2), [-3, -1])

    def test_empty_array(self):
        self.assertEqual(module_0.maximum([], 0), [])
        self.assertEqual(module_0.maximum([], 3), [])

    def test_single_element(self):
        self.assertEqual(module_0.maximum([7], 1), [7])

    def test_result_is_sorted_ascending(self):
        result = module_0.maximum([10, 1, 8, 3, 6], 3)
        self.assertEqual(result, sorted(result))
        self.assertEqual(result, [6, 8, 10])

    def test_mixed_values(self):
        self.assertEqual(module_0.maximum([0, -10, 5, 100, -50, 42], 3), [5, 42, 100])


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 06:45:41.820106
# Unit test for function maximum
def test_maximum():
# nonce:25277ef1
    # k == 0 returns an empty list
    assert module_0.maximum([1, 2, 3], 0) == []
    assert module_0.maximum([], 0) == []

    # k equals array length -> whole array, sorted ascending
    assert module_0.maximum([-3, -4, 5], 3) == [-4, -3, 5]

    # k smaller than array length -> k largest elements, sorted ascending
    assert module_0.maximum([4, -4, 5], 2) == [-4, 5]
    assert module_0.maximum([-3, 2, 1, 2, -1, -2, 1], 1) == [2]
    assert module_0.maximum([2, -7, 8, -1, 3, -10, 2, -2, -6, 5, 3, 2, -4, 1], 5) == [2, 3, 3, 5, 8]

    # duplicates are preserved
    assert module_0.maximum([5, 5, 5, 1], 2) == [5, 5]

    # k larger than array length returns all elements sorted
    assert module_0.maximum([4, -4, 5], 4) == [-4, 4, 5]

    # single-element array
    assert module_0.maximum([7], 1) == [7]

    # all-negative values
    assert module_0.maximum([-5, -2, -9], 2) == [-5, -2]

# Generated at 2026-11-02 06:46:43.974233
# Unit test for function maximum
def test_maximum():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMaximum)
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    return result.wasSuccessful()

if __name__ == "__main__":
    test_maximum()

# Generated at 2026-11-02 06:47:19.106365
# Unit test for function maximum
def test_maximum():
    assert module_0.maximum([1, 2, 3, 4, 5], 3) == [3, 4, 5]
    assert module_0.maximum([1, 2, 3, 4, 5], 0) == []
    assert module_0.maximum([5, 1, 3], 2) == [3, 5]
    assert module_0.maximum([-1, -2, -3], 2) == [-2, -1]
    assert module_0.maximum([7], 1) == [7]
    assert module_0.maximum([10, 10, 10], 2) == [10, 10]