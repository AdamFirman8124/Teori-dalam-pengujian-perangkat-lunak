# file: project/f032/__init__.py:9-21
# asked: {"lines": [11, 12, 13, 14, 15, 16, 17, 18, 20, 21], "branches": [[12, 13], [12, 15], [15, 16], [15, 21], [17, 18], [17, 20]]}
# gained: {"lines": [11, 12, 13, 14, 15, 16, 17, 18, 20, 21], "branches": [[12, 13], [12, 15], [15, 16], [15, 21], [17, 18], [17, 20]]}

import pytest

from f032 import find_zero, poly


def test_find_zero_uses_both_bisection_branches():
    result = find_zero([0.0, 1.0])

    assert -1e-10 <= result <= 0.0
    assert abs(poly([0.0, 1.0], result)) <= 1e-10


def test_find_zero_expands_initial_interval():
    result = find_zero([-2.0, 1.0])

    assert result == pytest.approx(2.0, abs=1e-10)
    assert abs(poly([-2.0, 1.0], result)) <= 1e-10
