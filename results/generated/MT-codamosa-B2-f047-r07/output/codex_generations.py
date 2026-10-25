

# Generated at 2026-10-24 13:33:50.913102
# Unit test for function median

# Generated at 2026-10-24 13:33:53.329825
# Unit test for function median

# Generated at 2026-10-24 13:33:55.746608
# Unit test for function median

# Generated at 2026-10-24 13:33:58.167526
# Unit test for function median

# Generated at 2026-10-24 13:34:08.178683
# Unit test for function median
def test_median():assert module_0.median([3, 1, 2]) == 2

# Generated at 2026-10-24 13:34:09.839502
# Unit test for function median
def test_median():
    # Odd-length lists
    assert module_0.median([1, 2, 3]) == 2
    assert module_0.median([3, 1, 2]) == 2          # unsorted input
    assert module_0.median([5]) == 5                # single element
    assert module_0.median([1, 3, 2, 5, 4]) == 3

    # Even-length lists
    assert module_0.median([1, 2, 3, 4]) == 2.5
    assert module_0.median([4, 1, 3, 2]) == 2.5
    assert module_0.median([1, 2]) == 1.5

    # Duplicates
    assert module_0.median([2, 2, 2, 2]) == 2.0
    assert module_0.median([1, 2, 2, 3]) == 2.0

    # Negative numbers and floats
    assert module_0.median([-5, -1, -3]) == -3
    assert module_0.median([1.5, 2.5, 3.5]) == 2.5
    assert module_0.median([1, 2.5, 4]) == 2.5

    # Input list must not be modified
    data = [3, 1, 2]
    module_0.median(data)
    assert data == [3, 1, 2]

    # Empty list should raise
    try:
        module_0.median([])
        assert False, "expected IndexError"
    except IndexError:
        pass

    print("All median tests passed.")

# Generated at 2026-10-24 13:34:11.241040
# Unit test for function median
def test_median():
    # Odd-length lists
    assert module_0.median([1, 2, 3]) == 2
    assert module_0.median([3, 1, 2]) == 2          # unsorted input
    assert module_0.median([5]) == 5                # single element
    assert module_0.median([1, 3, 2, 5, 4]) == 3

    # Even-length lists
    assert module_0.median([1, 2, 3, 4]) == 2.5
    assert module_0.median([4, 1, 3, 2]) == 2.5
    assert module_0.median([1, 2]) == 1.5

    # Duplicates
    assert module_0.median([2, 2, 2, 2]) == 2.0
    assert module_0.median([1, 2, 2, 3]) == 2.0

    # Negative numbers and floats
    assert module_0.median([-5, -1, -3]) == -3
    assert module_0.median([1.5, 2.5, 3.5]) == 2.5
    assert module_0.median([1, 2.5, 4]) == 2.5

    # Input list must not be modified
    data = [3, 1, 2]
    module_0.median(data)
    assert data == [3, 1, 2]

    # Empty list should raise
    try:
        module_0.median([])
        assert False, "expected IndexError"
    except IndexError:
        pass

    print("All median tests passed.")

# Generated at 2026-10-24 13:34:12.732217
# Unit test for function median
def test_median():
    # Odd-length lists
    assert module_0.median([1, 2, 3]) == 2
    assert module_0.median([3, 1, 2]) == 2          # unsorted input
    assert module_0.median([5]) == 5                # single element
    assert module_0.median([1, 3, 2, 5, 4]) == 3

    # Even-length lists
    assert module_0.median([1, 2, 3, 4]) == 2.5
    assert module_0.median([4, 1, 3, 2]) == 2.5
    assert module_0.median([1, 2]) == 1.5

    # Duplicates
    assert module_0.median([2, 2, 2, 2]) == 2.0
    assert module_0.median([1, 2, 2, 3]) == 2.0

    # Negative numbers and floats
    assert module_0.median([-5, -1, -3]) == -3
    assert module_0.median([1.5, 2.5, 3.5]) == 2.5
    assert module_0.median([1, 2.5, 4]) == 2.5

    # Input list must not be modified
    data = [3, 1, 2]
    module_0.median(data)
    assert data == [3, 1, 2]

    # Empty list should raise
    try:
        module_0.median([])
        assert False, "expected IndexError"
    except IndexError:
        pass

    print("All median tests passed.")