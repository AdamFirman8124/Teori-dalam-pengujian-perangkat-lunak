# file: project/f151/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f151 import double_the_difference


def test_double_the_difference_full_coverage():
    # Covers: positive odd ints (included), negative ints, even ints,
    # zero, and floats with '.' in their string representation (excluded).
    lst = [1, 3, -2, 4, 0, 1.5, 7]
    # Included: 1, 3, 7 -> 1 + 9 + 49 = 59
    assert double_the_difference(lst) == 59


def test_double_the_difference_empty_list():
    # Executes line 3 with an empty comprehension result.
    assert double_the_difference([]) == 0


def test_double_the_difference_all_excluded():
    # Every element fails at least one condition of the comprehension filter.
    lst = [-1, -3, 2, 4, 0, 2.5, -1.5]
    assert double_the_difference(lst) == 0


def test_double_the_difference_float_without_dot_in_str():
    # A float whose str() contains no '.' (e.g. 1e30) but is even -> excluded by parity.
    # A float like 3.0 has '.' in str -> excluded by the '.' check.
    lst = [3.0, 5.0]
    assert double_the_difference(lst) == 0


def test_double_the_difference_mixed_types():
    # Ensure booleans (True is odd and > 0) are handled: True**2 == 1.
    lst = [True, 5]
    assert double_the_difference(lst) == 1 + 25
