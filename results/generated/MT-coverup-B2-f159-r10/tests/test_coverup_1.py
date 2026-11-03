# file: project/f159/__init__.py:1-6
# asked: {"lines": [3, 4, 6], "branches": [[3, 4], [3, 6]]}
# gained: {"lines": [3, 4, 6], "branches": [[3, 4], [3, 6]]}

import pytest

from f159 import eat


def test_eat_enough_remaining():
    """Covers the 'need <= remaining' branch (lines 3-4).

    Postconditions:
    - returns [number + need, remaining - need] when there is enough remaining.
    """
    result = eat(5, 2, 8)
    assert result == [7, 6]
    # Boundary case: need exactly equals remaining
    result_equal = eat(5, 8, 8)
    assert result_equal == [13, 0]
    # No side effects: calling again with same args gives same result
    assert eat(5, 2, 8) == [7, 6]


def test_eat_not_enough_remaining():
    """Covers the else branch (lines 5-6).

    Postconditions:
    - returns [number + remaining, 0] when remaining is insufficient.
    """
    result = eat(5, 8, 3)
    assert result == [8, 0]
    # Zero remaining case: all remaining is eaten
    result_zero = eat(10, 4, 0)
    assert result_zero == [10, 0]
    # No side effects: calling again with same args gives same result
    assert eat(5, 8, 3) == [8, 0]
