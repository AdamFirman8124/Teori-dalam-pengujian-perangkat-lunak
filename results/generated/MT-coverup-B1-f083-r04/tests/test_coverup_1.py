# file: project/f083/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}

import pytest

from f083 import starts_one_ends


def test_starts_one_ends_n_equals_one():
    """Covers lines 3-4: the n == 1 branch."""
    assert starts_one_ends(1) == 1


def test_starts_one_ends_n_greater_than_one():
    """Covers line 5: the general formula branch."""
    assert starts_one_ends(2) == 18
    assert starts_one_ends(3) == 180
    assert starts_one_ends(5) == 18000
