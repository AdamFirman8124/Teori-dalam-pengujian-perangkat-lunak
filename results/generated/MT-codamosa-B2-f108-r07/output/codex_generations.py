

# Generated at 2026-11-01 21:21:59.630443
# Unit test for function count_nums
def test_count_nums():
    # Empty list -> no numbers counted
    assert module_0.count_nums([]) == 0

    # All negative single digits -> digit sums negative
    assert module_0.count_nums([-1, -2, -3]) == 0

    # Mixed: -1 -> -1, 11 -> 2, -11 -> -2
    assert module_0.count_nums([-1, 11, -11]) == 1

    # All positive single digits
    assert module_0.count_nums([1, 1, 2]) == 3

    # Zero is not counted (sum == 0)
    assert module_0.count_nums([0, 1]) == 1

    # 10 -> 1, -10 -> -1, 20 -> 2, -20 -> -2
    assert module_0.count_nums([10, -10, 20, -20]) == 2

    # 100 -> 1, -100 -> -1
    assert module_0.count_nums([100, -100]) == 1

    # -999 -> -9 + 9 + 9 = 9 > 0
    assert module_0.count_nums([-999]) == 1

    # Single positive number
    assert module_0.count_nums([5]) == 1

    # -123 -> -1+2+3 = 4, 456 -> 15, -789 -> -7+8+9 = 10, 0 -> 0
    assert module_0.count_nums([-123, 456, -789, 0]) == 3

    # -321 -> -3+2+1 = 0 (not counted), -123 -> 4 (counted)
    assert module_0.count_nums([-123, -321]) == 1

    # Larger mixed list
    assert module_0.count_nums([12, -34, 56, -78, 90]) == 4


test_count_nums()
print("All tests passed!")

# Generated at 2026-11-01 21:22:36.170458
# Unit test for function count_nums
def test_count_nums():
    # nonce:643d962c

    # Empty array
    assert module_0.count_nums([]) == 0

    # All positive digit sums
    assert module_0.count_nums([1, 1, 2]) == 3
    assert module_0.count_nums([123, 456, 789]) == 3

    # All negative digit sums (including zero sum)
    assert module_0.count_nums([-1, -2, 0]) == 0
    assert module_0.count_nums([-10, -20, -30]) == 0

    # Zero counts as non-positive
    assert module_0.count_nums([0]) == 0
    assert module_0.count_nums([0, 0, 0]) == 0

    # Mixed positive and negative digit sums
    assert module_0.count_nums([1, -12, 0]) == 2          # 1 -> 1, -12 -> -1+2=1, 0 -> 0
    assert module_0.count_nums([-1, 11, -11]) == 1        # -1 -> -1, 11 -> 2, -11 -> -1+1=0

    # Negative numbers where signed digit sum is still positive
    assert module_0.count_nums([-123]) == 1               # -123 -> -1+2+3=4
    assert module_0.count_nums([-999, 999]) == 2          # -999 -> -9+9+9=9

    # Negative numbers where signed digit sum is negative
    assert module_0.count_nums([-21]) == 0                # -21 -> -2+1=-1
    assert module_0.count_nums([-100]) == 0               # -100 -> -1+0+0=-1

    # Boundary: signed digit sum exactly zero is not counted
    assert module_0.count_nums([-101]) == 0               # -101 -> -1+0+1=0
    assert module_0.count_nums([10, -10]) == 1            # 10 -> 1, -10 -> -1

    # Single positive digit
    assert module_0.count_nums([5]) == 1
    assert module_0.count_nums([9]) == 1

    print("All tests passed!")


if __name__ == "__main__":
    test_count_nums()

