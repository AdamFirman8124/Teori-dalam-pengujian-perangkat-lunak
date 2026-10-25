

# Generated at 2026-10-24 21:37:50.767049
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    grades = [
        4.0, 3.8, 3.5, 3.1, 2.8, 2.4, 2.1,
        1.8, 1.4, 1.1, 0.8, 0.1, 0.0
    ]

    expected = [
        "A+", "A", "A-", "B+", "B", "B-", "C+",
        "C", "C-", "D+", "D", "D-", "E"
    ]

    assert module_0.numerical_letter_grade(grades) == expected

    # Test exact boundary values
    assert module_0.numerical_letter_grade(
        [3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7]
    ) == [
        "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-"
    ]

    # Test an empty input
    assert module_0.numerical_letter_grade([]) == []

# Generated at 2026-10-24 21:37:57.737602
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    grades = [
        4.0, 3.8, 3.7, 3.4, 3.3, 3.1,
        3.0, 2.8, 2.7, 2.4, 2.3, 2.1,
        2.0, 1.8, 1.7, 1.4, 1.3, 1.1,
        1.0, 0.8, 0.7, 0.1, 0.0
    ]

    expected = [
        "A+", "A", "A-", "A-", "B+", "B+",
        "B", "B", "B-", "B-", "C+", "C+",
        "C", "C", "C-", "C-", "D+", "D+",
        "D", "D", "D-", "D-", "E"
    ]

    assert module_0.numerical_letter_grade(grades) == expected

# Generated at 2026-10-24 21:38:00.159807
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 21:38:02.581048
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 21:38:05.176103
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 21:38:07.597124
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 21:38:10.013387
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 21:38:12.430178
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 21:38:14.850922
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 21:38:17.267247
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 21:38:19.689193
# Unit test for function numerical_letter_grade