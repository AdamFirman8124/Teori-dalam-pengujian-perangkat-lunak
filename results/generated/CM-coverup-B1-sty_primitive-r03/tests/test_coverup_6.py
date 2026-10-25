# file: project/sty/primitive.py:40-63
# asked: {"lines": [55, 56, 57, 58, 61], "branches": [[50, 55], [55, 56], [55, 61]]}
# gained: {"lines": [55, 56, 57, 58, 61], "branches": [[50, 55], [55, 56], [55, 61]]}

from typing import Callable, Dict, List, Tuple

import pytest

from sty.primitive import Style, _render_rules
from sty.rendertype import RenderType


class _DummyRenderType(RenderType):
    """Minimal concrete RenderType used only for testing."""

    def __init__(self, *args) -> None:
        self.args = list(args)


def test_render_rules_with_nested_style() -> None:
    """Covers lines 55-58: the Style branch, including recursion."""

    def render_dummy(*args) -> str:
        return "<{}>".format(",".join(str(a) for a in args))

    renderfuncs: Dict[type, Callable] = {_DummyRenderType: render_dummy}

    inner_rule = _DummyRenderType("inner")
    nested_style = Style(inner_rule)
    outer_rule = _DummyRenderType("outer")

    rendered, flattened = _render_rules(renderfuncs, [outer_rule, nested_style])

    # Postcondition: rendered string contains both inner and outer renders,
    # in order (outer first, then the nested style's inner rule).
    assert rendered == "<outer><inner>"
    # Postcondition: rules are flattened in the same order.
    assert flattened == [outer_rule, inner_rule]
    # Postcondition: the Style instance itself is not included in the output.
    assert nested_style not in flattened


def test_render_rules_invalid_rule_raises_value_error() -> None:
    """Covers line 61: the else branch raising ValueError."""

    renderfuncs: Dict[type, Callable] = {}

    with pytest.raises(ValueError) as excinfo:
        _render_rules(renderfuncs, ["not-a-rule"])  # type: ignore[list-item]

    assert "Parameter 'rules' must be of type Iterable[Rule]." in str(excinfo.value)


def test_render_rules_empty_input() -> None:
    """Sanity check for the base case (no rules): empty results, no pollution."""

    rendered, flattened = _render_rules({}, [])

    assert rendered == ""
    assert flattened == []
    assert isinstance(flattened, list)
