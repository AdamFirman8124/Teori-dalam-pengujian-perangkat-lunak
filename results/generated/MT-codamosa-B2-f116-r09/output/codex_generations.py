

# Generated at 2026-11-02 12:50:57.810950
# Unit test for function sort_array
def test_sort_array():
    # Basic example: sort by value first, then by number of 1-bits
    assert module_0.sort_array([1, 5, 2, 3, 4]) == [1, 2, 4, 3, 5]

    # Same set in different order should give the same result
    assert module_0.sort_array([2, 4, 1, 3, 5]) == [1, 2, 4, 3, 5]

    # Range 0-7: 0(0 ones), 1(1), 2(1), 3(2), 4(1), 5(2), 6(2), 7(3)
    assert module_0.sort_array([0, 1, 2, 3, 4, 5, 6, 7]) == [0, 1, 2, 4, 3, 5, 6, 7]

    # Empty array
    assert module_0.sort_array([]) == []

    # Single element
    assert module_0.sort_array([7]) == [7]

    # Already sorted input
    assert module_0.sort_array([1, 2, 4, 3, 5]) == [1, 2, 4, 3, 5]

    # Duplicates should be preserved
    assert module_0.sort_array([3, 3, 1]) == [1, 3, 3]
    assert module_0.sort_array([5, 5, 5]) == [5, 5, 5]

    # Powers of two all have exactly one 1-bit; ties broken by value
    assert module_0.sort_array([8, 2, 4, 1]) == [1, 2, 4, 8]

    # Larger values with more 1-bits come after values with fewer
    assert module_0.sort_array([15, 1, 7]) == [1, 7, 15]  # 15->1111(4), 1->1(1), 7->111(3)

    # Reverse-sorted input
    assert module_0.sort_array([5, 3, 4, 2, 1]) == [1, 2, 4, 3, 5]

    # Negative numbers: bin(-n) = '-0b' + bin(n), so bit counts mirror positive
    # counterparts; value sort puts negatives first
    assert module_0.sort_array([-2, -1]) == [-2, -1]
    assert module_0.sort_array([-3, -1, 0]) == [-1, -3, 0]  # -1:1 one, -3:2 ones, 0:0 ones

    # Mixed input
    assert module_0.sort_array([6, 1, 0, 8, 7]) == [0, 1, 8, 6, 7]  # 0:0, 1:1, 8:1, 6:2, 7:3

    print("All tests passed!")


if __name__ == "__main__":
    test_sort_array()

# Generated at 2026-11-02 12:51:56.061404
# Unit test for function sort_array
def test_sort_array():import unittest


def module_0.sort_array(arr):
    return sorted(sorted(arr), key=lambda x: bin(x)[2:].count('1'))


class TestSortArray(unittest.TestCase):

    def test_example_case(self):
        self.assertEqual(module_0.sort_array([1, 5, 2, 3, 4]), [1, 2, 4, 3, 5])

    def test_negative_numbers(self):
        self.assertEqual(module_0.sort_array([-2, -3, -4, -5, -6]), [-6, -5, -4, -3, -2])

    def test_empty_array(self):
        self.assertEqual(module_0.sort_array([]), [])

    def test_single_element(self):
        self.assertEqual(module_0.sort_array([7]), [7])

    def test_with_zero(self):
        self.assertEqual(module_0.sort_array([1, 0, 2, 3, 4]), [0, 1, 2, 4, 3])

    def test_already_sorted_by_bits(self):
        self.assertEqual(module_0.sort_array([1, 2, 4, 8]), [1, 2, 4, 8])

    def test_duplicates(self):
        self.assertEqual(module_0.sort_array([3, 3, 1, 1]), [1, 1, 3, 3])

    def test_all_same_bit_count(self):
        # 1, 2, 4, 8 all have one bit set; ties broken by ascending value
        self.assertEqual(module_0.sort_array([8, 4, 2, 1]), [1, 2, 4, 8])

    def test_power_of_two_and_three(self):
        # 2 has one '1' bit, 3 has two '1' bits
        self.assertEqual(module_0.sort_array([3, 2]), [2, 3])

    def test_does_not_modify_original(self):
        arr = [3, 1, 2]
        module_0.sort_array(arr)
        self.assertEqual(arr, [3, 1, 2])


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 12:54:13.823748
# Unit test for function sort_array
def test_sort_array():
    # Basic case: sorted by number of 1 bits, ties broken by numeric order
    assert module_0.sort_array([1, 5, 2, 3, 4]) == [1, 2, 4, 3, 5]

    # Includes zero (0 has zero 1-bits)
    assert module_0.sort_array([0, 1, 2, 3, 4]) == [0, 1, 2, 4, 3]

    # Descending input
    assert module_0.sort_array([7, 6, 5]) == [5, 6, 7]

    # Powers of two each have exactly one 1-bit, keep numeric order
    assert module_0.sort_array([8, 4, 2, 1]) == [1, 2, 4, 8]

    # Negative numbers: bin(-n) contains '1' count of magnitude's bits
    # bin(-1) = '-0b1' -> 1 one-bit; bin(-2) = '-0b10' -> 1 one-bit
    assert module_0.sort_array([-2, -3, -4]) == [-2, -4, -3]

    # Empty array
    assert module_0.sort_array([]) == []

    # Single element
    assert module_0.sort_array([42]) == [42]

    # Duplicates preserved
    assert module_0.sort_array([3, 3, 1]) == [1, 3, 3]

    # Larger mixed case
    assert module_0.sort_array([2, 22, 10, 15, 7]) == [2, 10, 15, 7, 22]

    print("All sort_array tests passed!")

# Generated at 2026-11-02 12:56:46.659949
# Unit test for function sort_array
def test_sort_array():
    # Basic case: ties in bit-count preserve numeric order (stable sort)
    assert module_0.sort_array([1, 5, 2, 3, 4]) == [1, 2, 4, 3, 5]

    # Negative numbers: bin(x)[2:] uses magnitude bits
    assert module_0.sort_array([-2, -3, -4, -5, -6]) == [-4, -2, -6, -5, -3]

    # Includes zero (zero has zero '1' bits, comes first)
    assert module_0.sort_array([1, 0, 2, 3, 4]) == [0, 1, 2, 4, 3]

    # Edge cases: empty and single-element arrays
    assert module_0.sort_array([]) == []
    assert module_0.sort_array([7]) == [7]

    # Mixed values with differing bit counts
    assert module_0.sort_array([3, 6, 44, 12, 32, 5]) == [32, 3, 5, 6, 12, 44]

    # Powers of two all have exactly one '1' bit
    assert module_0.sort_array([2, 4, 8, 16, 32]) == [2, 4, 8, 16, 32]

    # Larger numbers
    assert module_0.sort_array([10, 100, 1000, 10000]) == [10, 100, 10000, 1000]

    # Descending input, increasing bit counts
    assert module_0.sort_array([15, 14, 13, 12]) == [12, 13, 14, 15]

    print("test_sort_array passed")

# Generated at 2026-11-02 12:59:26.110655
# Unit test for function sort_array