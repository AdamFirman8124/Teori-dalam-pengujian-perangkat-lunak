# file: project/f083/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}

import pytest

from f083 import starts_one_ends


def test_starts_one_ends_base_case():
    """Covers lines 3-4: the n == 1 branch."""
    assert starts_one_ends(1) == 1


@pytest.mark.parametrize(
    "n, expected",
    [
        (2, 18),
        (3, 180),
        (5, 18_000),
        (10, 18 * 10 ** 8),
    ],
)
def test_starts_one_ends_general_case(n, expected):
    """Covers line 5: the n != 1 branch."""
    assert starts_one_ends(n) == expected
