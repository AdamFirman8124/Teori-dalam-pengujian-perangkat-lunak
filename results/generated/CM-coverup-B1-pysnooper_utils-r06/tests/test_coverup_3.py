# file: project/pysnooper/utils.py:50-56
# asked: {"lines": [51, 52, 53, 54, 55, 56], "branches": [[51, 52], [51, 56], [52, 53], [52, 54], [54, 51], [54, 55]]}
# gained: {"lines": [51, 52, 53, 54, 55, 56], "branches": [[51, 52], [51, 56], [52, 53], [52, 54], [54, 51], [54, 55]]}

import pytest

from pysnooper.utils import get_repr_function


def test_get_repr_function_with_type_condition():
    """A type in custom_repr is converted to an isinstance check (lines 51-53)."""
    item = 'hello'
    repr_function = get_repr_function(item, [(str, lambda x: 'STR')])
    assert repr_function is not None
    assert repr_function(item) == 'STR'


def test_get_repr_function_with_callable_condition():
    """A callable condition is used directly (lines 54-55)."""
    item = 42
    repr_function = get_repr_function(
        item, [(lambda x: x > 10, lambda x: 'BIG')])
    assert repr_function(item) == 'BIG'


def test_get_repr_function_no_match_returns_repr():
    """When nothing matches, the builtin repr is returned (line 56)."""
    item = object()
    repr_function = get_repr_function(item, [(str, lambda x: 'STR')])
    assert repr_function is repr
    assert repr_function(item) == repr(item)


def test_get_repr_function_type_condition_checks_isinstance_not_identity():
    """The generated lambda checks isinstance, so subclasses match too."""
    class Base:
        pass

    class Child(Base):
        pass

    repr_function = get_repr_function(Child(), [(Base, lambda x: 'BASE')])
    assert repr_function(Child()) == 'BASE'
    assert repr_function(Base()) == 'BASE'


def test_get_repr_function_first_match_wins():
    """The first matching condition's action is returned."""
    item = 'hello'
    repr_function = get_repr_function(item, [
        (str, lambda x: 'FIRST'),
        (str, lambda x: 'SECOND'),
    ])
    assert repr_function(item) == 'FIRST'


def test_get_repr_function_empty_custom_repr_returns_repr():
    """An empty custom_repr falls through the loop to return repr."""
    item = 123
    repr_function = get_repr_function(item, [])
    assert repr_function is repr
    assert repr_function(item) == '123'
