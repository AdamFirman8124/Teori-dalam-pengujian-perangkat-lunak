# file: project/f110/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 8], [6, 5], [6, 7], [8, 9], [8, 11], [9, 8], [9, 10], [11, 12], [11, 13]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 8], [6, 5], [6, 7], [8, 9], [8, 11], [9, 8], [9, 10], [11, 12], [11, 13]]}

import pytest

from f110 import exchange


@pytest.mark.parametrize(
    ("lst1", "lst2", "expected"),
    [
        ([1, 2, 3], [2, 4, 5], "YES"),
        ([1, 3, 5], [2, 7, 9], "NO"),
    ],
)
def test_exchange(lst1, lst2, expected):
    original_lst1 = lst1.copy()
    original_lst2 = lst2.copy()

    assert exchange(lst1, lst2) == expected
    assert lst1 == original_lst1
    assert lst2 == original_lst2
