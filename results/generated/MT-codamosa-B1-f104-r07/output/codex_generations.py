

# Generated at 2026-10-24 11:59:29.773458
# Unit test for function unique_digits

# Generated at 2026-10-24 11:59:32.194633
# Unit test for function unique_digits

# Generated at 2026-10-24 11:59:34.617037
# Unit test for function unique_digits

# Generated at 2026-10-24 12:00:04.408252
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

# Generated at 2026-10-24 12:00:35.211297
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

# Generated at 2026-10-24 12:00:51.578368
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

# Generated at 2026-10-24 12:01:08.420829
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