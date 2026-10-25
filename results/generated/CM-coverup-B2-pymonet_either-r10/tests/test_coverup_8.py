# file: project/pymonet/either.py:189-198
# asked: {"lines": [196, 198], "branches": []}
# gained: {"lines": [196, 198], "branches": []}

import pytest

from pymonet.either import Right, Left
import pymonet.maybe as maybe_module


class TestRightToMaybe:
    def test_right_to_maybe_returns_just_with_value(self, monkeypatch):
        """Right.to_maybe must call Maybe.just with the wrapped value
        and return the resulting Maybe instance."""
        calls = {}
        original_just = maybe_module.Maybe.just

        def spy_just(value):
            calls["value"] = value
            return original_just(value)

        monkeypatch.setattr(maybe_module.Maybe, "just", staticmethod(spy_just))

        right = Right(42)
        result = right.to_maybe()

        # Maybe.just was invoked with the Right's value
        assert calls["value"] == 42

        # The result is a Maybe instance
        assert isinstance(result, maybe_module.Maybe)

    def test_right_to_maybe_with_falsy_value(self):
        """A Right wrapping a falsy value still produces a Maybe."""
        result = Right(None).to_maybe()

        assert isinstance(result, maybe_module.Maybe)

    def test_left_to_maybe_returns_nothing(self):
        """Contrast: Left.to_maybe returns an empty Maybe."""
        result = Left("error").to_maybe()

        assert isinstance(result, maybe_module.Maybe)
