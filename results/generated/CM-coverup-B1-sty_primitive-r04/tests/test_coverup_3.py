# file: project/sty/primitive.py:170-179
# asked: {"lines": [174, 176, 177, 178, 179], "branches": [[176, 0], [176, 177], [178, 176], [178, 179]]}
# gained: {"lines": [174, 176, 177, 178, 179], "branches": [[176, 0], [176, 177], [178, 176], [178, 179]]}

import pytest

from sty.primitive import Register, Style


def test_unmute_with_style_attribute_executes_style_branch():
    reg = Register()
    try:
        reg.my_style = Style(value="placeholder")
        reg.plain_number = 42
        reg.plain_text = "hello"

        # Force muted state without altering the stored Style via mute().
        reg.is_muted = True
        assert reg.is_muted is True

        reg.unmute()

        assert reg.is_muted is False
        assert isinstance(reg.my_style, Style)
        assert reg.my_style.rules == ()
        assert reg.plain_number == 42
        assert reg.plain_text == "hello"
    finally:
        reg.__dict__.clear()
        reg.is_muted = False


def test_unmute_after_mute_restores_unmuted_state():
    reg = Register()
    try:
        reg.my_style = Style(value="placeholder")

        reg.mute()
        assert reg.is_muted is True
        assert isinstance(reg.my_style, Style)
        assert str(reg.my_style) == ""

        reg.unmute()

        assert reg.is_muted is False
        assert isinstance(reg.my_style, Style)
        assert reg.my_style.rules == ()
        # No styling rules were registered, so rendering produces "".
        assert str(reg.my_style) == ""
    finally:
        reg.__dict__.clear()
        reg.is_muted = False


def test_unmute_without_style_attributes_executes_non_style_branch():
    reg = Register()
    try:
        reg.plain_number = 123
        reg.plain_text = "not-a-style"
        reg.is_muted = True
        assert reg.is_muted is True
        assert not any(
            isinstance(getattr(reg, name), Style) for name in vars(reg)
        )

        reg.unmute()

        assert reg.is_muted is False
        assert reg.plain_number == 123
        assert reg.plain_text == "not-a-style"

        # Idempotent: unmuting an already unmuted register keeps state.
        reg.unmute()
        assert reg.is_muted is False
        assert reg.plain_number == 123
        assert reg.plain_text == "not-a-style"
    finally:
        reg.__dict__.clear()
        reg.is_muted = False
