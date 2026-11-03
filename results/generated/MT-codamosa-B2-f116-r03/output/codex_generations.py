

# Generated at 2026-11-03 03:54:55.614729
# Unit test for function sort_array
def test_sort_array():# Positive integers: numeric sort first, then stable sort by count of 1-bits
    assert module_0.sort_array([1, 5, 2, 3, 4]) == [1, 2, 4, 3, 5]
    assert module_0.sort_array([1, 0, 2, 3, 4]) == [0, 1, 2, 4, 3]
    assert module_0.sort_array([3, 6, 44, 10, 1, 8, 9]) == [1, 8, 3, 6, 9, 10, 44]

    # Empty and single-element inputs
    assert module_0.sort_array([]) == []
    assert module_0.sort_array([7]) == [7]

    # Powers of two each contain exactly one 1-bit; order falls back to numeric
    assert module_0.sort_array([16, 4, 8, 2]) == [2, 4, 8, 16]

    # All equal bit counts -> pure ascending numeric order (stable pre-sort)
    assert module_0.sort_array([9, 3, 6, 10]) == [3, 6, 9, 10]

    # Negative numbers: bin(x)[2:] counts 1s in the magnitude digits
    # counts: -4->1, -2->1, -6->2, -5->2, -3->2 (ties keep numeric order)
    assert module_0.sort_array([-2, -3, -4, -5, -6]) == [-4, -2, -6, -5, -3]

    # Already sorted input is unchanged
    assert module_0.sort_array([0, 1, 2, 3]) == [0, 1, 2, 3]

# Generated at 2026-11-03 03:56:13.434125
# Unit test for function sort_array
def test_sort_array():import unittest


class TestSortArray(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(module_0.sort_array([1, 5, 2, 3, 4]), [1, 2, 4, 3, 5])

    def test_example_two(self):
        self.assertEqual(module_0.sort_array([-2, -3, -4, -5, -6]), [-4, -2, -6, -5, -3])

    def test_empty(self):
        self.assertEqual(module_0.sort_array([]), [])

    def test_single_element(self):
        self.assertEqual(module_0.sort_array([7]), [7])

    def test_already_sorted_by_bits(self):
        self.assertEqual(module_0.sort_array([0, 1, 2, 3]), [0, 1, 2, 3])

    def test_duplicates(self):
        self.assertEqual(module_0.sort_array([3, 3, 1, 1]), [1, 1, 3, 3])

    def test_with_zero(self):
        self.assertEqual(module_0.sort_array([1, 0, 2, 3, 4]), [0, 1, 2, 4, 3])

    def test_reverse_order_input(self):
        self.assertEqual(module_0.sort_array([5, 4, 3, 2, 1]), [1, 2, 4, 3, 5])

    def test_large_numbers(self):
        self.assertEqual(module_0.sort_array([8, 15, 7]), [8, 7, 15])

    def test_result_is_sorted_first(self):
        result = module_0.sort_array([9, 8, 7, 6, 5])
        # numeric order preserved for equal bit counts
        self.assertEqual(result, [8, 5, 6, 7, 9])


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-03 03:58:10.274094
# Unit test for function sort_array
def test_sort_array():
    # Basic case: sort by number of 1s in binary, ties broken by value
    assert module_0.sort_array([1, 5, 2, 3, 4]) == [1, 2, 4, 3, 5]

    # Same number of ones -> sorted numerically
    assert module_0.sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]

    # Array with equal bit counts grouped together
    assert module_0.sort_array([0, 1, 2, 3, 4, 5, 6, 7]) == [0, 1, 2, 4, 3, 5, 6, 7]

    # Empty array
    assert module_0.sort_array([]) == []

    # Single element
    assert module_0.sort_array([42]) == [42]

    # Duplicates preserved
    assert module_0.sort_array([3, 3, 1, 1]) == [1, 1, 3, 3]

    # Already sorted result stays stable in value order for ties
    assert module_0.sort_array([2, 4, 8]) == [2, 4, 8]

    # Larger values with varying bit counts
    assert module_0.sort_array([10, 15, 7, 1]) == [1, 10, 7, 15]

    # Negative numbers: bin(-n)[2:] mirrors positive bit count
    assert module_0.sort_array([-1, 1, -3, 3]) == [-1, 1, -3, 3]

    print("All tests passed!")

if __name__ == "__main__":
    test_sort_array()

# Generated at 2026-11-03 03:59:35.491525
# Unit test for function sort_array
def test_sort_array():
    # Basic case: sort by value first, then by number of 1 bits
    assert module_0.sort_array([1, 5, 2, 3, 4]) == [1, 2, 4, 3, 5]

    # Powers of two all have a single 1 bit, order preserved ascending
    assert module_0.sort_array([2, 4, 8, 16]) == [2, 4, 8, 16]

    # Already sorted by bit count
    assert module_0.sort_array([3, 7, 5]) == [3, 5, 7]

    # Empty array
    assert module_0.sort_array([]) == []

    # Single element
    assert module_0.sort_array([42]) == [42]

    # Duplicates
    assert module_0.sort_array([5, 5, 5]) == [5, 5, 5]

    # Range including zero
    assert module_0.sort_array([0, 1, 2, 3, 4, 5, 6, 7]) == [0, 1, 2, 4, 3, 5, 6, 7]

    # Unsorted input with equal bit counts keeps ascending value order (stable sort)
    assert module_0.sort_array([7, 3, 11]) == [3, 7, 11]

    # Larger mixed example
    assert module_0.sort_array([9, 1, 6, 15, 8]) == [1, 8, 9, 6, 15]

    # Negative numbers: bin(-x)[2:] still counts the 1 bits of the magnitude
    assert module_0.sort_array([-1, -2, -3]) == [-3, -2, -1] or module_0.sort_array([-1, -2, -3]) == [-2, -1, -3]

    # Result must always be a list
    assert isinstance(module_0.sort_array([3, 1, 2]), list)

    # Verify bit-count ordering property on random-ish data
    data = [10, 0, 7, 14, 3, 6, 13, 1]
    result = module_0.sort_array(data)
    ones = [bin(x)[2:].count('1') for x in result]
    assert ones == sorted(ones)

    print("All tests passed!")


if __name__ == "__main__":
    test_sort_array()