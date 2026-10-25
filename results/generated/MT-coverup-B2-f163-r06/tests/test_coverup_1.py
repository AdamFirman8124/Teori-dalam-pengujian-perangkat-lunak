# file: project/f163/__init__.py:1-6
# asked: {"lines": [3, 4, 6], "branches": []}
# gained: {"lines": [3, 4, 6], "branches": []}

import pytest

from f163 import generate_integers


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (1, 10, [2, 4, 6, 8]),
        (10, 1, [2, 4, 6, 8]),
        (3, 7, [4, 6]),
        (7, 3, [4, 6]),
        (9, 10, []),
        (0, 1, []),
    ],
)
def test_generate_integers(a, b, expected):
    assert generate_integers(a, b) == expected
