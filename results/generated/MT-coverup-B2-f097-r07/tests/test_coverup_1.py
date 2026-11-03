# file: project/f097/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f097 import multiply


def test_multiply_positive_single_digits():
    # Executes line 3 with simple positive operands.
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0


def test_multiply_negative_operands():
    # Python's % with a positive modulus already yields non-negative
    # results (e.g. -3 % 10 == 7), so abs() is applied to values >= 0.
    assert multiply(-3, 4) == 28       # abs(-3 % 10) * abs(4 % 10)  = 7 * 4
    assert multiply(4, -3) == 28       # abs(4 % 10) * abs(-3 % 10)  = 4 * 7
    assert multiply(-13, -24) == 42    # abs(7) * abs(6)             = 42


def test_multiply_multi_digit_operands():
    # Operands >= 10 exercise the modulo reduction.
    assert multiply(13, 24) == 12      # 3 * 4
    assert multiply(19, 29) == 81      # 9 * 9
    assert multiply(10, 10) == 0       # 0 * 0
