# file: project/f069/__init__.py:1-21
# asked: {"lines": [12, 13, 14, 16, 17, 18, 19, 21], "branches": [[13, 14], [13, 16], [17, 18], [17, 21], [18, 17], [18, 19]]}
# gained: {"lines": [12, 13, 14, 16, 17, 18, 19, 21], "branches": [[13, 14], [13, 16], [17, 18], [17, 21], [18, 17], [18, 19]]}

from f069 import search


def test_search_returns_greatest_qualifying_integer():
    values = [4, 1, 2, 2, 3, 1]

    assert search(values) == 2
    assert values == [4, 1, 2, 2, 3, 1]


def test_search_returns_minus_one_when_no_integer_qualifies():
    values = [5, 5, 4, 4, 4]

    assert search(values) == -1
    assert values == [5, 5, 4, 4, 4]
