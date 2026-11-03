# file: project/f015/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f015 import string_sequence


def test_string_sequence_zero():
    """n = 0: range(1) yields a single element '0'."""
    assert string_sequence(0) == "0"


def test_string_sequence_positive():
    """n > 0: numbers 0..n joined by spaces."""
    assert string_sequence(5) == "0 1 2 3 4 5"
    assert string_sequence(1) == "0 1"


def test_string_sequence_negative():
    """n < 0: range(n + 1) is empty, so the join yields an empty string."""
    assert string_sequence(-1) == ""
    assert string_sequence(-10) == ""
