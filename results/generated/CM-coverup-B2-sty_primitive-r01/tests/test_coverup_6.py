# file: project/sty/primitive.py:40-63
# asked: {"lines": [55, 56, 57, 58, 61], "branches": [[50, 55], [55, 56], [55, 61]]}
# gained: {"lines": [55, 56, 57, 58, 61], "branches": [[50, 55], [55, 56], [55, 61]]}

import pytest

from sty.primitive import Style, _render_rules
from sty.rendertype import RenderType


class _FakeRenderType(RenderType):
    """Minimal concrete RenderType for testing."""

    def __init__(self, *args):
        self.args = args


def test_render_rules_with_style():
    """Lines 55-58: a Style rule is recursively rendered and flattened."""
    inner_rule = _FakeRenderType("inner")
    outer_rule = _FakeRenderType("outer")
    style = Style(inner_rule, value="\x1b[1m")

    renderfuncs = {
        _FakeRenderType: lambda *args: "<{}>".format("-".join(args)),
    }

    rendered, flattened = _render_rules(renderfuncs, [style])

    # The inner rule of the Style was rendered and appended to the output.
    assert rendered == "<inner>"
    # The inner rule was flattened into the result list.
    assert flattened == [inner_rule]
    # The Style object itself must NOT appear in the flattened rules.
    assert outer_rule not in flattened
    assert style not in flattened
    # Style is still a valid str subclass carrying its rules.
    assert isinstance(style, Style)
    assert isinstance(style, str)
    assert style.rules == (inner_rule,)


def test_render_rules_invalid_rule_raises():
    """Line 61: a rule that is neither RenderType nor Style raises ValueError."""
    renderfuncs = {_FakeRenderType: lambda *args: ""}

    with pytest.raises(ValueError) as excinfo:
        _render_rules(renderfuncs, ["not-a-rule"])

    assert "Parameter 'rules' must be of type Iterable[Rule]." in str(excinfo.value)


def test_render_rules_mixed_rules():
    """Both branches together: RenderType, Style, and invalid rule ordering."""
    rule_a = _FakeRenderType("a")
    rule_b = _FakeRenderType("b")
    style = Style(rule_b)

    renderfuncs = {
        _FakeRenderType: lambda *args: "<{}>".format("-".join(args)),
    }

    rendered, flattened = _render_rules(renderfuncs, [rule_a, style])

    assert rendered == "<a><b>"
    assert flattened == [rule_a, rule_b]

    # Invalid rule after valid ones still raises, and no state leaks out.
    with pytest.raises(ValueError):
        _render_rules(renderfuncs, [rule_a, 12345])
