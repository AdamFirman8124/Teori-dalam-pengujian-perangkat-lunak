# file: project/pysnooper/utils.py:50-56
# asked: {"lines": [51, 52, 53, 54, 55, 56], "branches": [[51, 52], [51, 56], [52, 53], [52, 54], [54, 51], [54, 55]]}
# gained: {"lines": [51, 52, 53, 54, 55, 56], "branches": [[51, 52], [51, 56], [52, 53], [52, 54], [54, 51], [54, 55]]}

from pysnooper.utils import get_repr_function


def test_get_repr_function_matches_type_condition():
    def action(value):
        return f"integer: {value}"

    result = get_repr_function(42, [(int, action)])

    assert result is action
    assert result(42) == "integer: 42"


def test_get_repr_function_matches_callable_after_nonmatching_condition():
    calls = []

    def never_matches(item):
        calls.append(("never", item))
        return False

    def matches(item):
        calls.append(("matches", item))
        return item == "target"

    def action(value):
        return value.upper()

    result = get_repr_function(
        "target",
        [(never_matches, str), (matches, action)],
    )

    assert result is action
    assert result("target") == "TARGET"
    assert calls == [("never", "target"), ("matches", "target")]


def test_get_repr_function_returns_repr_when_no_condition_matches():
    result = get_repr_function(
        3.14,
        [
            (str, lambda value: value.upper()),
            (lambda item: item is None, lambda value: "none"),
        ],
    )

    assert result is repr
    assert result(3.14) == repr(3.14)
