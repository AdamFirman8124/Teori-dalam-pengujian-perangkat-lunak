# file: project/f081/__init__.py:1-33
# asked: {"lines": [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 32, 33], "branches": [[6, 7], [6, 33], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 15], [15, 16], [15, 17], [17, 18], [17, 19], [19, 20], [19, 21], [21, 22], [21, 23], [23, 24], [23, 25], [25, 26], [25, 27], [27, 28], [27, 29], [29, 30], [29, 32]]}
# gained: {"lines": [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 32, 33], "branches": [[6, 7], [6, 33], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 15], [15, 16], [15, 17], [17, 18], [17, 19], [19, 20], [19, 21], [21, 22], [21, 23], [23, 24], [23, 25], [25, 26], [25, 27], [27, 28], [27, 29], [29, 30], [29, 32]]}

from f081 import numerical_letter_grade


def test_numerical_letter_grade_all_branches():
    grades = [4.0, 3.9, 3.75, 3.5, 3.2, 2.9, 2.5, 2.1, 1.9, 1.5, 1.15, 0.9, 0.5, 0.0, -1.0]
    expected = ["A+", "A", "A", "A-", "B+", "B", "B-", "C+", "C", "C-",
                "D+", "D", "D-", "E", "E"]
    result = numerical_letter_grade(grades)
    assert result == expected
    assert len(result) == len(grades)


def test_numerical_letter_grade_empty():
    assert numerical_letter_grade([]) == []


def test_numerical_letter_grade_boundaries():
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


def test_numerical_letter_grade_does_not_mutate_input():
    grades = [4.0, 0.0]
    numerical_letter_grade(grades)
    assert grades == [4.0, 0.0]
