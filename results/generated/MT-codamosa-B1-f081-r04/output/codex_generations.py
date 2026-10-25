

# Generated at 2026-10-24 13:48:57.159134
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

# Generated at 2026-10-24 13:49:14.467841
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

# Generated at 2026-10-24 13:49:16.887066
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 13:49:19.304077
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 13:49:21.732002
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 13:49:24.149681
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 13:49:26.566115
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 13:49:28.981988
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 13:49:38.943770
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    assert module_0.numerical_letter_grade([]) == []
    assert module_0.numerical_letter_grade([4.0]) == ["A+"]
    assert module_0.numerical_letter_grade([3.9, 3.8]) == ["A", "A"]
    assert module_0.numerical_letter_grade([3.6, 3.4]) == ["A-", "A-"]
    assert module_0.numerical_letter_grade([3.2, 3.1]) == ["B+", "B+"]
    assert module_0.numerical_letter_grade([2.9, 2.8]) == ["B", "B"]
    assert module_0.numerical_letter_grade([2.6, 2.4]) == ["B-", "B-"]
    assert module_0.numerical_letter_grade([2.2, 2.1]) == ["C+", "C+"]
    assert module_0.numerical_letter_grade([1.9, 1.8]) == ["C", "C"]
    assert module_0.numerical_letter_grade([1.6, 1.4]) == ["C-", "C-"]
    assert module_0.numerical_letter_grade([1.2, 1.1]) == ["D+", "D+"]
    assert module_0.numerical_letter_grade([0.9, 0.8]) == ["D", "D"]
    assert module_0.numerical_letter_grade([0.6, 0.1]) == ["D-", "D-"]
    assert module_0.numerical_letter_grade([0.0, -1.0]) == ["E", "E"]
    assert module_0.numerical_letter_grade([3.7]) == ["A-"]
    assert module_0.numerical_letter_grade([3.3]) == ["B+"]
    assert module_0.numerical_letter_grade([3.0]) == ["B"]
    assert module_0.numerical_letter_grade([2.7]) == ["B-"]
    assert module_0.numerical_letter_grade([2.3]) == ["C+"]
    assert module_0.numerical_letter_grade([2.0]) == ["C"]
    assert module_0.numerical_letter_grade([1.7]) == ["C-"]
    assert module_0.numerical_letter_grade([1.3]) == ["D+"]
    assert module_0.numerical_letter_grade([1.0]) == ["D"]
    assert module_0.numerical_letter_grade([0.7]) == ["D-"]
    assert module_0.numerical_letter_grade([4.0, 3.9, 3.5, 3.1, 2.9, 2.5, 2.1, 1.9, 1.5, 1.2, 0.9, 0.5, 0.0]) == ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"]