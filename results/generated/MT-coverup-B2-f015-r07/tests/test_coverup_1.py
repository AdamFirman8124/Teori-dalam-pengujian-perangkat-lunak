# file: project/f015/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f015 import string_sequence


def test_string_sequence_zero_executes_line_3():
    """n = 0: the comprehension loop runs exactly once (0)."""
    result = string_sequence(0)
    assert result == "0"
    assert isinstance(result, str)


def test_string_sequence_positive_executes_line_3():
    """n > 0: the comprehension loop runs multiple times."""
    result = string_sequence(5)
    assert result == "0 1 2 3 4 5"
    assert result.split(" ") == ["0", "1", "2", "3", "4", "5"]


def test_string_sequence_negative_skips_loop_body():
    """n = -1: range(0) is empty, so the comprehension body never runs,
    covering the branch where the loop is not entered."""
    result = string_sequence(-1)
    assert result == ""


def test_string_sequence_large_n():
    """Sanity check on a larger input to confirm full sequence."""
    result = string_sequence(10)
    assert result == " ".join(str(x) for x in range(11))
    assert len(result.split(" ")) == 11
