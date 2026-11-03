# file: project/f097/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f097 import multiply


def test_multiply_positive_and_wrapped_values():
    # Calling multiply executes the return statement on line 3.
    # Plain positive single-digit operands: 3 * 4 == 12.
    assert multiply(3, 4) == 12
    # Only the last digit of each operand contributes (12 -> 2, 25 -> 5).
    assert multiply(12, 25) == 10
    # A zero operand forces a zero product.
    assert multiply(0, 7) == 0


def test_multiply_negative_values():
    # Python's % with a positive modulus yields non-negative results:
    # (-3 % 10) == 7 and (-8 % 10) == 2, so abs() leaves them unchanged.
    assert multiply(-3, -8) == 14
    # (-7 % 10) == 3 -> 3 * 4 == 12.
    assert multiply(-7, 4) == 12
