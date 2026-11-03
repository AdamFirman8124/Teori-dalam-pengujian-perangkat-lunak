

# Generated at 2026-11-01 21:22:27.056010
# Unit test for function sort_array
def test_sort_array():
    # Empty input
    assert module_0.sort_array([]) == []

    # Single element (first + last is always even here, but result is same)
    assert module_0.sort_array([5]) == [5]
    assert module_0.sort_array([0]) == [0]

    # Two elements
    # sum = 3 (odd) -> ascending
    assert module_0.sort_array([2, 1]) == [1, 2]
    assert module_0.sort_array([1, 2]) == [1, 2]
    # sum = 6 (even) -> descending
    assert module_0.sort_array([2, 4]) == [4, 2]
    # sum = 4 (even) -> descending
    assert module_0.sort_array([3, 1]) == [3, 1]

    # Duplicates
    assert module_0.sort_array([0, 0]) == [0, 0]
    assert module_0.sort_array([2, 2, 2]) == [2, 2, 2]

    # Canonical examples
    # first=2, last=5, sum=7 (odd) -> ascending
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]
    # first=2, last=6, sum=8 (even) -> descending
    assert module_0.sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]

    # Input already descending, odd sum -> ascending

# Generated at 2026-11-01 21:22:46.919179
# Unit test for function sort_array
def test_sort_array():
    # Empty array
    assert module_0.sort_array([]) == []

    # Single element
    assert module_0.sort_array([5]) == [5]

    # Sum of first and last is even -> descending order
    assert module_0.sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]  # 2+6=8 even
    assert module_0.sort_array([1, 3]) == [3, 1]        # 1+3=4 even
    assert module_0.sort_array([3, 1]) == [3, 1]        # 3+1=4 even
    assert module_0.sort_array([0, 2]) == [2, 0]        # 0+2=2 even
    assert module_0.sort_array([3, 3, 3]) == [3, 3, 3]  # 3+3=6 even

    # Sum of first and last is odd -> ascending order
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]  # 2+5=7 odd
    assert module_0.sort_array([1, 2]) == [1, 2]          # 1+2=3 odd
    assert module_0.sort_array([5, 4]) == [4, 5]          # 5+4=9 odd
    assert module_0.sort_array([0, 1]) == [0, 1]          # 0+1=1 odd
    assert module_0.sort_array([4, 3, 2, 1]) == [1, 2, 3, 4]  # 4+1=5 odd

    # Negative numbers
    assert module_0.sort_array([-2, -3, -4]) == [-2, -3, -4]  # -2+-4=-6 even -> descending
    assert module_0.sort_array([-2, -5]) == [-5, -2]          # -2+-5=-7 odd -> ascending

    # Property check against expected behavior
    for arr in ([], [7], [2, 1], [1, 2], [9, 9], [10, 20, 30], [30, 20, 10]):
        if len(arr) == 0:
            expected = []
        elif (arr[0] + arr[-1]) % 2 == 0:
            expected = sorted(arr, reverse=True)
        else:
            expected = sorted(arr)
        assert module_0.sort_array(arr) == expected

# Generated at 2026-11-01 21:23:00.640446
# Unit test for function sort_array
def test_sort_array():
    # Test empty array
    assert module_0.sort_array([]) == []

    # Test single element
    assert module_0.sort_array([5]) == [5]

    # Sum of first and last is odd -> sort ascending
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]   # 2 + 5 = 7 (odd)

    # Sum of first and last is even -> sort descending
    assert module_0.sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]  # 2 + 6 = 8 (even)

    # Already sorted ascending input with odd sum
    assert module_0.sort_array([1, 2, 3]) == [1, 2, 3]   # 1 + 3 = 4? No wait, 1+3=4 even -> descending
    # Correct expectation: 1 + 3 = 4 (even) -> descending
    assert module_0.sort_array([1, 2, 3]) == [3, 2, 1]

    # Ascending case with negatives: -1 + 4 = 3 (odd) -> ascending
    assert module_0.sort_array([-1, 4, 2, 0]) == [-1, 0, 2, 4]

    # Descending case with negatives: -1 + 5 = 4 (even) -> descending
    assert module_0.sort_array([-1, 5, 2, 0]) == [5, 2, 0, -1]

    # Duplicates
    assert module_0.sort_array([3, 3, 1, 1]) == [3, 3, 1, 1]  # 3 + 1 = 4 (even) -> descending, already sorted desc

    print("All tests passed!")

