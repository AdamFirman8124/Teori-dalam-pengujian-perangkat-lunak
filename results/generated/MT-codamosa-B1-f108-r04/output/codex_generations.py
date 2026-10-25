

# Generated at 2026-10-24 13:25:15.095630
# Unit test for function count_nums

# Generated at 2026-10-24 13:25:17.511271
# Unit test for function count_nums

# Generated at 2026-10-24 13:25:19.930033
# Unit test for function count_nums

# Generated at 2026-10-24 13:25:22.343281
# Unit test for function count_nums

# Generated at 2026-10-24 13:25:30.366547
# Unit test for function count_nums
def test_count_nums():
    # Empty input
    assert module_0.count_nums([]) == 0

    # All positive digit sums
    assert module_0.count_nums([1, 1, 2]) == 3

    # Mixed: -1 -> -1 (no), 11 -> 2 (yes), -11 -> -1+1 = 0 (no)
    assert module_0.count_nums([-1, 11, -11]) == 1

    # Negative with heavier tail digits: -123 -> -1+2+3 = 4 (yes)
    assert module_0.count_nums([-123]) == 1

    # Negative with heavy first digit: -32 -> -3+2 = -1 (no)
    assert module_0.count_nums([-32]) == 0

    # Zero contributes nothing
    assert module_0.count_nums([0]) == 0

    # Multi-digit mix
    # 156 -> 12 (yes), -23 -> -2+3 = 1 (yes), -99 -> -9+9 = 0 (no), 0 -> 0 (no)
    assert module_0.count_nums([156, -23, -99, 0]) == 2

# Generated at 2026-10-24 13:25:41.848721
# Unit test for function count_nums
def test_count_nums():
    assert module_0.count_nums([]) == 0
    assert module_0.count_nums([0]) == 0
    assert module_0.count_nums([1, 2, 3, 4]) == 4
    assert module_0.count_nums([-1, -2, -3, -4]) == 0
    assert module_0.count_nums([-10, -11, -12]) == 1        # -1, 0, 1
    assert module_0.count_nums([-123]) == 1                 # -1 + 2 + 3 = 4
    assert module_0.count_nums([-1000]) == 0                # -1 + 0 + 0 + 0 = -1
    assert module_0.count_nums([10, 100, 101]) == 3         # 1, 1, 2
    assert module_0.count_nums([-1, 21, -11]) == 1          # -1, 3, 0
    assert module_0.count_nums([999, -999]) == 2            # 27, -9 + 9 + 9 = 9
    assert module_0.count_nums([-1, 11, -11, 3, 0, -100, 100]) == 3
    print("All tests passed")

test_count_nums()

# Generated at 2026-10-24 13:25:43.285566
# Unit test for function count_nums
def test_count_nums():
    assert module_0.count_nums([]) == 0
    assert module_0.count_nums([0]) == 0
    assert module_0.count_nums([1, 2, 3, 4]) == 4
    assert module_0.count_nums([-1, -2, -3, -4]) == 0
    assert module_0.count_nums([-10, -11, -12]) == 1        # -1, 0, 1
    assert module_0.count_nums([-123]) == 1                 # -1 + 2 + 3 = 4
    assert module_0.count_nums([-1000]) == 0                # -1 + 0 + 0 + 0 = -1
    assert module_0.count_nums([10, 100, 101]) == 3         # 1, 1, 2
    assert module_0.count_nums([-1, 21, -11]) == 1          # -1, 3, 0
    assert module_0.count_nums([999, -999]) == 2            # 27, -9 + 9 + 9 = 9
    assert module_0.count_nums([-1, 11, -11, 3, 0, -100, 100]) == 3
    print("All tests passed")

test_count_nums()

# Generated at 2026-10-24 13:25:44.774159
# Unit test for function count_nums
def test_count_nums():
    assert module_0.count_nums([]) == 0
    assert module_0.count_nums([0]) == 0
    assert module_0.count_nums([1, 2, 3, 4]) == 4
    assert module_0.count_nums([-1, -2, -3, -4]) == 0
    assert module_0.count_nums([-10, -11, -12]) == 1        # -1, 0, 1
    assert module_0.count_nums([-123]) == 1                 # -1 + 2 + 3 = 4
    assert module_0.count_nums([-1000]) == 0                # -1 + 0 + 0 + 0 = -1
    assert module_0.count_nums([10, 100, 101]) == 3         # 1, 1, 2
    assert module_0.count_nums([-1, 21, -11]) == 1          # -1, 3, 0
    assert module_0.count_nums([999, -999]) == 2            # 27, -9 + 9 + 9 = 9
    assert module_0.count_nums([-1, 11, -11, 3, 0, -100, 100]) == 3
    print("All tests passed")

test_count_nums()