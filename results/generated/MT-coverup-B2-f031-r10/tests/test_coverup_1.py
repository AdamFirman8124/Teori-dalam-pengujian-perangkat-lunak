# file: project/f031/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8], [6, 5], [6, 7]]}

import pytest

from f031 import is_prime


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (-1, False),
        (1, False),
        (2, True),
        (4, False),
        (5, True),
    ],
)
def test_is_prime_covers_all_branches(n, expected):
    assert is_prime(n) is expected
