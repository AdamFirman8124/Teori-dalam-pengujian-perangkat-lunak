

# Generated at 2026-11-02 10:05:04.109669
# Unit test for function pairs_sum_to_zero
def test_pairs_sum_to_zero():
    # Basic cases
    assert module_0.pairs_sum_to_zero([1, 3, 5, 0]) == False
    assert module_0.pairs_sum_to_zero([1, 3, -2, 1]) == False
    assert module_0.pairs_sum_to_zero([1, 2, 3, 7]) == False
    assert module_0.pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True

    # Edge cases
    assert module_0.pairs_sum_to_zero([]) == False
    assert module_0.pairs_sum_to_zero([1]) == False
    assert module_0.pairs_sum_to_zero([0]) == False
    assert module_0.pairs_sum_to_zero([0, 0]) == True   # two distinct indices with 0
    assert module_0.pairs_sum_to_zero([0, 1]) == False

    # Simple positive/negative pair
    assert module_0.pairs_sum_to_zero([1, -1]) == True
    assert module_0.pairs_sum_to_zero([-1, 1]) == True

    # Negative number cases
    assert module_0.pairs_sum_to_zero([-3, 9, -1, 3, 2, 30]) == True
    assert module_0.pairs_sum_to_zero([-3, 9, -1, 3, 2, 31]) == False
    assert module_0.pairs_sum_to_zero([-3, 9, -1, 4, 2, 30]) == False
    assert module_0.pairs_sum_to_zero([-3, 9, -1, 4, 2, 31]) == False

    # Duplicates
    assert module_0.pairs_sum_to_zero([2, 2, -2]) == True
    assert module_0.pairs_sum_to_zero([5, 5, 5]) == False

    # Same element must not pair with itself
    assert module_0.pairs_sum_to_zero([0]) == False

    print("All tests passed!")


# Run tests
test_pairs_sum_to_zero()

# Generated at 2026-11-02 10:05:32.783448
# Unit test for function pairs_sum_to_zero
def test_pairs_sum_to_zero():
    class TestPairsSumToZero(unittest.TestCase):

        def test_true_case_with_negation(self):
            self.assertTrue(module_0.pairs_sum_to_zero([1, 3, 5, 0]))
            self.assertTrue(module_0.pairs_sum_to_zero([1, 3, -2, 1]))

        def test_false_case_no_pairs(self):
            self.assertFalse(module_0.pairs_sum_to_zero([1, 2, 3, 7]))
            self.assertFalse(module_0.pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))

        def test_empty_list(self):
            self.assertFalse(module_0.pairs_sum_to_zero([]))

        def test_single_element(self):
            self.assertFalse(module_0.pairs_sum_to_zero([1]))
            self.assertFalse(module_0.pairs_sum_to_zero([0]))

        def test_two_elements_sum_zero(self):
            self.assertTrue(module_0.pairs_sum_to_zero([1, -1]))
            self.assertTrue(module_0.pairs_sum_to_zero([-5, 5]))

        def test_two_elements_sum_nonzero(self):
            self.assertFalse(module_0.pairs_sum_to_zero([1, 1]))
            self.assertFalse(module_0.pairs_sum_to_zero([2, -3]))

        def test_zero_with_zero(self):
            self.assertTrue(module_0.pairs_sum_to_zero([0, 0]))
            self.assertTrue(module_0.pairs_sum_to_zero([1, 0, 0, 3]))

        def test_single_zero_only(self):
            self.assertFalse(module_0.pairs_sum_to_zero([0]))

        def test_negative_numbers_only(self):
            self.assertTrue(module_0.pairs_sum_to_zero([-3, -1, 3]))
            self.assertFalse(module_0.pairs_sum_to_zero([-1, -2, -3]))

        def test_duplicates_but_no_zero_sum(self):
            self.assertFalse(module_0.pairs_sum_to_zero([1, 1, 1]))

        def test_large_numbers(self):
            self.assertTrue(module_0.pairs_sum_to_zero([1000000, -1000000]))
            self.assertFalse(module_0.pairs_sum_to_zero([1000000, 1000000]))

        def test_pair_not_adjacent(self):
            self.assertTrue(module_0.pairs_sum_to_zero([4, 7, 9, 1, -4]))

    suite = unittest.TestLoader().loadTestsFromTestCase(TestPairsSumToZero)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    test_pairs_sum_to_zero()

