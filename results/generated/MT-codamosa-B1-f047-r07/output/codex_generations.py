

# Generated at 2026-10-24 15:27:01.996233
# Unit test for function median

# Generated at 2026-10-24 15:27:04.408255
# Unit test for function median

# Generated at 2026-10-24 15:27:06.821840
# Unit test for function median

# Generated at 2026-10-24 15:27:09.238210
# Unit test for function median

# Generated at 2026-10-24 15:27:11.649990
# Unit test for function median

# Generated at 2026-10-24 15:27:14.061416
# Unit test for function median

# Generated at 2026-10-24 15:27:16.473476
# Unit test for function median

# Generated at 2026-10-24 15:27:18.886899
# Unit test for function median

# Generated at 2026-10-24 15:27:21.300448
# Unit test for function median

# Generated at 2026-10-24 15:27:23.713731
# Unit test for function median

# Generated at 2026-10-24 15:27:26.126684
# Unit test for function median

# Generated at 2026-10-24 15:27:28.539925
# Unit test for function median

# Generated at 2026-10-24 15:27:30.149074
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