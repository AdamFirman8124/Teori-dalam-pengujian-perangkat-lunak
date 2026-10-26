# file: project/f103/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}

from f103 import rounded_avg


def test_rounded_avg_m_less_than_n_returns_minus_one():
    assert rounded_avg(5, 1) == -1
    assert rounded_avg(10, 5) == -1
    assert rounded_avg(0, -1) == -1


def test_rounded_avg_single_element_range():
    result = rounded_avg(5, 5)
    assert result == bin(5)
    assert result == "0b101"
    assert isinstance(result, str)


def test_rounded_avg_typical_range():
    result = rounded_avg(1, 5)
    # sum(1..5) = 15, average = 3.0, round = 3
    assert result == bin(3)
    assert result == "0b11"
    assert isinstance(result, str)


def test_rounded_avg_rounding_and_zero():
    # sum(1..4) = 10, average = 2.5, round() -> 2 (banker's rounding)
    assert rounded_avg(1, 4) == "0b10"
    # sum(1..6) = 21, average = 3.5, round() -> 4
    assert rounded_avg(1, 6) == "0b100"
    assert rounded_avg(0, 0) == "0b0"


def test_rounded_avg_negative_range():
    # sum(-3..-1) = -6, average = -2.0, round = -2
    assert rounded_avg(-3, -1) == bin(-2)
    assert rounded_avg(-3, -1) == "-0b10"
