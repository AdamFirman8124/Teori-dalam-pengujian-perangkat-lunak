# file: project/f076/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}

import pytest

from f076 import is_simple_power


@pytest.mark.parametrize(
    ("x", "n", "expected"),
    [
        (1, 1, True),
        (2, 1, False),
        (1, 2, True),
        (8, 2, True),
        (3, 2, False),
    ],
)
def test_is_simple_power(x, n, expected):
    assert is_simple_power(x, n) is expected
