

# Generated at 2026-11-02 10:34:52.052781
# Unit test for function count_nums
def test_count_nums():
    # Empty array
    assert module_0.count_nums([]) == 0
    # Single elements
    assert module_0.count_nums([0]) == 0
    assert module_0.count_nums([1]) == 1
    assert module_0.count_nums([-1]) == 0
    # All negative single digits -> digit sums negative
    assert module_0.count_nums([-1, -2, -3]) == 0
    # Mixed with zero digit sum
    assert module_0.count_nums([-1, 11, -11]) == 1
    # All positive
    assert module_0.count_nums([1, 1, 2]) == 3
    # Zero is not counted
    assert module_0.count_nums([0, 1]) == 1
    # Multi-digit numbers
    assert module_0.count_nums([10, -10, 20, -20]) == 2
    assert module_0.count_nums([99, -99, 9, -9]) == 2
    # Negative numbers whose signed digit sum is positive
    assert module_0.count_nums([-123, 123, 456, -456]) == 4
    # Negative number with negative signed digit sum
    assert module_0.count_nums([-21, 12]) == 1
    # Larger mixed case
    assert module_0.count_nums([5, -55, 55, -5, 0, 14]) == 3

# Generated at 2026-11-02 10:35:38.120729
# Unit test for function count_nums
def test_count_nums():
    # Empty list -> 0
    assert module_0.count_nums([]) == 0

    # All positive digit sums
    assert module_0.count_nums([1, 1, 2]) == 3

    # All negative results (first digit negated dominates)
    assert module_0.count_nums([-1, -2, -3]) == 0

    # Mixed: -1 -> -1, 11 -> 2, -11 -> 0 (not > 0)
    assert module_0.count_nums([-1, 11, -11]) == 1

    # Zero contributes nothing
    assert module_0.count_nums([0, 1]) == 1

    # Negative number with larger digit sum stays positive
    assert module_0.count_nums([123, -123]) == 2

    # -10 -> -1 (not counted), 10 -> 1 (counted)
    assert module_0.count_nums([-10, 10]) == 1

    # Multi-digit negatives where sum is exactly zero
    assert module_0.count_nums([-11, 22]) == 1

    print("All test_count_nums tests passed!")


if __name__ == "__main__":
    test_count_nums()

# Generated at 2026-11-02 10:36:50.916968
# Unit test for function count_nums
def test_count_nums():
    # Empty array
    assert module_0.count_nums([]) == 0

    # Canonical examples
    assert module_0.count_nums([-1, 11, -11]) == 1
    assert module_0.count_nums([1, 1, 2]) == 3

    # Zeros have digit sum 0 (not counted)
    assert module_0.count_nums([0, 0, 0]) == 0

    # All negative single digits -> negative digit sums
    assert module_0.count_nums([-1, -2, -3, -9]) == 0

    # Single positive digit
    assert module_0.count_nums([5]) == 1
    assert module_0.count_nums([-5]) == 0

    # Negative multi-digit numbers where later digits outweigh the negated first digit
    assert module_0.count_nums([-12, 12]) == 2      # -1+2=1 > 0, 1+2=3 > 0
    assert module_0.count_nums([-123, 123]) == 2    # -1+2+3=4 > 0, 1+2+3=6 > 0

    # Negative multi-digit numbers where the negated first digit dominates
    assert module_0.count_nums([-20, -100]) == 0    # -2+0=-2, -1+0+0=-1

    # Trailing zero cases
    assert module_0.count_nums([10, -10]) == 1      # 1+0=1 > 0, -1+0=-1

    # Mixed array
    assert module_0.count_nums([0, 1, -1, 100, -100, 999]) == 3

    # Large numbers
    assert module_0.count_nums([999999, -999999]) == 2  # 54 > 0, -9+99999=99990 > 0

# Generated at 2026-11-02 10:38:04.442657
# Unit test for function count_nums
def test_count_nums():
    # Empty list -> no numbers
    assert module_0.count_nums([]) == 0

    # All positive numbers -> all counted
    assert module_0.count_nums([1, 1, 2]) == 3

    # Mixed signs: -1 -> -1 (not counted), 11 -> 2 (counted), -11 -> -1+1 = 0 (not counted)
    assert module_0.count_nums([-1, 11, -11]) == 1

    # Single positive number
    assert module_0.count_nums([5]) == 1

    # Single negative number: -9 -> -9 (not counted)
    assert module_0.count_nums([-9]) == 0

    # Zero has digit sum 0 -> not counted
    assert module_0.count_nums([0]) == 0

    # -12 -> -1+2 = 1 (counted), 12 -> 3 (counted)
    assert module_0.count_nums([-12, 12]) == 2

    # Negative leading digit larger than rest of digits: -101 -> -1+0+1 = 0 (not counted)
    assert module_0.count_nums([-101]) == 0

    # Negative where later digits outweigh first: -123 -> -1+2+3 = 4 (counted)
    assert module_0.count_nums([-123]) == 1

    # Larger mixed example
    # 10 -> 1, -34 -> -3+4 = 1, 22 -> 4, -5 -> -5, 0 -> 0
    assert module_0.count_nums([10, -34, 22, -5, 0]) == 3

    print("All tests passed!")


test_count_nums()

# Generated at 2026-11-02 10:38:56.870045
# Unit test for function count_nums
def test_count_nums():
    assert module_0.count_nums([]) == 0  # empty array
    assert module_0.count_nums([1, 1, 2]) == 3  # all positive sums
    assert module_0.count_nums([-1, -2, -3]) == 0  # all negative single digits
    assert module_0.count_nums([-1, 11, -11]) == 1  # mixed: -1 -> -1, 11 -> 2, -11 -> -2
    assert module_0.count_nums([0]) == 0  # zero has digit sum 0, not counted
    assert module_0.count_nums([123, 456]) == 2  # multi-digit positives
    assert module_0.count_nums([-123, -456]) == 2  # negatives where sum stays positive
    assert module_0.count_nums([-5, 5]) == 1  # -5 -> -5, 5 -> 5
    assert module_0.count_nums([-1, 0, 1]) == 1  # only 1 counts
    assert module_0.count_nums([20, -20, 100]) == 3  # 2, -2, 1 all positive
    print("All test_count_nums tests passed!")


if __name__ == "__main__":
    test_count_nums()