# file: project/f151/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f151 import double_the_difference


def test_double_the_difference_covers_all_branches():
    # Positive odd integers are included: 1**2 + 3**2 = 1 + 9 = 10
    # Negative numbers excluded (-3), even numbers excluded (2, 4),
    # zero excluded, floats with '.' in str excluded (1.5, 3.0)
    lst = [1, 3, -3, 2, 4, 0, 1.5, 3.0]
    assert double_the_difference(lst) == 10


def test_double_the_difference_empty_list():
    # Executes line 3 with an empty list; sum of empty comprehension is 0
    assert double_the_difference([]) == 0


def test_double_the_difference_only_floats():
    # All elements contain '.' in their string representation, so the
    # comprehension filter rejects everything, but line 3 still executes.
    assert double_the_difference([0.5, -1.5, 2.5]) == 0


def test_double_the_difference_mixed_types():
    # Booleans: True == 1 is odd and positive, but str(True) has no '.',
    # so True is included (True**2 == 1); False is even (0 % 2 == 0), excluded.
    assert double_the_difference([True, False, 5]) == 1 + 25
