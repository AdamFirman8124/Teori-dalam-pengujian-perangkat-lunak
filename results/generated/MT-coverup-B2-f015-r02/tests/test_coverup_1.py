# file: project/f015/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f015 import string_sequence


def test_string_sequence_returns_inclusive_sequence():
    assert string_sequence(3) == "0 1 2 3"


def test_string_sequence_returns_zero_for_zero():
    assert string_sequence(0) == "0"
