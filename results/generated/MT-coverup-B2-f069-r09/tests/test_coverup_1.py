# file: project/f069/__init__.py:1-21
# asked: {"lines": [12, 13, 14, 16, 17, 18, 19, 21], "branches": [[13, 14], [13, 16], [17, 18], [17, 21], [18, 17], [18, 19]]}
# gained: {"lines": [12, 13, 14, 16, 17, 18, 19, 21], "branches": [[13, 14], [13, 16], [17, 18], [17, 21], [18, 17], [18, 19]]}

from f069 import search


def test_search_example_one():
    assert search([4, 1, 2, 2, 3, 1]) == 2


def test_search_example_two():
    assert search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3


def test_search_no_such_value():
    assert search([5, 5, 4, 4, 4]) == -1


def test_search_single_element_qualifies():
    assert search([1]) == 1


def test_search_single_element_does_not_qualify():
    assert search([2]) == -1


def test_search_greatest_qualifying_value():
    assert search([2, 2, 3, 3, 3, 1]) == 3


def test_search_frequency_exceeds_value():
    assert search([1, 1, 1, 2, 2]) == 2
