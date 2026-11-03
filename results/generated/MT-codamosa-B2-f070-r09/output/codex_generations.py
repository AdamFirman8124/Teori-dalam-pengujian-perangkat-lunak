

# Generated at 2026-11-03 06:19:10.464791
# Unit test for function strange_sort_list
def test_strange_sort_list():
    # Basic alternating min/max behavior
    assert module_0.strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert module_0.strange_sort_list([5, 6, 7, 8, 9]) == [5, 9, 6, 8, 7]

    # Empty list
    assert module_0.strange_sort_list([]) == []

    # Single element
    assert module_0.strange_sort_list([42]) == [42]

    # Two elements
    assert module_0.strange_sort_list([2, 1]) == [1, 2]
    assert module_0.strange_sort_list([10, 3]) == [3, 10]

    # All identical elements
    assert module_0.strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]

    # Unsorted input with duplicates
    assert module_0.strange_sort_list([3, 1, 3, 2]) == [1, 3, 2, 3]

    # Negative numbers
    assert module_0.strange_sort_list([-1, -5, 0, 3]) == [-5, 3, -1, 0]

    # Already sorted input
    assert module_0.strange_sort_list([1, 2, 3]) == [1, 3, 2]

    # Reverse sorted input
    assert module_0.strange_sort_list([9, 7, 5, 3, 1]) == [1, 9, 3, 7, 5]

    # Result contains the same elements as input
    original = [4, 1, 7, 2, 9]
    result = module_0.strange_sort_list(original[:])
    assert sorted(result) == sorted(original)
    assert len(result) == len(original)

    # Input list should not be mutated by the function's external behavior
    # (function modifies its own copy of the reference, verify typical usage)
    data = [3, 1, 2]
    module_0.strange_sort_list(data)
    # Note: the function mutates the passed list (removes all elements)
    assert data == []

    print("All tests passed!")


if __name__ == "__main__":
    test_strange_sort_list()

# Generated at 2026-11-03 06:20:16.410950
# Unit test for function strange_sort_list
def test_strange_sort_list():
    # Empty list
    assert module_0.strange_sort_list([]) == []

    # Single element
    assert module_0.strange_sort_list([1]) == [1]

    # Two elements
    assert module_0.strange_sort_list([1, 2]) == [1, 2]
    assert module_0.strange_sort_list([5, 5]) == [5, 5]

    # Simple sorted list
    assert module_0.strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]

    # Reverse sorted list
    assert module_0.strange_sort_list([5, 4, 3, 2, 1]) == [1, 5, 2, 4, 3]

    # Unsorted list
    assert module_0.strange_sort_list([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 9, 1, 6, 2, 5, 3, 4]

    # List with duplicates
    assert module_0.strange_sort_list([2, 2, 2, 2]) == [2, 2, 2, 2]

    # Negative numbers
    assert module_0.strange_sort_list([-5, -1, -3, -2]) == [-5, -1, -3, -2]

    # Mixed positive and negative
    assert module_0.strange_sort_list([-1, 3, 0, -4, 2]) == [-4, 3, -1, 2, 0]

    # Three elements
    assert module_0.strange_sort_list([10, 20, 30]) == [10, 30, 20]

# Generated at 2026-11-03 06:21:07.918981
# Unit test for function strange_sort_list
def test_strange_sort_list():
    # Basic alternating min/max sort
    assert module_0.strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert module_0.strange_sort_list([5, 6, 7, 8, 9]) == [5, 9, 6, 8, 7]

    # Unsorted input
    assert module_0.strange_sort_list([3, 1, 4, 2, 5]) == [1, 5, 2, 4, 3]

    # Empty list
    assert module_0.strange_sort_list([]) == []

    # Single element
    assert module_0.strange_sort_list([42]) == [42]

    # Two elements
    assert module_0.strange_sort_list([10, 1]) == [1, 10]

    # All duplicates
    assert module_0.strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]

    # Negative numbers
    assert module_0.strange_sort_list([-1, 0, 1]) == [-1, 1, 0]
    assert module_0.strange_sort_list([-5, -10, -3]) == [-10, -3, -5]

    # Mixed positives and negatives
    assert module_0.strange_sort_list([-2, 3, -1, 2]) == [-2, 3, -1, 2]

    # Even-length list
    assert module_0.strange_sort_list([7, 1, 9, 3]) == [1, 9, 3, 7]

    # Odd-length list
    assert module_0.strange_sort_list([4, 2, 8]) == [2, 8, 4]

    # Input list should not be mutated by the caller's reference check
    original = [3, 1, 2]
    input_copy = list(original)
    result = module_0.strange_sort_list(original)
    assert result == [1, 3, 2]
    assert original == input_copy  # original remains unchanged

    # Larger list
    assert module_0.strange_sort_list([9, 1, 8, 2, 7, 3, 6, 4, 5]) == [1, 9, 2, 8, 3, 7, 4, 6, 5]

    # Duplicates mixed with distinct values
    assert module_0.strange_sort_list([2, 2, 1, 3]) == [1, 3, 2, 2]

    print("All tests passed!")


