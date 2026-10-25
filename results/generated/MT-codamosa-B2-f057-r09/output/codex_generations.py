

# Generated at 2026-10-24 06:24:53.211309
# Unit test for function monotonic
def test_monotonic():
    assert module_0.monotonic([]) is True
    assert module_0.monotonic([1]) is True
    assert module_0.monotonic([1, 2, 3, 4]) is True
    assert module_0.monotonic([4, 3, 2, 1]) is True
    assert module_0.monotonic([1, 2, 2, 3]) is True
    assert module_0.monotonic([3, 2, 2, 1]) is True

    assert module_0.monotonic([1, 3, 2]) is False
    assert module_0.monotonic([3, 1, 2]) is False
    assert module_0.monotonic([2, 1, 3, 2]) is False

# Generated at 2026-10-24 06:25:09.627887
# Unit test for function monotonic
def test_monotonic():
    # Increasing sequence
    assert module_0.monotonic([1, 2, 3, 4]) is True

    # Decreasing sequence
    assert module_0.monotonic([4, 3, 2, 1]) is True

    # Sequence with equal adjacent values
    assert module_0.monotonic([1, 2, 2, 3]) is True
    assert module_0.monotonic([3, 2, 2, 1]) is True

    # Non-monotonic sequence
    assert module_0.monotonic([1, 3, 2, 4]) is False

    # Empty and single-element lists
    assert module_0.monotonic([]) is True
    assert module_0.monotonic([5]) is True

# Generated at 2026-10-24 06:25:12.044019
# Unit test for function monotonic

# Generated at 2026-10-24 06:25:14.628639
# Unit test for function monotonic

# Generated at 2026-10-24 06:25:17.041872
# Unit test for function monotonic

# Generated at 2026-10-24 06:25:19.458658
# Unit test for function monotonic

# Generated at 2026-10-24 06:25:21.873947
# Unit test for function monotonic

# Generated at 2026-10-24 06:25:24.290132
# Unit test for function monotonic

# Generated at 2026-10-24 06:25:26.706739
# Unit test for function monotonic

# Generated at 2026-10-24 06:25:29.120992
# Unit test for function monotonic

# Generated at 2026-10-24 06:25:34.220802
# Unit test for function monotonic
def test_monotonic():assert module_0.monotonic([]) is True