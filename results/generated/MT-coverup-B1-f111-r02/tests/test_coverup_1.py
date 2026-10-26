# file: project/f111/__init__.py:1-15
# asked: {"lines": [3, 4, 5, 7, 8, 9, 10, 11, 12, 14, 15], "branches": [[7, 8], [7, 10], [8, 7], [8, 9], [10, 11], [10, 15], [11, 12], [11, 15], [12, 11], [12, 14]]}
# gained: {"lines": [3, 4, 5, 7, 8, 9, 10, 11, 12, 14, 15], "branches": [[7, 8], [7, 10], [8, 7], [8, 9], [10, 11], [10, 15], [11, 12], [11, 15], [12, 11], [12, 14]]}

from f111 import histogram


def test_empty_string_returns_empty_dict():
    result = histogram("")
    assert result == {}


def test_all_spaces_returns_empty_dict():
    result = histogram("   ")
    assert result == {}


def test_single_word():
    result = histogram("a")
    assert result == {"a": 1}


def test_single_winner():
    result = histogram("a b a")
    assert result == {"a": 2}


def test_tie_returns_all_winners():
    result = histogram("a b a b c")
    assert result == {"a": 2, "b": 2}


def test_repeated_token_covers_count_not_greater_branch():
    result = histogram("a a")
    assert result == {"a": 2}


def test_extra_spaces_with_majority_covers_empty_filtered_in_second_loop():
    # split -> ['a', 'a', '', 'b']: '' count (1) != t (2) so '' excluded
    result = histogram("a a  b")
    assert result == {"a": 2}


def test_extra_spaces_without_majority_includes_empty_token():
    # split -> ['a', '', 'b']: all counts == 1 == t, so '' is included
    result = histogram("a  b")
    assert result == {"a": 1, "": 1, "b": 1}
