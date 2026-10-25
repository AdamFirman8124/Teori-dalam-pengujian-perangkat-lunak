# file: project/f086/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f086 import anti_shuffle


def test_anti_shuffle_sorts_each_word_and_preserves_spaces():
    assert anti_shuffle("hello world") == "ehllo dlorw"
    assert anti_shuffle("ba  dc") == "ab  cd"
