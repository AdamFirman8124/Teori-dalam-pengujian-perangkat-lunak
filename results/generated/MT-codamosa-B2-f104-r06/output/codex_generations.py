

# Generated at 2026-10-24 14:57:44.924542
# Unit test for function unique_digits
def test_unique_digits():
    # Basic cases
    assert module_0.unique_digits([15, 33, 1422, 1]) == [1, 15, 33]
    assert module_0.unique_digits([152, 323, 1422, 10]) == []

    # Single element / empty input
    assert module_0.unique_digits([7]) == [7]
    assert module_0.unique_digits([]) == []

    # Sorting check (unsorted input)
    assert module_0.unique_digits([31, 13, 3]) == [3, 13, 31]

    # Zero and even digits excluded
    assert module_0.unique_digits([0, 12, 24, 35]) == [35]

    # Negative numbers: '-' is not a digit, digits of -13 are 1,3 â valid
    assert module_0.unique_digits([-13, -24]) == [-13]

    # Duplicates preserved
    assert module_0.unique_digits([11, 11, 2]) == [11, 11]

    print("All tests passed.")

test_unique_digits()

# Generated at 2026-10-24 14:57:47.338060
# Unit test for function unique_digits

# Generated at 2026-10-24 14:57:49.751554
# Unit test for function unique_digits

# Generated at 2026-10-24 14:57:52.164596
# Unit test for function unique_digits

# Generated at 2026-10-24 14:57:54.577002
# Unit test for function unique_digits

# Generated at 2026-10-24 14:57:56.989081
# Unit test for function unique_digits

# Generated at 2026-10-24 14:57:59.403492
# Unit test for function unique_digits

# Generated at 2026-10-24 14:58:01.813644
# Unit test for function unique_digits

# Generated at 2026-10-24 14:58:04.226726
# Unit test for function unique_digits

# Generated at 2026-10-24 14:58:06.638774
# Unit test for function unique_digits

# Generated at 2026-10-24 14:58:09.051313
# Unit test for function unique_digits

# Generated at 2026-10-24 14:58:11.465367
# Unit test for function unique_digits

# Generated at 2026-10-24 14:58:13.877323
# Unit test for function unique_digits