

# Generated at 2026-10-24 06:13:24.302535
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 06:13:26.717732
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 06:13:29.133575
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 06:13:31.548679
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 06:13:33.964860
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 06:13:36.379181
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 06:13:38.794630
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 06:13:41.209636
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 06:13:43.623337
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 06:13:46.037518
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 06:13:48.451618
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 06:13:50.866734
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 06:14:03.696698
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():assert module_0.numerical_letter_grade([4.0, 3.8, 3.7, 3.4, 3.3, 3.1, 3.0]) == [
        "A+", "A", "A-", "A-", "B+", "B+", "B"
    ]

# Generated at 2026-10-24 06:14:15.138912
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
    assert module_0.numerical_letter_grade([]) == []


test_numerical_letter_grade()
print("All tests passed.")

# Generated at 2026-10-24 06:14:22.926239
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    grades = [
        4.0, 3.8, 3.5, 3.2, 2.9, 2.5, 2.2,
        1.9, 1.5, 1.2, 0.9, 0.5, 0.0
    ]

    expected = [
        "A+", "A", "A-", "B+", "B", "B-", "C+",
        "C", "C-", "D+", "D", "D-", "E"
    ]

    assert module_0.numerical_letter_grade(grades) == expected


test_numerical_letter_grade()

# Generated at 2026-10-24 06:14:32.597989
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    grades = [
        4.0, 3.8, 3.5, 3.2,
        2.9, 2.5, 2.2, 1.9,
        1.5, 1.2, 0.9, 0.5, 0.0
    ]

    expected = [
        "A+", "A", "A-", "B+",
        "B", "B-", "C+", "C",
        "C-", "D+", "D", "D-", "E"
    ]

    assert module_0.numerical_letter_grade(grades) == expected


test_numerical_letter_grade()

# Generated at 2026-10-24 06:14:42.118648
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

# Generated at 2026-10-24 06:14:44.538078
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 06:14:47.039199
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 06:14:49.456172
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 06:14:51.957873
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 06:14:54.374233
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 06:15:11.316410
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():assert module_0.numerical_letter_grade([4.0, 3.8, 3.5, 3.1, 2.8, 2.5, 2.1, 1.8, 1.5, 1.1, 0.8, 0.3, 0.0]) == [
        "A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"
    ]

# Generated at 2026-10-24 06:15:20.212061
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    grades = [
        4.0, 3.9, 3.7, 3.5, 3.3, 3.1,
        3.0, 2.8, 2.7, 2.5, 2.3, 2.1,
        2.0, 1.8, 1.7, 1.5, 1.3, 1.1,
        1.0, 0.8, 0.7, 0.5, 0.0
    ]

    expected = [
        "A+", "A", "A-", "A-", "B+", "B+",
        "B", "B", "B-", "B-", "C+", "C+",
        "C", "C", "C-", "C-", "D+", "D+",
        "D", "D", "D-", "D-", "E"
    ]

    assert module_0.numerical_letter_grade(grades) == expected

# Generated at 2026-10-24 06:15:30.144858
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    grades = [
        4.0, 3.8, 3.7, 3.4, 3.3, 3.1, 3.0,
        2.8, 2.7, 2.4, 2.3, 2.1, 2.0,
        1.8, 1.7, 1.4, 1.3, 1.1, 1.0,
        0.8, 0.7, 0.1, 0.0
    ]

    expected = [
        "A+", "A", "A-", "A-", "B+", "B+", "B",
        "B", "B-", "B-", "C+", "C+", "C",
        "C", "C-", "C-", "D+", "D+", "D",
        "D", "D-", "D-", "E"
    ]

    assert module_0.numerical_letter_grade(grades) == expected
    assert module_0.numerical_letter_grade([]) == []

# Generated at 2026-10-24 06:15:39.464170
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    # Test each letter-grade range
    grades = [
        4.0, 3.8, 3.5, 3.2, 2.8, 2.5, 2.2,
        1.8, 1.5, 1.2, 0.8, 0.5, 0.0
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
        "A-", "B+", "B", "B-", "C+",
        "C", "C-", "D+", "D", "D-"
    ]

    # Test an empty list
    assert module_0.numerical_letter_grade([]) == []

# Generated at 2026-10-24 06:15:46.629130
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    grades = [
        4.0, 3.8, 3.5, 3.2, 2.9, 2.5, 2.1,
        1.8, 1.5, 1.1, 0.8, 0.5, 0.0
    ]

    expected = [
        "A+", "A", "A-", "B+", "B", "B-", "C+",
        "C", "C-", "D+", "D", "D-", "E"
    ]

    assert module_0.numerical_letter_grade(grades) == expected


def test_numerical_letter_grade_boundaries():
    grades = [4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0,
              1.7, 1.3, 1.0, 0.7, 0.0]

    expected = ["A+", "A-", "B+", "B", "B-", "C+", "C",
                "C-", "D+", "D", "D-", "E"]

    assert module_0.numerical_letter_grade(grades) == expected