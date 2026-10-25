

# Generated at 2026-10-24 19:47:28.946968
# Unit test for function can_arrange
def test_can_arrange():
    assert module_0.can_arrange([]) == -1
    assert module_0.can_arrange([1]) == -1
    assert module_0.can_arrange([1, 2, 3, 4]) == -1
    assert module_0.can_arrange([1, 3, 2, 4]) == 2
    assert module_0.can_arrange([3, 2, 1]) == 2
    assert module_0.can_arrange([1, 4, 3, 2]) == 3

# Generated at 2026-10-24 19:47:31.367444
# Unit test for function can_arrange

# Generated at 2026-10-24 19:47:33.786696
# Unit test for function can_arrange

# Generated at 2026-10-24 19:47:36.202001
# Unit test for function can_arrange

# Generated at 2026-10-24 19:47:38.619363
# Unit test for function can_arrange

# Generated at 2026-10-24 19:47:41.034745
# Unit test for function can_arrange

# Generated at 2026-10-24 19:47:48.078289
# Unit test for function can_arrange
def test_can_arrange():
    assert module_0.can_arrange([1, 2, 4, 3, 5]) == 3
    assert module_0.can_arrange([1, 2, 3]) == -1
    assert module_0.can_arrange([]) == -1
    assert module_0.can_arrange([5]) == -1
    assert module_0.can_arrange([2, 1]) == 1
    assert module_0.can_arrange([1, 3, 2, 4, 3, 5]) == 4
    assert module_0.can_arrange([5, 4, 3, 2, 1]) == 4
    assert module_0.can_arrange([1, 2, 2, 3]) == -1
    assert module_0.can_arrange([3, 3, 2, 2]) == 3

# Generated at 2026-10-24 19:48:01.651894
# Unit test for function can_arrange
def test_can_arrange():
    assert module_0.can_arrange([]) == -1
    assert module_0.can_arrange([5]) == -1
    assert module_0.can_arrange([1, 2, 3, 4]) == -1
    assert module_0.can_arrange([1, 3, 2, 4]) == 2
    assert module_0.can_arrange([3, 1, 2, 0]) == 3
    assert module_0.can_arrange([5, 4, 3, 2]) == 3

# Generated at 2026-10-24 19:48:15.027213
# Unit test for function can_arrange
def test_can_arrange():
    # Already arranged in nondecreasing order
    assert module_0.can_arrange([1, 2, 3, 4]) == -1

    # One descending pair: 3 < 5 at index 2
    assert module_0.can_arrange([1, 5, 3, 4]) == 2

    # Multiple descending pairs; returns the last descending index
    assert module_0.can_arrange([5, 3, 4, 2, 6]) == 3

    # Empty and single-element lists
    assert module_0.can_arrange([]) == -1
    assert module_0.can_arrange([10]) == -1

    # Equal adjacent values are allowed
    assert module_0.can_arrange([1, 1, 2, 2]) == -1