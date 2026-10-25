

# Generated at 2026-10-24 04:33:28.632894
# Unit test for function compare
def test_compare():
    assert module_0.compare([1, 2, 3], [4, 0, 3]) == [3, 2, 0]
    assert module_0.compare([-1, 5], [2, -3]) == [3, 8]
    assert module_0.compare([], []) == []

# Generated at 2026-10-24 04:33:32.454088
# Unit test for function compare
def test_compare():
    assert module_0.compare([1, 2, 3], [3, 2, 1]) == [2, 0, 2]
    assert module_0.compare([5, 10], [2, 15]) == [3, 5]
    assert module_0.compare([], []) == []
    assert module_0.compare([1, -2], [-1, 2]) == [2, 4]

# Generated at 2026-10-24 04:33:37.541092
# Unit test for function compare
def test_compare():
    assert module_0.compare([1, 2, 3], [3, 2, 1]) == [2, 0, 2]
    assert module_0.compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]
    assert module_0.compare([-1, -5], [2, -2]) == [3, 3]
    assert module_0.compare([], []) == []

# Generated at 2026-10-24 04:33:42.968472
# Unit test for function compare
def test_compare():
    assert module_0.compare([1, 2, 3], [3, 2, 1]) == [2, 0, 2]
    assert module_0.compare([5, 10, 15], [5, 10, 15]) == [0, 0, 0]
    assert module_0.compare([], []) == []

# Generated at 2026-10-24 04:33:47.587429
# Unit test for function compare
def test_compare():
    assert module_0.compare([1, 5, 3], [2, 2, 3]) == [1, 3, 0]
    assert module_0.compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]
    assert module_0.compare([], []) == []