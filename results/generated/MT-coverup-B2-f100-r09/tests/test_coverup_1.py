# file: project/f100/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f100 import make_a_pile


def test_make_a_pile() -> None:
    assert make_a_pile(4) == [4, 6, 8, 10]
