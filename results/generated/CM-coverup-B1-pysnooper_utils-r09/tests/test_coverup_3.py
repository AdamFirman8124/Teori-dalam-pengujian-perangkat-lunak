# file: project/pysnooper/utils.py:50-56
# asked: {"lines": [51, 52, 53, 54, 55, 56], "branches": [[51, 52], [51, 56], [52, 53], [52, 54], [54, 51], [54, 55]]}
# gained: {"lines": [51, 52, 53, 54, 55, 56], "branches": [[51, 52], [51, 56], [52, 53], [52, 54], [54, 51], [54, 55]]}

import pytest

from pysnooper import utils


class Foo(object):
    pass


class Bar(object):
    pass


def test_get_repr_function_with_type_condition():
    """A type in custom_repr is converted to an isinstance check."""
    custom_repr = ((Foo, lambda x: 'foo!'),)
    result = utils.get_repr_function(Foo(), custom_repr)
    assert result is not None
    assert result(Foo()) == 'foo!'


def test_get_repr_function_with_type_condition_no_match():
    """A type condition that doesn't match falls through to the next entry."""
    custom_repr = ((Foo, lambda x: 'foo!'), (Bar, lambda x: 'bar!'))
    result = utils.get_repr_function(Bar(), custom_repr)
    assert result(Bar()) == 'bar!'


def test_get_repr_function_with_callable_condition():
    """A plain callable condition is used as-is."""
    custom_repr = ((lambda x: x == 42, lambda x: 'the answer'),)
    result = utils.get_repr_function(42, custom_repr)
    assert result(42) == 'the answer'


def test_get_repr_function_no_match_returns_repr():
    """When no condition matches, the builtin repr is returned."""
    custom_repr = ((Foo, lambda x: 'foo!'),)
    result = utils.get_repr_function('hello', custom_repr)
    assert result is repr
    assert result('hello') == repr('hello')
