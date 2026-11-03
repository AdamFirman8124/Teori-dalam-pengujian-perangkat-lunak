# file: project/f069/__init__.py:1-21
# asked: {"lines": [12, 13, 14, 16, 17, 18, 19, 21], "branches": [[13, 14], [13, 16], [17, 18], [17, 21], [18, 17], [18, 19]]}
# gained: {"lines": [12, 13, 14, 16, 17, 18, 19, 21], "branches": [[13, 14], [13, 16], [17, 18], [17, 21], [18, 17], [18, 19]]}

"""Tests for f069.search, covering lines 12-21 and both branches of `frq[i] >= i`.

The function under test is pure (no I/O, no globals, no side effects), so no
monkeypatching or cleanup is required; each test operates only on local data.
"""

from f069 import search


def test_search_returns_greatest_integer_meeting_frequency():
    # frq = [0, 2, 2, 1, 1]
    # i=1: 2 >= 1 -> True  (ans = 1)   [True branch]
    # i=2: 2 >= 2 -> True  (ans = 2)   [True branch]
    # i=3: 1 >= 3 -> False             [False branch]
    # i=4: 1 >= 4 -> False             [False branch]
    assert search([4, 1, 2, 2, 3, 1]) == 2


def test_search_prefers_largest_qualifying_value():
    # frq = [0, 1, 2, 3, 3]
    # i=1: 1 >= 1 -> True  (ans = 1)   [True branch]
    # i=2: 2 >= 2 -> True  (ans = 2)   [True branch]
    # i=3: 3 >= 3 -> True  (ans = 3)   [True branch]
    # i=4: 3 >= 4 -> False             [False branch]
    assert search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3


def test_search_returns_minus_one_when_no_value_qualifies():
    # frq = [0, 0, 0, 0, 3, 2]
    # Every i in 1..5 fails frq[i] >= i [False branch each iteration],
    # so the initial ans = -1 (line 16) is returned (line 21).
    assert search([5, 5, 4, 4, 4]) == -1


def test_search_single_element_list():
    # Minimal input exercising the frequency loop (lines 13-14) exactly once.
    # search([1]): frq = [0, 1]; i=1: 1 >= 1 -> True  -> returns 1 [True branch]
    assert search([1]) == 1
    # search([2]): frq = [0, 0, 1]; i=1: 0 >= 1 -> False; i=2: 1 >= 2 -> False
    # -> returns -1 [False branch]
    assert search([2]) == -1
