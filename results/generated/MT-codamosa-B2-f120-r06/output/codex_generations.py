

# Generated at 2026-11-02 21:42:59.072771
# Unit test for function maximum
def test_maximum():
    # k == 0 returns empty list
    assert module_0.maximum([1, 2, 3], 0) == []
    assert module_0.maximum([], 0) == []

    # Basic cases: k largest elements in ascending order
    assert module_0.maximum([-1, -2, -3], 2) == [-2, -1]
    assert module_0.maximum([1, 2, 3, 4, 5], 3) == [3, 4, 5]
    assert module_0.maximum([5, 1, 3, 2, 4], 2) == [4, 5]
    assert module_0.maximum([10, 20, 30], 1) == [30]

    # Duplicates
    assert module_0.maximum([3, 3, 3, 3], 2) == [3, 3]
    assert module_0.maximum([1, 2, 2, 3], 3) == [2, 2, 3]

    # Negative numbers and mixed values
    assert module_0.maximum([-5, 0, 5, -10], 2) == [0, 5]
    assert module_0.maximum([-1, -5, -3], 3) == [-5, -3, -1]

    # k equals array length
    assert module_0.maximum([4, -4, 0], 3) == [-4, 0, 4]

    # k larger than array length returns all elements sorted
    assert module_0.maximum([2, 1], 5) == [1, 2]

    # Single element
    assert module_0.maximum([7], 1) == [7]

    # Empty array with k > 0
    assert module_0.maximum([], 3) == []

    # Floats
    assert module_0.maximum([1.5, 2.5, 0.5], 2) == [1.5, 2.5]

    print("All tests passed!")


if __name__ == "__main__":
    test_maximum()

# Generated at 2026-11-02 21:45:00.719635
# Unit test for function maximum
def test_maximum():
    # k == 0 returns empty list
    assert module_0.maximum([1, 2, 3], 0) == []
    
    # k equals array length returns all elements sorted
    assert module_0.maximum([3, 1, 2], 3) == [1, 2, 3]
    
    # k larger than array length returns sorted array
    assert module_0.maximum([5, 2, 8], 10) == [2, 5, 8]
    
    # typical case: k largest elements in ascending order
    assert module_0.maximum([1, 5, 3, 9, 7], 2) == [7, 9]
    
    # k == 1 returns single largest element
    assert module_0.maximum([4, -1, 10, 3], 1) == [10]
    
    # duplicates handled correctly
    assert module_0.maximum([2, 2, 2, 2], 2) == [2, 2]
    assert module_0.maximum([5, 1, 5, 1, 5], 3) == [1, 5, 5]
    
    # negative numbers
    assert module_0.maximum([-1, -5, -3], 2) == [-3, -1]
    
    # single-element array
    assert module_0.maximum([7], 1) == [7]
    
    # already sorted input
    assert module_0.maximum([1, 2, 3, 4], 2) == [3, 4]
    
    # floats work too
    assert module_0.maximum([1.5, 0.5, 2.5], 2) == [1.5, 2.5]

test_maximum()
print("All tests passed!")

# Generated at 2026-11-02 21:46:40.544712
# Unit test for function maximum
def test_maximum():
    # k == 0 returns empty list
    assert module_0.maximum([1, 2, 3], 0) == []

    # Basic case: k largest elements in sorted (ascending) order
    assert module_0.maximum([1, 2, 3, 4, 5], 3) == [3, 4, 5]

    # k equals array length
    assert module_0.maximum([1, 2, 3], 3) == [1, 2, 3]

    # k greater than array length returns all elements
    assert module_0.maximum([1], 5) == [1]

    # Array with negative numbers
    assert module_0.maximum([-1, -5, -3, 2], 2) == [-3, 2]

    # Array with duplicates
    assert module_0.maximum([5, 5, 5, 1], 2) == [5, 5]

    # Single element array
    assert module_0.maximum([7], 1) == [7]

    # Unsorted input array
    assert module_0.maximum([9, 1, 8, 2, 7], 2) == [8, 9]

    # Empty array with k == 0
    assert module_0.maximum([], 0) == []

# Generated at 2026-11-02 21:48:06.090813
# Unit test for function maximum
def test_maximum():import unittest


class TestMaximum(unittest.TestCase):

    def test_k_zero_returns_empty_list(self):
        self.assertEqual(module_0.maximum([1, 2, 3], 0), [])

    def test_basic_case(self):
        self.assertEqual(module_0.maximum([1, 2, 3, 4, 5], 3), [3, 4, 5])

    def test_k_equals_length(self):
        self.assertEqual(module_0.maximum([4, -4, 4], 3), [-4, 4, 4])

    def test_k_greater_than_length(self):
        self.assertEqual(module_0.maximum([1, 2], 5), [1, 2])

    def test_single_element(self):
        self.assertEqual(module_0.maximum([7], 1), [7])

    def test_empty_array(self):
        self.assertEqual(module_0.maximum([], 3), [])

    def test_with_duplicates(self):
        self.assertEqual(module_0.maximum([5, 5, 3, 5], 2), [5, 5])

    def test_negative_numbers(self):
        self.assertEqual(module_0.maximum([-10, -20, -30], 2), [-20, -10])

    def test_unsorted_input(self):
        self.assertEqual(module_0.maximum([9, 1, 8, 2, 7], 2), [8, 9])

    def test_result_is_sorted_ascending(self):
        result = module_0.maximum([3, 1, 4, 1, 5, 9, 2, 6], 4)
        self.assertEqual(result, sorted(result))

    def test_k_one_returns_max(self):
        self.assertEqual(module_0.maximum([3, 7, 1, 9, 4], 1), [9])

    def test_input_is_sorted_in_place(self):
        arr = [5, 2, 8, 1]
        module_0.maximum(arr, 2)
        self.assertEqual(arr, [1, 2, 5, 8])


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 21:49:25.433189
# Unit test for function maximum
def test_maximum():
    # k == 0 returns an empty list
    assert module_0.maximum([1, 2, 3], 0) == []

    # basic case: returns k largest elements in ascending order
    assert module_0.maximum([1, 2, 3, 4, 5], 2) == [4, 5]
    assert module_0.maximum([1, 2, 3, 4, 5], 3) == [3, 4, 5]

    # unsorted input array
    assert module_0.maximum([9, 1, 8, 2, 7], 2) == [8, 9]

    # negative numbers
    assert module_0.maximum([-1, -5, -3, -2], 2) == [-3, -2]

    # duplicates
    assert module_0.maximum([5, 5, 3, 3, 5], 2) == [5, 5]

    # k equals length of array -> all elements sorted ascending
    assert module_0.maximum([3, 1, 2], 3) == [1, 2, 3]

    # k greater than length of array -> all elements sorted ascending
    assert module_0.maximum([3, 1, 2], 5) == [1, 2, 3]

    # single element array
    assert module_0.maximum([7], 1) == [7]

    # k == 0 on empty array
    assert module_0.maximum([], 0) == []