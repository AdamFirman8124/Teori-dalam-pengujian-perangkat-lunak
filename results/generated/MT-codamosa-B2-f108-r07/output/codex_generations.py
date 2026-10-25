

# Generated at 2026-10-24 21:04:43.899937
# Unit test for function count_nums
def test_count_nums():
    assert module_0.count_nums([]) == 0
    assert module_0.count_nums([0]) == 0
    assert module_0.count_nums([1, 2, 3]) == 3
    assert module_0.count_nums([-1, -2, -3]) == 0
    assert module_0.count_nums([123, -123, 0]) == 2  # 6, 4, 0
    assert module_0.count_nums([-99, -12, -21]) == 1  # 0, 1, -1
    assert module_0.count_nums([-123, -99, -10, 0, 10, 99, 123]) == 4

# Generated at 2026-10-24 21:04:50.178622
# Unit test for function count_nums
def test_count_nums():
    assert module_0.count_nums([1, 2, 3]) == 3
    assert module_0.count_nums([-1, -2, -3]) == 0
    assert module_0.count_nums([-12, -21, -11]) == 2
    assert module_0.count_nums([0, 10, -10, 99, -99]) == 2
    assert module_0.count_nums([]) == 0

# Generated at 2026-10-24 21:04:56.701373
# Unit test for function count_nums
def test_count_nums():
    assert module_0.count_nums([]) == 0
    assert module_0.count_nums([1, -1, 0]) == 1
    assert module_0.count_nums([123, -123, 404, -404]) == 3
    assert module_0.count_nums([-12, -21, 10, -10]) == 2
    assert module_0.count_nums([-100, 100, 999, -999]) == 2

# Generated at 2026-10-24 21:05:04.688439
# Unit test for function count_nums
def test_count_nums():
    assert module_0.count_nums([]) == 0
    assert module_0.count_nums([0, 0]) == 0
    assert module_0.count_nums([1, 2, 3]) == 3
    assert module_0.count_nums([-1, -2, -3]) == 0
    assert module_0.count_nums([123, -123, 0, -1, 10, -19, -99]) == 4
    assert module_0.count_nums([-12, -11, -10, 10, 11, 12]) == 4

# Generated at 2026-10-24 21:05:12.570476
# Unit test for function count_nums
def test_count_nums():
    assert module_0.count_nums([]) == 0
    assert module_0.count_nums([0, 1, -1]) == 1
    assert module_0.count_nums([12, 5, 101]) == 3
    assert module_0.count_nums([-123, -21, -10, -11]) == 1
    assert module_0.count_nums([10, -123, -21, 0, 5]) == 3