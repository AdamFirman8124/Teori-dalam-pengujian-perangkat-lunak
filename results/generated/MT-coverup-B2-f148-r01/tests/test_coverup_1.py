# file: project/f148/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [8, 9], [8, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [8, 9], [8, 11]]}

import pytest

from f148 import bf


@pytest.mark.parametrize(
    ("planet1", "planet2", "expected"),
    [
        ("Mercury", "Mars", ("Venus", "Earth")),
        ("Mars", "Mercury", ("Venus", "Earth")),
        ("Mercury", "Venus", ()),
        ("Venus", "Mercury", ()),
        ("Earth", "Earth", ()),
        ("Pluto", "Earth", ()),
        ("Earth", "Pluto", ()),
    ],
)
def test_bf(planet1, planet2, expected):
    assert bf(planet1, planet2) == expected
