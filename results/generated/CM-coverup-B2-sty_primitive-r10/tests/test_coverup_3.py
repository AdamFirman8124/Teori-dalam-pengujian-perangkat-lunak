# file: project/sty/primitive.py:158-168
# asked: {"lines": [163, 165, 166, 167, 168], "branches": [[165, 0], [165, 166], [167, 165], [167, 168]]}
# gained: {"lines": [163, 165, 166, 167, 168], "branches": [[165, 0], [165, 166], [167, 165], [167, 168]]}

import sty.primitive as primitive
from sty.primitive import Register, Style


def test_mute_sets_flag_and_clears_style_values():
    reg = Register()
    reg.custom = Style()

    assert reg.is_muted is False
    assert str(reg.custom) == ""

    reg.mute()

    assert reg.is_muted is True
    assert isinstance(reg.custom, Style)
    assert str(reg.custom) == ""
    assert reg.custom.rules == ()
    # muted register returns empty string when called
    assert reg("custom") == ""


def test_mute_preserves_rules_but_clears_rendered_value(monkeypatch):
    dummy_rule = object()
    monkeypatch.setattr(
        primitive,
        "_render_rules",
        lambda renderfuncs, rules: ("\x1b[1m", tuple(rules)),
    )

    reg = Register()
    reg.bold = Style(dummy_rule)
    assert str(reg.bold) == "\x1b[1m"

    reg.mute()

    assert reg.is_muted is True
    assert isinstance(reg.bold, Style)
    assert str(reg.bold) == ""
    assert reg.bold.rules == (dummy_rule,)


def test_mute_leaves_non_style_attributes_untouched_and_is_idempotent():
    reg = Register()
    reg.plain = 42
    reg.styled = Style()

    reg.mute()
    reg.mute()

    assert reg.is_muted is True
    assert reg.plain == 42
    assert isinstance(reg.styled, Style)
    assert str(reg.styled) == ""


def test_unmute_after_mute_restores_rendering(monkeypatch):
    dummy_rule = object()
    monkeypatch.setattr(
        primitive,
        "_render_rules",
        lambda renderfuncs, rules: ("\x1b[1m", tuple(rules)),
    )

    reg = Register()
    reg.bold = Style(dummy_rule)
    reg.mute()
    assert str(reg.bold) == ""

    reg.unmute()

    assert reg.is_muted is False
    assert str(reg.bold) == "\x1b[1m"
    assert reg.bold.rules == (dummy_rule,)
