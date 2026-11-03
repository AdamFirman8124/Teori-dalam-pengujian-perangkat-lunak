# file: project/f081/__init__.py:1-33
# asked: {"lines": [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 32, 33], "branches": [[6, 7], [6, 33], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 15], [15, 16], [15, 17], [17, 18], [17, 19], [19, 20], [19, 21], [21, 22], [21, 23], [23, 24], [23, 25], [25, 26], [25, 27], [27, 28], [27, 29], [29, 30], [29, 32]]}
# gained: {"lines": [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 32, 33], "branches": [[6, 7], [6, 33], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 15], [15, 16], [15, 17], [17, 18], [17, 19], [19, 20], [19, 21], [21, 22], [21, 23], [23, 24], [23, 25], [25, 26], [25, 27], [27, 28], [27, 29], [29, 30], [29, 32]]}

import pytest

from f081 import numerical_letter_grade


@pytest.mark.parametrize(
    "gpa, expected",
    [
        (4.0, "A+"),   # gpa == 4.0 branch
        (3.9, "A"),    # gpa > 3.7 branch
        (3.7, "A-"),   # boundary: 3.7 > 3.7 is False -> falls to next branch
        (3.5, "A-"),   # gpa > 3.3 branch
        (3.3, "B+"),   # boundary: 3.3 > 3.3 is False
        (3.1, "B+"),   # gpa > 3.0 branch
        (3.0, "B"),    # boundary: 3.0 > 3.0 is False
        (2.9, "B"),    # gpa > 2.7 branch
        (2.7, "B-"),   # boundary: 2.7 > 2.7 is False
        (2.5, "B-"),   # gpa > 2.3 branch
        (2.3, "C+"),   # boundary: 2.3 > 2.3 is False
        (2.1, "C+"),   # gpa > 2.0 branch
        (2.0, "C"),    # boundary: 2.0 > 2.0 is False
        (1.9, "C"),    # gpa > 1.7 branch
        (1.7, "C-"),   # boundary: 1.7 > 1.7 is False
        (1.5, "C-"),   # gpa > 1.3 branch
        (1.3, "D+"),   # boundary: 1.3 > 1.3 is False
        (1.1, "D+"),   # gpa > 1.0 branch
        (1.0, "D"),    # boundary: 1.0 > 1.0 is False
        (0.9, "D"),    # gpa > 0.7 branch
        (0.7, "D-"),   # boundary: 0.7 > 0.7 is False
        (0.5, "D-"),   # gpa > 0.0 branch
        (0.0, "E"),    # boundary: 0.0 > 0.0 is False -> else branch
        (-1.5, "E"),   # else branch (negative gpa)
    ],
)
def test_numerical_letter_grade_boundaries(gpa, expected):
    result = numerical_letter_grade([gpa])
    assert result == [expected]
    assert isinstance(result, list)


def test_numerical_letter_grade_all_branches_single_call():
    grades = [4.0, 3.9, 3.7, 3.5, 3.3, 3.1, 3.0, 2.9, 2.7, 2.5,
              2.3, 2.1, 2.0, 1.9, 1.7, 1.5, 1.3, 1.1, 1.0, 0.9,
              0.7, 0.5, 0.0, -2.0]
    expected = ["A+", "A", "A-", "A-", "B+", "B+", "B", "B", "B-", "B-",
                "C+", "C+", "C", "C", "C-", "C-", "D+", "D+", "D", "D",
                "D-", "D-", "E", "E"]
    result = numerical_letter_grade(grades)
    assert result == expected
    assert len(result) == len(grades)


def test_numerical_letter_grade_empty_input():
    # Covers the case where the for-loop body never executes.
    assert numerical_letter_grade([]) == []
