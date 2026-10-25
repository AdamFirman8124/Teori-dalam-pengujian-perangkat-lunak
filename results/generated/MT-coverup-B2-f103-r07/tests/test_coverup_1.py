# file: project/f103/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}

from f103 import rounded_avg


def test_rounded_avg_m_less_than_n_returns_minus_one():
    assert rounded_avg(5, 3) == -1
    assert rounded_avg(10, 0) == -1
    assert rounded_avg(1, -1) == -1


def test_rounded_avg_normal_range():
    # sum(1..5) = 15, avg = 3.0, round = 3, bin = '0b11'
    assert rounded_avg(1, 5) == "0b11"
    # sum(1..3) = 6, avg = 2.0, round = 2, bin = '0b10'
    assert rounded_avg(1, 3) == "0b10"
    assert isinstance(rounded_avg(1, 5), str)


def test_rounded_avg_single_element():
    # n == m: loop executes exactly once
    assert rounded_avg(1, 1) == "0b1"
    assert rounded_avg(0, 0) == "0b0"
    assert rounded_avg(7, 7) == "0b111"


def test_rounded_avg_rounding():
    # sum(1..4) = 10, avg = 2.5, round = 2 (banker's rounding)
    assert rounded_avg(1, 4) == "0b10"
    # sum(1..6) = 21, avg = 3.5, round = 4
    assert rounded_avg(1, 6) == "0b100"
    # sum(1..2) = 3, avg = 1.5, round = 2
    assert rounded_avg(1, 2) == "0b10"


def test_rounded_avg_negative_range():
    # sum(-5..-1) = -15, avg = -3.0, round = -3, bin = '-0b11'
    assert rounded_avg(-5, -1) == "-0b11"
    # sum(-2..2) = 0, avg = 0.0
    assert rounded_avg(-2, 2) == "0b0"
