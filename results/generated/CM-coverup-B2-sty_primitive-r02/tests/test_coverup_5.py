# file: project/sty/primitive.py:40-63
# asked: {"lines": [55, 56, 57, 58, 61], "branches": [[50, 55], [55, 56], [55, 61]]}
# gained: {"lines": [55, 56, 57, 58, 61], "branches": [[50, 55], [55, 56], [55, 61]]}

import pytest

from sty.primitive import Style, _render_rules
from sty.rendertype import RgbFg, Sgr


def _make_renderfuncs():
    return {
        Sgr: lambda num: f"\x1b[{num}m",
        RgbFg: lambda r, g, b: f"\x1b[38;2;{r};{g};{b}m",
    }


def test_render_rules_with_single_style():
    renderfuncs = _make_renderfuncs()
    sgr = Sgr(1)
    rgb = RgbFg(1, 5, 10)
    style = Style(sgr, rgb)

    rendered, flattened = _render_rules(renderfuncs, [style])

    assert rendered == "\x1b[1m\x1b[38;2;1;5;10m"
    assert list(flattened) == [sgr, rgb]
    assert style not in list(flattened)


def test_render_rules_with_nested_style_flattens_recursively():
    renderfuncs = _make_renderfuncs()
    sgr_bold = Sgr(1)
    sgr_dim = Sgr(2)
    rgb = RgbFg(10, 20, 30)
    inner = Style(sgr_bold, rgb)
    outer = Style(inner, sgr_dim)

    rendered, flattened = _render_rules(renderfuncs, [outer])

    assert rendered == "\x1b[1m\x1b[38;2;10;20;30m\x1b[2m"
    assert list(flattened) == [sgr_bold, rgb, sgr_dim]


def test_render_rules_with_mixed_rendertype_and_style():
    renderfuncs = _make_renderfuncs()
    top = Sgr(4)
    nested_sgr = Sgr(1)
    rgb = RgbFg(1, 2, 3)
    style = Style(nested_sgr, rgb)

    rendered, flattened = _render_rules(renderfuncs, [top, style])

    assert rendered == "\x1b[4m\x1b[1m\x1b[38;2;1;2;3m"
    assert list(flattened) == [top, nested_sgr, rgb]


def test_render_rules_with_empty_style():
    renderfuncs = _make_renderfuncs()
    style = Style()

    rendered, flattened = _render_rules(renderfuncs, [style])

    assert rendered == ""
    assert list(flattened) == []


def test_render_rules_with_deeply_nested_empty_and_nonempty_styles():
    renderfuncs = _make_renderfuncs()
    sgr = Sgr(7)
    outer = Style(Style(), Style(Style(sgr)))

    rendered, flattened = _render_rules(renderfuncs, [outer])

    assert rendered == "\x1b[7m"
    assert list(flattened) == [sgr]


@pytest.mark.parametrize("bad_rule", [123, 3.14, "plain-string", None, object(), ["nested-list"]])
def test_render_rules_with_invalid_rule_raises_value_error(bad_rule):
    renderfuncs = _make_renderfuncs()

    with pytest.raises(
        ValueError,
        match=r"Parameter 'rules' must be of type Iterable\[Rule\]\.",
    ):
        _render_rules(renderfuncs, [bad_rule])


def test_render_rules_with_invalid_rule_inside_style_raises_value_error():
    renderfuncs = _make_renderfuncs()
    style = Style(Sgr(1), 999)  # type: ignore[arg-type]

    with pytest.raises(
        ValueError,
        match=r"Parameter 'rules' must be of type Iterable\[Rule\]\.",
    ):
        _render_rules(renderfuncs, [style])


def test_render_rules_with_invalid_rule_after_valid_rule_raises_value_error():
    renderfuncs = _make_renderfuncs()

    with pytest.raises(
        ValueError,
        match=r"Parameter 'rules' must be of type Iterable\[Rule\]\.",
    ):
        _render_rules(renderfuncs, [Sgr(1), Style(Sgr(2)), "bad"])  # type: ignore[list-item]
