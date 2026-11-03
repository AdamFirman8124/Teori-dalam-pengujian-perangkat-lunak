# file: project/f060/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f060 import sum_to_n


def test_sum_to_n_executes_return_line():
    # Calling the function executes line 3 (the return statement).
    # Verify postconditions for several inputs, including edge cases.
    assert sum_to_n(0) == 0          # sum(range(1)) == 0
    assert sum_to_n(1) == 1          # sum(range(2)) == 0 + 1
    assert sum_to_n(5) == 15         # 0 + 1 + 2 + 3 + 4 + 5
    assert sum_to_n(10) == 55        # triangular number T(10)
    assert sum_to_n(-1) == 0         # range(0) is empty -> sum is 0
    assert sum_to_n(100) == 5050     # Gauss' classic result
