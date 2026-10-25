# file: project/pytutils/path.py:4-6
# asked: {"lines": [5, 6], "branches": [[5, 0], [5, 6]]}
# gained: {"lines": [5, 6], "branches": [[5, 0], [5, 6]]}

import os

from pytutils.path import join_each


def test_join_each_joins_every_path():
    parent = os.path.join("root", "parent")
    children = ["first.txt", os.path.join("nested", "second.txt")]

    assert list(join_each(parent, children)) == [
        os.path.join(parent, child) for child in children
    ]


def test_join_each_with_empty_iterable():
    assert list(join_each("parent", [])) == []
