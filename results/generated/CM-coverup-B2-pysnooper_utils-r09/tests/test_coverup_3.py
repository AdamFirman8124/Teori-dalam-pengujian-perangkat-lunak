# file: project/pysnooper/utils.py:50-56
# asked: {"lines": [51, 52, 53, 54, 55, 56], "branches": [[51, 52], [51, 56], [52, 53], [52, 54], [54, 51], [54, 55]]}
# gained: {"lines": [51, 52, 53, 54, 55, 56], "branches": [[51, 52], [51, 56], [52, 53], [52, 54], [54, 51], [54, 55]]}

import pytest

from pysnooper import utils


def test_get_repr_function_type_condition_matches():
    """A condition given as a type is converted to an isinstance check (lines 52-53),
    and when the item is an instance of that type, its action is returned (lines 54-55)."""

    class Foo:
        pass

    foo_action = lambda x: 'foo repr'
    custom_repr = [(Foo, foo_action)]

    result = utils.get_repr_function(Foo(), custom_repr)

    assert result is foo_action
    assert result(Foo()) == 'foo repr'


def test_get_repr_function_type_condition_skipped_then_callable_matches():
    """A type condition that does not match is skipped, and a later callable
    condition that matches returns its action."""

    class Foo:
        pass

    foo_action = lambda x: 'foo repr'
    answer_action = lambda x: 'answer repr'
    custom_repr = [(Foo, foo_action), (lambda x: x == 42, answer_action)]

    result = utils.get_repr_function(42, custom_repr)

    assert result is answer_action
    assert result(42) == 'answer repr'


def test_get_repr_function_callable_condition_used_directly():
    """A callable condition is used as-is (line 52's isinstance check is False),
    and when it matches, its action is returned."""

    is_answer = lambda x: x == 42
    answer_action = lambda x: 'answer repr'
    custom_repr = [(is_answer, answer_action)]

    result = utils.get_repr_function(42, custom_repr)

    assert result is answer_action
    assert result(42) == 'answer repr'


def test_get_repr_function_no_match_returns_builtin_repr():
    """When no condition matches, the built-in repr is returned (line 56)."""

    class Foo:
        pass

    custom_repr = [(Foo, lambda x: 'foo repr')]

    result = utils.get_repr_function(42, custom_repr)

    assert result is repr
    assert result(42) == '42'
    assert result('abc') == "'abc'"


def test_get_repr_function_empty_custom_repr_returns_builtin_repr():
    """With an empty custom_repr list, the built-in repr is returned (line 56)."""

    result = utils.get_repr_function(object(), [])

    assert result is repr
    assert result(3.5) == '3.5'
