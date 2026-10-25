

# Generated at 2026-10-24 15:43:04.314455
# Unit test for function compare
def test_compare():
    assert module_0.compare([1, 2, 3, 4], [1, 2, 3, 4]) == [0, 0, 0, 0]
    assert module_0.compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]
    assert module_0.compare([0, 0], [10, -10]) == [10, 10]
    assert module_0.compare([-5, 0, 5], [-2, 0, 2]) == [3, 0, 3]
    assert module_0.compare([], []) == []
    assert module_0.compare([1, 2, 3], [1]) == [0]
    assert module_0.compare([1.5, -2.5], [1.0, 2.5]) == [0.5, 5.0]

# Generated at 2026-10-24 15:43:40.726560
# Unit test for function compare
def test_compare():
    assert module_0.compare([1, 2, 3], [1, 4, 2]) == [0, 2, 1]
    assert module_0.compare([-1, 5], [2, 3]) == [3, 2]
    assert module_0.compare([], []) == []

# Generated at 2026-10-24 15:44:12.359969
# Unit test for function compare
def test_compare():
    assert module_0.compare([1, 2, 3], [3, 1, 5]) == [2, 1, 2]

# Generated at 2026-10-24 15:45:11.146642
# Unit test for function compare
def test_compare():
    assert module_0.compare([1, 2, 3], [4, 0, 5]) == [3, 2, 2]
    assert module_0.compare([10, 5], [7, 8]) == [3, 3]
    assert module_0.compare([], []) == []

# Generated at 2026-10-24 15:45:43.505047
# Unit test for function compare
def test_compare():
    # identical -> all zeros
    assert module_0.compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

    # general case
    assert module_0.compare([10, 20, 30], [8, 25, 30]) == [2, 5, 0]

    # order doesn't matter due to abs
    assert module_0.compare([3], [5]) == [2]
    assert module_0.compare([5], [3]) == [2]

    # negatives
    assert module_0.compare([-1, -5], [2, 3]) == [3, 8]

    # floats
    assert module_0.compare([1.5, 2.0], [1.0, 2.5]) == [0.5, 0.5]

    # empty
    assert module_0.compare([], []) == []
    assert module_0.compare([], [1, 2]) == []

    # different lengths -> zip truncates to shortest
    assert module_0.compare([1, 2, 3], [1, 2]) == [0, 0]