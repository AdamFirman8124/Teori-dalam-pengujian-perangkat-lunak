

# Generated at 2026-10-24 12:03:02.951638
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    # Top grade
    assert module_0.numerical_letter_grade([4.0]) == ["A+"]

    # One value in each band
    assert module_0.numerical_letter_grade(
        [3.9, 3.5, 3.1, 2.9, 2.5, 2.1, 1.9, 1.5, 1.1, 0.9, 0.5]
    ) == ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-"]

    # Boundaries fall into the lower band
    assert module_0.numerical_letter_grade(
        [3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0]
    ) == ["A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"]

    # Failing and empty input
    assert module_0.numerical_letter_grade([0.0, -1.0]) == ["E", "E"]
    assert module_0.numerical_letter_grade([]) == []

# Generated at 2026-10-24 12:03:19.696270
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    # test each branch - mid-range values
    assert module_0.numerical_letter_grade([4.0]) == ["A+"]
    assert module_0.numerical_letter_grade([3.8]) == ["A"]
    assert module_0.numerical_letter_grade([3.5]) == ["A-"]
    assert module_0.numerical_letter_grade([3.2]) == ["B+"]
    assert module_0.numerical_letter_grade([2.9]) == ["B"]
    assert module_0.numerical_letter_grade([2.5]) == ["B-"]
    assert module_0.numerical_letter_grade([2.2]) == ["C+"]
    assert module_0.numerical_letter_grade([1.9]) == ["C"]
    assert module_0.numerical_letter_grade([1.5]) == ["C-"]
    assert module_0.numerical_letter_grade([1.2]) == ["D+"]
    assert module_0.numerical_letter_grade([0.9]) == ["D"]
    assert module_0.numerical_letter_grade([0.5]) == ["D-"]
    assert module_0.numerical_letter_grade([0.0]) == ["E"]

    # test list input
    assert module_0.numerical_letter_grade(
        [4.0, 3.9, 3.5, 3.2, 2.9, 2.5, 2.2, 1.9, 1.5, 1.2, 0.9, 0.5, 0.0]
    ) == ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"]

    # test empty and E cases
    assert module_0.numerical_letter_grade([]) == []
    assert module_0.numerical_letter_grade([0.0, -1.0]) == ["E", "E"]

# Generated at 2026-10-24 12:03:36.693789
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    # Top grade
    assert module_0.numerical_letter_grade([4.0]) == ["A+"]

    # One value in each band
    assert module_0.numerical_letter_grade(
        [3.9, 3.5, 3.1, 2.9, 2.5, 2.1, 1.9, 1.5, 1.1, 0.9, 0.5]
    ) == ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-"]

    # Boundaries fall into the lower band
    assert module_0.numerical_letter_grade(
        [3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0]
    ) == ["A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"]

    # Failing and empty input
    assert module_0.numerical_letter_grade([0.0, -1.0]) == ["E", "E"]
    assert module_0.numerical_letter_grade([]) == []

# Generated at 2026-10-24 12:03:39.126876
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 12:03:41.546005
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 12:03:43.963508
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 12:03:46.378265
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 12:03:48.796911
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 12:04:18.941807
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():assert module_0.numerical_letter_grade([4.0, 3.8, 3.5, 3.1, 2.8]) == ["A+", "A", "A-", "B+", "B"]