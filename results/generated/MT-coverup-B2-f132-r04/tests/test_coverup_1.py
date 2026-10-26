# file: project/f132/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[5, 6], [5, 10], [6, 7], [6, 9], [14, 15], [14, 18], [15, 14], [15, 16]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[5, 6], [5, 10], [6, 7], [6, 9], [14, 15], [14, 18], [15, 14], [15, 16]]}

from f132 import is_nested


def test_is_nested_true_when_two_nested_pairs():
    # "[[]]": opening at 0,1; closing at 2,3 -> both openings match -> cnt == 2
    assert is_nested("[[]]") is True


def test_is_nested_false_single_pair():
    # "[]": only one match -> cnt == 1
    assert is_nested("[]") is False


def test_is_nested_false_no_match_for_second_opening():
    # "[][]": opening [0,2], closing reversed [3,1]
    # idx=0 matches (cnt=1, i=1); idx=2: i < l but 2 < 1 is False -> exercises
    # the False branch of "idx < closing_bracket_index[i]"
    assert is_nested("[][]") is False


def test_is_nested_false_closing_list_exhausted():
    # "[[]": opening [0,1], closing reversed [2]
    # idx=0 matches (cnt=1, i=1); idx=1: i < l is False -> exercises the
    # False branch of "i < l"
    assert is_nested("[[]") is False


def test_is_nested_empty_string():
    # No brackets at all: loops never run, cnt == 0
    assert is_nested("") is False
