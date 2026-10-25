

# Generated at 2026-10-24 06:23:27.116268
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    # Test a representative value from every grade range
    grades = [4.0, 3.8, 3.5, 3.2, 2.8, 2.5, 2.2,
              1.8, 1.5, 1.2, 0.8, 0.5, 0.0]

    expected = ["A+", "A", "A-", "B+", "B", "B-", "C+",
                "C", "C-", "D+", "D", "D-", "E"]

    assert module_0.numerical_letter_grade(grades) == expected

    # Test exact boundary values
    assert module_0.numerical_letter_grade(
        [3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7]
    ) == [
        "A-", "B+", "B", "B-", "C+",
        "C", "C-", "D+", "D", "D-"
    ]

    # Test an empty input
    assert module_0.numerical_letter_grade([]) == []

# Generated at 2026-10-24 06:23:33.884149
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    grades = [
        4.0, 3.8, 3.5, 3.1, 2.8, 2.5, 2.1,
        1.8, 1.5, 1.1, 0.8, 0.5, 0.0
    ]

    expected = [
        "A+", "A", "A-", "B+", "B", "B-", "C+",
        "C", "C-", "D+", "D", "D-", "E"
    ]

    assert module_0.numerical_letter_grade(grades) == expected

    # Check exact boundary values.
    assert module_0.numerical_letter_grade(
        [3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7]
    ) == [
        "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-"
    ]

# Generated at 2026-10-24 06:23:44.362369
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    assert module_0.numerical_letter_grade(
        [4.0, 3.8, 3.5, 3.2, 2.9, 2.5, 2.2,
         1.9, 1.5, 1.2, 0.9, 0.5, 0.0]
    ) == [
        "A+", "A", "A-", "B+", "B", "B-", "C+",
        "C", "C-", "D+", "D", "D-", "E"
    ]

    # Exact boundaries follow the function's strict `>` comparisons.
    assert module_0.numerical_letter_grade(
        [3.7, 3.3, 3.0, 2.7, 2.3, 2.0,
         1.7, 1.3, 1.0, 0.7, 0.0]
    ) == [
        "A-", "B+", "B", "B-", "C+", "C",
        "C-", "D+", "D", "D-", "E"
    ]

    assert module_0.numerical_letter_grade([]) == []

# Generated at 2026-10-24 06:23:53.443793
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    assert module_0.numerical_letter_grade([4.0, 3.8, 3.5, 3.2]) == [
        "A+", "A", "A-", "B+"
    ]

    assert module_0.numerical_letter_grade([2.8, 2.5, 2.2, 1.8]) == [
        "B", "B-", "C+", "C"
    ]

    assert module_0.numerical_letter_grade([1.5, 1.2, 0.8, 0.5, 0.0]) == [
        "C-", "D+", "D", "D-", "E"
    ]

    # Test exact grade boundaries
    assert module_0.numerical_letter_grade(
        [3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7]
    ) == [
        "A-", "B+", "B", "B-", "C+",
        "C", "C-", "D+", "D", "D-"
    ]

    assert module_0.numerical_letter_grade([]) == []

# Generated at 2026-10-24 06:24:02.249679
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    grades = [
        4.0, 3.8, 3.5, 3.2, 2.9, 2.5, 2.1,
        1.8, 1.5, 1.1, 0.8, 0.5, 0.0
    ]

    expected = [
        "A+", "A", "A-", "B+", "B", "B-",
        "C+", "C", "C-", "D+", "D", "D-", "E"
    ]

    assert module_0.numerical_letter_grade(grades) == expected


test_numerical_letter_grade()
print("All tests passed.")