# file: project/f100/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f100 import make_a_pile


def test_make_a_pile_returns_consecutive_odd_spaced_values():
    assert make_a_pile(3) == [3, 5, 7]
