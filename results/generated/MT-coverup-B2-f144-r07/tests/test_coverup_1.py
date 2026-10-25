# file: project/f144/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[7, 8], [7, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[7, 8], [7, 9]]}

import pytest

from f144 import simplify


@pytest.mark.parametrize(
    ("x", "n", "expected"),
    [
        ("1/2", "2/1", True),
        ("1/2", "1/1", False),
    ],
)
def test_simplify(x, n, expected):
    assert simplify(x, n) is expected
