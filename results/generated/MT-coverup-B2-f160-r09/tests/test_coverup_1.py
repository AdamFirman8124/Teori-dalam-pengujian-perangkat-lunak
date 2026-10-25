# file: project/f160/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}

import pytest

from f160 import do_algebra


@pytest.mark.parametrize(
    ("operators", "operands", "expected"),
    [
        ([], [7], 7),
        (["+", "*"], [2, 3, 4], 14),
    ],
)
def test_do_algebra(operators, operands, expected):
    assert do_algebra(operators, operands) == expected
