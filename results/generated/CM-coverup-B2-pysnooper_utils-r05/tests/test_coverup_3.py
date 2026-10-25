# file: project/pysnooper/utils.py:50-56
# asked: {"lines": [51, 52, 53, 54, 55, 56], "branches": [[51, 52], [51, 56], [52, 53], [52, 54], [54, 51], [54, 55]]}
# gained: {"lines": [51, 52, 53, 54, 55, 56], "branches": [[51, 52], [51, 56], [52, 53], [52, 54], [54, 51], [54, 55]]}

import pytest

from pysnooper import utils


def test_get_repr_function_with_type_condition_match():
    """When condition is a type, it's converted to an isinstance check."""
    class Foo(object):
        pass

    def action(x):
        return 'foo repr'

    result = utils.get_repr_function(Foo(), [(Foo, action)])
    assert result is action
    # Verify the converted condition really is an isinstance check:
    # a subclass of Foo must also match.
    class SubFoo(Foo):
        pass

    result_sub = utils.get_repr_function(SubFoo(), [(Foo, action)])
    assert result_sub is action


def test_get_repr_function_with_type_condition_no_match():
    """A type condition must not match an instance of another type."""
    class Foo(object):
        pass

    class Bar(object):
        pass

    def action(x):
        return 'foo repr'

    result = utils.get_repr_function(Bar(), [(Foo, action)])
    assert result is repr


def test_get_repr_function_with_callable_condition_match():
    """When condition is a plain callable, it is used as-is."""
    def condition(x):
        return x == 42

    def action(x):
        return 'answer repr'

    result = utils.get_repr_function(42, [(condition, action)])
    assert result is action


def test_get_repr_function_with_callable_condition_no_match():
    """A callable condition that returns False must be skipped."""
    def condition(x):
        return False

    def action(x):
        return 'never'

    result = utils.get_repr_function('anything', [(condition, action)])
    assert result is repr


def test_get_repr_function_empty_custom_repr():
    """With no custom_repr entries, the builtin repr is returned."""
    result = utils.get_repr_function(object(), [])
    assert result is repr


def test_get_repr_function_first_match_wins():
    """The first matching entry in custom_repr is used."""
    class Foo(object):
        pass

    def action1(x):
        return 'first'

    def action2(x):
        return 'second'

    result = utils.get_repr_function(Foo(), [(Foo, action1), (Foo, action2)])
    assert result is action1
