# file: project/f081/__init__.py:1-33
# asked: {"lines": [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 32, 33], "branches": [[6, 7], [6, 33], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 15], [15, 16], [15, 17], [17, 18], [17, 19], [19, 20], [19, 21], [21, 22], [21, 23], [23, 24], [23, 25], [25, 26], [25, 27], [27, 28], [27, 29], [29, 30], [29, 32]]}
# gained: {"lines": [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 32, 33], "branches": [[6, 7], [6, 33], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 15], [15, 16], [15, 17], [17, 18], [17, 19], [19, 20], [19, 21], [21, 22], [21, 23], [23, 24], [23, 25], [25, 26], [25, 27], [27, 28], [27, 29], [29, 30], [29, 32]]}

import pytest

from f081 import numerical_letter_grade


def test_all_branches_covered():
    grades = [
        4.0,   # == 4.0 -> "A+"
        3.9,   # > 3.7  -> "A"
        3.5,   # > 3.3  -> "A-"
        3.1,   # > 3.0  -> "B+"
        2.8,   # > 2.7  -> "B"
        2.5,   # > 2.3  -> "B-"
        2.1,   # > 2.0  -> "C+"
        1.8,   # > 1.7  -> "C"
        1.5,   # > 1.3  -> "C-"
        1.1,   # > 1.0  -> "D+"
        0.8,   # > 0.7  -> "D"
        0.3,   # > 0.0  -> "D-"
        0.0,   # else   -> "E"
    ]
    expected = [
        "A+", "A", "A-", "B+", "B", "B-",
        "C+", "C", "C-", "D+", "D", "D-", "E",
    ]
    result = numerical_letter_grade(grades)
    assert result == expected
    assert len(result) == len(grades)


def test_empty_input():
    assert numerical_letter_grade([]) == []


def test_boundary_values():
    # Exact boundary values fall to the next lower bucket (strict > comparisons)
    assert numerical_letter_grade([3.7]) == ["A-"]
    assert numerical_letter_grade([3.3]) == ["B+"]
    assert numerical_letter_grade([3.0]) == ["B"]
    assert numerical_letter_grade([2.7]) == ["B-"]
    assert numerical_letter_grade([2.3]) == ["C+"]
    assert numerical_letter_grade([2.0]) == ["C"]
    assert numerical_letter_grade([1.7]) == ["C-"]
    assert numerical_letter_grade([1.3]) == ["D+"]
    assert numerical_letter_grade([1.0]) == ["D"]
    assert numerical_letter_grade([0.7]) == ["D-"]


def test_result_is_new_list_not_mutating_input():
    grades = [4.0, 0.0]
    result = numerical_letter_grade(grades)
    assert result == ["A+", "E"]
    assert result is not grades
    assert grades == [4.0, 0.0]
