

# Generated at 2026-11-02 18:07:31.536267
# Unit test for function double_the_difference
def test_double_the_difference():import unittest


class TestDoubleTheDifference(unittest.TestCase):

    def test_basic_positive_odd_numbers(self):
        self.assertEqual(module_0.double_the_difference([1, 3, 5]), 1 + 9 + 25)

    def test_single_element(self):
        self.assertEqual(module_0.double_the_difference([3]), 9)

    def test_empty_list(self):
        self.assertEqual(module_0.double_the_difference([]), 0)

    def test_excludes_even_numbers(self):
        self.assertEqual(module_0.double_the_difference([2, 4, 6]), 0)

    def test_excludes_negative_numbers(self):
        self.assertEqual(module_0.double_the_difference([-1, -3, -5]), 0)

    def test_excludes_zero(self):
        self.assertEqual(module_0.double_the_difference([0]), 0)

    def test_excludes_floats(self):
        self.assertEqual(module_0.double_the_difference([1.5, 3.2, -0.5]), 0)

    def test_mixed_list(self):
        self.assertEqual(module_0.double_the_difference([1, 2, 3, -4, 5.5, 7]), 1 + 9 + 49)

    def test_large_numbers(self):
        self.assertEqual(module_0.double_the_difference([101, 103]), 101**2 + 103**2)

    def test_result_is_sum_of_squares(self):
        lst = [1, 3, 5, 2, -3, 4.5, 0]
        expected = sum(i**2 for i in lst if i > 0 and i % 2 != 0 and "." not in str(i))
        self.assertEqual(module_0.double_the_difference(lst), expected)

    def test_float_whole_value_excluded(self):
        # 3.0 contains "." in str(), so it must be excluded
        self.assertEqual(module_0.double_the_difference([3.0]), 0)

    def test_negative_float_excluded(self):
        self.assertEqual(module_0.double_the_difference([-1.0, -3.0]), 0)


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 18:09:05.465750
# Unit test for function double_the_difference
def test_double_the_difference():
    # Empty list
    assert module_0.double_the_difference([]) == 0

    # Positive odd numbers only
    assert module_0.double_the_difference([5, 4]) == 25
    assert module_0.double_the_difference([1, 3, 5, 7]) == 1 + 9 + 25 + 49

    # Even numbers contribute nothing
    assert module_0.double_the_difference([2, 4, 6]) == 0

    # Negative numbers contribute nothing
    assert module_0.double_the_difference([-10, -20, -30]) == 0
    assert module_0.double_the_difference([-1, -2, 0]) == 0

    # Floats contribute nothing
    assert module_0.double_the_difference([0.1, 0.2, 0.3]) == 0
    assert module_0.double_the_difference([1.5, 2.5, 3.5]) == 0

    # Mixed list: only positive odd integers count
    assert module_0.double_the_difference([1, -1, 2, -2, 3, -3]) == 1 + 9
    assert module_0.double_the_difference([9, -9, 0.5]) == 81

    # Zero contributes nothing
    assert module_0.double_the_difference([0]) == 0

    # Larger values
    assert module_0.double_the_difference([11, 13, -15, 4.2]) == 121 + 169

# Generated at 2026-11-02 18:10:03.289420
# Unit test for function double_the_difference
def test_double_the_difference():
    # Empty list should return 0
    assert module_0.double_the_difference([]) == 0

    # Sum of squares of positive odd integers
    assert module_0.double_the_difference([1, 3, 5]) == 35  # 1 + 9 + 25

    # Negative odd numbers are excluded
    assert module_0.double_the_difference([-1, -3, -5]) == 0

    # Even positive numbers are excluded
    assert module_0.double_the_difference([2, 4, 6]) == 0

    # Zero is excluded
    assert module_0.double_the_difference([0]) == 0

    # Floats are excluded (contain "." in string representation)
    assert module_0.double_the_difference([1.5, 3.5, 2.0]) == 0

    # Mixed list: only positive odd integers count
    assert module_0.double_the_difference([-2, -1, 0, 1, 2, 3]) == 10  # 1 + 9

    # Larger values
    assert module_0.double_the_difference([9, -9, 10, 11]) == 202  # 81 + 121

    # Single element
    assert module_0.double_the_difference([7]) == 49

    # Combination with duplicates
    assert module_0.double_the_difference([1, 1, 3, 3]) == 20  # 1 + 1 + 9 + 9

    print("All tests passed!")

test_double_the_difference()

# Generated at 2026-11-02 18:10:52.952239
# Unit test for function double_the_difference
def test_double_the_difference():
# nonce:2bb7f8b5
    assert module_0.double_the_difference([1, 3, 2, 0]) == 10
    assert module_0.double_the_difference([-1, -2, 0]) == 0
    assert module_0.double_the_difference([9, -2]) == 81
    assert module_0.double_the_difference([0]) == 0
    assert module_0.double_the_difference([]) == 0
    assert module_0.double_the_difference([1, -1, 2, -2, 3, -3]) == 10
    assert module_0.double_the_difference([2, 4, 6]) == 0
    assert module_0.double_the_difference([-3, -5, -7]) == 0
    assert module_0.double_the_difference([1.5, 3]) == 9
    assert module_0.double_the_difference([0.5, 2.5, 3]) == 9
    assert module_0.double_the_difference([1, 3, 5, 7]) == 84

# Generated at 2026-11-02 18:11:46.943230
# Unit test for function double_the_difference
def test_double_the_difference():
    assert module_0.double_the_difference([1, 3, 2, 0]) == 10
    assert module_0.double_the_difference([-1, -2, 0]) == 0
    assert module_0.double_the_difference([9, -2]) == 81
    assert module_0.double_the_difference([0]) == 0
    assert module_0.double_the_difference([]) == 0
    assert module_0.double_the_difference([-1, -3, 5]) == 25
    assert module_0.double_the_difference([1.5, 2.5]) == 0
    assert module_0.double_the_difference([1, 2.5, 3]) == 10