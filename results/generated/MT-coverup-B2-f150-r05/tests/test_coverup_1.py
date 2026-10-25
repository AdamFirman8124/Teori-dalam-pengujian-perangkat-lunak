# file: project/f150/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 10], "branches": [[3, 4], [3, 5], [5, 6], [5, 10], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 10], "branches": [[3, 4], [3, 5], [5, 6], [5, 10], [6, 5], [6, 7]]}

import pytest

from f150 import x_or_y


@pytest.mark.parametrize(
    ("n", "x", "y", "expected"),
    [
        (1, "prime", "not prime", "not prime"),
        (4, "prime", "not prime", "not prime"),
        (5, "prime", "not prime", "prime"),
    ],
)
def test_x_or_y(n, x, y, expected):
    assert x_or_y(n, x, y) == expected
