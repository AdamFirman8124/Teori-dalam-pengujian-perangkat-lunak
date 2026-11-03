

# Generated at 2026-11-03 00:05:58.444596
# Unit test for function count_nums
def test_count_nums():
    # nonce:ae0a3994

    # Empty input
    assert module_0.count_nums([]) == 0

    # All positive digit sums
    assert module_0.count_nums([1, 1, 2]) == 3
    assert module_0.count_nums([1, 2, 3, 4, 5]) == 5
    assert module_0.count_nums([123, 456]) == 2  # 6 and 15 are both > 0

    # Zero has digit sum 0 -> not counted (must be strictly > 0)
    assert module_0.count_nums([0]) == 0
    assert module_0.count_nums([0, 0, 0]) == 0

    # Negative numbers: first digit is negated
    assert module_0.count_nums([-1]) == 0        # -1 + 0 = -1
    assert module_0.count_nums([-11]) == 0       # -1 + 1 = 0
    assert module_0.count_nums([-12]) == 1       # -1 + 2 = 1
    assert module_0.count_nums([-123]) == 1      # -1 + 2 + 3 = 4
    assert module_0.count_nums([-10]) == 0       # -1 + 0 = -1
    assert module_0.count_nums([-91]) == 0       # -9 + 1 = -8
    assert module_0.count_nums([-99]) == 0       # -9 + 9 = 0
    assert module_0.count_nums([-100]) == 0      # -1 + 0 + 0 = -1

    # Classic example
    assert module_0.count_nums([-1, 11, -11]) == 1  # only 11 -> 2 > 0

    # Mixed positives and negatives
    assert module_0.count_nums([-1, 1, -2, 2]) == 2
    assert module_0.count_nums([-12, 12]) == 2       # 1 and 3 both > 0
    assert module_0.count_nums([0, -1, -11, 5]) == 1

    # Large values
    assert module_0.count_nums([999999999]) == 1
    assert module_0.count_nums([-999999999]) == 1    # -9 + 8*9 = 63 > 0

    # Return type check
    assert isinstance(module_0.count_nums([1, -1]), int)

    print("All test_count_nums tests passed!")

# Generated at 2026-11-03 00:07:34.063626
# Unit test for function count_nums
def test_count_nums():
# nonce:ee94d768
    assert module_0.count_nums([]) == 0
    assert module_0.count_nums([-1, 11, -11]) == 1
    assert module_0.count_nums([1, 1, 2]) == 3
    assert module_0.count_nums([0, 0, 0]) == 0
    assert module_0.count_nums([-1, -2, -3]) == 0
    assert module_0.count_nums([123, -123]) == 2
    assert module_0.count_nums([-10]) == 0
    assert module_0.count_nums([-12]) == 1
    assert module_0.count_nums([5, -55, 555]) == 2
    assert module_0.count_nums([999, -999, 99]) == 3

# Generated at 2026-11-03 00:09:49.745669
# Unit test for function count_nums
def test_count_nums():
    # Empty array
    assert module_0.count_nums([]) == 0

    # All positive digit sums
    assert module_0.count_nums([1, 1, 2]) == 3

    # Mixed positive and negative numbers
    assert module_0.count_nums([-1, 11, -11]) == 1

    # Single element with positive digit sum
    assert module_0.count_nums([5]) == 1

    # Single element with negative digit sum (negative first digit)
    assert module_0.count_nums([-5]) == 0

    # Zero has digit sum of 0, not counted
    assert module_0.count_nums([0]) == 0

    # Negative number where digit sum is exactly zero
    assert module_0.count_nums([-11]) == 0
    assert module_0.count_nums([-101]) == 0  # -1 + 0 + 1 = 0

    # Negative number with positive digit sum
    assert module_0.count_nums([-12]) == 1  # -1 + 2 = 1

    # Large numbers
    assert module_0.count_nums([123, -123, 999]) == 2  # 6, -4, 27

    # All negative digit sums
    assert module_0.count_nums([-1, -2, -3]) == 0

    # Combination of zeros and positives
    assert module_0.count_nums([0, 10, 20]) == 2

    # Multi-digit negatives with mixed results
    assert module_0.count_nums([-20, -21, -30]) == 2  # -2, 1, -3

    print("All tests passed!")


test_count_nums()

