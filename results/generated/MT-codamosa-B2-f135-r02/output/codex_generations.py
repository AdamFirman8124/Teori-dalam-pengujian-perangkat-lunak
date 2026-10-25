

# Generated at 2026-10-24 12:54:35.259614
# Unit test for function can_arrange

# Generated at 2026-10-24 12:54:37.955613
# Unit test for function can_arrange

# Generated at 2026-10-24 12:54:40.482013
# Unit test for function can_arrange

# Generated at 2026-10-24 12:54:42.893127
# Unit test for function can_arrange

# Generated at 2026-10-24 12:54:45.474762
# Unit test for function can_arrange

# Generated at 2026-10-24 12:54:47.891659
# Unit test for function can_arrange

# Generated at 2026-10-24 12:54:50.306530
# Unit test for function can_arrange

# Generated at 2026-10-24 12:54:52.721672
# Unit test for function can_arrange

# Generated at 2026-10-24 12:54:55.138108
# Unit test for function can_arrange

# Generated at 2026-10-24 12:55:06.087353
# Unit test for function can_arrange
def test_can_arrange():
    # no descent -> -1
    assert module_0.can_arrange([]) == -1
    assert module_0.can_arrange([1]) == -1
    assert module_0.can_arrange([1, 2, 3, 4]) == -1
    assert module_0.can_arrange([1, 1, 1]) == -1

    # single descent
    assert module_0.can_arrange([1, 2, 4, 3]) == 3
    assert module_0.can_arrange([2, 1]) == 1
    assert module_0.can_arrange([1, 3, 2]) == 2

    # returns last descent
    assert module_0.can_arrange([3, 2, 1]) == 2
    assert module_0.can_arrange([1, 2, 1, 2, 1]) == 4
    assert module_0.can_arrange([5, 4, 3, 4, 3]) == 4

# Generated at 2026-10-24 12:55:07.551267
# Unit test for function can_arrange
def test_can_arrange():
    # no descent -> -1
    assert module_0.can_arrange([]) == -1
    assert module_0.can_arrange([1]) == -1
    assert module_0.can_arrange([1, 2, 3, 4]) == -1
    assert module_0.can_arrange([1, 1, 1]) == -1

    # single descent
    assert module_0.can_arrange([1, 2, 4, 3]) == 3
    assert module_0.can_arrange([2, 1]) == 1
    assert module_0.can_arrange([1, 3, 2]) == 2

    # returns last descent
    assert module_0.can_arrange([3, 2, 1]) == 2
    assert module_0.can_arrange([1, 2, 1, 2, 1]) == 4
    assert module_0.can_arrange([5, 4, 3, 4, 3]) == 4