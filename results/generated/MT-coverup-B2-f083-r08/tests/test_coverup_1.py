# file: project/f083/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}

import pytest

from f083 import starts_one_ends


def test_starts_one_ends_n_equals_one():
    """Covers lines 3-4: the n == 1 branch returns 1."""
    assert starts_one_ends(1) == 1


def test_starts_one_ends_n_greater_than_one():
    """Covers line 5: the general formula 18 * 10 ** (n - 2)."""
    assert starts_one_ends(2) == 18
    assert starts_one_ends(3) == 180
    assert starts_one_ends(5) == 18 * 10 ** 3


def test_starts_one_ends_matches_formula():
    """Property check: for n > 1 the result equals 18 * 10 ** (n - 2)."""
    for n in range(2, 8):
        assert starts_one_ends(n) == 18 * 10 ** (n - 2)
