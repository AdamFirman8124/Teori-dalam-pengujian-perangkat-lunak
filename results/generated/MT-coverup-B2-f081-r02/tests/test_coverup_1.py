# file: project/f081/__init__.py:1-33
# asked: {"lines": [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 32, 33], "branches": [[6, 7], [6, 33], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 15], [15, 16], [15, 17], [17, 18], [17, 19], [19, 20], [19, 21], [21, 22], [21, 23], [23, 24], [23, 25], [25, 26], [25, 27], [27, 28], [27, 29], [29, 30], [29, 32]]}
# gained: {"lines": [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 32, 33], "branches": [[6, 7], [6, 33], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 15], [15, 16], [15, 17], [17, 18], [17, 19], [19, 20], [19, 21], [21, 22], [21, 23], [23, 24], [23, 25], [25, 26], [25, 27], [27, 28], [27, 29], [29, 30], [29, 32]]}

import pytest

from f081 import numerical_letter_grade


@pytest.mark.parametrize(
    ("gpa", "expected"),
    [
        # Exact equality branch (line 7-8)
        (4.0, "A+"),
        # Each elif branch taken with a value strictly inside its range
        (3.8, "A"),    # > 3.7
        (3.5, "A-"),   # > 3.3
        (3.2, "B+"),   # > 3.0
        (2.9, "B"),    # > 2.7
        (2.5, "B-"),   # > 2.3
        (2.1, "C+"),   # > 2.0
        (1.9, "C"),    # > 1.7
        (1.5, "C-"),   # > 1.3
        (1.1, "D+"),   # > 1.0
        (0.8, "D"),    # > 0.7
        (0.5, "D-"),   # > 0.0
        # else branch (line 31-32)
        (0.0, "E"),
        (-2.5, "E"),
    ],
)
def test_numerical_letter_grade_single_value(gpa, expected):
    """Each GPA value maps to exactly one letter grade."""
    result = numerical_letter_grade([gpa])
    assert result == [expected]
    assert isinstance(result, list)


@pytest.mark.parametrize(
    ("gpa", "expected"),
    [
        # Boundary values: each elif condition is False, falls to next branch
        (3.7, "A-"),
        (3.3, "B+"),
        (3.0, "B"),
        (2.7, "B-"),
        (2.3, "C+"),
        (2.0, "C"),
        (1.7, "C-"),
        (1.3, "D+"),
        (1.0, "D"),
        (0.7, "D-"),
    ],
)
def test_numerical_letter_grade_boundaries(gpa, expected):
    """Values exactly at a threshold do not satisfy the strict '>' comparison."""
    assert numerical_letter_grade([gpa]) == [expected]


def test_numerical_letter_grade_all_branches_in_one_call():
    """A single call exercises every line and branch of the function."""
    grades = [4.0, 3.9, 3.5, 3.2, 2.9, 2.5, 2.1, 1.9, 1.5, 1.1, 0.8, 0.4, 0.0]
    expected = [
        "A+", "A", "A-", "B+", "B", "B-",
        "C+", "C", "C-", "D+", "D", "D-", "E",
    ]
    result = numerical_letter_grade(grades)
    assert result == expected
    assert len(result) == len(grades)


def test_numerical_letter_grade_empty_input():
    """An empty input yields an empty result list."""
    assert numerical_letter_grade([]) == []


def test_numerical_letter_grade_does_not_mutate_input():
    """The function must not modify the input sequence."""
    grades = [4.0, 2.5, 0.0]
    snapshot = list(grades)
    result = numerical_letter_grade(grades)
    assert grades == snapshot
    assert result == ["A+", "B-", "E"]
    assert result is not grades
