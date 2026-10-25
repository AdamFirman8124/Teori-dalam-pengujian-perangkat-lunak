# file: project/f132/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[5, 6], [5, 10], [6, 7], [6, 9], [14, 15], [14, 18], [15, 14], [15, 16]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[5, 6], [5, 10], [6, 7], [6, 9], [14, 15], [14, 18], [15, 14], [15, 16]]}

import pytest

from f132 import is_nested


def test_is_nested_empty_string():
    # No brackets at all: loops do not run, cnt stays 0.
    assert is_nested("") is False


def test_is_nested_single_pair():
    # "[]" -> one matched pair, cnt == 1, which is not >= 2.
    assert is_nested("[]") is False


def test_is_nested_nested_pair():
    # "[[]]" -> two matched pairs, cnt == 2 -> True.
    assert is_nested("[[]]") is True


def test_is_nested_reversed_brackets():
    # "][" -> opening index 1 is never < closing index 0, cnt == 0.
    assert is_nested("][") is False


def test_is_nested_only_opening_brackets():
    # "[[[[" -> closing list empty, so the `i < l` guard is False
    # (short-circuit branch), cnt == 0.
    assert is_nested("[[[[") is False


def test_is_nested_multiple_groups():
    # "[[]][[]]" -> four matched pairs -> True.
    assert is_nested("[[]][[]]") is True


def test_is_nested_mixed_unmatched():
    # "[[]][]" -> three matched pairs -> True.
    assert is_nested("[[]][]") is True
