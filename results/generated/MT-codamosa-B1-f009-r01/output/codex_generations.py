

# Generated at 2026-10-25 12:19:30.171706
# Unit test for function rolling_max
def test_rolling_max():
    assert module_0.rolling_max([]) == []
    assert module_0.rolling_max([1]) == [1]
    assert module_0.rolling_max([3, 1, 5, 2, 4]) == [3, 3, 5, 5, 5]
    assert module_0.rolling_max([-5, -2, -8, -1]) == [-5, -2, -2, -1]
    assert module_0.rolling_max([2, 2, 2]) == [2, 2, 2]

# Generated at 2026-10-25 12:19:55.661444
# Unit test for function rolling_max
def test_rolling_max():
    assert module_0.rolling_max([1, 3, 2, 5, 4]) == [1, 3, 3, 5, 5]
    assert module_0.rolling_max([-4, -2, -7, 0]) == [-4, -2, -2, 0]
    assert module_0.rolling_max([]) == []
    assert module_0.rolling_max([10]) == [10]

# Generated at 2026-10-25 12:20:43.356439
# Unit test for function rolling_max

# Generated at 2026-10-25 12:20:52.245582
# Unit test for function rolling_max
def test_rolling_max():assert module_0.rolling_max([]) == []

# Generated at 2026-10-25 12:21:11.025786
# Unit test for function rolling_max
def test_rolling_max():
    assert module_0.rolling_max([1, 3, 2, 5, 4]) == [1, 3, 3, 5, 5]
    assert module_0.rolling_max([-3, -1, -5, 0]) == [-3, -1, -1, 0]
    assert module_0.rolling_max([]) == []
    assert module_0.rolling_max([7]) == [7]

# Generated at 2026-10-25 12:21:17.478889
# Unit test for function rolling_max
def test_rolling_max():
    numbers = [3, 1, 4, 2, 5]
    expected = [3, 3, 4, 4, 5]

    assert module_0.rolling_max(numbers) == expected


def test_rolling_max_empty_list():
    assert module_0.rolling_max([]) == []