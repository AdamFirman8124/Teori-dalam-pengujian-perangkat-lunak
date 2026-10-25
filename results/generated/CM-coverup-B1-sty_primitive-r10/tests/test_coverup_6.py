# file: project/sty/primitive.py:40-63
# asked: {"lines": [55, 56, 57, 58, 61], "branches": [[50, 55], [55, 56], [55, 61]]}
# gained: {"lines": [55, 56, 57, 58, 61], "branches": [[50, 55], [55, 56], [55, 61]]}

import pytest

from sty.primitive import Style, _render_rules
from sty.rendertype import RenderType, RgbFg, Sgr


def test_render_rules_with_nested_style():
    """Lines 55-58: a Style rule is recursively rendered and flattened."""

    def render_sgr(num: int) -> str:
        return "\x1b[{}m".format(num)

    def render_rgbfg(r: int, g: int, b: int) -> str:
        return "\x1b[38;2;{};{};{}m".format(r, g, b)

    renderfuncs = {Sgr: render_sgr, RgbFg: render_rgbfg}

    rgb_rule = RgbFg(1, 5, 10)
    inner_rule = Sgr(1)
    last_rule = Sgr(4)
    inner_style = Style(rgb_rule, inner_rule)
    outer_style = Style(inner_style, last_rule)

    rendered, flattened = _render_rules(renderfuncs, [outer_style])

    # Postcondition: rendered string contains the ANSI sequences of all
    # nested rules, in order (innermost first).
    assert rendered == "\x1b[38;2;1;5;10m\x1b[1m\x1b[4m"

    # Postcondition: nested rules are flattened into a flat list of
    # RenderType instances, preserving order. RenderType does not define
    # __eq__, so compare by identity (same objects) and by type/args.
    assert flattened == [rgb_rule, inner_rule, last_rule]
    assert [type(r) for r in flattened] == [RgbFg, Sgr, Sgr]
    assert [r.args for r in flattened] == [[1, 5, 10], [1], [4]]
    assert all(isinstance(r, RenderType) for r in flattened)


def test_render_rules_invalid_rule_type_raises():
    """Line 61: a rule that is neither RenderType nor Style raises ValueError."""

    def render_sgr(num: int) -> str:
        return "\x1b[{}m".format(num)

    renderfuncs = {Sgr: render_sgr}

    with pytest.raises(ValueError) as excinfo:
        _render_rules(renderfuncs, ["not-a-rule"])

    assert "Parameter 'rules' must be of type Iterable[Rule]." in str(excinfo.value)


def test_render_rules_mixed_rules():
    """RenderType, Style and invalid rules can be mixed; the invalid one
    still triggers the error after valid ones are processed."""

    def render_sgr(num: int) -> str:
        return "\x1b[{}m".format(num)

    renderfuncs = {Sgr: render_sgr}

    with pytest.raises(ValueError):
        _render_rules(renderfuncs, [Sgr(1), Style(Sgr(2)), 42])
