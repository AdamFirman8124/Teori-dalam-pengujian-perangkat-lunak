# file: project/f086/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f086 import anti_shuffle


def test_anti_shuffle_sorts_each_word_and_preserves_spaces():
    assert anti_shuffle("dcba  zy") == "abcd  yz"
    assert anti_shuffle("") == ""
