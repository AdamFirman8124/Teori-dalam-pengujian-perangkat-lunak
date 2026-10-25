# file: project/pysnooper/utils.py:50-56
# asked: {"lines": [51, 52, 53, 54, 55, 56], "branches": [[51, 52], [51, 56], [52, 53], [52, 54], [54, 51], [54, 55]]}
# gained: {"lines": [51, 52, 53, 54, 55, 56], "branches": [[51, 52], [51, 56], [52, 53], [52, 54], [54, 51], [54, 55]]}

import pytest

from pysnooper import utils


class Dummy:
    pass


class Other:
    pass


def test_get_repr_function_with_class_condition():
    """A bare class in custom_repr is converted to an isinstance check."""
    custom_repr = [(Dummy, lambda x: 'dummy-repr')]
    func = utils.get_repr_function(Dummy(), custom_repr)
    assert func is custom_repr[0][1]
    assert func(Dummy()) == 'dummy-repr'


def test_get_repr_function_with_callable_condition():
    """A callable condition is used as-is."""
    condition = lambda x: isinstance(x, Other)
    action = lambda x: 'other-repr'
    custom_repr = [(condition, action)]
    func = utils.get_repr_function(Other(), custom_repr)
    assert func is action
    assert func(Other()) == 'other-repr'


def test_get_repr_function_no_match_returns_repr():
    """When no condition matches, the builtin repr is returned."""
    custom_repr = [(Dummy, lambda x: 'dummy-repr')]
    func = utils.get_repr_function(Other(), custom_repr)
    assert func is repr
    obj = Other()
    assert func(obj) == repr(obj)


def test_get_repr_function_empty_custom_repr_returns_repr():
    """With an empty custom_repr, builtin repr is returned."""
    func = utils.get_repr_function(object(), [])
    assert func is repr
    obj = object()
    assert func(obj) == repr(obj)


def test_get_repr_function_first_match_wins():
    """The first matching entry in custom_repr takes precedence."""
    custom_repr = [
        (Dummy, lambda x: 'first'),
        (Dummy, lambda x: 'second'),
    ]
    func = utils.get_repr_function(Dummy(), custom_repr)
    assert func(Dummy()) == 'first'
