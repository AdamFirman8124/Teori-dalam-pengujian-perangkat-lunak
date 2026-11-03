# file: project/f083/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}

import pytest

from f083 import starts_one_ends


def test_starts_one_ends_with_n_equal_one():
    # Covers line 3 (the `if` condition, true branch) and line 4.
    result = starts_one_ends(1)
    # Postcondition: a 1-digit number is trivially counted as 1.
    assert result == 1


@pytest.mark.parametrize(
    "n, expected",
    [
        (2, 18),
        (3, 180),
        (4, 1800),
        (10, 18 * 10 ** 8),
    ],
)
def test_starts_one_ends_with_n_greater_than_one(n, expected):
    # Covers line 3 (the `if` condition, false branch) and line 5.
    result = starts_one_ends(n)
    # Postcondition: result follows the closed-form formula 18 * 10**(n - 2).
    assert result == 18 * 10 ** (n - 2)
    assert result == expected
