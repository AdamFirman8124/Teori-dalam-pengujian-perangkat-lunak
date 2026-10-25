# file: project/sty/primitive.py:78-91
# asked: {"lines": [83], "branches": [[82, 83]]}
# gained: {"lines": [83], "branches": [[82, 83]]}

import pytest

from sty.primitive import Register, Style
from sty.rendertype import Sgr


def test_setattr_on_muted_register_executes_line_83():
    """Setting a Style on a muted Register must hit line 83: the style is
    re-created with the same rules but an empty rendered value."""
    reg = Register()
    # Register a renderfunc for Sgr so that unmute() (which re-renders all
    # style attributes via __setattr__) does not raise a KeyError.
    reg.set_renderfunc(Sgr, lambda x: f"\x1b[{x}m")

    rule = Sgr(1)
    original = Style(rule, value="\x1b[1m")

    reg.mute()
    try:
        assert reg.is_muted is True
        reg.myattr = original

        stored = reg.myattr
        # Postconditions: stored value is a Style, its rendered string is
        # empty (muted), and the original rules are preserved.
        assert isinstance(stored, Style)
        assert str(stored) == ""
        assert stored.rules == (rule,)
        assert stored.rules == original.rules
    finally:
        # Cleanup: restore the instance state (it is local, but be explicit
        # to avoid any state pollution).
        reg.unmute()
        assert reg.is_muted is False


def test_setattr_on_unmuted_register_renders_style():
    """Cover the else-branch of the is_muted check for completeness."""
    reg = Register()
    reg.set_renderfunc(Sgr, lambda x: f"\x1b[{x}m")

    rule = Sgr(1)
    original = Style(rule, value="\x1b[1m")

    reg.myattr = original

    stored = reg.myattr
    assert isinstance(stored, Style)
    assert stored.rules == (rule,)


def test_setattr_with_non_style_value():
    """Cover the outer else-branch: non-Style values are set as-is."""
    reg = Register()

    reg.plain = "hello"

    assert reg.plain == "hello"
    assert not isinstance(reg.plain, Style)
