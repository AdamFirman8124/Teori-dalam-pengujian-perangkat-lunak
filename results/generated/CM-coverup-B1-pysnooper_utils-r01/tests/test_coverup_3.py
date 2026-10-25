# file: project/pysnooper/utils.py:50-56
# asked: {"lines": [51, 52, 53, 54, 55, 56], "branches": [[51, 52], [51, 56], [52, 53], [52, 54], [54, 51], [54, 55]]}
# gained: {"lines": [51, 52, 53, 54, 55, 56], "branches": [[51, 52], [51, 56], [52, 53], [52, 54], [54, 51], [54, 55]]}

from pysnooper.utils import get_repr_function


def test_get_repr_function_returns_action_for_matching_type():
    def action(value):
        return f"integer: {value}"

    selected = get_repr_function(42, [(int, action)])

    assert selected is action
    assert selected(42) == "integer: 42"


def test_get_repr_function_returns_repr_when_condition_does_not_match():
    calls = []

    def condition(value):
        calls.append(value)
        return False

    def action(value):
        return "unused"

    selected = get_repr_function("value", [(condition, action)])

    assert selected is repr
    assert selected("value") == "'value'"
    assert calls == ["value"]
