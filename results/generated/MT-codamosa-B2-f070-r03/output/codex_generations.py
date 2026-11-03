

# Generated at 2026-11-02 16:25:57.723405
# Unit test for function strange_sort_list
def test_strange_sort_list():
    # Basic alternating min/max sort
    assert module_0.strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert module_0.strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]

    # Edge cases
    assert module_0.strange_sort_list([]) == []
    assert module_0.strange_sort_list([7]) == [7]
    assert module_0.strange_sort_list([1, 2]) == [1, 2]

    # Unsorted input
    assert module_0.strange_sort_list([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 9, 1, 6, 2, 5, 3, 4]

    # Already sorted / reverse sorted
    assert module_0.strange_sort_list([1, 2, 3]) == [1, 3, 2]
    assert module_0.strange_sort_list([3, 2, 1]) == [1, 3, 2]

    # Negative numbers
    assert module_0.strange_sort_list([-1, -5, -3]) == [-5, -1, -3]
    assert module_0.strange_sort_list([-2, 2, -10, 10]) == [-10, 10, -2, 2]

    # Duplicates
    assert module_0.strange_sort_list([2, 2, 1, 1]) == [1, 2, 1, 2]

    # Original list is not mutated by caller's copy semantics (input not reused)
    original = [4, 1, 3]
    snapshot = list(original)
    module_0.strange_sort_list(original)
    assert original == snapshot

    print("All tests passed!")


if __name__ == "__main__":
    test_strange_sort_list()

# Generated at 2026-11-02 16:27:54.100674
# Unit test for function strange_sort_list
def test_strange_sort_list():import unittest


class TestStrangeSortList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(module_0.strange_sort_list([]), [])

    def test_single_element(self):
        self.assertEqual(module_0.strange_sort_list([7]), [7])

    def test_two_elements(self):
        self.assertEqual(module_0.strange_sort_list([3, 1]), [1, 3])

    def test_basic_case(self):
        self.assertEqual(module_0.strange_sort_list([1, 2, 3, 4]), [1, 4, 2, 3])

    def test_unsorted_input(self):
        self.assertEqual(module_0.strange_sort_list([5, 2, 8, 1, 9]), [1, 9, 2, 8, 5])

    def test_all_same_elements(self):
        self.assertEqual(module_0.strange_sort_list([4, 4, 4, 4]), [4, 4, 4, 4])

    def test_negative_numbers(self):
        self.assertEqual(module_0.strange_sort_list([-5, -1, -3, -2]), [-5, -1, -3, -2])

    def test_mixed_positive_negative(self):
        self.assertEqual(module_0.strange_sort_list([-3, 7, 0, 2, -8]), [-8, 7, -3, 2, 0])

    def test_duplicates(self):
        self.assertEqual(module_0.strange_sort_list([2, 2, 1, 3, 3]), [1, 3, 2, 3, 2])

    def test_result_is_alternating(self):
        lst = [10, 3, 7, 1, 9, 5]
        result = module_0.strange_sort_list(lst[:])
        self.assertEqual(result, sorted(lst)[::2] + sorted(lst)[1::2][::-1])

    def test_input_list_is_consumed(self):
        lst = [3, 1, 2]
        module_0.strange_sort_list(lst)
        self.assertEqual(lst, [])


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 16:28:45.685476
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

    def test_empty_list(self):
        self.assertEqual(module_0.strange_sort_list([]), [])

    def test_single_element(self):
        self.assertEqual(module_0.strange_sort_list([1]), [1])

    def test_two_elements(self):
        self.assertEqual(module_0.strange_sort_list([1, 2]), [1, 2])

    def test_typical_case(self):
        self.assertEqual(module_0.strange_sort_list([1, 2, 3, 4]), [1, 4, 2, 3])

    def test_another_typical_case(self):
        self.assertEqual(module_0.strange_sort_list([5, 5, 5, 5]), [5, 5, 5, 5])

    def test_unsorted_input(self):
        self.assertEqual(module_0.strange_sort_list([3, 1, 4, 2, 5]), [1, 5, 2, 4, 3])

    def test_negative_numbers(self):
        self.assertEqual(module_0.strange_sort_list([-1, -5, 0, 3]), [-5, 3, -1, 0])

    def test_duplicates(self):
        self.assertEqual(module_0.strange_sort_list([2, 2, 1, 3]), [1, 3, 2, 2])

    def test_already_min_max_sorted(self):
        self.assertEqual(module_0.strange_sort_list([10, 1]), [1, 10])

    def test_mixed_values(self):
        self.assertEqual(module_0.strange_sort_list([7, 0, -3, 9, 4]), [-3, 9, 0, 7, 4])


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 16:30:02.388652
# Unit test for function strange_sort_list
def test_strange_sort_list():
    # Empty list
    assert module_0.strange_sort_list([]) == []
    # Single element
    assert module_0.strange_sort_list([1]) == [1]
    # Two elements
    assert module_0.strange_sort_list([1, 2]) == [1, 2]
    # Even-length list
    assert module_0.strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    # Odd-length list
    assert module_0.strange_sort_list([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]
    # All duplicates
    assert module_0.strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    # Negative numbers
    assert module_0.strange_sort_list([-1, -5, 2, -2]) == [-5, 2, -2, -1]
    # Unsorted input
    assert module_0.strange_sort_list([3, 1, 4, 2, 5]) == [1, 5, 2, 4, 3]
    # Mixed values with duplicates
    assert module_0.strange_sort_list([2, 2, 1, 3]) == [1, 3, 2, 2]
    # Larger list
    assert module_0.strange_sort_list([10, 1, 7, 3, 9, 5]) == [1, 10, 3, 9, 5, 7]
    # Result length matches input length
    assert len(module_0.strange_sort_list([4, 8, 15, 16, 23, 42])) == 6
    print("All tests passed!")

# Generated at 2026-11-02 16:31:33.786554
# Unit test for function strange_sort_list
def test_strange_sort_list():
    # Empty list
    assert module_0.strange_sort_list([]) == []

    # Single element
    assert module_0.strange_sort_list([1]) == [1]
    assert module_0.strange_sort_list([7]) == [7]

    # Two elements
    assert module_0.strange_sort_list([1, 2]) == [1, 2]
    assert module_0.strange_sort_list([2, 1]) == [1, 2]

    # Already sorted list
    assert module_0.strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]

    # Unsorted list
    assert module_0.strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    assert module_0.strange_sort_list([3, 1, 2]) == [1, 3, 2]
    assert module_0.strange_sort_list([4, 1, 3, 2]) == [1, 4, 2, 3]

    # Negative numbers
    assert module_0.strange_sort_list([-1, -5, 0, 3]) == [-5, 3, -1, 0]
    assert module_0.strange_sort_list([-2, -1, -3]) == [-3, -1, -2]

    # Duplicates mixed with others
    assert module_0.strange_sort_list([1, 2, 2, 3]) == [1, 3, 2, 2]

    # Mixed positive/negative/zero
    assert module_0.strange_sort_list([0, -10, 10, 5]) == [-10, 10, 0, 5]

    # Larger list
    assert module_0.strange_sort_list([9, 1, 8, 2, 7, 3]) == [1, 9, 2, 8, 3, 7]

    # Input list is consumed (mutated) by the algorithm
    data = [3, 1, 2]
    module_0.strange_sort_list(data)
    assert data == []

    print("All tests passed!")


if __name__ == "__main__":
    test_strange_sort_list()