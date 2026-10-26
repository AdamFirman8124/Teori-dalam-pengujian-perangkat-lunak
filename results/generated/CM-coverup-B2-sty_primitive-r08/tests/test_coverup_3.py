# file: project/sty/primitive.py:158-168
# asked: {"lines": [163, 165, 166, 167, 168], "branches": [[165, 0], [165, 166], [167, 165], [167, 168]]}
# gained: {"lines": [163, 165, 166, 167, 168], "branches": [[165, 0], [165, 166], [167, 165], [167, 168]]}

import pytest

from sty.primitive import Register, Style


def test_mute_clears_style_value_and_keeps_rules(monkeypatch):
    rule = object()

    class MyRegister(Register):
        my_style = Style(rule, value="\x1b[1m")

    reg = MyRegister()
    assert reg.is_muted is False
    assert str(reg.my_style) == "\x1b[1m"

    reg.mute()

    assert reg.is_muted is True
    muted = reg.my_style
    assert isinstance(muted, Style)
    assert str(muted) == ""
    assert muted.rules == (rule,)
    # the class-level Style must not be mutated in place
    assert str(MyRegister.my_style) == "\x1b[1m"

    monkeypatch.delattr(reg, "my_style", raising=False)


def test_mute_clears_all_style_attributes_and_keeps_non_style(monkeypatch):
    rule = object()

    class MyRegister(Register):
        style_a = Style(value="a")
        style_b = Style(rule, value="b")

    reg = MyRegister()
    object.__setattr__(reg, "plain", 42)

    reg.mute()

    assert reg.is_muted is True
    assert reg.plain == 42
    assert isinstance(reg.style_a, Style)
    assert isinstance(reg.style_b, Style)
    assert str(reg.style_a) == ""
    assert str(reg.style_b) == ""
    assert reg.style_a.rules == ()
    assert reg.style_b.rules == (rule,)

    monkeypatch.delattr(reg, "plain", raising=False)
    monkeypatch.delattr(reg, "style_a", raising=False)
    monkeypatch.delattr(reg, "style_b", raising=False)


def test_mute_is_idempotent_and_blocks_new_style_rendering(monkeypatch):
    class MyRegister(Register):
        style_a = Style(value="a")

    reg = MyRegister()

    reg.mute()
    reg.mute()

    assert reg.is_muted is True
    assert str(reg.style_a) == ""

    # assigning a new Style while muted must store an empty value
    reg.style_new = Style(object(), value="rendered")

    assert isinstance(reg.style_new, Style)
    assert str(reg.style_new) == ""
    assert len(reg.style_new.rules) == 1

    monkeypatch.delattr(reg, "style_a", raising=False)
    monkeypatch.delattr(reg, "style_new", raising=False)
