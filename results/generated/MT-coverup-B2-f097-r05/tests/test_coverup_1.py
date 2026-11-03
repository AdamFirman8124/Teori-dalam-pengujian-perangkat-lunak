# file: project/f097/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f097 import multiply


def test_multiply_return_line_executes():
    """Exercise line 3 (the return statement) of f097.multiply.

    The function is pure (no I/O, no global state), so no monkeypatching
    or cleanup is required; calling it is sufficient to execute line 3.
    """
    # Positive single-digit inputs
    assert multiply(3, 4) == 12

    # Multi-digit inputs: only the last digits contribute
    assert multiply(13, 24) == 12
    assert multiply(17, 25) == 35

    # Negative inputs: Python's % yields a non-negative remainder for a
    # positive divisor, so abs() leaves it unchanged (e.g. -3 % 10 == 7)
    assert multiply(-3, 4) == 28
    assert multiply(-3, -4) == 42

    # Zero results
    assert multiply(0, 5) == 0
    assert multiply(10, 7) == 0
