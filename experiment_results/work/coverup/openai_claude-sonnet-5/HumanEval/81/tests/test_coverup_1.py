# file: script_81.py:1-56
# asked: {"lines": [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 55, 56], "branches": [[29, 30], [29, 56], [30, 31], [30, 32], [32, 33], [32, 34], [34, 35], [34, 36], [36, 37], [36, 38], [38, 39], [38, 40], [40, 41], [40, 42], [42, 43], [42, 44], [44, 45], [44, 46], [46, 47], [46, 48], [48, 49], [48, 50], [50, 51], [50, 52], [52, 53], [52, 55]]}
# gained: {"lines": [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 55, 56], "branches": [[29, 30], [29, 56], [30, 31], [30, 32], [32, 33], [32, 34], [34, 35], [34, 36], [36, 37], [36, 38], [38, 39], [38, 40], [40, 41], [40, 42], [42, 43], [42, 44], [44, 45], [44, 46], [46, 47], [46, 48], [48, 49], [48, 50], [50, 51], [50, 52], [52, 53], [52, 55]]}

import pytest
from script_81 import numerical_letter_grade


def test_empty_list():
    """Test with empty list."""
    assert numerical_letter_grade([]) == []


def test_single_grade_a_plus():
    """Test exact 4.0 GPA."""
    assert numerical_letter_grade([4.0]) == ["A+"]


def test_single_grade_a():
    """Test GPA > 3.7."""
    assert numerical_letter_grade([3.8]) == ["A"]


def test_single_grade_a_minus():
    """Test GPA > 3.3."""
    assert numerical_letter_grade([3.4]) == ["A-"]


def test_single_grade_b_plus():
    """Test GPA > 3.0."""
    assert numerical_letter_grade([3.1]) == ["B+"]


def test_single_grade_b():
    """Test GPA > 2.7."""
    assert numerical_letter_grade([2.8]) == ["B"]


def test_single_grade_b_minus():
    """Test GPA > 2.3."""
    assert numerical_letter_grade([2.4]) == ["B-"]


def test_single_grade_c_plus():
    """Test GPA > 2.0."""
    assert numerical_letter_grade([2.1]) == ["C+"]


def test_single_grade_c():
    """Test GPA > 1.7."""
    assert numerical_letter_grade([1.8]) == ["C"]


def test_single_grade_c_minus():
    """Test GPA > 1.3."""
    assert numerical_letter_grade([1.4]) == ["C-"]


def test_single_grade_d_plus():
    """Test GPA > 1.0."""
    assert numerical_letter_grade([1.1]) == ["D+"]


def test_single_grade_d():
    """Test GPA > 0.7."""
    assert numerical_letter_grade([0.8]) == ["D"]


def test_single_grade_d_minus():
    """Test GPA > 0.0."""
    assert numerical_letter_grade([0.1]) == ["D-"]


def test_single_grade_e():
    """Test GPA == 0.0."""
    assert numerical_letter_grade([0.0]) == ["E"]


def test_multiple_grades():
    """Test with multiple grades covering all branches."""
    result = numerical_letter_grade([4.0, 3.8, 3.4, 3.1, 2.8, 2.4, 2.1, 1.8, 1.4, 1.1, 0.8, 0.1, 0.0])
    expected = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"]
    assert result == expected


def test_example_from_docstring():
    """Test the example from the docstring."""
    assert numerical_letter_grade([4.0, 3.0, 1.7, 2.0, 3.5]) == ["A+", "B", "C-", "C", "A-"]


def test_boundary_values():
    """Test exact boundary values."""
    result = numerical_letter_grade([4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0])
    expected = ["A+", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"]
    assert result == expected
