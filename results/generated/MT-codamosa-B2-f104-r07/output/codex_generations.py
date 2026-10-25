

# Generated at 2026-10-24 13:36:39.773097
# Unit test for function unique_digits
def test_unique_digits():
    assert module_0.unique_digits([15, 33, 1422, 1]) == [1, 15, 33]
    assert module_0.unique_digits([152, 323, 1422, 10]) == []
    assert module_0.unique_digits([]) == []
    assert module_0.unique_digits([1, 3, 5, 7, 9]) == [1, 3, 5, 7, 9]
    assert module_0.unique_digits([2, 4, 6, 8, 0]) == []
    assert module_0.unique_digits([123, 135, 137, 111]) == [111, 135, 137]
    assert module_0.unique_digits([35, 53, 33, 55]) == [33, 35, 53, 55]
    assert module_0.unique_digits([101, 111, 131, 2468]) == [111, 131]

# Generated at 2026-10-24 13:36:41.309579
# Unit test for function unique_digits
def test_unique_digits():
    assert module_0.unique_digits([15, 33, 1422, 1]) == [1, 15, 33]
    assert module_0.unique_digits([152, 323, 1422, 10]) == []
    assert module_0.unique_digits([]) == []
    assert module_0.unique_digits([1, 3, 5, 7, 9]) == [1, 3, 5, 7, 9]
    assert module_0.unique_digits([2, 4, 6, 8, 0]) == []
    assert module_0.unique_digits([123, 135, 137, 111]) == [111, 135, 137]
    assert module_0.unique_digits([35, 53, 33, 55]) == [33, 35, 53, 55]
    assert module_0.unique_digits([101, 111, 131, 2468]) == [111, 131]

# Generated at 2026-10-24 13:36:57.741189
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

# Generated at 2026-10-24 13:37:14.281387
# Unit test for function unique_digits
def test_unique_digits():
    assert module_0.unique_digits([15, 33, 1422, 1]) == [1, 15, 33]
    assert module_0.unique_digits([152, 323, 1422, 10]) == []
    assert module_0.unique_digits([]) == []
    assert module_0.unique_digits([1, 3, 5, 7, 9]) == [1, 3, 5, 7, 9]
    assert module_0.unique_digits([2, 4, 6, 8, 0]) == []
    assert module_0.unique_digits([123, 135, 137, 111]) == [111, 135, 137]
    assert module_0.unique_digits([35, 53, 33, 55]) == [33, 35, 53, 55]
    assert module_0.unique_digits([101, 111, 131, 2468]) == [111, 131]

# Generated at 2026-10-24 13:37:16.698168
# Unit test for function unique_digits

# Generated at 2026-10-24 13:37:22.577156
# Unit test for function unique_digits
def test_unique_digits():
    assert module_0.unique_digits([15, 33, 1422, 1]) == [1, 15, 33]
    assert module_0.unique_digits([152, 323, 1422, 10]) == []
    assert module_0.unique_digits([]) == []
    assert module_0.unique_digits([2]) == []
    assert module_0.unique_digits([7]) == [7]
    assert module_0.unique_digits([135, 246, 97531, 111, 20]) == [111, 135, 97531]
    assert module_0.unique_digits([13, 31, 311, 113]) == [113, 13, 31, 311]
    assert module_0.unique_digits([0, 5, 55, 505]) == [5, 55]