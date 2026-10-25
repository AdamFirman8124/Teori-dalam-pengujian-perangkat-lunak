# file: project/f100/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f100 import make_a_pile


def test_make_a_pile_n_1():
    result = make_a_pile(1)
    assert result == [1]


def test_make_a_pile_n_2():
    result = make_a_pile(2)
    assert result == [2, 4]


def test_make_a_pile_n_3():
    result = make_a_pile(3)
    assert result == [3, 5, 7]


def test_make_a_pile_n_4():
    result = make_a_pile(4)
    assert result == [4, 6, 8, 10]


def test_make_a_pile_empty():
    result = make_a_pile(0)
    assert result == []


def test_make_a_pile_properties():
    for n in [5, 6, 10]:
        result = make_a_pile(n)
        assert len(result) == n
        assert result[0] == n
        assert result == [n + 2 * i for i in range(n)]
        assert all(result[i + 1] - result[i] == 2 for i in range(n - 1))
