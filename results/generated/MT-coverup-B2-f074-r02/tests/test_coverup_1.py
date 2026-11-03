# file: project/f074/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 7, 8, 9, 11, 12, 14], "branches": [[4, 5], [4, 7], [8, 9], [8, 11], [11, 12], [11, 14]]}
# gained: {"lines": [3, 4, 5, 7, 8, 9, 11, 12, 14], "branches": [[4, 5], [4, 7], [8, 9], [8, 11], [11, 12], [11, 14]]}

import f074


def test_total_match_lst1_shorter():
    assert f074.total_match(["a"], ["hi", "world"]) == ["a"]


def test_total_match_lst2_shorter():
    assert f074.total_match(["hi", "world"], ["a"]) == ["a"]


def test_total_match_equal():
    assert f074.total_match(["ab", "cd"], ["a", "bcd"]) == ["ab", "cd"]


def test_total_match_empty_lists():
    assert f074.total_match([], []) == []
    assert f074.total_match([], ["x"]) == []
    assert f074.total_match(["x"], []) == []
