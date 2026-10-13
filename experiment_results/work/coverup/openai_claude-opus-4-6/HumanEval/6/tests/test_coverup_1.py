# file: script_6.py:4-24
# asked: {"lines": [12, 13, 14, 15, 16, 17, 18, 20, 22, 24], "branches": [[15, 16], [15, 22], [16, 17], [16, 20]]}
# gained: {"lines": [12, 13, 14, 15, 16, 17, 18, 20, 22, 24], "branches": [[15, 16], [15, 22], [16, 17], [16, 20]]}

from script_6 import parse_nested_parens


def test_docstring_example_covers_nested_definition_and_comprehension():
    result = parse_nested_parens('(()()) ((())) () ((())()())')
    assert result == [2, 3, 1, 3]
    assert isinstance(result, list)
    assert all(isinstance(d, int) for d in result)


def test_single_groups_cover_both_branches_of_char_check():
    # Opening paren branch: depth += 1 and max_depth updated
    # Closing paren branch: depth -= 1
    assert parse_nested_parens('()') == [1]
    assert parse_nested_parens('(())') == [2]
    assert parse_nested_parens('(((())))') == [4]


def test_sibling_groups_do_not_raise_max_depth():
    # Peaks that occur before later siblings must remain the reported max
    assert parse_nested_parens('(()()())') == [2]
    assert parse_nested_parens('()()()') == [1]
    assert parse_nested_parens('(()()) ((()))') == [2, 3]


def test_empty_string_is_filtered_by_comprehension_guard():
    # ''.split(' ') == [''], and the `if x` filter must drop it
    result = parse_nested_parens('')
    assert result == []
    assert len(result) == 0


def test_extra_and_leading_trailing_whitespace_groups_are_skipped():
    # Multiple consecutive spaces yield empty tokens that must be filtered out
    assert parse_nested_parens('()  ()   ((()))') == [1, 1, 3]
    assert parse_nested_parens('   ') == []
    assert parse_nested_parens(' () ') == [1]


def test_unbalanced_close_first_group_keeps_max_depth_at_zero():
    # ')(' drives depth negative then back to 0; max_depth must stay 0
    result = parse_nested_parens(')(')
    assert result == [0]
    assert len(result) == 1


def test_output_length_matches_number_of_non_empty_groups():
    s = '() ((())) ()'
    result = parse_nested_parens(s)
    expected_count = len([token for token in s.split(' ') if token])
    assert len(result) == expected_count == 3
    assert result == [1, 3, 1]
