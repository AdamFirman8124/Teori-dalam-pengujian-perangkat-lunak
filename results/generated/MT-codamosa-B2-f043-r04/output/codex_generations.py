

# Generated at 2026-11-02 09:32:23.370201
# Unit test for function pairs_sum_to_zero
def test_pairs_sum_to_zero():
    # No pair sums to zero
    assert module_0.pairs_sum_to_zero([1, 3, 5, 0]) == False
    assert module_0.pairs_sum_to_zero([1, 3, -2, 1]) == False
    assert module_0.pairs_sum_to_zero([1, 2, 3, 7]) == False

    # Pair sums to zero
    assert module_0.pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
    assert module_0.pairs_sum_to_zero([1]) == False
    assert module_0.pairs_sum_to_zero([-3, 9, 5, 1, 3]) == True

    # Edge cases
    assert module_0.pairs_sum_to_zero([]) == False
    assert module_0.pairs_sum_to_zero([0, 0]) == True  # two zeros sum to zero
    assert module_0.pairs_sum_to_zero([0]) == False    # single zero, no pair
    assert module_0.pairs_sum_to_zero([1, -1]) == True
    assert module_0.pairs_sum_to_zero([5, 5, -5]) == True
    assert module_0.pairs_sum_to_zero([2, 4, 6]) == False

    print("All tests passed!")


if __name__ == "__main__":
    test_pairs_sum_to_zero()

# Generated at 2026-11-02 09:36:21.021134
# Unit test for function pairs_sum_to_zero
def test_pairs_sum_to_zero():import unittest


class TestPairsSumToZero(unittest.TestCase):

    def test_no_pairs_sum_to_zero(self):
        self.assertFalse(module_0.pairs_sum_to_zero([1, 3, 5, 0]))

    def test_negative_and_positive_no_zero_sum(self):
        self.assertFalse(module_0.pairs_sum_to_zero([1, 3, -2, 1]))

    def test_all_positive(self):
        self.assertFalse(module_0.pairs_sum_to_zero([1, 2, 3, 7]))

    def test_negative_not_matched(self):
        self.assertFalse(module_0.pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))

    def test_single_element(self):
        self.assertFalse(module_0.pairs_sum_to_zero([1]))

    def test_matching_pair(self):
        self.assertTrue(module_0.pairs_sum_to_zero([-3, 9, -1, 3, 2, 4]))

    def test_simple_pair(self):
        self.assertTrue(module_0.pairs_sum_to_zero([1, -1]))

    def test_two_zeros(self):
        self.assertTrue(module_0.pairs_sum_to_zero([0, 0]))

    def test_single_zero(self):
        self.assertFalse(module_0.pairs_sum_to_zero([0]))

    def test_empty_list(self):
        self.assertFalse(module_0.pairs_sum_to_zero([]))

    def test_multiple_pairs(self):
        self.assertTrue(module_0.pairs_sum_to_zero([2, -2, 3, -3]))

    def test_negative_only_no_match(self):
        self.assertFalse(module_0.pairs_sum_to_zero([-1, -2, -3]))


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 09:38:55.735245
# Unit test for function pairs_sum_to_zero
def test_pairs_sum_to_zero():
    # Pair exists: 1 + (-1) == 0
    assert module_0.pairs_sum_to_zero([1, 3, 5, 0]) == False
    assert module_0.pairs_sum_to_zero([1, 3, -2, 1]) == False
    assert module_0.pairs_sum_to_zero([1, 2, 3, 7]) == False
    assert module_0.pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == False
    assert module_0.pairs_sum_to_zero([1]) == False

    # No pair sums to zero
    assert module_0.pairs_sum_to_zero([1, -1]) == True
    assert module_0.pairs_sum_to_zero([1, 2, -2, 7]) == True
    assert module_0.pairs_sum_to_zero([-3, 1, 2, 3, 7]) == True
    assert module_0.pairs_sum_to_zero([5, -5, 10]) == True

    # Zero handling: two zeros sum to zero
    assert module_0.pairs_sum_to_zero([0, 0]) == True
    assert module_0.pairs_sum_to_zero([0]) == False

    # Edge cases: empty list and single element
    assert module_0.pairs_sum_to_zero([]) == False

    # Duplicates and mixed values
    assert module_0.pairs_sum_to_zero([2, 2, -2]) == True
    assert module_0.pairs_sum_to_zero([2, 2, 2]) == False
    assert module_0.pairs_sum_to_zero([-10, 10, -10, 10]) == True
    assert module_0.pairs_sum_to_zero([100, -100, 50, -50]) == True
    assert module_0.pairs_sum_to_zero([100, -99, 50, -50]) == True

    print("All tests passed!")


if __name__ == "__main__":
    test_pairs_sum_to_zero()