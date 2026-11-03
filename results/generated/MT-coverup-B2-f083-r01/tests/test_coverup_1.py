# file: project/f083/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}

import pytest

from f083 import starts_one_ends


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        # Covers lines 3-4: the `n == 1` branch.
        (1, 1),
        # Covers line 5: the general branch `18 * 10 ** (n - 2)`.
        (2, 18),
        (3, 180),
        (5, 18000),
    ],
)
def test_starts_one_ends(n, expected):
    """starts_one_ends returns 1 for n == 1 and 18 * 10**(n-2) otherwise."""
    assert starts_one_ends(n) == expected
