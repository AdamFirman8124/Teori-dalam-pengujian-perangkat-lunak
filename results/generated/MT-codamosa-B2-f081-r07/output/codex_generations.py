

# Generated at 2026-10-24 15:49:57.378637
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

# Generated at 2026-10-24 15:49:58.892533
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

# Generated at 2026-10-24 15:50:00.325828
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

# Generated at 2026-10-24 15:50:01.861698
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

# Generated at 2026-10-24 15:50:03.294810
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