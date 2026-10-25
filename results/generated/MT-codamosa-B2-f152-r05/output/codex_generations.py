

# Generated at 2026-10-24 23:25:19.853025
# Unit test for function compare
def test_compare():
    assert module_0.compare([1, 2, 3], [3, 2, 1]) == [2, 0, 2]
    assert module_0.compare([5, 5, 5], [5, 5, 5]) == [0, 0, 0]
    assert module_0.compare([], []) == []

# Generated at 2026-10-24 23:25:23.844943
# Unit test for function compare
def test_compare():
    assert module_0.compare([1, 2, 3], [3, 2, 1]) == [2, 0, 2]
    assert module_0.compare([5, 10], [2, 15]) == [3, 5]
    assert module_0.compare([], []) == []

# Generated at 2026-10-24 23:25:28.306626
# Unit test for function compare
def test_compare():
    assert module_0.compare([1, 2, 3], [3, 2, 1]) == [2, 0, 2]
    assert module_0.compare([5, 5], [5, 5]) == [0, 0]
    assert module_0.compare([], []) == []

# Generated at 2026-10-24 23:25:32.654391
# Unit test for function compare
def test_compare():
    game = [1, 5, 3, 8]
    guess = [2, 2, 3, 10]

    assert module_0.compare(game, guess) == [1, 3, 0, 2]

# Generated at 2026-10-24 23:25:36.758468
# Unit test for function compare
def test_compare():
    assert module_0.compare([1, 2, 3], [3, 2, 1]) == [2, 0, 2]
    assert module_0.compare([5, 10], [2, 15]) == [3, 5]
    assert module_0.compare([], []) == []