

# Generated at 2026-10-25 00:37:43.981366
# Unit test for function can_arrange
def test_can_arrange():
    assert module_0.can_arrange([1, 2, 4, 3, 5]) == 3
    assert module_0.can_arrange([2, 1, 3, 0]) == 3
    assert module_0.can_arrange([1, 2, 3, 4]) == -1
    assert module_0.can_arrange([1]) == -1
    assert module_0.can_arrange([]) == -1
    assert module_0.can_arrange([3, 3, 3]) == -1

# Generated at 2026-10-25 00:37:56.173732
# Unit test for function can_arrange
def test_can_arrange():
    assert module_0.can_arrange([]) == -1
    assert module_0.can_arrange([5]) == -1
    assert module_0.can_arrange([1, 2, 3, 4]) == -1
    assert module_0.can_arrange([1, 3, 2, 4]) == 2
    assert module_0.can_arrange([5, 4, 3, 2]) == 3
    assert module_0.can_arrange([3, 1, 4, 2, 5]) == 3
    assert module_0.can_arrange([1, 1, 2, 2]) == -1


test_can_arrange()
print("All tests passed.")

# Generated at 2026-10-25 00:38:01.600804
# Unit test for function can_arrange
def test_can_arrange():
    assert module_0.can_arrange([1, 2, 4, 3, 5]) == 3
    assert module_0.can_arrange([1, 2, 3, 4]) == -1
    assert module_0.can_arrange([4, 3, 2, 1]) == 3
    assert module_0.can_arrange([5]) == -1
    assert module_0.can_arrange([]) == -1
    assert module_0.can_arrange([3, 1, 4, 2]) == 3


test_can_arrange()
print("All tests passed.")

# Generated at 2026-10-25 00:38:06.650734
# Unit test for function can_arrange
def test_can_arrange():
    assert module_0.can_arrange([1, 2, 4, 3, 5]) == 3
    assert module_0.can_arrange([1, 3, 2, 5, 4]) == 4  # Last decreasing index
    assert module_0.can_arrange([1, 2, 3, 4]) == -1    # Already non-decreasing
    assert module_0.can_arrange([4, 3, 2, 1]) == 3
    assert module_0.can_arrange([]) == -1
    assert module_0.can_arrange([1]) == -1
    assert module_0.can_arrange([1, 1, 2, 2]) == -1

# Generated at 2026-10-25 00:38:10.971115
# Unit test for function can_arrange
def test_can_arrange():
    assert module_0.can_arrange([1, 2, 4, 3, 5]) == 3
    assert module_0.can_arrange([1, 3, 2, 5, 4]) == 4  # Returns the last matching index
    assert module_0.can_arrange([1, 2, 3, 4]) == -1
    assert module_0.can_arrange([]) == -1
    assert module_0.can_arrange([5]) == -1
    assert module_0.can_arrange([3, 2, 1]) == 2