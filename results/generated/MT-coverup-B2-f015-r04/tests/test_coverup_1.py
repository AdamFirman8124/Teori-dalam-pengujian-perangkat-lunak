# file: project/f015/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f015 import string_sequence


def test_string_sequence_includes_zero_through_n():
    assert string_sequence(0) == "0"
    assert string_sequence(5) == "0 1 2 3 4 5"
