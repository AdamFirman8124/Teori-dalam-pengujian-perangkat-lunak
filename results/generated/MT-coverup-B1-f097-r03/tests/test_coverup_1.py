# file: project/f097/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f097 import multiply


def test_multiply_basic_positive():
    assert multiply(148, 412) == 16


def test_multiply_single_digits():
    assert multiply(2, 3) == 6
    assert multiply(5, 5) == 25
    assert multiply(9, 9) == 81


def test_multiply_zero_unit():
    assert multiply(10, 20) == 0
    assert multiply(0, 5) == 0
    assert multiply(0, 0) == 0
    assert multiply(100, 7) == 0


def test_multiply_negative_numbers():
    # Python semantics: -15 % 10 == 5, -14 % 10 == 6
    assert multiply(14, -15) == 4 * 5
    assert multiply(-14, 15) == 6 * 5
    assert multiply(-14, -15) == 6 * 5
    assert multiply(-148, -412) == 2 * 8


def test_multiply_general_postcondition():
    cases = [(148, 412), (19, 28), (-19, 28), (19, -28), (-19, -28), (0, 0), (10, 10), (7, 13)]
    for a, b in cases:
        expected = abs(a % 10) * abs(b % 10)
        assert multiply(a, b) == expected
