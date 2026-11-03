

# Generated at 2026-11-02 13:22:23.796407
# Unit test for function strange_sort_list
def test_strange_sort_list():
    # Basic case with distinct elements
    assert module_0.strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert module_0.strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    assert module_0.strange_sort_list([]) == []
    assert module_0.strange_sort_list([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]
    assert module_0.strange_sort_list([1, 2, 3, 4, 5, 6]) == [1, 6, 2, 5, 3, 4]
    assert module_0.strange_sort_list([7, 3, 9, 1, 5]) == [1, 9, 3, 7, 5]
    assert module_0.strange_sort_list([10, 20, 30]) == [10, 30, 20]
    assert module_0.strange_sort_list([0, -10, 10, 5, -5]) == [-10, 10, -5, 5, 0]
    assert module_0.strange_sort_list([2, 1]) == [1, 2]
    assert module_0.strange_sort_list([1]) == [1]
    assert module_0.strange_sort_list([-1, -2, -3, -4]) == [-4, -1, -3, -2]
    assert module_0.strange_sort_list([3, 3, 3, 3, 3]) == [3, 3, 3, 3, 3]
    assert module_0.strange_sort_list([1, 1, 2, 2]) == [1, 2, 1, 2]
    assert module_0.strange_sort_list([0.5, 1.5, 2.5, -1.5]) == [-1.5, 2.5, 0.5, 1.5]
    # Input list should not be mutated unexpectedly (function removes from its copy)
    original = [3, 1, 2]
    result = module_0.strange_sort_list(original)
    assert result == [1, 3, 2]
    print("All tests passed!")

# Generated at 2026-11-02 13:23:32.729615
# Unit test for function strange_sort_list
def test_strange_sort_list():
    assert module_0.strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert module_0.strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    assert module_0.strange_sort_list([]) == []
    assert module_0.strange_sort_list([1]) == [1]
    assert module_0.strange_sort_list([2, 1, 3]) == [1, 3, 2]
    assert module_0.strange_sort_list([-1, -2, 0, 5]) == [-2, 5, -1, 0]
    assert module_0.strange_sort_list([10, 11, 12]) == [10, 12, 11]
    print("test_strange_sort_list passed")

if __name__ == "__main__":
    test_strange_sort_list()

# Generated at 2026-11-02 13:25:05.867803
# Unit test for function strange_sort_list
def test_strange_sort_list():
    # Empty list
    assert module_0.strange_sort_list([]) == []

    # Single element
    assert module_0.strange_sort_list([7]) == [7]

    # Two elements
    assert module_0.strange_sort_list([3, 1]) == [1, 3]

    # Simple ascending list
    assert module_0.strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]

    # Odd-length list
    assert module_0.strange_sort_list([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]

    # Unsorted input
    assert module_0.strange_sort_list([5, 1, 3, 2, 4]) == [1, 5, 2, 4, 3]

    # All duplicates
    assert module_0.strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]

    # Mixed duplicates
    assert module_0.strange_sort_list([2, 1, 2, 1]) == [1, 2, 1, 2]

    # Negative numbers
    assert module_0.strange_sort_list([-3, -1, -2, 0]) == [-3, 0, -2, -1]

    # Already strange-sorted input
    assert module_0.strange_sort_list([1, 4, 2, 3]) == [1, 4, 2, 3]

    # Large values
    assert module_0.strange_sort_list([1000000, -1000000]) == [-1000000, 1000000]

    print("All tests passed!")


if __name__ == "__main__":
    test_strange_sort_list()

# Generated at 2026-11-02 13:27:36.911645
# Unit test for function strange_sort_list
def test_strange_sort_list():
    # Basic alternating min/max
    assert module_0.strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert module_0.strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    assert module_0.strange_sort_list([]) == []
    assert module_0.strange_sort_list([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]
    assert module_0.strange_sort_list([1, 2, 3, 4, 5, 6, 7]) == [1, 7, 2, 6, 3, 5, 4]

    # Single element
    assert module_0.strange_sort_list([7]) == [7]

    # Two elements
    assert module_0.strange_sort_list([3, 1]) == [1, 3]

    # Negative numbers
    assert module_0.strange_sort_list([-2, 5, 0, -1]) == [-2, 5, -1, 0]

    # Unsorted input with duplicates
    assert module_0.strange_sort_list([4, 1, 4, 2]) == [1, 4, 2, 4]

# Generated at 2026-11-02 13:29:44.950011
# Unit test for function strange_sort_list
def test_strange_sort_list():import unittest


def module_0.strange_sort_list(lst):
    
    res, switch = [], True
    while lst:
        res.append(min(lst) if switch else max(lst))
        lst.remove(res[-1])
        switch = not switch
    return res


class TestStrangeSortList(unittest.TestCase):

    def test_basic_mixed_list(self):
        self.assertEqual(module_0.strange_sort_list([1, 2, 3, 4]), [1, 4, 2, 3])

    def test_all_equal_elements(self):
        self.assertEqual(module_0.strange_sort_list([5, 5, 5, 5]), [5, 5, 5, 5])

    def test_empty_list(self):
        self.assertEqual(module_0.strange_sort_list([]), [])

    def test_single_element(self):
        self.assertEqual(module_0.strange_sort_list([42]), [42])

    def test_negative_numbers(self):
        self.assertEqual(module_0.strange_sort_list([1, -1, 2, -2, 3, -3]),
                         [-3, 3, -2, 2, -1, 1])

    def test_two_elements(self):
        self.assertEqual(module_0.strange_sort_list([10, 2]), [2, 10])

    def test_duplicates(self):
        self.assertEqual(module_0.strange_sort_list([3, 1, 3, 1, 2]), [1, 3, 1, 3, 2])

    def test_already_alternating(self):
        self.assertEqual(module_0.strange_sort_list([1, 4, 2, 3]), [1, 4, 2, 3])

    def test_unsorted_input(self):
        self.assertEqual(module_0.strange_sort_list([9, 1, 5, 3, 7]), [1, 9, 3, 7, 5])

    def test_result_length_matches(self):
        original = [4, 8, 15, 16, 23, 42]
        result = module_0.strange_sort_list(original[:])
        self.assertEqual(len(result), len(original))


if __name__ == "__main__":
    unittest.main()