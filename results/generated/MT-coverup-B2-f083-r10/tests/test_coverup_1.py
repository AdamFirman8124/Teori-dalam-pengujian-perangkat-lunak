# file: project/f083/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}

import f083
from f083 import starts_one_ends


def test_starts_one_ends_n_equals_one():
    """Covers the 'if n == 1' branch (lines 3-4): a 1-digit number is 1."""
    assert starts_one_ends(1) == 1


def test_starts_one_ends_n_greater_than_one():
    """Covers the fall-through branch (line 5): 18 * 10**(n-2)."""
    assert starts_one_ends(2) == 18
    assert starts_one_ends(3) == 180
    assert starts_one_ends(5) == 18000


def test_starts_one_ends_matches_formula():
    """Verify the general formula for several n > 1 values."""
    for n in range(2, 8):
        assert starts_one_ends(n) == 18 * (10 ** (n - 2))
