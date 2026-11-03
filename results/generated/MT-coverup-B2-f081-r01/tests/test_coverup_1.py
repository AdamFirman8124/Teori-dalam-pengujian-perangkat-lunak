# file: project/f081/__init__.py:1-33
# asked: {"lines": [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 32, 33], "branches": [[6, 7], [6, 33], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 15], [15, 16], [15, 17], [17, 18], [17, 19], [19, 20], [19, 21], [21, 22], [21, 23], [23, 24], [23, 25], [25, 26], [25, 27], [27, 28], [27, 29], [29, 30], [29, 32]]}
# gained: {"lines": [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 32, 33], "branches": [[6, 7], [6, 33], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 15], [15, 16], [15, 17], [17, 18], [17, 19], [19, 20], [19, 21], [21, 22], [21, 23], [23, 24], [23, 25], [25, 26], [25, 27], [27, 28], [27, 29], [29, 30], [29, 32]]}

import pytest

from f081 import numerical_letter_grade


@pytest.mark.parametrize(
    "gpa, expected",
    [
        (4.0, "A+"),   # exact equality branch (line 8)
        (3.9, "A"),    # gpa > 3.7 (line 10)
        (3.7, "A-"),   # boundary: not > 3.7, but > 3.3 (line 12)
        (3.4, "A-"),   # gpa > 3.3
        (3.3, "B+"),   # boundary: not > 3.3, but > 3.0 (line 14)
        (3.1, "B+"),   # gpa > 3.0
        (3.0, "B"),    # boundary: not > 3.0, but > 2.7 (line 16)
        (2.8, "B"),    # gpa > 2.7
        (2.7, "B-"),   # boundary: not > 2.7, but > 2.3 (line 18)
        (2.4, "B-"),   # gpa > 2.3
        (2.3, "C+"),   # boundary: not > 2.3, but > 2.0 (line 20)
        (2.1, "C+"),   # gpa > 2.0
        (2.0, "C"),    # boundary: not > 2.0, but > 1.7 (line 22)
        (1.8, "C"),    # gpa > 1.7
        (1.7, "C-"),   # boundary: not > 1.7, but > 1.3 (line 24)
        (1.4, "C-"),   # gpa > 1.3
        (1.3, "D+"),   # boundary: not > 1.3, but > 1.0 (line 26)
        (1.1, "D+"),   # gpa > 1.0
        (1.0, "D"),    # boundary: not > 1.0, but > 0.7 (line 28)
        (0.8, "D"),    # gpa > 0.7
        (0.7, "D-"),   # boundary: not > 0.7, but > 0.0 (line 30)
        (0.3, "D-"),   # gpa > 0.0
        (0.0, "E"),    # else branch (line 32)
        (-1.5, "E"),   # negative GPA also falls to else branch
    ],
)
def test_numerical_letter_grade_single_value(gpa, expected):
    result = numerical_letter_grade([gpa])
    assert result == [expected]


def test_numerical_letter_grade_all_branches_in_one_call():
    """A single call whose result covers every branch of the if/elif chain."""
    grades = [4.0, 3.9, 3.7, 3.4, 3.3, 3.1, 3.0, 2.8, 2.7,
              2.4, 2.3, 2.1, 2.0, 1.8, 1.7, 1.4, 1.3, 1.1,
              1.0, 0.8, 0.7, 0.3, 0.0]
    expected = ["A+", "A", "A-", "A-", "B+", "B+", "B", "B", "B-",
                "B-", "C+", "C+", "C", "C", "C-", "C-", "D+", "D+",
                "D", "D", "D-", "D-", "E"]
    result = numerical_letter_grade(grades)
    assert result == expected
    assert len(result) == len(grades)


def test_numerical_letter_grade_empty_input():
    """Empty input list yields an empty result list (loop body never runs)."""
    assert numerical_letter_grade([]) == []


def test_numerical_letter_grade_does_not_mutate_input():
    """The function must not modify the input collection."""
    grades = [4.0, 2.0, 0.0]
    original = list(grades)
    numerical_letter_grade(grades)
    assert grades == original
