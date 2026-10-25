# file: project/f032/__init__.py:9-21
# asked: {"lines": [11, 12, 13, 14, 15, 16, 17, 18, 20, 21], "branches": [[12, 13], [12, 15], [15, 16], [15, 21], [17, 18], [17, 20]]}
# gained: {"lines": [11, 12, 13, 14, 15, 16, 17, 18, 20, 21], "branches": [[12, 13], [12, 15], [15, 16], [15, 21], [17, 18], [17, 20]]}

from f032 import find_zero


def test_find_zero_expands_initial_interval():
    coefficients = [-2.0, 1.0]

    result = find_zero(coefficients)

    assert 0.0 <= 2.0 - result <= 1e-10
    assert coefficients == [-2.0, 1.0]


def test_find_zero_takes_else_branch_when_center_is_root():
    coefficients = [0.0, 1.0]

    result = find_zero(coefficients)

    assert -1e-10 <= result <= 0.0
    assert coefficients == [0.0, 1.0]
