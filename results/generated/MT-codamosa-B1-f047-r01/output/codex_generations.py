

# Generated at 2026-10-24 11:26:45.633506
# Unit test for function median

# Generated at 2026-10-24 11:26:48.062414
# Unit test for function median

# Generated at 2026-10-24 11:27:00.205230
# Unit test for function median
def test_median():assert module_0.median([3, 1, 2]) == 2

# Generated at 2026-10-24 11:27:05.390461
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

# Generated at 2026-10-24 11:27:06.718048
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

# Generated at 2026-10-24 11:27:08.042275
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

# Generated at 2026-10-24 11:27:09.363186
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