# file: project/f069/__init__.py:1-21
# asked: {"lines": [12, 13, 14, 16, 17, 18, 19, 21], "branches": [[13, 14], [13, 16], [17, 18], [17, 21], [18, 17], [18, 19]]}
# gained: {"lines": [12, 13, 14, 16, 17, 18, 19, 21], "branches": [[13, 14], [13, 16], [17, 18], [17, 21], [18, 17], [18, 19]]}

from f069 import search


def test_search_example_greatest_is_two():
    assert search([4, 1, 2, 2, 3, 1]) == 2


def test_search_multiple_candidates_picks_greatest():
    # freq: 1->1, 2->2, 3->3 satisfy, 4->3 does not; greatest satisfying is 3
    # covers both True and False outcomes of `if frq[i] >= i` and repeated `ans = i`
    assert search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3


def test_search_no_match_returns_minus_one():
    # freq: 4->3 < 4, 5->2 < 5, all others 0; covers False branch only
    assert search([5, 5, 4, 4, 4]) == -1


def test_search_singleton_satisfying():
    assert search([1]) == 1


def test_search_singleton_not_satisfying():
    assert search([2]) == -1


def test_search_overwrite_to_greater_value():
    # both 1 and 2 satisfy, verifies greatest (last True) wins
    assert search([1, 2, 2]) == 2
