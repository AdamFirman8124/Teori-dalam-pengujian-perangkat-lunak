# file: project/f058/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [6, 5], [6, 7]]}

import pytest

from f058 import common


def _assert_postconditions(result, l1, l2):
    assert isinstance(result, list)
    assert result == sorted(result)
    assert len(result) == len(set(result))
    assert all(e in l1 and e in l2 for e in result)


def test_common_basic_overlap():
    l1, l2 = [1, 2, 3], [2, 3, 4]
    result = common(l1, l2)
    assert result == [2, 3]
    _assert_postconditions(result, l1, l2)


def test_common_no_overlap_covers_false_branch():
    l1, l2 = [1, 2], [3, 4]
    result = common(l1, l2)
    assert result == []
    _assert_postconditions(result, l1, l2)


def test_common_empty_first_list_skips_outer_loop():
    l1, l2 = [], [1, 2, 3]
    result = common(l1, l2)
    assert result == []
    _assert_postconditions(result, l1, l2)


def test_common_empty_second_list_skips_inner_loop():
    l1, l2 = [1, 2, 3], []
    result = common(l1, l2)
    assert result == []
    _assert_postconditions(result, l1, l2)


def test_common_both_empty():
    result = common([], [])
    assert result == []


def test_common_duplicates_are_deduplicated():
    l1, l2 = [1, 1, 2, 2], [1, 2, 2, 3]
    result = common(l1, l2)
    assert result == [1, 2]
    _assert_postconditions(result, l1, l2)


def test_common_output_is_sorted_regardless_of_input_order():
    l1, l2 = [3, 1, 2], [2, 3, 1]
    result = common(l1, l2)
    assert result == [1, 2, 3]
    _assert_postconditions(result, l1, l2)


def test_common_with_strings():
    l1, l2 = ["b", "a", "c"], ["c", "a", "z"]
    result = common(l1, l2)
    assert result == ["a", "c"]
    _assert_postconditions(result, l1, l2)


def test_common_does_not_mutate_inputs():
    l1, l2 = [1, 2, 3], [2, 3, 4]
    l1_copy, l2_copy = list(l1), list(l2)
    common(l1, l2)
    assert l1 == l1_copy
    assert l2 == l2_copy


@pytest.mark.parametrize(
    "l1, l2, expected",
    [
        ([1], [1], [1]),
        ([1], [2], []),
        ([1, 2, 3], [3, 2, 1], [1, 2, 3]),
        ([0, -1, 5], [-1, 0], [-1, 0]),
    ],
)
def test_common_parametrized(l1, l2, expected):
    result = common(l1, l2)
    assert result == expected
    _assert_postconditions(result, l1, l2)
