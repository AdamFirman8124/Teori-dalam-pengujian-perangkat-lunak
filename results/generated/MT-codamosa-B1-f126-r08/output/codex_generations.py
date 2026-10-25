

# Generated at 2026-10-24 06:27:22.421384
# Unit test for function is_sorted
def test_is_sorted():
    assert module_0.is_sorted([]) is True
    assert module_0.is_sorted([1]) is True
    assert module_0.is_sorted([1, 2, 3]) is True
    assert module_0.is_sorted([1, 1, 2, 2, 3]) is True

    assert module_0.is_sorted([3, 2, 1]) is False       # Not sorted
    assert module_0.is_sorted([1, 3, 2]) is False       # Not sorted
    assert module_0.is_sorted([1, 1, 1, 2]) is False    # A value occurs over twice

# Generated at 2026-10-24 06:27:29.545708
# Unit test for function is_sorted
def test_is_sorted():
    assert module_0.is_sorted([]) is True
    assert module_0.is_sorted([1]) is True
    assert module_0.is_sorted([1, 2, 3, 4]) is True
    assert module_0.is_sorted([-3, -1, 0, 2]) is True
    assert module_0.is_sorted([1, 1, 2, 2, 3]) is True

    assert module_0.is_sorted([2, 1]) is False
    assert module_0.is_sorted([1, 3, 2, 4]) is False
    assert module_0.is_sorted([1, 1, 1, 2]) is False
    assert module_0.is_sorted([3, 3, 3]) is False

# Generated at 2026-10-24 06:27:39.133923
# Unit test for function is_sorted
def test_is_sorted():
    assert module_0.is_sorted([]) is True
    assert module_0.is_sorted([1]) is True
    assert module_0.is_sorted([1, 2, 3, 4]) is True
    assert module_0.is_sorted([-3, -1, 0, 2]) is True
    assert module_0.is_sorted([1, 1, 2, 2, 3]) is True

    assert module_0.is_sorted([2, 1]) is False
    assert module_0.is_sorted([1, 3, 2, 4]) is False
    assert module_0.is_sorted([1, 1, 1, 2]) is False
    assert module_0.is_sorted([1, 2, 2, 2]) is False

# Generated at 2026-10-24 06:27:47.018446
# Unit test for function is_sorted
def test_is_sorted():
    assert module_0.is_sorted([]) is True
    assert module_0.is_sorted([1]) is True
    assert module_0.is_sorted([1, 2, 3, 4]) is True
    assert module_0.is_sorted([1, 1, 2, 2, 3]) is True

    assert module_0.is_sorted([1, 3, 2, 4]) is False
    assert module_0.is_sorted([4, 3, 2, 1]) is False
    assert module_0.is_sorted([1, 1, 1, 2]) is False  # A value occurs over twice
    assert module_0.is_sorted([1, 2, 2, 2]) is False

# Generated at 2026-10-24 06:27:49.440210
# Unit test for function is_sorted

# Generated at 2026-10-24 06:27:51.858189
# Unit test for function is_sorted

# Generated at 2026-10-24 06:27:54.271028
# Unit test for function is_sorted