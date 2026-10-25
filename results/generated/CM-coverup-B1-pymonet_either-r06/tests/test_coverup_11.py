# file: project/pymonet/either.py:37-46
# asked: {"lines": [46], "branches": []}
# gained: {"lines": [46], "branches": []}

from pymonet.either import Either, Left, Right


def test_ap_right_applies_wrapped_function_to_right_value():
    applicative = Right(41)
    fn_container = Right(lambda x: x + 1)
    result = fn_container.ap(applicative)

    assert isinstance(result, Right)
    assert result.value == 42
    assert result == Right(42)
    assert applicative == Right(41)


def test_ap_right_with_left_applicative_returns_left():
    applicative = Left('error')
    fn_container = Right(lambda x: x + 1)
    result = fn_container.ap(applicative)

    assert isinstance(result, Left)
    assert result.value == 'error'
    assert result == Left('error')


def test_ap_delegates_to_applicative_map_with_self_value(monkeypatch):
    applicative = Right(10)
    fn = lambda x: x * 2
    fn_container = Right(fn)
    received = []
    original_map = applicative.map

    def spy_map(mapper):
        received.append(mapper)
        return original_map(mapper)

    monkeypatch.setattr(applicative, 'map', spy_map)

    result = fn_container.ap(applicative)

    assert received == [fn]
    assert isinstance(result, Right)
    assert result.value == 20