# Generated at 2026-11-03 00:11:58.061270
# Unit test for function count_nums
def test_count_nums():
    # Empty array
    assert module_0.count_nums([]) == 0

    # Single positive numbers
    assert module_0.count_nums([1]) == 1
    assert module_0.count_nums([5]) == 1
    assert module_0.count_nums([123]) == 1  # 1+2+3 = 6 > 0

    # Single negative numbers
    assert module_0.count_nums([-1]) == 0  # sum = -1
    assert module_0.count_nums([-12]) == 0  # sum = -1+2 = 1 > 0, so actually 1
    assert module_0.count_nums([-12]) == 1  # -1+2 = 1 > 0
    assert module_0.count_nums([-123]) == 1  # -1+2+3 = 4 > 0
    assert module_0.count_nums([-21]) == 0  # -2+1 = -1, not > 0

    # Zero is not counted (digit sum is 0, not > 0)
    assert module_0.count_nums([0]) == 0
    assert module_0.count_nums([0, 0, 0]) == 0

    # Classic example: only 11 has positive signed digit sum
    assert module_0.count_nums([-1, 11, -11]) == 1
    # -1 -> -1, 11 -> 2, -11 -> (-1)+1 = 0

    # All positive
    assert module_0.count_nums([1, 1, 2]) == 3

    # All negative with negative sums
    assert module_0.count_nums([-1, -2, -3]) == 0

    # Mixed
    assert module_0.count_nums([1, -1, 0, 12, -12]) == 3
    # 1 -> 1, -1 -> -1, 0 -> 0, 12 -> 3, -12 -> 1

    # Multi-digit negatives where sign applies to first digit
    assert module_0.count_nums([-30, -3]) == 0
    # -30 -> -3+0 = -3, -3 -> -3

    assert module_0.count_nums([10, -10]) == 2
    # 10 -> 1, -10 -> -1+0 = -1... wait: -10 -> -(1)+0 = -1
    # Correction: only 10 counts
    assert module_0.count_nums([10, -10]) == 1
    # 10 -> 1 > 0; -10 -> -1+0 = -1, not > 0

    # Large numbers
    assert module_0.count_nums([999999999]) == 1
    assert module_0.count_nums([-999999999]) == 0  # -9+9+9+9+9+9+9+9+9 = 63 > 0
    assert module_0.count_nums([-999999999]) == 1  # -9 + (8 nines) = -9+72 = 63 > 0

    # Negative first digit outweighs rest
    assert module_0.count_nums([-90]) == 0  # -9+0 = -9
    assert module_0.count_nums([-91]) == 0  # -9+1 = -8
    assert module_0.count_nums([-19]) == 1  # -1+9 = 8 > 0

    # Combination of all above behaviors
    assert module_0.count_nums([-19, -91, 0, 7, -7]) == 2
    # -19 -> 8 (>0), -91 -> -8, 0 -> 0, 7 -> 7 (>0), -7 -> -7

# Generated at 2026-11-03 00:14:10.484610
# Unit test for function count_nums
def test_count_nums():
    # Empty array
    assert module_0.count_nums([]) == 0
    # Classic cases
    assert module_0.count_nums([-1, 11, -11]) == 1
    assert module_0.count_nums([1, 1, 2]) == 3
    # Zero contributes nothing (digit sum is 0, not > 0)
    assert module_0.count_nums([0]) == 0
    assert module_0.count_nums([0, 0, 0]) == 0
    # Negative single digits have negative digit sums
    assert module_0.count_nums([-5]) == 0
    assert module_0.count_nums([-1, -2, -3]) == 0
    # Negative multi-digit numbers where first digit is outweighed
    assert module_0.count_nums([-123, 123]) == 2   # -1+2+3=4, 1+2+3=6
    assert module_0.count_nums([-12, 13]) == 2     # -1+2=1, 1+3=4
    assert module_0.count_nums([-15, 25, -32]) == 2  # 4, 7, -3+2=-1
    # Negative multi-digit numbers where digit sum is <= 0
    assert module_0.count_nums([-10]) == 0         # -1+0=-1
    assert module_0.count_nums([-11]) == 0         # -1+1=0
    assert module_0.count_nums([-100]) == 0        # -1+0+0=-1
    # Mixed positive/negative results
    assert module_0.count_nums([1, -1, 2, -2, 3]) == 3
    assert module_0.count_nums([100, -100]) == 1   # 1 > 0, -1 <= 0
    assert module_0.count_nums([999, -999, 55, -55]) == 3  # 27, -9+9+9=9, 10, -5+5=0