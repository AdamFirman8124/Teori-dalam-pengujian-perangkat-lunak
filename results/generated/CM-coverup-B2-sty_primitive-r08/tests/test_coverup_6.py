# file: project/sty/primitive.py:40-63
# asked: {"lines": [55, 56, 57, 58, 61], "branches": [[50, 55], [55, 56], [55, 61]]}
# gained: {"lines": [55, 56, 57, 58, 61], "branches": [[50, 55], [55, 56], [55, 61]]}

import pytest

from sty.primitive import Style, _render_rules
from sty.rendertype import RenderType, Sgr


class _FakeRenderType(RenderType):
    """Minimal concrete RenderType for testing."""

    def __init__(self, *args):
        self.args = list(args)


class TestRenderRulesMissingLines:
    def test_render_rules_with_style_rule(self):
        """Lines 55-58: a Style rule is recursively rendered and flattened."""
        renderfuncs = {
            Sgr: lambda *args: f"<sgr:{','.join(map(str, args))}>",
            _FakeRenderType: lambda *args: f"<fake:{','.join(map(str, args))}>",
        }

        fake_rule = _FakeRenderType("a")
        inner_sgr = Sgr(1)
        outer_sgr = Sgr(31)
        top_sgr = Sgr(4)

        inner_style = Style(inner_sgr, value="inner")
        outer_style = Style(fake_rule, inner_style, outer_sgr, value="outer")

        rendered, flattened = _render_rules(renderfuncs, [outer_style, top_sgr])

        # The nested Style's rules are rendered in order, followed by the
        # top-level Sgr rule.
        assert rendered == "<fake:a><sgr:1><sgr:31><sgr:4>"

        # Rules are flattened depth-first: outer Style's rules first
        # (with the nested Style replaced by its own rules), then the
        # top-level Sgr rule. The exact same rule objects are returned.
        assert flattened == [fake_rule, inner_sgr, outer_sgr, top_sgr]

    def test_render_rules_with_empty_style(self):
        """A Style with no rules contributes nothing to output or flattening."""
        renderfuncs = {Sgr: lambda *args: f"<sgr:{args[0]}>"}

        sgr_rule = Sgr(2)
        empty_style = Style(value="empty")
        rendered, flattened = _render_rules(renderfuncs, [empty_style, sgr_rule])

        assert rendered == "<sgr:2>"
        assert flattened == [sgr_rule]

    def test_render_rules_with_invalid_rule_raises(self):
        """Line 61: a rule that is neither RenderType nor Style raises ValueError."""
        renderfuncs = {Sgr: lambda *args: ""}

        with pytest.raises(ValueError) as excinfo:
            _render_rules(renderfuncs, ["not-a-rule"])

        assert str(excinfo.value) == (
            "Parameter 'rules' must be of type Iterable[Rule]."
        )

    def test_render_rules_mixed_valid_then_invalid(self):
        """Valid rules are processed before the invalid one triggers the error."""
        renderfuncs = {Sgr: lambda *args: f"<sgr:{args[0]}>"}

        with pytest.raises(ValueError):
            _render_rules(renderfuncs, [Sgr(1), 42])

    def test_render_rules_nested_style_error_propagates(self):
        """An invalid rule nested inside a Style also raises ValueError."""
        renderfuncs = {Sgr: lambda *args: ""}

        bad_style = Style(Sgr(1), 3.14, value="bad")

        with pytest.raises(ValueError):
            _render_rules(renderfuncs, [bad_style])
