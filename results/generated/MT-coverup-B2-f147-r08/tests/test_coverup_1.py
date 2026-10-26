# file: project/f147/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 10], [6, 5], [6, 7], [7, 6], [7, 8], [8, 7], [8, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 10], [6, 5], [6, 7], [7, 6], [7, 8], [8, 7], [8, 9]]}

from f147 import get_max_triples


def test_get_max_triples_n_zero():
    assert get_max_triples(0) == 0


def test_get_max_triples_n_one():
    assert get_max_triples(1) == 0


def test_get_max_triples_n_two():
    assert get_max_triples(2) == 0


def test_get_max_triples_n_three_no_match():
    # A = [1, 3, 7], 1+3+7=11 % 3 != 0, exercises `if` False branch
    assert get_max_triples(3) == 0


def test_get_max_triples_n_four_one_match():
    # A = [1, 3, 7, 13], only (1, 7, 13) sums to 21 % 3 == 0
    # exercises `if` True branch and line 9
    assert get_max_triples(4) == 1


def test_get_max_triples_n_five():
    assert get_max_triples(5) == 1


def test_get_max_triples_n_six():
    assert get_max_triples(6) == 4


def test_get_max_triples_n_ten():
    # cnt0 = 3 (i=2,5,8), cnt1 = 7 -> C(7,3)+C(3,3) = 35+1 = 36
    assert get_max_triples(10) == 36
