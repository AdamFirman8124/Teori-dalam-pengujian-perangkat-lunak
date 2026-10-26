# file: project/sty/primitive.py:170-179
# asked: {"lines": [174, 176, 177, 178, 179], "branches": [[176, 0], [176, 177], [178, 176], [178, 179]]}
# gained: {"lines": [174, 176, 177, 178, 179], "branches": [[176, 0], [176, 177], [178, 176], [178, 179]]}

import pytest

from sty.primitive import Register

try:
    from sty import Style
except ImportError:  # pragma: no cover - depends on package layout
    from sty.primitive import Style

from sty.rendertype import Sgr


def test_unmute_renders_muted_style_attributes():
    """Lines 174-179: unmute() resets is_muted and re-renders Style attributes."""
    reg = Register()
    # Provide a render function so re-rendering produces a deterministic string.
    reg.set_renderfunc(Sgr, lambda rule: "\x1b[1m")

    # Setting a Style attribute while unmuted renders it immediately.
    reg.bold = Style(Sgr(1), value="placeholder")
    assert isinstance(reg.bold, Style)
    assert reg.bold == "\x1b[1m"

    original_rules = reg.bold.rules
    assert len(original_rules) == 1

    # Muting blanks out all Style attribute values.
    reg.mute()
    assert reg.is_muted is True
    assert reg.bold == ""

    # unmute() must execute lines 174-179: reset the flag and re-set every
    # Style attribute, which re-renders it via the registered renderfuncs.
    reg.unmute()

    assert reg.is_muted is False
    assert isinstance(reg.bold, Style)
    assert reg.bold == "\x1b[1m"
    # The styling rules must have been preserved through mute/unmute.
    # Sgr instances have no __eq__, so compare their string representations.
    assert [str(rule) for rule in reg.bold.rules] == [
        str(rule) for rule in original_rules
    ]


def test_unmute_without_style_attributes_is_safe():
    """Lines 176-179 loop must also run (and do nothing) when there are
    no Style attributes and the register was never muted."""
    reg = Register()

    reg.unmute()

    assert reg.is_muted is False
    # Non-Style attributes are left untouched.
    assert reg.renderfuncs == {}
    assert callable(reg.eightbit_call)
    assert callable(reg.rgb_call)
