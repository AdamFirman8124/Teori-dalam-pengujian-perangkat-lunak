# file: project/pymonet/either.py:48-57
# asked: {"lines": [55, 57], "branches": []}
# gained: {"lines": [55, 57], "branches": []}

import pytest

from pymonet.either import Left, Right
from pymonet.box import Box


@pytest.mark.parametrize("either, value", [
    (Left("error-value"), "error-value"),
    (Right(42), 42),
])
def test_to_box_wraps_value_in_box(either, value):
    box = either.to_box()
    assert isinstance(box, Box)
    assert box.value == value


def test_left_to_box_is_fresh_box(monkeypatch):
    """Ensure the local import inside to_box is exercised and a new Box is returned."""
    called = {}

    real_box = Box

    def spy_box(value):
        called["value"] = value
        return real_box(value)

    monkeypatch.setattr("pymonet.box.Box", spy_box)

    either = Left("oops")
    box = either.to_box()

    assert called["value"] == "oops"
    assert isinstance(box, real_box)
    assert box.value == "oops"
