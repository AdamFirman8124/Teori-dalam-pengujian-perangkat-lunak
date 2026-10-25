# file: project/f142/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 7], [7, 8], [7, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 7], [7, 8], [7, 10]]}

import pytest

from f142 import sum_squares


def test_sum_squares_all_branches():
    # indices: 0 (i%3==0), 1 (else), 2 (else), 3 (i%3==0),
    # 4 (i%4==0 and i%3!=0), 5 (else), 6 (i%3==0)
    lst = [2, 3, 4, 5, 6, 7, 8]
    # i=0: 2**2 = 4
    # i=1: 3
    # i=2: 4
    # i=3: 5**2 = 25
    # i=4: 6**3 = 216
    # i=5: 7
    # i=6: 8**2 = 64
    assert sum_squares(lst) == 4 + 3 + 4 + 25 + 216 + 7 + 64


def test_sum_squares_empty_list():
    assert sum_squares([]) == 0


def test_sum_squares_single_element():
    # i=0 hits the i % 3 == 0 branch
    assert sum_squares([10]) == 100


def test_sum_squares_index_multiple_of_4_not_3():
    # length 5: indices 0..4; index 4 hits the elif branch
    lst = [1, 1, 1, 1, 3]
    # i=0: 1**2 = 1, i=1..3: 1 each, i=4: 3**3 = 27
    assert sum_squares(lst) == 1 + 1 + 1 + 1 + 27
