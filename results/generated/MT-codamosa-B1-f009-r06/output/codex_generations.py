

# Generated at 2026-10-24 14:11:09.492225
# Unit test for function rolling_max
def test_rolling_max():
    assert module_0.rolling_max([]) == []
    assert module_0.rolling_max([1]) == [1]
    assert module_0.rolling_max([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert module_0.rolling_max([4, 3, 2, 1]) == [4, 4, 4, 4]
    assert module_0.rolling_max([1, 3, 2, 5, 4]) == [1, 3, 3, 5, 5]
    assert module_0.rolling_max([-1, -5, -3, 0, -2]) == [-1, -1, -1, 0, 0]
    assert module_0.rolling_max([2, 2, 2]) == [2, 2, 2]

# Generated at 2026-10-24 14:11:10.938832
# Unit test for function rolling_max
def test_rolling_max():
    assert module_0.rolling_max([]) == []
    assert module_0.rolling_max([1]) == [1]
    assert module_0.rolling_max([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert module_0.rolling_max([4, 3, 2, 1]) == [4, 4, 4, 4]
    assert module_0.rolling_max([1, 3, 2, 5, 4]) == [1, 3, 3, 5, 5]
    assert module_0.rolling_max([-1, -5, -3, 0, -2]) == [-1, -1, -1, 0, 0]
    assert module_0.rolling_max([2, 2, 2]) == [2, 2, 2]

# Generated at 2026-10-24 14:11:23.109248
# Unit test for function rolling_max
def test_rolling_max():
    assert module_0.rolling_max([]) == []
    assert module_0.rolling_max([3]) == [3]
    assert module_0.rolling_max([1, 3, 2, 5, 4]) == [1, 3, 3, 5, 5]
    assert module_0.rolling_max([-5, -2, -8, -1]) == [-5, -2, -2, -1]
    assert module_0.rolling_max([7, 7, 7]) == [7, 7, 7]

# Generated at 2026-10-24 14:11:31.814713
# Unit test for function rolling_max
def test_rolling_max():
    assert module_0.rolling_max([]) == []
    assert module_0.rolling_max([1]) == [1]
    assert module_0.rolling_max([1, 3, 2, 5, 4]) == [1, 3, 3, 5, 5]
    assert module_0.rolling_max([-5, -2, -10, -1]) == [-5, -2, -2, -1]
    assert module_0.rolling_max([7, 7, 7]) == [7, 7, 7]

# Generated at 2026-10-24 14:11:42.772195
# Unit test for function rolling_max
def test_rolling_max():
    assert module_0.rolling_max([]) == []
    assert module_0.rolling_max([5]) == [5]
    assert module_0.rolling_max([1, 3, 2, 5, 4]) == [1, 3, 3, 5, 5]
    assert module_0.rolling_max([5, 4, 3, 2, 1]) == [5, 5, 5, 5, 5]
    assert module_0.rolling_max([-3, -1, -4, 0]) == [-3, -1, -1, 0]


if __name__ == "__main__":
    test_rolling_max()
    print("All tests passed")