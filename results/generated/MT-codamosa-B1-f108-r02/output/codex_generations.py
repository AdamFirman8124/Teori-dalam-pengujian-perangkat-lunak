

# Generated at 2026-10-24 13:51:06.223563
# Unit test for function count_nums

# Generated at 2026-10-24 13:51:08.639454
# Unit test for function count_nums

# Generated at 2026-10-24 13:51:11.055807
# Unit test for function count_nums

# Generated at 2026-10-24 13:51:13.471223
# Unit test for function count_nums

# Generated at 2026-10-24 13:51:15.885812
# Unit test for function count_nums

# Generated at 2026-10-24 13:51:18.298517
# Unit test for function count_nums

# Generated at 2026-10-24 13:51:20.712887
# Unit test for function count_nums

# Generated at 2026-10-24 13:51:23.128209
# Unit test for function count_nums

# Generated at 2026-10-24 13:51:25.548259
# Unit test for function count_nums

# Generated at 2026-10-24 13:51:27.963020
# Unit test for function count_nums

# Generated at 2026-10-24 13:51:30.379710
# Unit test for function count_nums

# Generated at 2026-10-24 13:51:32.795996
# Unit test for function count_nums

# Generated at 2026-10-24 13:51:35.210103
# Unit test for function count_nums

# Generated at 2026-10-24 13:51:37.625964
# Unit test for function count_nums

# Generated at 2026-10-24 13:51:40.037714
# Unit test for function count_nums

# Generated at 2026-10-24 13:51:42.450875
# Unit test for function count_nums

# Generated at 2026-10-24 13:51:44.865217
# Unit test for function count_nums

# Generated at 2026-10-24 13:51:47.303766
# Unit test for function count_nums

# Generated at 2026-10-24 13:51:49.704139
# Unit test for function count_nums

# Generated at 2026-10-24 13:51:52.118315
# Unit test for function count_nums

# Generated at 2026-10-24 13:51:54.532471
# Unit test for function count_nums

# Generated at 2026-10-24 13:51:56.947638
# Unit test for function count_nums

# Generated at 2026-10-24 13:51:59.362184
# Unit test for function count_nums

# Generated at 2026-10-24 13:52:01.779803
# Unit test for function count_nums

# Generated at 2026-10-24 13:52:17.455617
# Unit test for function count_nums
def test_count_nums():
    assert module_0.count_nums([]) == 0
    assert module_0.count_nums([0]) == 0
    assert module_0.count_nums([1, 2, 3]) == 3
    assert module_0.count_nums([1, 1, 2]) == 3
    assert module_0.count_nums([-1, -2, -3]) == 0
    assert module_0.count_nums([-1, 11, -11]) == 1
    assert module_0.count_nums([-10, 10]) == 1
    assert module_0.count_nums([-123]) == 1
    assert module_0.count_nums([-19]) == 1
    assert module_0.count_nums([-100]) == 0
    assert module_0.count_nums([-11]) == 0
    assert module_0.count_nums([100, -100]) == 1
    assert module_0.count_nums([5, -5]) == 1
    assert module_0.count_nums([-11, 11, 0]) == 1
    assert module_0.count_nums([123, -123, 1000, -1000]) == 3
    assert module_0.count_nums([19, -19, 90, -90]) == 3
    assert module_0.count_nums([999, -999]) == 2

# Generated at 2026-10-24 13:52:18.894763
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

# Generated at 2026-10-24 13:52:20.201229
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

# Generated at 2026-10-24 13:52:21.523583
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

# Generated at 2026-10-24 13:52:22.842753
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

# Generated at 2026-10-24 13:52:24.177034
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

# Generated at 2026-10-24 13:52:25.504767
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