

# Generated at 2026-10-24 07:58:59.710787
# Unit test for function compare
def test_compare():
    assert module_0.compare([1, 2, 3], [3, 2, 1]) == [2, 0, 2]
    assert module_0.compare([5, 10], [2, 15]) == [3, 5]
    assert module_0.compare([], []) == []
    assert module_0.compare([1, -2], [-1, 3]) == [2, 5]

# Generated at 2026-10-24 07:59:04.752719
# Unit test for function compare
def test_compare():
    assert module_0.compare([1, 2, 3], [1, 4, 0]) == [0, 2, 3]
    assert module_0.compare([-1, 5], [2, -3]) == [3, 8]
    assert module_0.compare([], []) == []

# Generated at 2026-10-24 07:59:08.835482
# Unit test for function compare
def test_compare():
    assert module_0.compare([1, 2, 3], [1, 4, 6]) == [0, 2, 3]
    assert module_0.compare([5, 5], [2, 8]) == [3, 3]
    assert module_0.compare([], []) == []

# Generated at 2026-10-24 07:59:14.775634
# Unit test for function compare
def test_compare():
    assert module_0.compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]
    assert module_0.compare([1, 5, 10], [4, 3, 15]) == [3, 2, 5]
    assert module_0.compare([-2, 0, 4], [3, -5, 1]) == [5, 5, 3]
    assert module_0.compare([], []) == []

# Generated at 2026-10-24 07:59:19.687202
# Unit test for function compare
def test_compare():
    assert module_0.compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]
    assert module_0.compare([1, 5, 10], [4, 2, 6]) == [3, 3, 4]
    assert module_0.compare([], []) == []