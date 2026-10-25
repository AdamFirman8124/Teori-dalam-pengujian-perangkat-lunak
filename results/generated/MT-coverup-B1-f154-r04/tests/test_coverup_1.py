# file: project/f154/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7], [7, 6], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7], [7, 6], [7, 8]]}

from f154 import cycpattern_check


def test_cycpattern_direct_match():
    assert cycpattern_check("abcd", "abc") is True


def test_cycpattern_rotation_match():
    # "cab" is a rotation of "abc", requires inner loop to iterate past failures
    assert cycpattern_check("cab", "abc") is True
    assert cycpattern_check("xxxxbca yyyy", "abc") is True


def test_cycpattern_no_match():
    # exercises inner condition False for every i, j then return False
    assert cycpattern_check("abcd", "efg") is False


def test_cycpattern_a_shorter_than_b():
    # outer range is empty, skips both loops and returns False
    assert cycpattern_check("ab", "abcde") is False
