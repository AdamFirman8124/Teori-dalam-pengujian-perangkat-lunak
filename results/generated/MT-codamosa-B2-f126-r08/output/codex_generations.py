

# Generated at 2026-10-24 22:31:52.825023
# Unit test for function is_sorted

# Generated at 2026-10-24 22:31:55.241697
# Unit test for function is_sorted

# Generated at 2026-10-24 22:31:57.658554
# Unit test for function is_sorted

# Generated at 2026-10-24 22:32:04.343313
# Unit test for function is_sorted
def test_is_sorted():assert module_0.is_sorted([]) is True

# Generated at 2026-10-24 22:32:10.899064
# Unit test for function is_sorted
def test_is_sorted():
    assert module_0.is_sorted([]) is True
    assert module_0.is_sorted([1]) is True
    assert module_0.is_sorted([1, 2, 3, 4]) is True
    assert module_0.is_sorted([1, 1, 2, 2, 3]) is True

    assert module_0.is_sorted([3, 2, 1]) is False
    assert module_0.is_sorted([1, 3, 2, 4]) is False
    assert module_0.is_sorted([1, 1, 1, 2]) is False  # More than two occurrences


test_is_sorted()

# Generated at 2026-10-24 22:32:15.607729
# Unit test for function is_sorted
def test_is_sorted():
    assert module_0.is_sorted([]) is True
    assert module_0.is_sorted([1]) is True
    assert module_0.is_sorted([1, 2, 3, 4]) is True
    assert module_0.is_sorted([1, 1, 2, 2, 3]) is True
    assert module_0.is_sorted([3, 2, 1]) is False
    assert module_0.is_sorted([1, 3, 2, 4]) is False
    assert module_0.is_sorted([1, 1, 1, 2]) is False  # More than two occurrences
    assert module_0.is_sorted([-3, -2, -2, 0]) is True

# Generated at 2026-10-24 22:32:20.830808
# Unit test for function is_sorted
def test_is_sorted():
    assert module_0.is_sorted([]) is True
    assert module_0.is_sorted([1]) is True
    assert module_0.is_sorted([1, 2, 3, 4]) is True
    assert module_0.is_sorted([1, 1, 2, 2, 3]) is True

    # No value may occur more than twice
    assert module_0.is_sorted([1, 1, 1, 2, 3]) is False

    # Unsorted lists
    assert module_0.is_sorted([3, 2, 1]) is False
    assert module_0.is_sorted([1, 3, 2]) is False
    assert module_0.is_sorted([2, 1, 1]) is False


test_is_sorted()
print("All tests passed.")