# file: project/f148/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [8, 9], [8, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [8, 9], [8, 11]]}

import pytest

from f148 import bf


def test_bf_forward_order_returns_planets_between():
    result = bf("Mercury", "Mars")
    assert result == ("Venus", "Earth")
    assert isinstance(result, tuple)


def test_bf_reverse_order_returns_planets_between():
    result = bf("Mars", "Mercury")
    assert result == ("Venus", "Earth")
    assert isinstance(result, tuple)


def test_bf_adjacent_planets_returns_empty_tuple():
    assert bf("Earth", "Mars") == ()
    assert bf("Mars", "Earth") == ()


def test_bf_full_range_forward_and_reverse():
    expected = ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert bf("Mercury", "Neptune") == expected
    assert bf("Neptune", "Mercury") == expected


def test_bf_same_planet_returns_empty_tuple():
    assert bf("Earth", "Earth") == ()
    assert bf("Neptune", "Neptune") == ()


@pytest.mark.parametrize(
    "planet1, planet2",
    [
        ("Pluto", "Mars"),
        ("Mars", "Pluto"),
        ("pluto", "mars"),
        ("", "Earth"),
        ("Earth", ""),
        (None, "Earth"),
        ("Earth", None),
        (1, "Earth"),
    ],
)
def test_bf_invalid_planet_names_return_empty_tuple(planet1, planet2):
    result = bf(planet1, planet2)
    assert result == ()
    assert isinstance(result, tuple)


def test_bf_does_not_mutate_module_state(monkeypatch):
    import f148

    original = getattr(f148, "bf", None)
    assert bf("Venus", "Jupiter") == ("Earth", "Mars")
    assert getattr(f148, "bf", None) is original
    assert bf("Venus", "Jupiter") == ("Earth", "Mars")
