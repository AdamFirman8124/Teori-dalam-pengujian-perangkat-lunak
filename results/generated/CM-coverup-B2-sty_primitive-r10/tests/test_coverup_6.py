# file: project/sty/primitive.py:40-63
# asked: {"lines": [55, 56, 57, 58, 61], "branches": [[50, 55], [55, 56], [55, 61]]}
# gained: {"lines": [55, 56, 57, 58, 61], "branches": [[50, 55], [55, 56], [55, 61]]}

from typing import Callable, Dict, List, Tuple

import pytest

from sty.primitive import Style, _render_rules
from sty.rendertype import RenderType, Sgr, RgbFg


def _sgr_render(num: int) -> str:
    return "\x1b[{}m".format(num)


def _rgb_fg_render(r: int, g: int, b: int) -> str:
    return "\x1b[38;2;{};{};{}m".format(r, g, b)


def _rules_equal(actual: list, expected: list) -> bool:
    """
    RenderType instances do not implement __eq__, so compare them by
    type and args instead of identity.
    """
    if len(actual) != len(expected):
        return False
    for a, e in zip(actual, expected):
        if type(a) is not type(e) or list(a.args) != list(e.args):
            return False
    return True


def test_render_rules_with_style_rule() -> None:
    """
    Covers lines 55-58: a Style instance inside 'rules' triggers the
    recursive branch. The nested Style contains RenderType rules whose
    rendered output must be concatenated and whose rules must be
    flattened into the result.
    """
    renderfuncs: Dict[type, Callable] = {
        Sgr: _sgr_render,
        RgbFg: _rgb_fg_render,
    }

    # A Style wrapping two RenderType rules.
    inner_style = Style(Sgr(1), RgbFg(1, 5, 10), value="inner")

    # A top-level list mixing a plain RenderType and the Style.
    rules = [Sgr(4), inner_style]

    rendered, flattened = _render_rules(renderfuncs, rules)

    # Postcondition: rendered string contains the top-level rule output
    # followed by the recursively rendered Style rules, in order.
    assert rendered == "\x1b[4m" + "\x1b[1m" + "\x1b[38;2;1;5;10m"

    # Postcondition: the nested Style's rules are flattened (not the
    # Style itself) and preserve order, after the top-level RenderType.
    # Compare by type and args, since RenderType has no __eq__.
    assert _rules_equal(flattened, [Sgr(4), Sgr(1), RgbFg(1, 5, 10)])
    assert all(isinstance(r, RenderType) for r in flattened)
    assert not any(isinstance(r, Style) for r in flattened)


def test_render_rules_with_nested_styles() -> None:
    """
    Covers lines 55-58 again, with a Style nested inside another Style,
    to make sure the recursion handles arbitrary depth and that the
    flattening extends through multiple levels.
    """
    renderfuncs: Dict[type, Callable] = {Sgr: _sgr_render}

    inner = Style(Sgr(7), value="inner")
    outer = Style(inner, Sgr(2), value="outer")

    rendered, flattened = _render_rules(renderfuncs, [outer])

    assert rendered == "\x1b[7m\x1b[2m"
    assert _rules_equal(flattened, [Sgr(7), Sgr(2)])


def test_render_rules_with_invalid_rule_raises() -> None:
    """
    Covers line 61: a rule that is neither a RenderType nor a Style
    must raise a ValueError with the documented message.
    """
    renderfuncs: Dict[type, Callable] = {Sgr: _sgr_render}

    with pytest.raises(ValueError) as excinfo:
        _render_rules(renderfuncs, [Sgr(1), "not-a-rule"])  # type: ignore[list-item]

    assert str(excinfo.value) == "Parameter 'rules' must be of type Iterable[Rule]."


def test_render_rules_empty_rules() -> None:
    """
    Sanity check for the base case: an empty iterable returns an empty
    string and an empty list. Also guards against state pollution
    between calls, since the function builds fresh containers each run.
    """
    renderfuncs: Dict[type, Callable] = {Sgr: _sgr_render}

    rendered: str
    flattened: List[RenderType]
    rendered, flattened = _render_rules(renderfuncs, [])

    assert rendered == ""
    assert flattened == []
