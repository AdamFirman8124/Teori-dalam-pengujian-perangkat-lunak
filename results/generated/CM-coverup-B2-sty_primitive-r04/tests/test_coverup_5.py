# file: project/sty/primitive.py:40-63
# asked: {"lines": [55, 56, 57, 58, 61], "branches": [[50, 55], [55, 56], [55, 61]]}
# gained: {"lines": [55, 56, 57, 58, 61], "branches": [[50, 55], [55, 56], [55, 61]]}

import pytest

from sty.primitive import Style, _render_rules
from sty.rendertype import RenderType


def test_render_rules_flattens_nested_styles():
    class ExampleRule(RenderType):
        def __init__(self, *args):
            self.args = args

    first = ExampleRule("first")
    second = ExampleRule("second")
    rules = [Style(first, Style(second))]
    renderfuncs = {ExampleRule: lambda value: f"<{value}>"}

    rendered, flattened = _render_rules(renderfuncs, rules)

    assert rendered == "<first><second>"
    assert list(flattened) == [first, second]


def test_render_rules_rejects_invalid_rule():
    with pytest.raises(
        ValueError,
        match=r"^Parameter 'rules' must be of type Iterable\[Rule\]\.$",
    ):
        _render_rules({}, [object()])
