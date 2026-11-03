

# Generated at 2026-11-03 03:41:46.001050
# Unit test for function strange_sort_list
def test_strange_sort_list():import unittest


class TestStrangeSortList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(module_0.strange_sort_list([]), [])

    def test_single_element(self):
        self.assertEqual(module_0.strange_sort_list([7]), [7])

    def test_two_elements(self):
        self.assertEqual(module_0.strange_sort_list([2, 1]), [1, 2])

    def test_already_sorted(self):
        self.assertEqual(module_0.strange_sort_list([1, 2, 3, 4]), [1, 4, 2, 3])

    def test_unsorted_input(self):
        self.assertEqual(module_0.strange_sort_list([3, 1, 2]), [1, 3, 2])

    def test_reverse_sorted(self):
        self.assertEqual(module_0.strange_sort_list([5, 4, 3, 2, 1]), [1, 5, 2, 4, 3])

    def test_duplicates(self):
        self.assertEqual(module_0.strange_sort_list([5, 5, 5, 5]), [5, 5, 5, 5])

    def test_negative_numbers(self):
        self.assertEqual(module_0.strange_sort_list([-1, 0, 1]), [-1, 1, 0])

    def test_mixed_negatives_and_positives(self):
        self.assertEqual(module_0.strange_sort_list([-3, 2, -1, 4]), [-3, 4, -1, 2])

    def test_odd_length(self):
        self.assertEqual(module_0.strange_sort_list([10, 20, 30]), [10, 30, 20])

    def test_result_length_matches_input(self):
        data = [8, 3, 5, 1, 9, 2]
        self.assertEqual(len(module_0.strange_sort_list(data)), len(data))


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-03 03:42:39.885905
# Unit test for function strange_sort_list
def test_strange_sort_list():
    # Empty list
    assert module_0.strange_sort_list([]) == []

    # Single element
    assert module_0.strange_sort_list([1]) == [1]
    assert module_0.strange_sort_list([42]) == [42]

    # Even-length list, already sorted
    assert module_0.strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]

    # Odd-length list
    assert module_0.strange_sort_list([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]

    # Unsorted input
    assert module_0.strange_sort_list([5, 1, 3, 2, 4]) == [1, 5, 2, 4, 3]

    # Duplicates
    assert module_0.strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    assert module_0.strange_sort_list([1, 1, 2, 2]) == [1, 2, 1, 2]

    # Negative numbers
    assert module_0.strange_sort_list([-2, -1, 0, 1]) == [-2, 1, -1, 0]
    assert module_0.strange_sort_list([-5, -3, -1]) == [-5, -1, -3]

    # Two elements
    assert module_0.strange_sort_list([7, 3]) == [3, 7]

    # Larger mixed list
    assert module_0.strange_sort_list([10, -1, 0, 3, 7, 2]) == [-1, 10, 0, 7, 2, 3]

    print("All tests passed!")


test_strange_sort_list()

# Generated at 2026-11-03 03:43:34.645509
# Unit test for function strange_sort_list
def test_strange_sort_list():
    # Typical case: alternating min/max
    assert module_0.strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert module_0.strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]

    # Empty list
    assert module_0.strange_sort_list([]) == []

    # Single element
    assert module_0.strange_sort_list([7]) == [7]

    # Two elements
    assert module_0.strange_sort_list([1, 2]) == [1, 2]
    assert module_0.strange_sort_list([2, 1]) == [1, 2]

    # Unsorted input with negatives
    assert module_0.strange_sort_list([-3, 4, -1, 2, 5]) == [-3, 5, -1, 4, 2]

    # Duplicates
    assert module_0.strange_sort_list([1, 1, 2, 2]) == [1, 2, 1, 2]

    # Already sorted input
    assert module_0.strange_sort_list([1, 2, 3]) == [1, 3, 2]

    # Reverse sorted input
    assert module_0.strange_sort_list([5, 4, 3, 2, 1]) == [1, 5, 2, 4, 3]

    # Result length preserved
    data = [9, 3, 7, 1, 8]
    assert len(module_0.strange_sort_list(data)) == len(data)

    print("All tests passed!")


test_strange_sort_list()

# Generated at 2026-11-03 03:44:58.407406
# Unit test for function strange_sort_list
def test_strange_sort_list():
    # Normal unsorted list
    assert module_0.strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert module_0.strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    
    # Single element
    assert module_0.strange_sort_list([7]) == [7]
    
    # Empty list
    assert module_0.strange_sort_list([]) == []
    
    # Two elements
    assert module_0.strange_sort_list([3, 1]) == [1, 3]
    
    # Duplicates mixed with other values
    assert module_0.strange_sort_list([1, 2, 2, 3]) == [1, 3, 2, 2]
    
    # Negative numbers
    assert module_0.strange_sort_list([-1, -5, 0, 3]) == [-5, 3, -1, 0]
    
    # Reverse sorted input
    assert module_0.strange_sort_list([5, 4, 3, 2, 1]) == [1, 5, 2, 4, 3]
    
    # Already sorted input
    assert module_0.strange_sort_list([1, 2, 3]) == [1, 3, 2]
    
    # Unsorted with larger range
    assert module_0.strange_sort_list([10, 2, 8, 4, 6]) == [2, 10, 4, 8, 6]
    
    # Verify result length matches input length
    assert len(module_0.strange_sort_list([9, 1, 8, 2, 7, 3])) == 6
    
    print("All test cases passed!")

# Run tests
test_strange_sort_list()

# Generated at 2026-11-03 03:47:03.134460
# Unit test for function strange_sort_list
def test_strange_sort_list():
    # Basic alternating min/max behavior
    assert module_0.strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert module_0.strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    assert module_0.strange_sort_list([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]

    # Edge cases
    assert module_0.strange_sort_list([]) == []
    assert module_0.strange_sort_list([1]) == [1]
    assert module_0.strange_sort_list([1, 2]) == [1, 2]
    assert module_0.strange_sort_list([2, 1]) == [1, 2]

    # Unsorted input
    assert module_0.strange_sort_list([3, 1, 2]) == [1, 3, 2]
    assert module_0.strange_sort_list([10, -5, 0, 7, 3]) == [-5, 10, 0, 7, 3]

    # Duplicates
    assert module_0.strange_sort_list([2, 2, 1, 1]) == [1, 2, 1, 2]

    # Negative numbers
    assert module_0.strange_sort_list([-3, -1, -2]) == [-3, -1, -2]

    # Floats
    assert module_0.strange_sort_list([1.5, 0.5, 2.5]) == [0.5, 2.5, 1.5]

    # Already sorted / reverse sorted
    assert module_0.strange_sort_list([1, 2, 3]) == [1, 3, 2]
    assert module_0.strange_sort_list([3, 2, 1]) == [1, 3, 2]

    # Result should contain same elements (multiset check)
    import random
    original = [random.randint(0, 100) for _ in range(20)]
    result = module_0.strange_sort_list(original.copy())
    assert sorted(result) == sorted(original)
    assert len(result) == len(original)