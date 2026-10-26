

# Generated at 2026-10-25 12:33:39.781140
# Unit test for function is_sorted
def test_is_sorted():
    # Sorted lists â True
    assert module_0.is_sorted([]) == True
    assert module_0.is_sorted([1]) == True
    assert module_0.is_sorted([1, 2, 3, 4]) == True
    assert module_0.is_sorted([1, 1, 2, 2, 3]) == True      # duplicates, but max 2 each

    # More than 2 duplicates â False even if sorted
    assert module_0.is_sorted([1, 1, 1]) == False
    assert module_0.is_sorted([1, 2, 2, 2, 3]) == False

    # Unsorted â False
    assert module_0.is_sorted([3, 1, 2]) == False
    assert module_0.is_sorted([2, 1]) == False
    assert module_0.is_sorted([1, 3, 2, 4]) == False

    # Unsorted AND >2 duplicates â False
    assert module_0.is_sorted([5, 5, 5, 1]) == False

    # Equal adjacent values â non-decreasing counts as sorted
    assert module_0.is_sorted([1, 2, 2]) == True

    print("All tests passed!")


test_is_sorted()

# Generated at 2026-10-25 12:33:42.658585
# Unit test for function is_sorted

# Generated at 2026-10-25 12:33:45.352823
# Unit test for function is_sorted

# Generated at 2026-10-25 12:33:47.767628
# Unit test for function is_sorted

# Generated at 2026-10-25 12:33:50.188412
# Unit test for function is_sorted

# Generated at 2026-10-25 12:33:52.601084
# Unit test for function is_sorted

# Generated at 2026-10-25 12:33:55.332527
# Unit test for function is_sorted

# Generated at 2026-10-25 12:33:57.752407
# Unit test for function is_sorted

# Generated at 2026-10-25 12:34:00.476599
# Unit test for function is_sorted

# Generated at 2026-10-25 12:34:02.889512
# Unit test for function is_sorted

# Generated at 2026-10-25 12:34:05.302348
# Unit test for function is_sorted

# Generated at 2026-10-25 12:34:07.714276
# Unit test for function is_sorted

# Generated at 2026-10-25 12:34:10.126935
# Unit test for function is_sorted