# file: project/pytutils/path.py:4-6
# asked: {"lines": [5, 6], "branches": [[5, 0], [5, 6]]}
# gained: {"lines": [5, 6], "branches": [[5, 0], [5, 6]]}

import os
import pytest
from pytutils.path import join_each

def test_join_each_multiple_elements():
 parent = "/foo"
 iterable = ["bar", "baz", "qux"]
 result = list(join_each(parent, iterable))
 assert result == ["/foo/bar", "/foo/baz", "/foo/qux"]

def test_join_each_single_element():
 parent = "relative"
 iterable = ["file.txt"]
 result = list(join_each(parent, iterable))
 assert result == ["relative/file.txt"]

def test_join_each_with_tuple():
 parent = "/root"
 iterable = ("sub1", "sub2")
 result = list(join_each(parent, iterable))
 assert result == ["/root/sub1", "/root/sub2"]

def test_join_each_with_generator():
 parent = "/gen"
 iterable = (f"item{i}" for i in range(3))
 result = list(join_each(parent, iterable))
 assert result == ["/gen/item0", "/gen/item1", "/gen/item2"]

def test_join_each_mixed_paths():
 parent = "/base/dir"
 iterable = ["sub/file.txt", "another", "last/"]
 result = list(join_each(parent, iterable))
 expected = [os.path.join(parent, p) for p in iterable]
 assert result == expected