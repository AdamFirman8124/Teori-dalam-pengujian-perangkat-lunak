# file: project/f150/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 10], "branches": [[3, 4], [3, 5], [5, 6], [5, 10], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 10], "branches": [[3, 4], [3, 5], [5, 6], [5, 10], [6, 5], [6, 7]]}

import pytest

from f150 import x_or_y


def test_x_or_y_n_equals_one_returns_y():
    """Covers line 3 (if n == 1) and line 4 (return y)."""
    assert x_or_y(1, "prime", "not-prime") == "not-prime"


def test_x_or_y_composite_returns_y():
    """Covers lines 5-7: loop body finds a divisor and returns y."""
    assert x_or_y(4, "prime", "not-prime") == "not-prime"
    assert x_or_y(9, "prime", "not-prime") == "not-prime"
    assert x_or_y(15, "prime", "not-prime") == "not-prime"


def test_x_or_y_prime_returns_x():
    """Covers line 5 loop completing and line 10 (for-else: return x)."""
    assert x_or_y(2, "prime", "not-prime") == "prime"
    assert x_or_y(3, "prime", "not-prime") == "prime"
    assert x_or_y(7, "prime", "not-prime") == "prime"
    assert x_or_y(13, "prime", "not-prime") == "prime"
