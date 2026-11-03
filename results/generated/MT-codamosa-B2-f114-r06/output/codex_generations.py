

# Generated at 2026-11-01 19:55:17.329706
# Unit test for function minSubArraySum
def test_minSubArraySum():import unittest


class TestMinSubArraySum(unittest.TestCase):

    def test_mixed_positive_negative(self):
        self.assertEqual(module_0.minSubArraySum([3, -4, 1]), -4)

    def test_all_positive_single_element_result(self):
        self.assertEqual(module_0.minSubArraySum([2, 3, 4, 1, 2, 4]), 1)

    def test_all_negative(self):
        self.assertEqual(module_0.minSubArraySum([-1, -2, -3]), -6)

    def test_all_negative_large(self):
        self.assertEqual(module_0.minSubArraySum([-1, -3, -10]), -14)

    def test_single_element_positive(self):
        self.assertEqual(module_0.minSubArraySum([100]), 100)

    def test_single_element_negative(self):
        self.assertEqual(module_0.minSubArraySum([-7]), -7)

    def test_with_zeros(self):
        self.assertEqual(module_0.minSubArraySum([0, 1, 2, 5, 6, 8, 9, 10]), 0)

    def test_pair_with_negative(self):
        self.assertEqual(module_0.minSubArraySum([1, -1]), -1)

    def test_whole_array_is_minimum(self):
        self.assertEqual(module_0.minSubArraySum([1, -2, 3]), -2)

    def test_two_positives(self):
        self.assertEqual(module_0.minSubArraySum([2, 3]), 2)


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-01 19:56:49.945264
# Unit test for function minSubArraySum
def test_minSubArraySum():
# nonce:4bd9b40d
    # Basic cases
    assert module_0.minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    assert module_0.minSubArraySum([-1, -2, -3]) == -6
    assert module_0.minSubArraySum([1, -2, 3, -4, 5]) == -4

    # Single element lists
    assert module_0.minSubArraySum([5]) == 5
    assert module_0.minSubArraySum([-7]) == -7
    assert module_0.minSubArraySum([0]) == 0

    # All zeros
    assert module_0.minSubArraySum([0, 0, 0]) == 0

    # Mixed positive/negative values
    assert module_0.minSubArraySum([10, -5, 3]) == -5
    assert module_0.minSubArraySum([3, -10, 2]) == -10
    assert module_0.minSubArraySum([1, -1, 1, -1]) == -1
    assert module_0.minSubArraySum([3, -10]) == -10
    assert module_0.minSubArraySum([-3, 10]) == -3

    # All positive -> minimum is the smallest single element
    assert module_0.minSubArraySum([4, 2, 8, 1]) == 1

    # All negative -> minimum is the sum of the whole array

# Generated at 2026-11-01 19:57:27.791240
# Unit test for function minSubArraySum
def test_minSubArraySum():
    # nonce:5464139a
    # All-positive array: min subarray sum is the smallest element
    assert module_0.minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    assert module_0.minSubArraySum([1, 2, 3]) == 1
    assert module_0.minSubArraySum([10, 20, 30, 40]) == 10

    # All-negative array: min subarray sum is the sum of all elements
    assert module_0.minSubArraySum([-1, -2, -3]) == -6
    assert module_0.minSubArraySum([-4, -5]) == -9

    # Mixed positive/negative arrays
    assert module_0.minSubArraySum([-1, -2, -3, 4, -1, -2, 1, 5, -3]) == -6
    assert module_0.minSubArraySum([3, -4, 2, -3, -1, 7, -5]) == -6
    assert module_0.minSubArraySum([1, -2, 3, -1, 2]) == -2

    # Single element arrays
    assert module_0.minSubArraySum([1]) == 1
    assert module_0.minSubArraySum([-5]) == -5
    assert module_0.minSubArraySum([0]) == 0

    # Array containing zero
    assert module_0.minSubArraySum([0, 10, 20, 1000000]) == 0
    assert module_0.minSubArraySum([5, 0, -3]) == -3

    # Large values
    assert module_0.minSubArraySum([1000000, 2000000, -3000000]) == -3000000

    print("All tests passed!")


test_minSubArraySum()

# Generated at 2026-11-01 19:58:37.564055
# Unit test for function minSubArraySum
def test_minSubArraySum():
# nonce:7d942a8e
    # All positive: minimum subarray is the single smallest element
    assert module_0.minSubArraySum([2, 3, 4, 1, 7]) == 1
    assert module_0.minSubArraySum([1, 2, 3, 4, 5]) == 1
    # All negative: whole array yields the minimum sum
    assert module_0.minSubArraySum([-1, -2, -3]) == -6
    # Negatives followed by a positive
    assert module_0.minSubArraySum([-1, -2, -3, 4]) == -6
    # Positive prefix with negative tail
    assert module_0.minSubArraySum([10, 20, 30, 40, 50, -10, -20]) == -30
    # Single-element arrays
    assert module_0.minSubArraySum([5]) == 5
    assert module_0.minSubArraySum([-5]) == -5
    # Arrays containing zero
    assert module_0.minSubArraySum([0, 1, 2]) == 0
    assert module_0.minSubArraySum([0, 0, 0]) == 0
    # Mixed values
    assert module_0.minSubArraySum([3, -4, 1, 2, -1]) == -4
    assert module_0.minSubArraySum([1, -11, -4, 3, -9]) == -21

# Generated at 2026-11-01 19:59:24.014842
# Unit test for function minSubArraySum
def test_minSubArraySum():
    # All positive numbers -> minimum is the smallest element
    assert module_0.minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    assert module_0.minSubArraySum([1, 2, 3]) == 1
    assert module_0.minSubArraySum([10, 20, 30, 40, 100, 90, 80, 70]) == 10
    assert module_0.minSubArraySum([100, 1, 457, 9, 1, 87, 24, 7, 8, 19, 19, 40]) == 1

    # All negative numbers -> minimum is the sum of the whole array
    assert module_0.minSubArraySum([-1, -2, -3]) == -6
    assert module_0.minSubArraySum([-1, -2, -3, -4]) == -10

    # Single element arrays
    assert module_0.minSubArraySum([0]) == 0
    assert module_0.minSubArraySum([-1]) == -1
    assert module_0.minSubArraySum([5]) == 5

    # Arrays containing zero
    assert module_0.minSubArraySum([0, 1, 2, 3, 4, 5]) == 0
    assert module_0.minSubArraySum([1, 0, -2]) == -2

    # Mixed positive and negative numbers
    assert module_0.minSubArraySum([1, -1]) == -1
    assert module_0.minSubArraySum([3, -4, 1, -1]) == -4
    assert module_0.minSubArraySum([1, -2, 3, -5, 4]) == -5
    assert module_0.minSubArraySum([5, -3, 2, -1]) == -3
    assert module_0.minSubArraySum([-1, 2, -3]) == -3
    assert module_0.minSubArraySum([2, -3, 4, -1, 2]) == -3

    # Larger mixed array
    assert module_0.minSubArraySum([1, -2, -3, 4, -5, 6]) == -5

    print("All tests passed!")


if __name__ == "__main__":
    test_minSubArraySum()