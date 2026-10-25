# file: project/pysnooper/utils.py:50-56
# asked: {"lines": [51, 52, 53, 54, 55, 56], "branches": [[51, 52], [51, 56], [52, 53], [52, 54], [54, 51], [54, 55]]}
# gained: {"lines": [51, 52, 53, 54, 55, 56], "branches": [[51, 52], [51, 56], [52, 53], [52, 54], [54, 51], [54, 55]]}

from pysnooper.utils import get_repr_function


def test_empty_custom_repr_returns_repr():
    assert get_repr_function(123, []) is repr
    assert get_repr_function("abc", ()) is repr


def test_type_condition_match_returns_action():
    def my_action(x):
        return "custom:{}".format(x)

    result = get_repr_function(42, [(int, my_action)])
    assert result is my_action
    assert result(42) == "custom:42"


def test_type_condition_no_match_returns_repr():
    def my_action(x):
        return "custom"

    result = get_repr_function("hello", [(int, my_action)])
    assert result is repr
    assert result("hello") == repr("hello")


def test_callable_condition_match_returns_action():
    def my_action(x):
        return "big:{}".format(x)

    result = get_repr_function(10, [(lambda x: x > 5, my_action)])
    assert result is my_action
    assert result(10) == "big:10"


def test_callable_condition_no_match_returns_repr():
    def my_action(x):
        return "big"

    result = get_repr_function(3, [(lambda x: x > 5, my_action)])
    assert result is repr


def test_mixed_conditions_first_miss_second_hit():
    def action_str(x):
        return "str-action"

    def action_int(x):
        return "int-action"

    custom_repr = [
        (str, action_str),
        (lambda x: isinstance(x, int) and x > 100, action_int),
    ]
    assert get_repr_function(200, custom_repr) is action_int
    assert get_repr_function("hi", custom_repr) is action_str
    # neither matches -> falls through to repr (covers loop-exhausted branch)
    assert get_repr_function(50, custom_repr) is repr


def test_multiple_type_conditions_closure_correctness():
    def action_int(x):
        return "int"

    def action_str(x):
        return "str"

    custom_repr = [(int, action_int), (str, action_str)]
    assert get_repr_function(99, custom_repr) is action_int
    assert get_repr_function("hi", custom_repr) is action_str
    assert get_repr_function(3.14, custom_repr) is repr
