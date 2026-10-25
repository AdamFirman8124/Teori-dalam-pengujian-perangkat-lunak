

# Generated at 2026-10-24 23:26:56.623424
# Unit test for function is_sorted
def test_is_sorted():
    assert module_0.is_sorted([]) is True
    assert module_0.is_sorted([1]) is True
    assert module_0.is_sorted([1, 2, 3]) is True
    assert module_0.is_sorted([1, 1, 2, 2, 3]) is True

    assert module_0.is_sorted([3, 2, 1]) is False
    assert module_0.is_sorted([1, 3, 2]) is False
    assert module_0.is_sorted([1, 1, 1, 2]) is False
    assert module_0.is_sorted([1, 2, 2, 2]) is False

# Generated at 2026-10-24 23:27:00.715602
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

# Generated at 2026-10-24 23:27:06.553876
# Unit test for function is_sorted
def test_is_sorted():
    assert module_0.is_sorted([]) is True
    assert module_0.is_sorted([1]) is True
    assert module_0.is_sorted([1, 2, 3]) is True
    assert module_0.is_sorted([1, 1, 2, 2, 3]) is True

    # Not sorted
    assert module_0.is_sorted([3, 2, 1]) is False
    assert module_0.is_sorted([1, 3, 2]) is False

    # A value appears more than twice
    assert module_0.is_sorted([1, 1, 1, 2]) is False
    assert module_0.is_sorted([1, 2, 2, 2, 3]) is False

# Generated at 2026-10-24 23:27:13.720510
# Unit test for function is_sorted
def test_is_sorted():
    assert module_0.is_sorted([]) is True
    assert module_0.is_sorted([1]) is True
    assert module_0.is_sorted([1, 2, 3, 4]) is True
    assert module_0.is_sorted([1, 1, 2, 2, 3]) is True

    # Not sorted
    assert module_0.is_sorted([1, 3, 2, 4]) is False
    assert module_0.is_sorted([3, 2, 1]) is False

    # A value cannot occur more than twice
    assert module_0.is_sorted([1, 1, 1, 2, 3]) is False
    assert module_0.is_sorted([1, 2, 2, 2, 3]) is False

# Generated at 2026-10-24 23:27:21.200396
# Unit test for function is_sorted
def test_is_sorted():
    assert module_0.is_sorted([]) is True
    assert module_0.is_sorted([5]) is True
    assert module_0.is_sorted([1, 2, 3, 4]) is True
    assert module_0.is_sorted([1, 1, 2, 2, 3]) is True

    assert module_0.is_sorted([3, 2, 1]) is False
    assert module_0.is_sorted([1, 3, 2, 4]) is False
    assert module_0.is_sorted([1, 1, 1, 2]) is False  # More than two occurrences