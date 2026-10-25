# file: project/pytutils/path.py:4-6
# asked: {"lines": [5, 6], "branches": [[5, 0], [5, 6]]}
# gained: {"lines": [5, 6], "branches": [[5, 0], [5, 6]]}

import os
from pytutils.path import join_each


def test_join_each_with_items():
    parent = "/parent"
    items = ["a", "b", "c"]
    expected = [os.path.join(parent, p) for p in items]
    result = list(join_each(parent, items))
    assert result == expected
    assert result == ["/parent/a", "/parent/b", "/parent/c"]


def test_join_each_empty_iterable():
    result = list(join_each("/parent", []))
    assert result == []
