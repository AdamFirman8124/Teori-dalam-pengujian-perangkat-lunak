

# Generated at 2026-10-24 22:08:36.444598
# Unit test for function is_sorted
def test_is_sorted():
    assert module_0.is_sorted([]) is True
    assert module_0.is_sorted([1]) is True
    assert module_0.is_sorted([1, 2, 3, 4]) is True
    assert module_0.is_sorted([1, 1, 2, 2, 3]) is True

    assert module_0.is_sorted([2, 1, 3]) is False
    assert module_0.is_sorted([1, 2, 2, 2, 3]) is False
    assert module_0.is_sorted([3, 2, 1]) is False

# Generated at 2026-10-24 22:08:42.380109
# Unit test for function is_sorted
def test_is_sorted():
    assert module_0.is_sorted([]) is True
    assert module_0.is_sorted([1]) is True
    assert module_0.is_sorted([1, 2, 3]) is True
    assert module_0.is_sorted([1, 1, 2, 2, 3]) is True

    assert module_0.is_sorted([3, 2, 1]) is False
    assert module_0.is_sorted([1, 3, 2]) is False
    assert module_0.is_sorted([1, 1, 1, 2]) is False  # More than two occurrences
    assert module_0.is_sorted([2, 1, 1, 1]) is False  # Unsorted and too many occurrences

# Generated at 2026-10-24 22:08:44.913389
# Unit test for function is_sorted

# Generated at 2026-10-24 22:08:47.335053
# Unit test for function is_sorted

# Generated at 2026-10-24 22:08:49.755751
# Unit test for function is_sorted

# Generated at 2026-10-24 22:08:56.752739
# Unit test for function is_sorted
def test_is_sorted():assert module_0.is_sorted([]) is True

# Generated at 2026-10-24 22:09:03.210855
# Unit test for function is_sorted
def test_is_sorted():
    assert module_0.is_sorted([]) is True
    assert module_0.is_sorted([1]) is True
    assert module_0.is_sorted([1, 2, 3, 4]) is True
    assert module_0.is_sorted([1, 1, 2, 2, 3]) is True

    assert module_0.is_sorted([1, 3, 2, 4]) is False
    assert module_0.is_sorted([3, 2, 1]) is False
    assert module_0.is_sorted([1, 1, 1, 2]) is False
    assert module_0.is_sorted([1, 2, 2, 2, 3]) is False