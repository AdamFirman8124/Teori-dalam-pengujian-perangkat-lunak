# file: project/f100/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f100 import make_a_pile


def test_make_a_pile_executes_return():
    result = make_a_pile(3)
    assert result == [3, 5, 7]


def test_make_a_pile_zero():
    assert make_a_pile(0) == []


def test_make_a_pile_one():
    assert make_a_pile(1) == [1]
