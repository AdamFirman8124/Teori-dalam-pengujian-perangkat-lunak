# file: project/sty/primitive.py:40-63
# asked: {"lines": [55, 56, 57, 58, 61], "branches": [[50, 55], [55, 56], [55, 61]]}
# gained: {"lines": [55, 56, 57, 58, 61], "branches": [[50, 55], [55, 56], [55, 61]]}

import pytest

from sty.primitive import Style, _render_rules
from sty.rendertype import RenderType


def test_render_rules_recursively_renders_and_flattens_styles():
    class DummyRenderType(RenderType):
        def __init__(self, value):
            self.args = [value]

    first = DummyRenderType("first")
    second = DummyRenderType("second")
    nested_style = Style(first, Style(second))
    renderfuncs = {DummyRenderType: lambda value: f"<{value}>"}

    rendered, flattened = _render_rules(renderfuncs, [nested_style])

    assert rendered == "<first><second>"
    assert list(flattened) == [first, second]


def test_render_rules_rejects_invalid_rule():
    invalid_rule = object()

    with pytest.raises(
        ValueError,
        match=r"^Parameter 'rules' must be of type Iterable\[Rule\]\.$",
    ):
        _render_rules({}, [invalid_rule])
