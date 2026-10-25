# file: project/sty/primitive.py:40-63
# asked: {"lines": [55, 56, 57, 58, 61], "branches": [[50, 55], [55, 56], [55, 61]]}
# gained: {"lines": [55, 56, 57, 58, 61], "branches": [[50, 55], [55, 56], [55, 61]]}

import pytest

from sty.primitive import Style, _render_rules
from sty.rendertype import Sgr


def test_render_rules_flattens_nested_style():
    first_rule = Sgr(1)
    second_rule = Sgr(4)
    style = Style(first_rule, Style(second_rule))

    rendered, flattened_rules = _render_rules(
        {Sgr: lambda value: f"<{value}>"},
        [style],
    )

    assert rendered == "<1><4>"
    assert list(flattened_rules) == [first_rule, second_rule]


def test_render_rules_rejects_invalid_rule():
    invalid_rule = object()

    with pytest.raises(ValueError) as exc_info:
        _render_rules({}, [invalid_rule])

    assert str(exc_info.value) == (
        "Parameter 'rules' must be of type Iterable[Rule]."
    )
