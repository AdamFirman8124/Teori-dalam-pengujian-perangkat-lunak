# file: project/sty/primitive.py:158-168
# asked: {"lines": [163, 165, 166, 167, 168], "branches": [[165, 0], [165, 166], [167, 165], [167, 168]]}
# gained: {"lines": [163, 165, 166, 167, 168], "branches": [[165, 0], [165, 166], [167, 165], [167, 168]]}

"""Tests targeting the previously uncovered body of ``sty.primitive.Register.mute``
(lines 163-168: setting ``is_muted`` and re-setting every ``Style`` attribute found
on the register).

All tests operate exclusively on locally created ``Register`` objects, so no global
sty state (``fg``, ``bg``, ``ef``, ``rs``) is ever mutated; therefore no
monkeypatching or explicit cleanup is required to avoid state pollution.
"""

from sty import Register, Style
from sty.rendertype import Sgr


def _render_sgr(*args):
    """Render an ``Sgr`` rule into an ANSI escape sequence.

    sty may invoke registered renderfuncs either with the rule object itself or
    with its unpacked constructor values; both conventions are supported here so
    the test does not depend on that internal detail.
    """
    if len(args) == 1 and hasattr(args[0], "values"):
        values = tuple(args[0].values)
    else:
        values = args
    return "\x1b[" + ";".join(str(v) for v in values) + "m"


def _make_register():
    """Create a fresh register holding two ``Style`` attributes."""
    reg = Register()
    reg.set_renderfunc(Sgr, _render_sgr)
    red_rule = Sgr(31)
    bold_rule = Sgr(1)
    reg.red = Style(red_rule)
    reg.bold = Style(bold_rule)
    return reg, red_rule, bold_rule


def test_mute_executes_full_loop_and_blanks_style_attributes():
    """mute() must set the flag (line 163), walk all attributes via dir()/getattr()
    (lines 165-166) and re-set every Style attribute (lines 167-168), exercising
    both the True and False branches of the isinstance check."""
    reg, red_rule, bold_rule = _make_register()

    # Pre-conditions: unmuted register whose styles render to escape codes.
    assert reg.is_muted is False
    assert isinstance(reg.red, Style)
    assert isinstance(reg.bold, Style)
    assert reg.red != ""
    assert reg.bold != ""
    assert reg.red.rules == (red_rule,)
    assert reg.bold.rules == (bold_rule,)
    assert reg("red") == reg.red

    reg.mute()

    # Line 163: the mute flag was flipped.
    assert reg.is_muted is True

    # Lines 165-168: the Style attributes were re-set through __setattr__, which
    # (while muted) stores them with an empty value while preserving their rules.
    assert isinstance(reg.red, Style)
    assert reg.red == ""
    assert reg.red.rules == (red_rule,)

    assert isinstance(reg.bold, Style)
    assert reg.bold == ""
    assert reg.bold.rules == (bold_rule,)

    # Non-Style attributes visited by the loop are left untouched.
    assert reg.renderfuncs[Sgr] is _render_sgr

    # A muted register returns an empty string when called.
    assert reg("red") == ""


def test_mute_on_register_without_style_attributes():
    """mute() must also work when the dir() loop finds no Style attribute, i.e.
    only the False branch of the isinstance check is taken (lines 163-167)."""
    reg = Register()
    reg.mute()
    assert reg.is_muted is True
    # Muted registers swallow all calls, even eight-bit ones.
    assert reg(1) == ""


def test_mute_then_unmute_restores_rendering():
    """unmute() reverses mute() by re-rendering the preserved styling rules."""
    reg, _red_rule, _bold_rule = _make_register()
    reg.mute()
    assert reg.is_muted is True
    assert reg.red == ""

    reg.unmute()

    assert reg.is_muted is False
    assert isinstance(reg.red, Style)
    assert reg.red != ""
    assert reg("red") == reg.red
