# file: project/sty/primitive.py:40-63
# asked: {"lines": [55, 56, 57, 58, 61], "branches": [[50, 55], [55, 56], [55, 61]]}
# gained: {"lines": [55, 56, 57, 58, 61], "branches": [[50, 55], [55, 56], [55, 61]]}

import pytest

from sty.primitive import Style, _render_rules
from sty.rendertype import RenderType


def test_render_rules_recursively_flattens_nested_styles():
    class ExampleRule(RenderType):
        pass

    rule = ExampleRule()
    rule.args = [2, 3]
    nested_style = Style(Style(rule, value="ignored"), value="also ignored")
    renderfuncs = {ExampleRule: lambda left, right: f"<{left + right}>"}

    rendered, flattened_rules = _render_rules(renderfuncs, [nested_style])

    assert rendered == "<5>"
    assert list(flattened_rules) == [rule]


def test_render_rules_rejects_invalid_rule():
    invalid_rule = object()

    with pytest.raises(
        ValueError,
        match=r"^Parameter 'rules' must be of type Iterable\[Rule\]\.$",
    ):
        _render_rules({}, [invalid_rule])
