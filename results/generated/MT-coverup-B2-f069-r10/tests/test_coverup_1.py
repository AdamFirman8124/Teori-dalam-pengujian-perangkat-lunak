# file: project/f069/__init__.py:1-21
# asked: {"lines": [12, 13, 14, 16, 17, 18, 19, 21], "branches": [[13, 14], [13, 16], [17, 18], [17, 21], [18, 17], [18, 19]]}
# gained: {"lines": [12, 13, 14, 16, 17, 18, 19, 21], "branches": [[13, 14], [13, 16], [17, 18], [17, 21], [18, 17], [18, 19]]}

"""Tests for f069.search covering all previously unexecuted lines (12-21).

The function under test is pure (no I/O, no globals, no side effects),
so no monkeypatching or teardown is required; each test works on its own
local list and cannot pollute state.
"""

from f069 import search


def test_search_docstring_examples():
    """Covers lines 12-21: building frq, counting, the loop, the
    frq[i] >= i branch (taken and not taken), and the final return."""
    assert search([4, 1, 2, 2, 3, 1]) == 2
    assert search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3


def test_search_returns_minus_one_when_no_value_qualifies():
    """Covers the branch where frq[i] >= i is never true, so ans stays -1."""
    assert search([5, 5, 4, 4, 4]) == -1


def test_search_single_element_list():
    """Smallest possible input: frq has exactly two slots, loop runs once."""
    assert search([1]) == 1


def test_search_answer_is_not_the_largest_value():
    """5 occurs once (1 < 5) so it never qualifies; the answer must be 1,
    verifying that later loop iterations with frq[i] < i do not overwrite
    a previously found answer."""
    assert search([1, 1, 5]) == 1


def test_search_all_elements_equal():
    """Every element identical: only i == 3 satisfies frq[i] >= i."""
    assert search([3, 3, 3]) == 3


def test_search_result_is_greatest_qualifying_value():
    """Both 2 and 3 qualify; the greatest (3) must be returned, exercising
    multiple consecutive updates of ans inside the loop."""
    assert search([2, 2, 3, 3, 3, 9]) == 3
