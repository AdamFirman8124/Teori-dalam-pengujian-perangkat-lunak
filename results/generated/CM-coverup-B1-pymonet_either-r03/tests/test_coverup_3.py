# file: project/pymonet/either.py:48-57
# asked: {"lines": [55, 57], "branches": []}
# gained: {"lines": [55, 57], "branches": []}

import pytest

from pymonet.either import Left, Right
from pymonet.box import Box


@pytest.mark.parametrize("either", [Left("error"), Right(42)])
def test_to_box_returns_box_with_value(either):
    """Either.to_box should wrap the underlying value in a Box."""
    box = either.to_box()

    assert isinstance(box, Box)
    assert box.value == either.value
    assert box == Box(either.value)


def test_to_box_uses_deferred_import(monkeypatch):
    """The local `from pymonet.box import Box` inside to_box must execute
    (lines 55-57) and the returned Box must come from that import."""
    calls = []
    real_box = Box

    def fake_box(value):
        calls.append(value)
        return real_box(value)

    monkeypatch.setattr("pymonet.box.Box", fake_box)

    result = Right(42).to_box()

    assert calls == [42]
    assert isinstance(result, Box)
    assert result.value == 42
