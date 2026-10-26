

# Generated at 2026-10-25 11:34:06.287721
# Unit test for function median

# Generated at 2026-10-25 11:34:08.701275
# Unit test for function median

# Generated at 2026-10-25 11:34:11.117342
# Unit test for function median

# Generated at 2026-10-25 11:34:13.532517
# Unit test for function median

# Generated at 2026-10-25 11:34:15.945822
# Unit test for function median

# Generated at 2026-10-25 11:34:18.362285
# Unit test for function median

# Generated at 2026-10-25 11:34:20.778698
# Unit test for function median

# Generated at 2026-10-25 11:34:23.193266
# Unit test for function median

# Generated at 2026-10-25 11:34:25.610456
# Unit test for function median

# Generated at 2026-10-25 11:34:28.022573
# Unit test for function median

# Generated at 2026-10-25 11:34:30.437445
# Unit test for function median

# Generated at 2026-10-25 11:34:32.855041
# Unit test for function median

# Generated at 2026-10-25 11:34:35.270168
# Unit test for function median

# Generated at 2026-10-25 11:34:37.686038
# Unit test for function median

# Generated at 2026-10-25 11:34:41.425413
# Unit test for function median
def test_median():
    # Odd-length list
    assert module_0.median([3, 1, 2]) == 2
    # Even-length list -> averaged middle values
    assert module_0.median([4, 1, 3, 2]) == 2.5
    # Unsorted input with duplicates
    assert module_0.median([5, 1, 5, 3, 3]) == 3
    # Negative numbers
    assert module_0.median([-5, -1, -3]) == -3
    # Two elements
    assert module_0.median([10, 20]) == 15.0
    # Single element
    assert module_0.median([7]) == 7
    # Floats mixed with ints
    assert module_0.median([1.5, 2, 0.5]) == 1.5