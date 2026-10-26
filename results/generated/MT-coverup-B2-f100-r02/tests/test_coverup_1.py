# file: project/f100/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f100 import make_a_pile


def test_make_a_pile_n0():
    assert make_a_pile(0) == []


def test_make_a_pile_n1():
    assert make_a_pile(1) == [1]


def test_make_a_pile_n2():
    assert make_a_pile(2) == [2, 4]


def test_make_a_pile_n3():
    assert make_a_pile(3) == [3, 5, 7]


def test_make_a_pile_n4():
    assert make_a_pile(4) == [4, 6, 8, 10]


def test_make_a_pile_n5():
    assert make_a_pile(5) == [5, 7, 9, 11, 13]
