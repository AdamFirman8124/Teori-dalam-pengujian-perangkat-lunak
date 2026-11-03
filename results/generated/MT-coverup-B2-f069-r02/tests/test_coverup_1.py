# file: project/f069/__init__.py:1-21
# asked: {"lines": [12, 13, 14, 16, 17, 18, 19, 21], "branches": [[13, 14], [13, 16], [17, 18], [17, 21], [18, 17], [18, 19]]}
# gained: {"lines": [12, 13, 14, 16, 17, 18, 19, 21], "branches": [[13, 14], [13, 16], [17, 18], [17, 21], [18, 17], [18, 19]]}

import pytest

from f069 import search


def test_search_basic():
    """Test the basic example from the docstring."""
    assert search([4, 1, 2, 2, 3, 1]) == 2


def test_search_multiple_candidates():
    """Test a case where multiple values satisfy the condition; the greatest should be returned."""
    assert search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3


def test_search_no_result():
    """Test a case where no value satisfies the condition; should return -1."""
    assert search([5, 5, 4, 4, 4]) == -1


def test_search_single_element():
    """Test a single-element list where the element satisfies the condition."""
    assert search([1]) == 1


def test_search_single_element_no_result():
    """Test a single-element list where the element does not satisfy the condition."""
    assert search([2]) == -1