# Generated at 2026-11-02 10:06:27.979870
# Unit test for function pairs_sum_to_zero
def test_pairs_sum_to_zero():
    # Pairs that sum to zero
    assert module_0.pairs_sum_to_zero([1, -1]) == True
    assert module_0.pairs_sum_to_zero([3, -3, 2, 1]) == True
    assert module_0.pairs_sum_to_zero([1, 2, -3, 4]) == True
    assert module_0.pairs_sum_to_zero([1, 2, 3, 4, -4]) == True
    assert module_0.pairs_sum_to_zero([5, -5]) == True
    assert module_0.pairs_sum_to_zero([0, 0]) == True  # 0 + 0 == 0

    # No pairs sum to zero
    assert module_0.pairs_sum_to_zero([1, 3, 5, 0]) == False
    assert module_0.pairs_sum_to_zero([1, 3, -2, 1]) == False
    assert module_0.pairs_sum_to_zero([1, 2, 3, 7]) == False
    assert module_0.pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == False
    assert module_0.pairs_sum_to_zero([-3, 9, -1, 4, 2, 30]) == False
    assert module_0.pairs_sum_to_zero([1, 1, 1]) == False

    # Edge cases
    assert module_0.pairs_sum_to_zero([]) == False
    assert module_0.pairs_sum_to_zero([1]) == False
    assert module_0.pairs_sum_to_zero([0]) == False

    # Negative numbers only, no zero pair
    assert module_0.pairs_sum_to_zero([-1, -2, -3]) == False

    print("All tests passed!")


if __name__ == "__main__":
    test_pairs_sum_to_zero()

# Generated at 2026-11-02 10:07:40.989478
# Unit test for function pairs_sum_to_zero
def test_pairs_sum_to_zero():
    # Test with list containing a pair that sums to zero
    assert module_0.pairs_sum_to_zero([1, 3, -2, 1, -1]) == True
    assert module_0.pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
    assert module_0.pairs_sum_to_zero([1, -1]) == True

    # Test with list with no pair summing to zero
    assert module_0.pairs_sum_to_zero([1, 3, 5, 0]) == False
    assert module_0.pairs_sum_to_zero([1, 3, -2, 1]) == False
    assert module_0.pairs_sum_to_zero([1, 2, 3, 7]) == False

    # Test edge cases
    assert module_0.pairs_sum_to_zero([]) == False
    assert module_0.pairs_sum_to_zero([1]) == False

    # Test with zeros (0 + 0 = 0 requires two zeros)
    assert module_0.pairs_sum_to_zero([0, 0]) == True
    assert module_0.pairs_sum_to_zero([0]) == False

    # Test with negative numbers only
    assert module_0.pairs_sum_to_zero([-1, -2, -3]) == False
    assert module_0.pairs_sum_to_zero([-1, 1, -2, 2]) == True

# Generated at 2026-11-02 10:08:36.213644
# Unit test for function pairs_sum_to_zero
def test_pairs_sum_to_zero():
    # Pair exists: 1 + (-1) == 0
    assert module_0.pairs_sum_to_zero([1, 3, 5, 0]) == False
    assert module_0.pairs_sum_to_zero([1, 3, -2, 1]) == False
    assert module_0.pairs_sum_to_zero([1, 2, 3, 7]) == False
    assert module_0.pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == False
    assert module_0.pairs_sum_to_zero([1]) == False

    # No pair exists
    assert module_0.pairs_sum_to_zero([1, 3, 5, 0]) == False
    assert module_0.pairs_sum_to_zero([1, 3, -2, 1]) == False

    # Pair exists
    assert module_0.pairs_sum_to_zero([1, -1]) == True
    assert module_0.pairs_sum_to_zero([2, 4, -5, 3, -4, 7]) == True
    assert module_0.pairs_sum_to_zero([5, -5, 10]) == True
    assert module_0.pairs_sum_to_zero([0, 1, -3, 3]) == True

    # Zeros: two zeros form a pair summing to zero
    assert module_0.pairs_sum_to_zero([0, 0]) == True
    assert module_0.pairs_sum_to_zero([1, 0, 0]) == True

    # Single zero: no second element to pair with
    assert module_0.pairs_sum_to_zero([0]) == False

    # Empty list
    assert module_0.pairs_sum_to_zero([]) == False

    # Duplicates that do not sum to zero
    assert module_0.pairs_sum_to_zero([2, 2, 2]) == False

    # Negative-only list with a valid pair
    assert module_0.pairs_sum_to_zero([-2, -4, 2]) == True

    # Larger list without a pair
    assert module_0.pairs_sum_to_zero(list(range(1, 100))) == False

    # Larger list with a pair at the end
    assert module_0.pairs_sum_to_zero(list(range(1, 100)) + [-50]) == True

    print("All tests passed!")


test_pairs_sum_to_zero()