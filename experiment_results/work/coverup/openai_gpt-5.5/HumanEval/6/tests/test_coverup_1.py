# file: script_6.py:4-24
# asked: {"lines": [12, 13, 14, 15, 16, 17, 18, 20, 22, 24], "branches": [[15, 16], [15, 22], [16, 17], [16, 20]]}
# gained: {"lines": [12, 13, 14, 15, 16, 17, 18, 20, 22, 24], "branches": [[15, 16], [15, 22], [16, 17], [16, 20]]}

import pytest

from script_6 import parse_nested_parens


def test_parse_nested_parens_multiple_groups_and_depths():
    assert parse_nested_parens("(()()) ((())) () ((())()())") == [2, 3, 1, 3]


def test_parse_nested_parens_ignores_extra_spaces_and_handles_flat_group():
    assert parse_nested_parens("  ()   (())  ") == [1, 2]
