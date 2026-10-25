# file: project/pymonet/either.py:37-46
# asked: {"lines": [46], "branches": []}
# gained: {"lines": [46], "branches": []}

import pytest

from pymonet.either import Either, Left, Right


def test_right_ap_applies_function_to_right_applicative():
    result = Right(lambda x: x + 1).ap(Right(2))

    assert result.is_right()
    assert result.value == 3


def test_right_ap_with_left_applicative_returns_left():
    result = Right(lambda x: x + 1).ap(Left('error'))

    assert result.is_left()
    assert result.value == 'error'


def test_right_ap_uses_inherited_either_ap():
    assert 'ap' not in Right.__dict__
    assert Right.ap is Either.ap


def test_right_ap_calls_map_on_applicative(monkeypatch):
    calls = []
    original_map = Right.map

    def spy_map(self, mapper):
        calls.append(mapper)
        return original_map(self, mapper)

    monkeypatch.setattr(Right, 'map', spy_map)

    result = Right(lambda x: x * 2).ap(Right(10))

    assert len(calls) == 1
    assert result.is_right()
    assert result.value == 20


def test_either_ap_base_implementation_delegates_to_applicative_map():
    class PlainEither(Either):
        def __init__(self, value):
            self.value = value

        def map(self, mapper):
            return PlainEither(mapper(self.value))

    result = PlainEither(lambda x: x + '!').ap(PlainEither('hi'))

    assert isinstance(result, PlainEither)
    assert result.value == 'hi!'
