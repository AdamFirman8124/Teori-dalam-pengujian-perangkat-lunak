# file: project/sty/primitive.py:40-63
# asked: {"lines": [55, 56, 57, 58, 61], "branches": [[50, 55], [55, 56], [55, 61]]}
# gained: {"lines": [55, 56, 57, 58, 61], "branches": [[50, 55], [55, 56], [55, 61]]}

from typing import Dict, Type

import pytest

from sty.primitive import Style, _render_rules
from sty.rendertype import RenderType, RgbFg, Sgr


def _mock_renderfuncs() -> Dict[Type[RenderType], object]:
    return {
        Sgr: lambda num: f"<sgr:{num}>",
        RgbFg: lambda r, g, b: f"<rgb:{r},{g},{b}>",
    }


def test_render_rules_with_nested_style():
    """Lines 55-58: a Style rule is recursively rendered and flattened."""
    renderfuncs = _mock_renderfuncs()

    inner = Style(RgbFg(1, 5, 10), Sgr(1))
    outer = Style(inner, Sgr(2))

    rendered, flattened = _render_rules(renderfuncs, [outer])

    assert rendered == "<rgb:1,5,10><sgr:1><sgr:2>"
    # The nested rules are flattened into a single list of RenderType rules.
    assert [type(r) for r in flattened] == [RgbFg, Sgr, Sgr]
    assert [r.args for r in flattened] == [[1, 5, 10], [1], [2]]
    assert all(isinstance(r, RenderType) for r in flattened)


def test_render_rules_with_deeply_nested_styles():
    """Lines 55-58: recursion works through multiple Style levels."""
    renderfuncs = _mock_renderfuncs()

    level2 = Style(Sgr(7))
    level1 = Style(level2, Sgr(3))
    level0 = Style(level1)

    rendered, flattened = _render_rules(renderfuncs, [level0])

    assert rendered == "<sgr:7><sgr:3>"
    assert [type(r) for r in flattened] == [Sgr, Sgr]
    assert [r.args for r in flattened] == [[7], [3]]


def test_render_rules_mixed_rules():
    """Lines 55-58 combined with the RenderType branch in one pass."""
    renderfuncs = _mock_renderfuncs()

    nested = Style(Sgr(4))
    direct_first = Sgr(1)
    direct_last = RgbFg(2, 3, 4)
    rules = [direct_first, nested, direct_last]

    rendered, flattened = _render_rules(renderfuncs, rules)

    assert rendered == "<sgr:1><sgr:4><rgb:2,3,4>"
    assert [type(r) for r in flattened] == [Sgr, Sgr, RgbFg]
    assert [r.args for r in flattened] == [[1], [4], [2, 3, 4]]


def test_render_rules_invalid_rule_raises_value_error():
    """Line 61: a rule that is neither RenderType nor Style raises ValueError."""
    renderfuncs = _mock_renderfuncs()

    with pytest.raises(ValueError) as excinfo:
        _render_rules(renderfuncs, ["not-a-rule"])

    assert "Parameter 'rules' must be of type Iterable[Rule]." in str(excinfo.value)
