# file: project/f148/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [8, 9], [8, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [8, 9], [8, 11]]}

from f148 import bf


def test_bf_invalid_first_planet():
    assert bf("Pluto", "Earth") == ()


def test_bf_invalid_second_planet():
    assert bf("Earth", "Pluto") == ()


def test_bf_both_invalid():
    assert bf("Pluto", "Nibiru") == ()


def test_bf_same_planet():
    assert bf("Earth", "Earth") == ()
    assert bf("Mars", "Mars") == ()


def test_bf_forward_order():
    result = bf("Mercury", "Jupiter")
    assert result == ("Venus", "Earth", "Mars")
    assert isinstance(result, tuple)


def test_bf_reverse_order():
    result = bf("Jupiter", "Mercury")
    assert result == ("Venus", "Earth", "Mars")
    assert isinstance(result, tuple)


def test_bf_forward_middle():
    assert bf("Venus", "Saturn") == ("Earth", "Mars", "Jupiter")


def test_bf_reverse_middle():
    assert bf("Saturn", "Venus") == ("Earth", "Mars", "Jupiter")


def test_bf_adjacent_forward_empty():
    assert bf("Earth", "Mars") == ()


def test_bf_adjacent_reverse_empty():
    assert bf("Mars", "Earth") == ()
