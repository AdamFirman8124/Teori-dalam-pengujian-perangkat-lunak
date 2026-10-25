

# Generated at 2026-10-24 04:09:06.591300
# Unit test for function is_sorted
def test_is_sorted():
    assert module_0.is_sorted([]) is True
    assert module_0.is_sorted([1]) is True
    assert module_0.is_sorted([1, 2, 3, 4]) is True
    assert module_0.is_sorted([1, 1, 2, 2, 3]) is True

    assert module_0.is_sorted([2, 1, 3]) is False       # Not sorted
    assert module_0.is_sorted([1, 2, 2, 2, 3]) is False  # Value occurs more than twice
    assert module_0.is_sorted([3, 2, 1]) is False

# Generated at 2026-10-24 04:09:12.333998
# Unit test for function is_sorted
def test_is_sorted():
    assert module_0.is_sorted([]) is True
    assert module_0.is_sorted([1]) is True
    assert module_0.is_sorted([1, 2, 3, 4]) is True
    assert module_0.is_sorted([1, 1, 2, 2, 3]) is True

    # Not sorted
    assert module_0.is_sorted([1, 3, 2]) is False
    assert module_0.is_sorted([3, 2, 1]) is False

    # An element occurs more than twice
    assert module_0.is_sorted([1, 1, 1, 2, 3]) is False

    # Duplicates are allowed when each occurs at most twice
    assert module_0.is_sorted([1, 1, 2, 3, 3]) is True

# Generated at 2026-10-24 04:09:18.558172
# Unit test for function is_sorted
def test_is_sorted():
    assert module_0.is_sorted([]) is True
    assert module_0.is_sorted([1]) is True
    assert module_0.is_sorted([1, 2, 3]) is True
    assert module_0.is_sorted([1, 1, 2, 2, 3]) is True
    assert module_0.is_sorted([-3, -2, -2, 0]) is True

    assert module_0.is_sorted([1, 3, 2]) is False
    assert module_0.is_sorted([3, 2, 1]) is False
    assert module_0.is_sorted([1, 1, 1, 2]) is False
    assert module_0.is_sorted([1, 2, 2, 2]) is False

# Generated at 2026-10-24 04:09:20.975893
# Unit test for function is_sorted

# Generated at 2026-10-24 04:09:23.399146
# Unit test for function is_sorted

# Generated at 2026-10-24 04:09:25.820006
# Unit test for function is_sorted

# Generated at 2026-10-24 04:09:28.330180
# Unit test for function is_sorted

# Generated at 2026-10-24 04:09:30.747151
# Unit test for function is_sorted

# Generated at 2026-10-24 04:09:33.161224
# Unit test for function is_sorted