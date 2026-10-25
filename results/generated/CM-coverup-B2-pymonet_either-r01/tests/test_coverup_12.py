# file: project/pymonet/either.py:81-82
# asked: {"lines": [82], "branches": []}
# gained: {"lines": [82], "branches": []}

from pymonet.either import Either


def test_is_right_executes_body_and_returns_none():
    either = Either(42)

    result = either.is_right()

    assert result is None
    assert either.value == 42


def test_is_right_is_side_effect_free_across_calls():
    either = Either('value')

    first = either.is_right()
    second = either.is_right()

    assert first is None
    assert second is None
    assert either.value == 'value'
