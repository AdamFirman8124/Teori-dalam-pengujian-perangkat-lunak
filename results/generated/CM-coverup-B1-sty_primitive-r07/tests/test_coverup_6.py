# file: project/sty/primitive.py:40-63
# asked: {"lines": [55, 56, 57, 58, 61], "branches": [[50, 55], [55, 56], [55, 61]]}
# gained: {"lines": [55, 56, 57, 58, 61], "branches": [[50, 55], [55, 56], [55, 61]]}

import pytest
from sty.primitive import Style, _render_rules
from sty.rendertype import RenderType


def test_render_rules_flattens_nested_style():
    class _Fake(RenderType):
        def __init__(self, *args):
            self.args = list(args)

    def _render(*args):
        return "[" + ",".join(map(str, args)) + "]"

    renderfuncs = {_Fake: _render}
    inner1 = _Fake(1, 2)
    inner2 = _Fake("x")
    nested = Style(inner1, inner2)

    rendered, flattened = _render_rules(renderfuncs, [nested])

    assert rendered == "[1,2][x]"
    assert list(flattened) == [inner1, inner2]
    assert all(isinstance(r, _Fake) for r in flattened)
    assert not any(isinstance(r, Style) for r in flattened)


def test_render_rules_mixed_top_level_and_nested_style():
    class _Fake(RenderType):
        def __init__(self, *args):
            self.args = list(args)

    renderfuncs = {_Fake: lambda *a: "<" + ",".join(map(str, a)) + ">"}
    top = _Fake("top")
    inner_a = _Fake("a")
    inner_b = _Fake("b")
    nested = Style(inner_a, inner_b)

    rendered, flattened = _render_rules(renderfuncs, [top, nested])

    assert rendered == "<top><a><b>"
    assert list(flattened) == [top, inner_a, inner_b]


def test_render_rules_deeply_nested_style_in_style():
    class _Fake(RenderType):
        def __init__(self, *args):
            self.args = list(args)

    renderfuncs = {_Fake: lambda *a: "(" + ",".join(map(str, a)) + ")"}
    leaf1 = _Fake(1)
    leaf2 = _Fake(2)
    leaf3 = _Fake(3)
    inner = Style(leaf1, leaf2)
    outer = Style(inner, leaf3)

    rendered, flattened = _render_rules(renderfuncs, [outer])

    assert rendered == "(1)(2)(3)"
    assert list(flattened) == [leaf1, leaf2, leaf3]


def test_render_rules_empty_style_renders_empty():
    class _Fake(RenderType):
        def __init__(self, *args):
            self.args = list(args)

    renderfuncs = {_Fake: lambda *a: "X"}
    empty = Style()

    rendered, flattened = _render_rules(renderfuncs, [empty])

    assert rendered == ""
    assert list(flattened) == []


def test_render_rules_invalid_rule_raises_value_error():
    with pytest.raises(ValueError, match="Parameter 'rules'"):
        _render_rules({}, [object()])

    with pytest.raises(ValueError, match="Parameter 'rules'"):
        _render_rules({}, ["not-a-rule"])

    with pytest.raises(ValueError, match="Parameter 'rules'"):
        _render_rules({}, [123])


def test_render_rules_invalid_nested_in_style_propagates():
    class _Fake(RenderType):
        def __init__(self, *args):
            self.args = list(args)

    renderfuncs = {_Fake: lambda *a: "ok"}
    bad_nested = Style(object())

    with pytest.raises(ValueError, match="Parameter 'rules'"):
        _render_rules(renderfuncs, [bad_nested])
