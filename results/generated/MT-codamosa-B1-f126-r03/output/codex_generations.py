

# Generated at 2026-10-25 02:54:02.712700
# Unit test for function is_sorted
def test_is_sorted():
    assert module_0.is_sorted([]) is True
    assert module_0.is_sorted([1]) is True
    assert module_0.is_sorted([1, 2, 3, 4]) is True
    assert module_0.is_sorted([1, 1, 2, 2, 3]) is True
    assert module_0.is_sorted([-3, -1, 0, 2]) is True

    assert module_0.is_sorted([3, 2, 1]) is False
    assert module_0.is_sorted([1, 3, 2, 4]) is False
    assert module_0.is_sorted([1, 1, 1, 2]) is False
    assert module_0.is_sorted([1, 2, 2, 2]) is False

# Generated at 2026-10-25 02:54:07.627806
# Unit test for function is_sorted
def test_is_sorted():
    assert module_0.is_sorted([]) is True
    assert module_0.is_sorted([1]) is True
    assert module_0.is_sorted([1, 2, 3, 4]) is True
    assert module_0.is_sorted([1, 1, 2, 2, 3]) is True

    assert module_0.is_sorted([3, 2, 1]) is False
    assert module_0.is_sorted([1, 3, 2, 4]) is False
    assert module_0.is_sorted([1, 1, 1, 2]) is False
    assert module_0.is_sorted([1, 2, 2, 2]) is False

# Generated at 2026-10-25 02:54:12.041302
# Unit test for function is_sorted
def test_is_sorted():
    assert module_0.is_sorted([]) is True
    assert module_0.is_sorted([1]) is True
    assert module_0.is_sorted([1, 2, 3, 4]) is True
    assert module_0.is_sorted([1, 1, 2, 2, 3]) is True

    assert module_0.is_sorted([3, 2, 1]) is False
    assert module_0.is_sorted([1, 3, 2]) is False
    assert module_0.is_sorted([1, 1, 1, 2]) is False
    assert module_0.is_sorted([1, 2, 2, 2]) is False

    print("All tests passed!")


test_is_sorted()

# Generated at 2026-10-25 02:54:16.878353
# Unit test for function is_sorted
def test_is_sorted():
    assert module_0.is_sorted([]) is True
    assert module_0.is_sorted([1]) is True
    assert module_0.is_sorted([1, 2, 3, 4]) is True
    assert module_0.is_sorted([1, 1, 2, 2, 3]) is True

    assert module_0.is_sorted([2, 1, 3]) is False       # Not sorted
    assert module_0.is_sorted([1, 2, 2, 2, 3]) is False  # Value occurs over twice
    assert module_0.is_sorted([3, 2, 1]) is False

    print("All tests passed.")


test_is_sorted()

# Generated at 2026-10-25 02:54:23.089451
# Unit test for function is_sorted
def test_is_sorted():
    assert module_0.is_sorted([]) is True
    assert module_0.is_sorted([1]) is True
    assert module_0.is_sorted([1, 2, 3, 4]) is True
    assert module_0.is_sorted([1, 1, 2, 2, 3]) is True

    assert module_0.is_sorted([3, 2, 1]) is False
    assert module_0.is_sorted([1, 3, 2, 4]) is False
    assert module_0.is_sorted([1, 1, 1, 2]) is False  # More than two occurrences

    print("All tests passed.")


test_is_sorted()