# file: project/f025/__init__.py:4-18
# asked: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 17, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14], [16, 17], [16, 18]]}
# gained: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 17, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14], [16, 17], [16, 18]]}

import pytest

from f025 import factorize


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (1, []),
        (8, [2, 2, 2]),
        (12, [2, 2, 3]),
        (13, [13]),
    ],
)
def test_factorize(number, expected):
    assert factorize(number) == expected
