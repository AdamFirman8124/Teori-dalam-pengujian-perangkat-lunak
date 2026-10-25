

# Generated at 2026-10-25 02:46:10.185868
# Unit test for function add
def test_add():
    # even values at odd indices are summed
    assert module_0.add([1, 2, 3, 4]) == 6            # 2 + 4
    assert module_0.add([1, 2]) == 2                   # index 1 -> 2
    assert module_0.add([1, 2, 3, 4, 5, 6]) == 12      # 2 + 4 + 6

    # odd values at odd indices are skipped
    assert module_0.add([1, 3, 5, 7]) == 0
    assert module_0.add([0, 1, 0, 3]) == 0

    # index 0 is never counted, even if the value is even
    assert module_0.add([100, 1]) == 0
    assert module_0.add([2, 4, 6, 8]) == 12            # 4 + 8 (2 and 6 at even indices)

    # empty / single-element
    assert module_0.add([]) == 0
    assert module_0.add([5]) == 0
    assert module_0.add([2]) == 0

    # zeros at odd indices still sum to 0
    assert module_0.add([0, 0, 0, 0]) == 0

# Generated at 2026-10-25 02:46:11.517002
# Unit test for function add
def test_add():
    # even values at odd indices are summed
    assert module_0.add([1, 2, 3, 4]) == 6            # 2 + 4
    assert module_0.add([1, 2]) == 2                   # index 1 -> 2
    assert module_0.add([1, 2, 3, 4, 5, 6]) == 12      # 2 + 4 + 6

    # odd values at odd indices are skipped
    assert module_0.add([1, 3, 5, 7]) == 0
    assert module_0.add([0, 1, 0, 3]) == 0

    # index 0 is never counted, even if the value is even
    assert module_0.add([100, 1]) == 0
    assert module_0.add([2, 4, 6, 8]) == 12            # 4 + 8 (2 and 6 at even indices)

    # empty / single-element
    assert module_0.add([]) == 0
    assert module_0.add([5]) == 0
    assert module_0.add([2]) == 0

    # zeros at odd indices still sum to 0
    assert module_0.add([0, 0, 0, 0]) == 0

# Generated at 2026-10-25 02:46:12.841940
# Unit test for function add
def test_add():
    # even values at odd indices are summed
    assert module_0.add([1, 2, 3, 4]) == 6            # 2 + 4
    assert module_0.add([1, 2]) == 2                   # index 1 -> 2
    assert module_0.add([1, 2, 3, 4, 5, 6]) == 12      # 2 + 4 + 6

    # odd values at odd indices are skipped
    assert module_0.add([1, 3, 5, 7]) == 0
    assert module_0.add([0, 1, 0, 3]) == 0

    # index 0 is never counted, even if the value is even
    assert module_0.add([100, 1]) == 0
    assert module_0.add([2, 4, 6, 8]) == 12            # 4 + 8 (2 and 6 at even indices)

    # empty / single-element
    assert module_0.add([]) == 0
    assert module_0.add([5]) == 0
    assert module_0.add([2]) == 0

    # zeros at odd indices still sum to 0
    assert module_0.add([0, 0, 0, 0]) == 0

# Generated at 2026-10-25 02:46:14.183738
# Unit test for function add
def test_add():
    # even values at odd indices are summed
    assert module_0.add([1, 2, 3, 4]) == 6            # 2 + 4
    assert module_0.add([1, 2]) == 2                   # index 1 -> 2
    assert module_0.add([1, 2, 3, 4, 5, 6]) == 12      # 2 + 4 + 6

    # odd values at odd indices are skipped
    assert module_0.add([1, 3, 5, 7]) == 0
    assert module_0.add([0, 1, 0, 3]) == 0

    # index 0 is never counted, even if the value is even
    assert module_0.add([100, 1]) == 0
    assert module_0.add([2, 4, 6, 8]) == 12            # 4 + 8 (2 and 6 at even indices)

    # empty / single-element
    assert module_0.add([]) == 0
    assert module_0.add([5]) == 0
    assert module_0.add([2]) == 0

    # zeros at odd indices still sum to 0
    assert module_0.add([0, 0, 0, 0]) == 0

# Generated at 2026-10-25 02:46:15.507065
# Unit test for function add
def test_add():
    # even values at odd indices are summed
    assert module_0.add([1, 2, 3, 4]) == 6            # 2 + 4
    assert module_0.add([1, 2]) == 2                   # index 1 -> 2
    assert module_0.add([1, 2, 3, 4, 5, 6]) == 12      # 2 + 4 + 6

    # odd values at odd indices are skipped
    assert module_0.add([1, 3, 5, 7]) == 0
    assert module_0.add([0, 1, 0, 3]) == 0

    # index 0 is never counted, even if the value is even
    assert module_0.add([100, 1]) == 0
    assert module_0.add([2, 4, 6, 8]) == 12            # 4 + 8 (2 and 6 at even indices)

    # empty / single-element
    assert module_0.add([]) == 0
    assert module_0.add([5]) == 0
    assert module_0.add([2]) == 0

    # zeros at odd indices still sum to 0
    assert module_0.add([0, 0, 0, 0]) == 0