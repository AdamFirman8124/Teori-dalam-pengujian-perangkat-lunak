# file: project/f081/__init__.py:1-33
# asked: {"lines": [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 32, 33], "branches": [[6, 7], [6, 33], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 15], [15, 16], [15, 17], [17, 18], [17, 19], [19, 20], [19, 21], [21, 22], [21, 23], [23, 24], [23, 25], [25, 26], [25, 27], [27, 28], [27, 29], [29, 30], [29, 32]]}
# gained: {"lines": [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 32, 33], "branches": [[6, 7], [6, 33], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 15], [15, 16], [15, 17], [17, 18], [17, 19], [19, 20], [19, 21], [21, 22], [21, 23], [23, 24], [23, 25], [25, 26], [25, 27], [27, 28], [27, 29], [29, 30], [29, 32]]}

import pytest

from f081 import numerical_letter_grade


@pytest.mark.parametrize(
    "gpa, expected",
    [
        (4.0, "A+"),   # line 8: gpa == 4.0
        (3.8, "A"),    # line 10: gpa > 3.7
        (3.5, "A-"),   # line 12: gpa > 3.3
        (3.1, "B+"),   # line 14: gpa > 3.0
        (2.9, "B"),    # line 16: gpa > 2.7
        (2.5, "B-"),   # line 18: gpa > 2.3
        (2.1, "C+"),   # line 20: gpa > 2.0
        (1.9, "C"),    # line 22: gpa > 1.7
        (1.5, "C-"),   # line 24: gpa > 1.3
        (1.1, "D+"),   # line 26: gpa > 1.0
        (0.9, "D"),    # line 28: gpa > 0.7
        (0.3, "D-"),   # line 30: gpa > 0.0
        (0.0, "E"),    # line 32: else branch
    ],
)
def test_numerical_letter_grade_single_value(gpa, expected):
    result = numerical_letter_grade([gpa])
    assert result == [expected]


@pytest.mark.parametrize(
    "gpa, expected",
    [
        (3.7, "A-"),   # boundary: not > 3.7, falls to gpa > 3.3
        (3.3, "B+"),   # boundary: not > 3.3, falls to gpa > 3.0
        (3.0, "B"),    # boundary: not > 3.0, falls to gpa > 2.7
        (2.7, "B-"),   # boundary: not > 2.7, falls to gpa > 2.3
        (2.3, "C+"),   # boundary: not > 2.3, falls to gpa > 2.0
        (2.0, "C"),    # boundary: not > 2.0, falls to gpa > 1.7
        (1.7, "C-"),   # boundary: not > 1.7, falls to gpa > 1.3
        (1.3, "D+"),   # boundary: not > 1.3, falls to gpa > 1.0
        (1.0, "D"),    # boundary: not > 1.0, falls to gpa > 0.7
        (0.7, "D-"),   # boundary: not > 0.7, falls to gpa > 0.0
    ],
)
def test_numerical_letter_grade_boundaries(gpa, expected):
    result = numerical_letter_grade([gpa])
    assert result == [expected]


def test_numerical_letter_grade_empty_input():
    assert numerical_letter_grade([]) == []


def test_numerical_letter_grade_all_branches_in_one_call():
    grades = [4.0, 3.8, 3.5, 3.1, 2.9, 2.5, 2.1, 1.9, 1.5, 1.1, 0.9, 0.3, 0.0]
    expected = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"]
    result = numerical_letter_grade(grades)
    assert result == expected
    assert len(result) == len(grades)


def test_numerical_letter_grade_preserves_order_and_length():
    grades = [0.0, 4.0, 2.9]
    result = numerical_letter_grade(grades)
    assert result == ["E", "A+", "B"]
    assert result is not grades  # returns a new list, input untouched
    assert grades == [0.0, 4.0, 2.9]  # input list is not mutated
