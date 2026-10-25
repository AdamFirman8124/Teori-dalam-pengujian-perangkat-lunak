# file: project/sty/primitive.py:40-63
# asked: {"lines": [55, 56, 57, 58, 61], "branches": [[50, 55], [55, 56], [55, 61]]}
# gained: {"lines": [55, 56, 57, 58, 61], "branches": [[50, 55], [55, 56], [55, 61]]}

import pytest

from sty.primitive import _render_rules, Style
from sty.rendertype import RenderType, Sgr


def test_render_rules_with_nested_style():
    """Lines 55-58: a Style rule is recursively rendered and flattened."""
    renderfuncs = {
        Sgr: lambda *args: "\x1b[{}m".format(";".join(str(a) for a in args)),
    }

    inner_rule = Sgr(1)
    outer_rule = Sgr(4)
    nested_style = Style(inner_rule, value="inner")
    top_style = Style(outer_rule, nested_style, value="outer")

    rendered, flattened = _render_rules(renderfuncs, [top_style])

    # Postconditions: rendered string contains both ANSI sequences in order,
    # and all nested rules were flattened into the result list.
    assert rendered == "\x1b[4m\x1b[1m"
    assert flattened == [outer_rule, inner_rule]
    assert all(isinstance(r, RenderType) for r in flattened)


def test_render_rules_with_empty_style():
    """Lines 55-58 with an empty Style: recursion returns empty results."""
    renderfuncs = {Sgr: lambda *args: "\x1b[{}m".format(args[0])}

    style = Style(value="empty")

    rendered, flattened = _render_rules(renderfuncs, [style])

    assert rendered == ""
    assert flattened == []


def test_render_rules_with_invalid_rule_raises():
    """Line 61: a rule that is neither RenderType nor Style raises ValueError."""
    renderfuncs = {Sgr: lambda *args: ""}

    with pytest.raises(ValueError) as excinfo:
        _render_rules(renderfuncs, ["not-a-rule"])

    assert "Parameter 'rules' must be of type Iterable[Rule]." in str(excinfo.value)
