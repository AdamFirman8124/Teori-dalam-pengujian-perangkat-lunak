# file: project/f148/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [8, 9], [8, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [8, 9], [8, 11]]}

from f148 import bf


def test_bf_rejects_invalid_or_identical_planets():
    assert bf("Pluto", "Earth") == ()
    assert bf("Earth", "Pluto") == ()
    assert bf("Earth", "Earth") == ()


def test_bf_returns_planets_between_in_forward_order():
    assert bf("Mercury", "Mars") == ("Venus", "Earth")
    assert bf("Mercury", "Venus") == ()


def test_bf_returns_planets_between_in_reverse_order():
    assert bf("Neptune", "Earth") == ("Mars", "Jupiter", "Saturn", "Uranus")
    assert bf("Venus", "Mercury") == ()