if __name__ == "__main__":
    test_strange_sort_list()

# Generated at 2026-11-03 06:22:03.793333
# Unit test for function strange_sort_list
def test_strange_sort_list():
    # Alternating min/max from a typical list
    assert module_0.strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]

    # Odd-length list
    assert module_0.strange_sort_list([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]

    # All identical elements
    assert module_0.strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]

    # Empty list
    assert module_0.strange_sort_list([]) == []

    # Single element
    assert module_0.strange_sort_list([1]) == [1]

    # Two elements
    assert module_0.strange_sort_list([3, 1]) == [1, 3]

    # Negative numbers and zero
    assert module_0.strange_sort_list([-2, 5, 0, -1]) == [-2, 5, -1, 0]

    # Unsorted input with duplicates
    assert module_0.strange_sort_list([7, 1, 7, 3, 3]) == [1, 7, 3, 7, 3]

    # Already sorted descending input
    assert module_0.strange_sort_list([9, 7, 5, 3]) == [3, 9, 5, 7]

    # Float values
    assert module_0.strange_sort_list([1.5, 0.5, 2.5]) == [0.5, 2.5, 1.5]

    # Verify the function does not modify behavior across repeated calls
    original = [4, 2, 6, 1]
    assert module_0.strange_sort_list(original) == [1, 6, 2, 4]

    print("All tests passed!")

# Generated at 2026-11-03 06:22:54.513614
# Unit test for function strange_sort_list
def test_strange_sort_list():import unittest


class TestStrangeSortList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(module_0.strange_sort_list([]), [])

    def test_single_element(self):
        self.assertEqual(module_0.strange_sort_list([1]), [1])

    def test_two_elements(self):
        self.assertEqual(module_0.strange_sort_list([1, 2]), [1, 2])
        self.assertEqual(module_0.strange_sort_list([2, 1]), [1, 2])

    def test_sorted_list(self):
        self.assertEqual(module_0.strange_sort_list([1, 2, 3, 4]), [1, 4, 2, 3])

    def test_reverse_sorted_list(self):
        self.assertEqual(module_0.strange_sort_list([5, 4, 3, 2, 1]), [1, 5, 2, 4, 3])

    def test_unsorted_list(self):
        self.assertEqual(module_0.strange_sort_list([3, 1, 4, 2, 5]), [1, 5, 2, 4, 3])

    def test_duplicates(self):
        self.assertEqual(module_0.strange_sort_list([2, 2, 2, 2]), [2, 2, 2, 2])
        self.assertEqual(module_0.strange_sort_list([1, 1, 2, 2]), [1, 2, 1, 2])

    def test_negative_numbers(self):
        self.assertEqual(module_0.strange_sort_list([-3, -1, -2]), [-3, -1, -2])

    def test_mixed_positive_negative(self):
        self.assertEqual(module_0.strange_sort_list([-5, 10, 0, 3]), [-5, 10, 0, 3])

    def test_all_same_values(self):
        self.assertEqual(module_0.strange_sort_list([7, 7, 7]), [7, 7, 7])

    def test_result_length_matches_input(self):
        lst = [9, 3, 5, 1, 8, 2]
        result = module_0.strange_sort_list(lst[:])
        self.assertEqual(len(result), len(lst))
        self.assertEqual(sorted(result), sorted(lst))

    def test_alternating_pattern(self):
        result = module_0.strange_sort_list([1, 2, 3, 4, 5, 6])
        self.assertEqual(result, [1, 6, 2, 5, 3, 4])


if __name__ == "__main__":
    unittest.main()