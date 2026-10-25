# file: project/sty/primitive.py:170-179
# asked: {"lines": [174, 176, 177, 178, 179], "branches": [[176, 0], [176, 177], [178, 176], [178, 179]]}
# gained: {"lines": [174, 176, 177, 178, 179], "branches": [[176, 0], [176, 177], [178, 176], [178, 179]]}

import pytest

from sty.primitive import Register, Style


def test_unmute_clears_muted_flag_and_rerenders_style_attributes(monkeypatch):
    render_calls = []

    def fake_render_rules(renderfuncs, rules):
        render_calls.append((renderfuncs, tuple(rules)))
        return "rendered-value", tuple(rules)

    monkeypatch.setattr("sty.primitive._render_rules", fake_render_rules)

    register = Register()
    register.custom = Style(value="original")
    register.plain_text = "not-a-style"
    register.plain_number = 42

    assert isinstance(register.custom, Style)
    assert str(register.custom) == "rendered-value"

    register.mute()
    assert register.is_muted is True
    assert isinstance(register.custom, Style)
    assert str(register.custom) == ""

    calls_before_unmute = len(render_calls)

    register.unmute()

    assert register.is_muted is False
    assert isinstance(register.custom, Style)
    assert str(register.custom) == "rendered-value"
    assert register.custom.rules == ()
    assert len(render_calls) > calls_before_unmute
    assert register.plain_text == "not-a-style"
    assert register.plain_number == 42
    assert register.renderfuncs == {}


def test_unmute_without_any_style_attributes():
    register = Register()
    register.plain_text = "text"
    register.plain_number = 123

    register.is_muted = True
    assert register.is_muted is True

    register.unmute()

    assert register.is_muted is False
    assert register.plain_text == "text"
    assert register.plain_number == 123
    assert register.renderfuncs == {}


def test_unmute_rerenders_all_style_attributes(monkeypatch):
    def fake_render_rules(renderfuncs, rules):
        return "restored", tuple(rules)

    monkeypatch.setattr("sty.primitive._render_rules", fake_render_rules)

    register = Register()
    register.first = Style(value="first-original")
    register.second = Style(value="second-original")
    register.non_style = "keep-me"

    register.mute()
    assert register.is_muted is True
    assert str(register.first) == ""
    assert str(register.second) == ""

    register.unmute()

    assert register.is_muted is False
    assert isinstance(register.first, Style)
    assert isinstance(register.second, Style)
    assert str(register.first) == "restored"
    assert str(register.second) == "restored"
    assert register.non_style == "keep-me"


def test_unmute_on_unmuted_register_preserves_style_rules():
    register = Register()
    register.custom = Style(value="value")

    assert register.is_muted is False

    register.unmute()

    assert register.is_muted is False
    assert isinstance(register.custom, Style)
    assert register.custom.rules == ()
