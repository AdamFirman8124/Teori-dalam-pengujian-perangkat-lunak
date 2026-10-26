# file: project/f147/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 10], [6, 5], [6, 7], [7, 6], [7, 8], [8, 7], [8, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 10], [6, 5], [6, 7], [7, 6], [7, 8], [8, 7], [8, 9]]}

import pytest

from f147 import get_max_triples


def test_get_max_triples_n5():
    # A = [1, 3, 7, 13, 21]; only (1, 7, 13) sums to a multiple of 3
    assert get_max_triples(5) == 1


def test_get_max_triples_n4():
    # A = [1, 3, 7, 13]; only (1, 7, 13) sums to 21, divisible by 3
    assert get_max_triples(4) == 1


def test_get_max_triples_small_n():
    # n = 0, 1, 2, 3 produce no valid triples
    assert get_max_triples(0) == 0
    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0
    # A = [1, 3, 7]; 1 + 3 + 7 = 11, not divisible by 3
    assert get_max_triples(3) == 0
