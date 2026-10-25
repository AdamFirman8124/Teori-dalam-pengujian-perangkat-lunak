# file: project/sty/primitive.py:40-63
# asked: {"lines": [55, 56, 57, 58, 61], "branches": [[50, 55], [55, 56], [55, 61]]}
# gained: {"lines": [55, 56, 57, 58, 61], "branches": [[50, 55], [55, 56], [55, 61]]}

import pytest

from sty.primitive import Style, _render_rules
from sty.rendertype import RenderType


def test_render_rules_with_style_recurses_and_flattens():
    class DummyRender(RenderType):
        def __init__(self, *args):
            self.args = list(args)

    def render(*args):
        return "<" + ",".join(str(arg) for arg in args) + ">"

    renderfuncs = {DummyRender: render}
    rule1 = DummyRender("a")
    rule2 = DummyRender("b")
    inner = Style(rule1, value="<a>")
    outer = Style(inner, rule2, value="<a><b>")

    rendered, flattened = _render_rules(renderfuncs, [outer])

    assert rendered == "<a><b>"
    assert list(flattened) == [rule1, rule2]
    assert isinstance(outer, Style)
    assert outer.rules == (inner, rule2)
    assert inner.rules == (rule1,)


def test_render_rules_with_mixed_style_and_rendertype():
    class DummyRender(RenderType):
        def __init__(self, *args):
            self.args = list(args)

    renderfuncs = {DummyRender: lambda *args: "".join(str(arg) for arg in args)}
    rule1 = DummyRender("x")
    rule2 = DummyRender("y")
    style = Style(rule2, value="y")

    rendered, flattened = _render_rules(renderfuncs, [rule1, style])

    assert rendered == "xy"
    assert list(flattened) == [rule1, rule2]


def test_render_rules_with_invalid_rule_raises_value_error():
    with pytest.raises(
        ValueError,
        match=r"Parameter 'rules' must be of type Iterable\[Rule\]\.",
    ):
        _render_rules({}, [123])


def test_render_rules_with_invalid_nested_rule_raises_value_error():
    style = Style(123, value="")

    with pytest.raises(
        ValueError,
        match=r"Parameter 'rules' must be of type Iterable\[Rule\]\.",
    ):
        _render_rules({}, [style])
