# file: project/sty/primitive.py:40-63
# asked: {"lines": [55, 56, 57, 58, 61], "branches": [[50, 55], [55, 56], [55, 61]]}
# gained: {"lines": [55, 56, 57, 58, 61], "branches": [[50, 55], [55, 56], [55, 61]]}

import pytest

from sty.primitive import Style, _render_rules
from sty.rendertype import RgbFg, Sgr


def _make_renderfuncs():
    return {
        Sgr: lambda num: f"<sgr:{num}>",
        RgbFg: lambda r, g, b: f"<rgb:{r},{g},{b}>",
    }


def test_render_rules_nested_style_is_flattened():
    renderfuncs = _make_renderfuncs()
    sgr_rule = Sgr(1)
    rgb_rule = RgbFg(10, 20, 30)
    nested = Style(sgr_rule, rgb_rule, value="ignored-value")

    rendered, flattened = _render_rules(renderfuncs, [nested])

    assert rendered == "<sgr:1><rgb:10,20,30>"
    assert list(flattened) == [sgr_rule, rgb_rule]
    assert flattened[0] is sgr_rule
    assert flattened[1] is rgb_rule


def test_render_rules_mixed_direct_and_nested_style():
    renderfuncs = _make_renderfuncs()
    direct = Sgr(4)
    inner_sgr = Sgr(1)
    inner_rgb = RgbFg(1, 5, 10)
    nested = Style(inner_sgr, inner_rgb, value="nested")
    outer = Style(nested, value="outer")

    rendered, flattened = _render_rules(renderfuncs, [direct, outer])

    assert rendered == "<sgr:4><sgr:1><rgb:1,5,10>"
    assert list(flattened) == [direct, inner_sgr, inner_rgb]


def test_render_rules_invalid_rule_raises_value_error():
    renderfuncs = _make_renderfuncs()

    with pytest.raises(ValueError, match="Parameter 'rules' must be of type"):
        _render_rules(renderfuncs, [object()])

    with pytest.raises(ValueError, match="Parameter 'rules' must be of type"):
        _render_rules(renderfuncs, [Sgr(1), "not-a-rule"])

    with pytest.raises(ValueError, match="Parameter 'rules' must be of type"):
        _render_rules(renderfuncs, [42])
