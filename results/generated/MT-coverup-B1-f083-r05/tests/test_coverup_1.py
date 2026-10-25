# file: project/f083/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}

import pytest

from f083 import starts_one_ends


def test_starts_one_ends_single_digit():
    # n == 1 branch: only the number 1 itself
    assert starts_one_ends(1) == 1


@pytest.mark.parametrize(
    "n, expected",
    [
        (2, 18),
        (3, 180),
        (4, 1800),
        (5, 18000),
    ],
)
def test_starts_one_ends_multi_digit(n, expected):
    # n > 1 branch: 18 * 10 ** (n - 2)
    assert starts_one_ends(n) == expected


def test_starts_one_ends_matches_formula():
    for n in range(2, 8):
        assert starts_one_ends(n) == 18 * (10 ** (n - 2))


def test_starts_one_ends_returns_int():
    assert isinstance(starts_one_ends(1), int)
    assert isinstance(starts_one_ends(3), int)