# Generated at 2026-11-01 21:22:54.393597
# Unit test for function count_nums
def test_count_nums():
    # Empty array -> no numbers counted
    assert module_0.count_nums([]) == 0

    # All positive numbers with positive digit sums
    assert module_0.count_nums([1, 1, 2]) == 3

    # Zero has digit sum 0, not counted
    assert module_0.count_nums([0]) == 0

    # Mixed positives and negatives
    # digits_sum(-1) = -1, digits_sum(11) = 2, digits_sum(-11) = -1+1 = 0
    assert module_0.count_nums([-1, 11, -11]) == 1

    # digits_sum(-10) = -1, digits_sum(10) = 1
    assert module_0.count_nums([-10, 10]) == 1

    # Both have positive digit sums: 6 and (-1+2+3)=4
    assert module_0.count_nums([123, -123]) == 2

    # Negative leading digit makes sum non-positive
    # digits_sum(-5) = -5, digits_sum(5) = 5
    assert module_0.count_nums([-5, 5]) == 1

    # Multi-digit negatives where later digits outweigh the first
    # digits_sum(-19) = -1 + 9 = 8 > 0
    assert module_0.count_nums([-19]) == 1

    # Negative where sum is exactly zero is not counted
    # digits_sum(-19... ) vs digits_sum(-18) = -1 + 8 = 7 > 0
    assert module_0.count_nums([-18]) == 1

    # Larger example
    assert module_0.count_nums([0, -2, 34, -34, 100, -100]) == 3
    # 0 -> 0 (no), -2 -> -2 (no), 34 -> 7 (yes),
    # -34 -> -3+4 = 1 (yes), 100 -> 1 (yes), -100 -> -1 (no)

    print("All tests passed!")

# Generated at 2026-11-01 21:23:17.739781
# Unit test for function count_nums
def test_count_nums():
    # Empty array
    assert module_0.count_nums([]) == 0

    # All positive numbers count
    assert module_0.count_nums([1, 1, 2]) == 3
    assert module_0.count_nums([1, 2, 3, 4, 5]) == 5

    # Zero has digit sum 0 -> not positive
    assert module_0.count_nums([0]) == 0
    assert module_0.count_nums([0, 0, 0]) == 0

    # Single negative digit -> negative digit sum
    assert module_0.count_nums([-1]) == 0
    assert module_0.count_nums([-1, -2, -3]) == 0

    # Negative numbers whose first digit is outweighed -> positive sum
    assert module_0.count_nums([-12]) == 1              # -1 + 2 = 1
    assert module_0.count_nums([-123, 456, -789]) == 3  # 4, 15, 10

    # Negative numbers with zero or negative digit sums
    assert module_0.count_nums([-11]) == 0              # -1 + 1 = 0
    assert module_0.count_nums([-10]) == 0              # -1 + 0 = -1
    assert module_0.count_nums([-21, -31]) == 0         # -1, -2

    # Mixed values
    assert module_0.count_nums([1, -2, 3, -4, 5]) == 3
    assert module_0.count_nums([-1, 11, -11]) == 2      # -1, 2, 0

    # Large numbers
    assert module_0.count_nums([99999, -99999]) == 2    # 45, 27

    print("All tests passed!")


if __name__ == "__main__":
    test_count_nums()

# Generated at 2026-11-01 21:23:44.467539
# Unit test for function count_nums
def test_count_nums():
    # nonce:82935560
    # Empty list
    assert module_0.count_nums([]) == 0

    # All non-positive digit sums
    assert module_0.count_nums([-1, -2, 0]) == 0

    # All positive digit sums
    assert module_0.count_nums([1, 1, 2]) == 3

    # Negative numbers whose first-digit negation still yields positive sum
    assert module_0.count_nums([-123, 123, 456]) == 3  # sums: 4, 6, 15

    # Zero digit sum does not count
    assert module_0.count_nums([-11, 11]) == 1  # -1+1=0 (not counted), 1+1=2 (counted)

    # Single values
    assert module_0.count_nums([-1]) == 0
    assert module_0.count_nums([0]) == 0
    assert module_0.count_nums([5]) == 1

    # Mixed values
    assert module_0.count_nums([-12, 12, -34, 34]) == 4  # sums: 1, 3, 1, 7

    # Multi-digit negatives where negated first digit dominates
    assert module_0.count_nums([-10, -100]) == 0  # sums: -1, -1

    # Large numbers
    assert module_0.count_nums([99999, -99999]) == 2  # sums: 45, 27