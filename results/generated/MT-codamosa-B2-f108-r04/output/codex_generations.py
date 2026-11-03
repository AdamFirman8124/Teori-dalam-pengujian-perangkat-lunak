

# Generated at 2026-11-02 22:09:36.952739
# Unit test for function count_nums
def test_count_nums():
    # Empty array
    assert module_0.count_nums([]) == 0

    # All positive single digits have positive digit sums
    assert module_0.count_nums([1, 1, 2]) == 3

    # Zero has digit sum 0, not counted
    assert module_0.count_nums([0]) == 0

    # Negative single-digit numbers have negative digit sums, not counted
    assert module_0.count_nums([-1, -2, -3]) == 0

    # Mixed positives and negatives
    # -1 -> -1 (not counted), 11 -> 2 (counted), -11 -> -1+1 = 0 (not counted)
    assert module_0.count_nums([-1, 11, -11]) == 1

    # Negative multi-digit with positive weighted sum
    # -12 -> -1+2 = 1 (counted), -123 -> -1+2+3 = 4 (counted)
    assert module_0.count_nums([-12, -123]) == 2

    # Negative multi-digit with negative weighted sum
    # -21 -> -2+1 = -1 (not counted), -99 -> -9+9 = 0 (not counted)
    assert module_0.count_nums([-21, -99]) == 0

    # Mixed large case
    # 1 -> 1 (counted), -12 -> 1 (counted), 0 -> 0 (no), -1 -> -1 (no)
    assert module_0.count_nums([1, -12, 0, -1]) == 2

    # All zeros
    assert module_0.count_nums([0, 0, 0]) == 0

    # Multi-digit positives
    assert module_0.count_nums([123, 456, 789]) == 3

    # Negative where first digit smaller than rest of digits
    # -19 -> -1+9 = 8 (counted), -91 -> -9+1 = -8 (not counted)
    assert module_0.count_nums([-19, -91]) == 1

    test_count_nums_passed = True
    assert test_count_nums_passed


class TestCountNums(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(module_0.count_nums([]), 0)

    def test_positive(self):
        self.assertEqual(module_0.count_nums([1, 1, 2]), 3)

    def test_zero_not_counted(self):
        self.assertEqual(module_0.count_nums([0, 0]), 0)

    def test_negative_single_digits(self):
        self.assertEqual(module_0.count_nums([-1, -2, -3]), 0)

    def test_mixed(self):
        self.assertEqual(module_0.count_nums([-1, 11, -11]), 1)
        self.assertEqual(module_0.count_nums([1, -12, 0, -1]), 2)

    def test_negative_multidigit(self):
        self.assertEqual(module_0.count_nums([-12, -123]), 2)
        self.assertEqual(module_0.count_nums([-21, -99]), 0)
        self.assertEqual(module_0.count_nums([-19, -91]), 1)


if __name__ == "__main__":
    test_count_nums()
    print("All tests passed!")
    unittest.main()

# Generated at 2026-11-02 22:11:53.018880
# Unit test for function count_nums
def test_count_nums():
    # Empty array -> 0
    assert module_0.count_nums([]) == 0

    # All positive digit sums
    assert module_0.count_nums([1, 1, 2]) == 3

    # -1 -> -1, 11 -> 2, -11 -> 0 (zero is not counted)
    assert module_0.count_nums([-1, 11, -11]) == 1

    # All negative digit sums
    assert module_0.count_nums([-1, -2, -3]) == 0

    # Zero has digit sum 0 -> not counted
    assert module_0.count_nums([0]) == 0

    # Negated first digit can still yield a positive sum
    assert module_0.count_nums([123, -123]) == 2  # 6 and (-1+2+3)=4

    # Mix of single/double digit positives and negatives
    assert module_0.count_nums([5, -5, 10, -10]) == 2  # 5, -5, 1, -1

    # Larger negatives
    assert module_0.count_nums([-19, 91, -91]) == 2  # 8, 10, -8

    # Duplicates are counted individually
    assert module_0.count_nums([22, 22, -22]) == 2  # 4, 4, 0

    print("All tests passed!")

# Generated at 2026-11-02 22:14:03.898089
# Unit test for function count_nums
def test_count_nums():
    # Empty array
    assert module_0.count_nums([]) == 0

    # All positive single digits
    assert module_0.count_nums([1, 1, 2]) == 3

    # Mix of positive and negative
    assert module_0.count_nums([-1, 11, -11]) == 1

    # Zero has digit sum 0, not counted
    assert module_0.count_nums([0]) == 0

    # Negative numbers where digit sum is positive
    # digits_sum(-123) = -1 + 2 + 3 = 4 > 0
    # digits_sum(456) = 15 > 0
    # digits_sum(-789) = -7 + 8 + 9 = 10 > 0
    assert module_0.count_nums([-123, 456, -789]) == 3

    # Negative numbers where digit sum is negative (not counted)
    assert module_0.count_nums([-1, -2, -3]) == 0

    # Negative number with digit sum exactly zero (not counted)
    # digits_sum(-11) = -1 + 1 = 0
    assert module_0.count_nums([-11]) == 0

    # Single positive number
    assert module_0.count_nums([5]) == 1

    # Positive multi-digit vs negative counterpart
    # digits_sum(10) = 1 > 0, digits_sum(-10) = -1 <= 0
    assert module_0.count_nums([10, -10]) == 1

    # Negative numbers where sign matters
    # digits_sum(-12) = -1 + 2 = 1 > 0
    # digits_sum(-13) = -1 + 3 = 2 > 0
    assert module_0.count_nums([-12, -13]) == 2

    # Larger mixed set
    # digits_sum(12) = 3 > 0
    # digits_sum(-6) = -6 <= 0
    # digits_sum(100) = 1 > 0
    # digits_sum(-100) = -1 <= 0
    assert module_0.count_nums([12, -6, 100, -100]) == 2

# Generated at 2026-11-02 22:15:57.767720
# Unit test for function count_nums
def test_count_nums():
# nonce:ed096903
    # Empty array should return 0
    assert module_0.count_nums([]) == 0

    # All positive numbers have positive digit sums
    assert module_0.count_nums([1, 1, 2]) == 3

    # All negative single-digit numbers have negative digit sums
    assert module_0.count_nums([-1, -2, -3]) == 0

    # Mix of negatives and positives: -1 -> -1, 1 -> 1, -2 -> -2, 2 -> 2
    assert module_0.count_nums([-1, 1, -2, 2]) == 2

    # -1 -> -1, 1 -> 1, 9 -> 9, -2 -> -2, 2 -> 2
    assert module_0.count_nums([-1, 1, 9, -2, 2]) == 3

    # Zero has digit sum 0 (not counted)
    assert module_0.count_nums([0]) == 0

    # Multi-digit negatives: -123 -> -1+2+3 = 4, 123 -> 6
    assert module_0.count_nums([-123, 123]) == 2

    # -11 -> -1+1 = 0 (not counted), 11 -> 2 (counted)
    assert module_0.count_nums([-11, 11]) == 1

    # Negative leading digit outweighed by rest: -230 -> -2+3+0 = 1
    assert module_0.count_nums([-230]) == 1

    # Negative leading digit not outweighed: -400 -> -4+0+0 = -4
    assert module_0.count_nums([-400]) == 0