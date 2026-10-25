# file: project/f081/__init__.py:1-33
# asked: {"lines": [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 32, 33], "branches": [[6, 7], [6, 33], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 15], [15, 16], [15, 17], [17, 18], [17, 19], [19, 20], [19, 21], [21, 22], [21, 23], [23, 24], [23, 25], [25, 26], [25, 27], [27, 28], [27, 29], [29, 30], [29, 32]]}
# gained: {"lines": [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 32, 33], "branches": [[6, 7], [6, 33], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 15], [15, 16], [15, 17], [17, 18], [17, 19], [19, 20], [19, 21], [21, 22], [21, 23], [23, 24], [23, 25], [25, 26], [25, 27], [27, 28], [27, 29], [29, 30], [29, 32]]}

import pytest

from f081 import numerical_letter_grade


def test_empty_list_returns_empty_list():
    result = numerical_letter_grade([])
    assert result == []
    assert isinstance(result, list)


def test_perfect_gpa_gets_a_plus():
    assert numerical_letter_grade([4.0]) == ["A+"]


def test_gpa_above_3_7_gets_a():
    assert numerical_letter_grade([3.8]) == ["A"]


def test_gpa_above_3_3_gets_a_minus():
    assert numerical_letter_grade([3.5]) == ["A-"]


def test_gpa_above_3_0_gets_b_plus():
    assert numerical_letter_grade([3.1]) == ["B+"]


def test_gpa_above_2_7_gets_b():
    assert numerical_letter_grade([2.8]) == ["B"]


def test_gpa_above_2_3_gets_b_minus():
    assert numerical_letter_grade([2.5]) == ["B-"]


def test_gpa_above_2_0_gets_c_plus():
    assert numerical_letter_grade([2.1]) == ["C+"]


def test_gpa_above_1_7_gets_c():
    assert numerical_letter_grade([1.8]) == ["C"]


def test_gpa_above_1_3_gets_c_minus():
    assert numerical_letter_grade([1.5]) == ["C-"]


def test_gpa_above_1_0_gets_d_plus():
    assert numerical_letter_grade([1.1]) == ["D+"]


def test_gpa_above_0_7_gets_d():
    assert numerical_letter_grade([0.8]) == ["D"]


def test_gpa_above_0_0_gets_d_minus():
    assert numerical_letter_grade([0.5]) == ["D-"]


def test_zero_and_negative_gpa_get_e():
    assert numerical_letter_grade([0.0, -1.0]) == ["E", "E"]


def test_boundary_values_fall_into_lower_bucket():
    grades = [3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7]
    assert numerical_letter_grade(grades) == [
        "A-",
        "B+",
        "B",
        "B-",
        "C+",
        "C",
        "C-",
        "D+",
        "D",
        "D-",
    ]


def test_mixed_grades_preserve_order_and_length():
    grades = [4.0, 3.9, 3.4, 3.2, 2.9, 2.4, 2.2, 1.9, 1.4, 1.2, 0.9, 0.1, 0.0]
    result = numerical_letter_grade(grades)
    assert result == [
        "A+",
        "A",
        "A-",
        "B+",
        "B",
        "B-",
        "C+",
        "C",
        "C-",
        "D+",
        "D",
        "D-",
        "E",
    ]
    assert len(result) == len(grades)


def test_input_list_is_not_mutated():
    grades = [4.0, 2.5, 0.0]
    snapshot = list(grades)
    numerical_letter_grade(grades)
    assert grades == snapshot


def test_returns_new_list_each_call():
    first = numerical_letter_grade([4.0])
    second = numerical_letter_grade([4.0])
    assert first == second
    assert first is not second


def test_accepts_tuple_and_generator_inputs():
    assert numerical_letter_grade((4.0, 0.0)) == ["A+", "E"]
    assert numerical_letter_grade(g for g in [3.5, 1.5]) == ["A-", "C-"]
