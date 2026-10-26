# file: project/sty/primitive.py:142-156
# asked: {"lines": [150, 153, 154, 155, 156], "branches": [[153, 0], [153, 154], [155, 153], [155, 156]]}
# gained: {"lines": [150, 153, 154, 155, 156], "branches": [[153, 0], [153, 154], [155, 153], [155, 156]]}

import pytest

from sty import Style
from sty.primitive import Register
from sty.rendertype import RenderType


def test_set_renderfunc_without_style_attributes():
    register = Register()
    func = lambda *args, **kwargs: "rendered"

    register.set_renderfunc(RenderType, func)

    assert register.renderfuncs == {RenderType: func}
    assert register.renderfuncs[RenderType] is func
    assert not any(
        isinstance(getattr(register, name), Style) for name in dir(register)
    )
    assert register.is_muted is False


def test_set_renderfunc_rerenders_existing_style_attributes():
    class DummyRule(RenderType):
        def __init__(self, *args):
            self.args = args

        def __iter__(self):
            return iter(self.args)

    def old_func(*args, **kwargs):
        return "OLD"

    def new_func(*args, **kwargs):
        return "NEW"

    register = Register()
    register.set_renderfunc(DummyRule, old_func)
    register.custom_style = Style(DummyRule(7), value="placeholder")
    register.plain_value = "keep-me"

    assert str(register.custom_style) == "OLD"
    assert isinstance(register.custom_style, Style)

    register.set_renderfunc(DummyRule, new_func)

    assert register.renderfuncs == {DummyRule: new_func}
    assert register.renderfuncs[DummyRule] is new_func
    assert isinstance(register.custom_style, Style)
    assert str(register.custom_style) == "NEW"
    assert len(register.custom_style.rules) == 1
    assert isinstance(register.custom_style.rules[0], DummyRule)
    assert register.custom_style.rules[0].args == (7,)
    assert register.plain_value == "keep-me"
    assert register.is_muted is False


def test_set_renderfunc_resets_only_style_attributes(monkeypatch):
    register = Register()
    register.custom_style = Style(value="placeholder")
    register.plain_value = 123

    original_setattr = Register.__setattr__
    calls = []

    def counting_setattr(self, name, value):
        calls.append((name, value))
        return original_setattr(self, name, value)

    monkeypatch.setattr(Register, "__setattr__", counting_setattr)

    func = lambda *args, **kwargs: "unused"
    register.set_renderfunc(RenderType, func)

    assert register.renderfuncs[RenderType] is func
    assert [name for name, value in calls if isinstance(value, Style)] == [
        "custom_style"
    ]
    assert all(name != "plain_value" for name, _ in calls)
    assert isinstance(register.custom_style, Style)
    assert register.custom_style.rules == ()
    assert str(register.custom_style) == ""
    assert register.plain_value == 123


def test_set_renderfunc_on_muted_register_keeps_style_empty():
    register = Register()
    register.custom_style = Style(value="placeholder")
    register.mute()

    func = lambda *args, **kwargs: "unused"
    register.set_renderfunc(RenderType, func)

    assert register.renderfuncs == {RenderType: func}
    assert register.is_muted is True
    assert isinstance(register.custom_style, Style)
    assert str(register.custom_style) == ""
    assert register.custom_style.rules == ()
