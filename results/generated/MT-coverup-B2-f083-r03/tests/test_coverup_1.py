# file: project/f083/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}

import pytest

from f083 import starts_one_ends


def test_starts_one_ends_base_case_hits_if_and_return_one():
    """n == 1 must take the true branch (lines 3-4) and return 1."""
    assert starts_one_ends(1) == 1


@pytest.mark.parametrize("n, expected", [
    (2, 18),          # 18 * 10**0
    (3, 180),         # 18 * 10**1
    (5, 18000),       # 18 * 10**3
])
def test_starts_one_ends_general_case_hits_final_return(n, expected):
    """n != 1 must skip the if-branch and execute line 5."""
    assert starts_one_ends(n) == expected
