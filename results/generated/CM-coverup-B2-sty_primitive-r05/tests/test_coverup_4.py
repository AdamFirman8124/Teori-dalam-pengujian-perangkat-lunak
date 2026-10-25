# file: project/sty/primitive.py:170-179
# asked: {"lines": [174, 176, 177, 178, 179], "branches": [[176, 0], [176, 177], [178, 176], [178, 179]]}
# gained: {"lines": [174, 176, 177, 178, 179], "branches": [[176, 0], [176, 177], [178, 176], [178, 179]]}

import pytest

from sty.primitive import Register, Style
from sty.rendertype import RenderType


class DummyRule(RenderType):
    """A minimal RenderType whose render function wraps its arg in angle brackets."""

    def __init__(self, code: str) -> None:
        self.args = [code]


def make_register() -> Register:
    register = Register()
    register.set_renderfunc(DummyRule, lambda code: f"<{code}>")
    return register


def test_unmute_after_mute_clears_muted_flag_and_reapplies_styles():
    register = make_register()
    try:
        register.red = Style(DummyRule("red-code"))
        assert register.is_muted is False
        assert isinstance(register.red, Style)
        assert str(register.red) == "<red-code>"

        register.mute()
        assert register.is_muted is True
        assert isinstance(register.red, Style)
        assert str(register.red) == ""

        register.unmute()

        assert register.is_muted is False
        assert isinstance(register.red, Style)
        assert str(register.red) == "<red-code>"
    finally:
        del register


def test_unmute_on_unmuted_register_preserves_style_attributes():
    register = make_register()
    try:
        register.bold = Style(DummyRule("bold-code"))
        register.plain_text = "not-a-style"
        register.count = 42

        register.unmute()

        assert register.is_muted is False
        assert isinstance(register.bold, Style)
        assert str(register.bold) == "<bold-code>"
        assert register.plain_text == "not-a-style"
        assert register.count == 42
    finally:
        del register


def test_unmute_with_no_style_attributes_preserves_non_style_attributes():
    register = make_register()
    try:
        register.is_muted = True
        assert register.is_muted is True

        register.unmute()

        assert register.is_muted is False
        assert register.renderfuncs == {DummyRule: register.renderfuncs[DummyRule]}
        assert callable(register.eightbit_call)
        assert register.eightbit_call("sentinel") == "sentinel"
        assert callable(register.rgb_call)
        assert register.rgb_call(1, 2, 3) == (1, 2, 3)
    finally:
        del register


def test_unmute_reapplies_multiple_style_attributes_and_is_idempotent():
    register = make_register()
    try:
        register.first = Style(DummyRule("first-code"))
        register.second = Style(DummyRule("first-code"), DummyRule("second-code"))

        register.unmute()
        register.unmute()

        assert register.is_muted is False
        assert isinstance(register.first, Style)
        assert str(register.first) == "<first-code>"
        assert isinstance(register.second, Style)
        assert str(register.second) == "<first-code><second-code>"
    finally:
        del register
