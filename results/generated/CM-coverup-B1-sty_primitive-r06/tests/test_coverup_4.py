# file: project/sty/primitive.py:170-179
# asked: {"lines": [174, 176, 177, 178, 179], "branches": [[176, 0], [176, 177], [178, 176], [178, 179]]}
# gained: {"lines": [174, 176, 177, 178, 179], "branches": [[176, 0], [176, 177], [178, 176], [178, 179]]}

import pytest

from sty.primitive import Register, Style


class _StyleRegister(Register):
    """A minimal register that owns one Style attribute and one non-Style attribute."""

    def __init__(self):
        super().__init__()
        # With no renderfuncs registered, __setattr__ renders the Style to ''.
        self.red = Style(value="\x1b[31m")
        self.plain = "not-a-style"


def test_unmute_resets_muted_state_and_reassigns_styles():
    reg = _StyleRegister()

    # Precondition: register starts unmuted.
    assert reg.is_muted is False
    assert isinstance(reg.red, Style)

    reg.mute()
    assert reg.is_muted is True
    # While muted, __setattr__ re-renders the Style with an empty value.
    assert isinstance(reg.red, Style)
    assert str(reg.red) == ""

    # Exercise Register.unmute (lines 174-179): is_muted reset plus the
    # dir()/getattr()/isinstance(Style)/setattr loop.
    reg.unmute()

    # Postconditions.
    assert reg.is_muted is False
    # The Style attribute must still be a Style after being re-assigned by
    # the unmute loop (no renderfuncs -> rendered value stays empty).
    assert isinstance(reg.red, Style)
    assert str(reg.red) == ""
    # Non-Style attributes must be untouched by the loop.
    assert reg.plain == "not-a-style"


def test_unmute_on_register_without_style_attributes():
    reg = Register()

    reg.mute()
    assert reg.is_muted is True

    reg.unmute()

    assert reg.is_muted is False
