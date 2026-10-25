# file: project/f148/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [8, 9], [8, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [8, 9], [8, 11]]}

from f148 import bf


def test_bf_forward_between():
    assert bf("Earth", "Jupiter") == ("Mars",)


def test_bf_reverse_between():
    assert bf("Jupiter", "Earth") == ("Mars",)


def test_bf_full_range_forward():
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")


def test_bf_full_range_reverse():
    assert bf("Neptune", "Mercury") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")


def test_bf_invalid_first_planet():
    assert bf("Pluto", "Earth") == ()


def test_bf_invalid_second_planet():
    assert bf("Earth", "Pluto") == ()


def test_bf_both_invalid():
    assert bf("Pluto", "Nibiru") == ()


def test_bf_same_planet():
    assert bf("Earth", "Earth") == ()


def test_bf_adjacent_forward_empty():
    assert bf("Venus", "Earth") == ()


def test_bf_adjacent_reverse_empty():
    assert bf("Earth", "Venus") == ()
