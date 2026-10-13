# file: script_6.py:4-24
# asked: {"lines": [12, 13, 14, 15, 16, 17, 18, 20, 22, 24], "branches": [[15, 16], [15, 22], [16, 17], [16, 20]]}
# gained: {"lines": [12, 13, 14, 15, 16, 17, 18, 20, 22, 24], "branches": [[15, 16], [15, 22], [16, 17], [16, 20]]}

import script_6


def test_parse_nested_parens_covers_both_branches_and_filters_empty_groups():
    assert script_6.parse_nested_parens("(()()) ((())) () ((())()())") == [2, 3, 1, 3]
    assert script_6.parse_nested_parens("  ()   ") == [1]
    assert script_6.parse_nested_parens("") == []
