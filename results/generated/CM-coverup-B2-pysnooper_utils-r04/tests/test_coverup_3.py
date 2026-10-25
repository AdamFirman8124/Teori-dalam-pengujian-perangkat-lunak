# file: project/pysnooper/utils.py:50-56
# asked: {"lines": [51, 52, 53, 54, 55, 56], "branches": [[51, 52], [51, 56], [52, 53], [52, 54], [54, 51], [54, 55]]}
# gained: {"lines": [51, 52, 53, 54, 55, 56], "branches": [[51, 52], [51, 56], [52, 53], [52, 54], [54, 51], [54, 55]]}

from pysnooper.utils import get_repr_function


def test_get_repr_function_matches_type_condition():
    action = lambda value: f"integer: {value}"

    result = get_repr_function(42, [(int, action)])

    assert result is action
    assert result(42) == "integer: 42"


def test_get_repr_function_matches_callable_after_failed_condition():
    first_action = lambda value: "first"
    matching_action = lambda value: value.upper()
    custom_repr = [
        (lambda value: value.startswith("missing"), first_action),
        (lambda value: value == "match", matching_action),
    ]

    result = get_repr_function("match", custom_repr)

    assert result is matching_action
    assert result("match") == "MATCH"


def test_get_repr_function_returns_repr_when_no_condition_matches():
    custom_repr = [
        (int, lambda value: f"integer: {value}"),
        (lambda value: value == "other", lambda value: "other"),
    ]

    result = get_repr_function("unmatched", custom_repr)

    assert result is repr
    assert result("unmatched") == "'unmatched'"
