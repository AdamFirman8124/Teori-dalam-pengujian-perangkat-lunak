

# Generated at 2026-10-25 11:17:42.340207
# Unit test for function can_arrange
def test_can_arrange():
    assert module_0.can_arrange([1, 2, 4, 3, 5]) == 3
    assert module_0.can_arrange([1, 2, 3, 4, 5]) == -1
    assert module_0.can_arrange([5, 4, 3, 2, 1]) == 4
    assert module_0.can_arrange([10]) == -1
    assert module_0.can_arrange([]) == -1
    assert module_0.can_arrange([1, 3, 2, 5, 4]) == 4


test_can_arrange()
print("All tests passed.")

# Generated at 2026-10-25 11:17:48.119449
# Unit test for function can_arrange
def test_can_arrange():
    assert module_0.can_arrange([1, 2, 4, 3, 5]) == 3
    assert module_0.can_arrange([1, 2, 3, 4]) == -1
    assert module_0.can_arrange([4, 3, 2, 1]) == 3
    assert module_0.can_arrange([1, 3, 2, 5, 4]) == 4
    assert module_0.can_arrange([1, 1, 2, 2]) == -1
    assert module_0.can_arrange([]) == -1
    assert module_0.can_arrange([5]) == -1

# Generated at 2026-10-25 11:17:54.966651
# Unit test for function can_arrange
def test_can_arrange():
    assert module_0.can_arrange([1, 2, 4, 3, 5]) == 3
    assert module_0.can_arrange([3, 2, 4, 1, 5]) == 3  # Last decreasing index
    assert module_0.can_arrange([1, 2, 3, 4]) == -1
    assert module_0.can_arrange([1, 1, 2, 2]) == -1
    assert module_0.can_arrange([2, 1]) == 1
    assert module_0.can_arrange([1]) == -1
    assert module_0.can_arrange([]) == -1

# Generated at 2026-10-25 11:18:00.686279
# Unit test for function can_arrange
def test_can_arrange():
    assert module_0.can_arrange([1, 2, 4, 3, 5]) == 3
    assert module_0.can_arrange([1, 2, 3, 2, 1]) == 4  # Last decreasing index
    assert module_0.can_arrange([1, 2, 3, 4]) == -1    # Already ordered
    assert module_0.can_arrange([4, 3, 2, 1]) == 3
    assert module_0.can_arrange([1, 1, 1]) == -1       # Equal values do not count
    assert module_0.can_arrange([]) == -1
    assert module_0.can_arrange([5]) == -1

# Generated at 2026-10-25 11:18:06.398795
# Unit test for function can_arrange
def test_can_arrange():
    assert module_0.can_arrange([1, 2, 4, 3, 5]) == 3
    assert module_0.can_arrange([5, 3, 4, 2, 1]) == 4  # Last decreasing index
    assert module_0.can_arrange([1, 2, 3, 4]) == -1
    assert module_0.can_arrange([4, 3, 2, 1]) == 3
    assert module_0.can_arrange([]) == -1
    assert module_0.can_arrange([1]) == -1


test_can_arrange()
print("All tests passed.")