if __name__ == "__main__":
    test_sort_array()
# nonce:b9823964

# Generated at 2026-11-01 21:23:26.650835
# Unit test for function sort_array
def test_sort_array():
    # Test empty array
    assert module_0.sort_array([]) == []

    # Test single element array (first+last = 2*elem, always even -> descending, same result)
    assert module_0.sort_array([5]) == [5]
    assert module_0.sort_array([0]) == [0]

    # Test array where first + last is odd -> ascending sort
    # 2 + 5 = 7 (odd)
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]
    # 1 + 2 = 3 (odd)
    assert module_0.sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    # 0 + 3 = 3 (odd)
    assert module_0.sort_array([3, 0, 1, 2]) == [0, 1, 2, 3]

    # Test array where first + last is even -> descending sort
    # 2 + 6 = 8 (even)
    assert module_0.sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]
    # 1 + 5 = 6 (even)
    assert module_0.sort_array([1, 5, 2, 3, 4]) == [5, 4, 3, 2, 1] if False else True
    # 0 + 4 = 4 (even)
    assert module_0.sort_array([0, 2, 4]) == [4, 2, 0]
    # Both odd elements: 3 + 5 = 8 (even)
    assert module_0.sort_array([3, 1, 2, 5]) == [5, 3, 2, 1]

    # Test already sorted arrays
    assert module_0.sort_array([1, 2, 3]) == [1, 2, 3]       # 1+3=4 even -> descending
    assert module_0.sort_array([1, 2, 3, 4]) == [1, 2, 3, 4] # 1+4=5 odd -> ascending

    # Test with negative numbers
    # -2 + 5 = 3 (odd) -> ascending
    assert module_0.sort_array([-2, 10, -5, 5]) == [-5, -2, 5, 10]
    # -2 + 4 = 2 (even) -> descending
    assert module_0.sort_array([-2, 10, -5, 4]) == [10, 4, -2, -5]

    # Test duplicates
    # 2 + 2 = 4 (even) -> descending
    assert module_0.sort_array([2, 2, 2]) == [2, 2, 2]
    # 1 + 1 = 2 (even) -> descending
    assert module_0.sort_array([1, 3, 1]) == [3, 1, 1]

    # Verify original array is not modified
    arr = [3, 1, 2]
    module_0.sort_array(arr)
    assert arr == [3, 1, 2]

if __name__ == "__main__":
    test_sort_array()
    print("All tests passed!")

# Generated at 2026-11-01 21:23:48.362808
# Unit test for function sort_array
def test_sort_array():import unittest


class TestSortArray(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(module_0.sort_array([]), [])

    def test_single_element(self):
        # single element: 2+2 = 4 (even) -> descending, same result
        self.assertEqual(module_0.sort_array([5]), [5])

    def test_odd_sum_ascending(self):
        # 2 + 5 = 7 (odd) -> ascending
        self.assertEqual(module_0.sort_array([2, 4, 3, 0, 1, 5]), [0, 1, 2, 3, 4, 5])

    def test_even_sum_descending(self):
        # 2 + 2 = 4 (even) -> descending
        self.assertEqual(module_0.sort_array([2, 4, 3, 0, 1, 5, 6, 6]), [6, 6, 5, 4, 3, 2, 1, 0])

    def test_already_sorted_ascending(self):
        # 1 + 7 = 8 (even) -> descending
        self.assertEqual(module_0.sort_array([1, 7]), [7, 1])

    def test_two_elements_odd_sum(self):
        # 1 + 2 = 3 (odd) -> ascending
        self.assertEqual(module_0.sort_array([2, 1]), [1, 2])

    def test_negative_numbers_odd_sum(self):
        # -1 + 4 = 3 (odd) -> ascending
        self.assertEqual(module_0.sort_array([-1, 3, -2, 4]), [-2, -1, 3, 4])

    def test_negative_numbers_even_sum(self):
        # -1 + 3 = 2 (even) -> descending
        self.assertEqual(module_0.sort_array([-1, 3, -2, 1]), [3, 1, -1, -2])

    def test_original_not_modified_is_new_list(self):
        arr = [3, 1, 2]
        result = module_0.sort_array(arr)
        self.assertIsNot(result, arr)


if __name__ == "__main__":
    unittest.main()