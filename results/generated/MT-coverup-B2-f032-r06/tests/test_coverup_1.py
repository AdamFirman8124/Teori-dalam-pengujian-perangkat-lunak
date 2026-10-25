# file: project/f032/__init__.py:9-21
# asked: {"lines": [11, 12, 13, 14, 15, 16, 17, 18, 20, 21], "branches": [[12, 13], [12, 15], [15, 16], [15, 21], [17, 18], [17, 20]]}
# gained: {"lines": [11, 12, 13, 14, 15, 16, 17, 18, 20, 21], "branches": [[12, 13], [12, 15], [15, 16], [15, 21], [17, 18], [17, 20]]}

import pytest

from f032 import find_zero


def test_find_zero_expands_interval_and_exercises_bisection_branches():
    coefficients = [-3.0, 1.0]

    result = find_zero(coefficients)

    assert result <= 3.0
    assert result == pytest.approx(3.0, abs=1e-10)
