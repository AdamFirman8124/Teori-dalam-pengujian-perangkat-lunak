

# Generated at 2026-10-24 20:04:13.193847
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    assert module_0.numerical_letter_grade([]) == []

    assert module_0.numerical_letter_grade(
        [4.0, 3.8, 3.7, 3.5, 3.3, 3.1, 3.0,
         2.8, 2.7, 2.5, 2.3, 2.1, 2.0,
         1.8, 1.7, 1.5, 1.3, 1.1, 1.0,
         0.8, 0.7, 0.1, 0.0, -1.0]
    ) == [
        "A+", "A", "A-", "A-", "B+", "B+", "B",
        "B", "B-", "B-", "C+", "C+", "C",
        "C", "C-", "C-", "D+", "D+", "D",
        "D", "D-", "D-", "E", "E"
    ]


test_numerical_letter_grade()
print("All tests passed.")

# Generated at 2026-10-24 20:04:23.120352
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    assert module_0.numerical_letter_grade([4.0, 3.8, 3.5, 3.1]) == [
        "A+", "A", "A-", "B+"
    ]

    assert module_0.numerical_letter_grade([3.0, 2.8, 2.5, 2.1]) == [
        "B", "B", "B-", "C+"
    ]

    assert module_0.numerical_letter_grade([2.0, 1.8, 1.5, 1.1]) == [
        "C", "C", "C-", "D+"
    ]

    assert module_0.numerical_letter_grade([1.0, 0.8, 0.5, 0.0]) == [
        "D", "D", "D-", "E"
    ]

    assert module_0.numerical_letter_grade([]) == []


test_numerical_letter_grade()
print("All tests passed.")

# Generated at 2026-10-24 20:04:30.800411
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    grades = [
        4.0,
        3.8, 3.7,
        3.4, 3.3,
        3.1, 3.0,
        2.8, 2.7,
        2.4, 2.3,
        2.1, 2.0,
        1.8, 1.7,
        1.4, 1.3,
        1.1, 1.0,
        0.8, 0.7,
        0.1, 0.0
    ]

    expected = [
        "A+",
        "A", "A-",
        "A-", "B+",
        "B+", "B",
        "B", "B-",
        "B-", "C+",
        "C+", "C",
        "C", "C-",
        "C-", "D+",
        "D+", "D",
        "D", "D-",
        "D-", "E"
    ]

    assert module_0.numerical_letter_grade(grades) == expected

# Generated at 2026-10-24 20:04:39.709291
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    grades = [
        4.0, 3.8, 3.7, 3.3, 3.0, 2.7, 2.3,
        2.0, 1.7, 1.3, 1.0, 0.7, 0.1, 0.0
    ]

    expected = [
        "A+", "A", "A-", "B+", "B", "B-", "C+",
        "C", "C-", "D+", "D", "D-", "D-", "E"
    ]

    assert module_0.numerical_letter_grade(grades) == expected
    assert module_0.numerical_letter_grade([]) == []

# Generated at 2026-10-24 20:04:42.128765
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 20:04:44.551259
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 20:04:47.110355
# Unit test for function numerical_letter_grade