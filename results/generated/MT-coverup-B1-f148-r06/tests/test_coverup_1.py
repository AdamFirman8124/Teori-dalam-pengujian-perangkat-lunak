# file: project/f148/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [8, 9], [8, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [8, 9], [8, 11]]}

from f148 import bf


def test_bf_invalid_planet1_returns_empty():
    assert bf("Pluto", "Earth") == ()


def test_bf_invalid_planet2_returns_empty():
    assert bf("Earth", "Pluto") == ()


def test_bf_both_invalid_returns_empty():
    assert bf("Pluto", "Xenon") == ()


def test_bf_same_planet_returns_empty():
    assert bf("Earth", "Earth") == ()


def test_bf_forward_order_returns_planets_between():
    result = bf("Mercury", "Mars")
    assert result == ("Venus", "Earth")
    assert isinstance(result, tuple)


def test_bf_reverse_order_returns_planets_between():
    result = bf("Mars", "Mercury")
    assert result == ("Venus", "Earth")
    assert isinstance(result, tuple)


def test_bf_adjacent_forward_returns_empty():
    assert bf("Earth", "Mars") == ()


def test_bf_adjacent_reverse_returns_empty():
    assert bf("Mars", "Earth") == ()


def test_bf_full_range_forward():
    assert bf("Mercury", "Neptune") == (
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
    )


def test_bf_full_range_reverse():
    assert bf("Neptune", "Mercury") == (
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
    )


def test_bf_middle_range_both_directions_same_result():
    expected = ("Mars", "Jupiter")
    assert bf("Earth", "Saturn") == expected
    assert bf("Saturn", "Earth") == expected
