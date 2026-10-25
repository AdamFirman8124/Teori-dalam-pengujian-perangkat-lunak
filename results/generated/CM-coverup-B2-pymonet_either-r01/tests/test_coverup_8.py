# file: project/pymonet/either.py:189-198
# asked: {"lines": [196, 198], "branches": []}
# gained: {"lines": [196, 198], "branches": []}

import pymonet.maybe as maybe_module
from pymonet.either import Left, Right


def _flag(obj, name):
    value = getattr(obj, name, None)
    if value is None:
        return None
    return value() if callable(value) else value


class TestRightToMaybe:
    def test_right_to_maybe_returns_just_with_value(self, monkeypatch):
        calls = {}
        original_just = maybe_module.Maybe.just

        def spy_just(value):
            calls["value"] = value
            return original_just(value)

        monkeypatch.setattr(maybe_module.Maybe, "just", staticmethod(spy_just))

        result = Right(42).to_maybe()

        assert calls["value"] == 42
        assert isinstance(result, maybe_module.Maybe)
        assert result.value == 42
        assert _flag(result, "is_nothing") is False
        assert result.map(lambda x: x + 1).value == 43

    def test_right_to_maybe_with_falsy_value(self):
        result = Right(None).to_maybe()

        assert isinstance(result, maybe_module.Maybe)
        assert result.value is None
        assert _flag(result, "is_nothing") is False
        assert result.map(lambda x: "seen").value == "seen"

    def test_right_to_maybe_with_string_value(self):
        result = Right("hello").to_maybe()

        assert isinstance(result, maybe_module.Maybe)
        assert result.value == "hello"
        assert _flag(result, "is_nothing") is False

    def test_left_to_maybe_returns_nothing(self):
        result = Left("error").to_maybe()

        assert isinstance(result, maybe_module.Maybe)
        assert _flag(result, "is_nothing") is True
        mapped = result.map(lambda x: "seen")
        assert isinstance(mapped, maybe_module.Maybe)
        assert _flag(mapped, "is_nothing") is True
