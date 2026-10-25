

# Generated at 2026-10-25 03:35:14.249943
# Unit test for function count_nums
def test_count_nums():assert module_0.count_nums([]) == 0

# Generated at 2026-10-25 03:35:30.838214
# Unit test for function count_nums
def test_count_nums():assert module_0.count_nums([]) == 0

# Generated at 2026-10-25 03:36:04.596275
# Unit test for function count_nums
def test_count_nums():assert module_0.count_nums([]) == 0

# Generated at 2026-10-25 03:36:28.080531
# Unit test for function count_nums
def test_count_nums():
    assert module_0.count_nums([]) == 0
    assert module_0.count_nums([1, 1, 2]) == 3
    assert module_0.count_nums([-1, 11, -11]) == 1
    assert module_0.count_nums([0, 0, 0]) == 0
    assert module_0.count_nums([10, -20, 30]) == 2

# Generated at 2026-10-25 03:37:00.746754
# Unit test for function count_nums
def test_count_nums():
    assert module_0.count_nums([]) == 0
    assert module_0.count_nums([0, 0, 0]) == 0
    assert module_0.count_nums([1, 1, 2]) == 3
    assert module_0.count_nums([-1, -2, -3]) == 0
    assert module_0.count_nums([-1, 11, -11]) == 1
    assert module_0.count_nums([10, -11, 0]) == 1
    assert module_0.count_nums([-12, -19, -91]) == 2
    assert module_0.count_nums([123, -123, 456, -456]) == 4
    assert module_0.count_nums([-100, -101, -102]) == 1
    assert module_0.count_nums([1000, -1000, 2000]) == 2