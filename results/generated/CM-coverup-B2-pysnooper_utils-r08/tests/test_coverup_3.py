# file: project/pysnooper/utils.py:50-56
# asked: {"lines": [51, 52, 53, 54, 55, 56], "branches": [[51, 52], [51, 56], [52, 53], [52, 54], [54, 51], [54, 55]]}
# gained: {"lines": [51, 52, 53, 54, 55, 56], "branches": [[51, 52], [51, 56], [52, 53], [52, 54], [54, 51], [54, 55]]}

"""
Tests for pysnooper.utils.get_repr_function.

These tests execute the previously-uncovered lines 51-56 and all of their
branches:

* line 51      - iterating over ``custom_repr`` (both non-empty and empty)
* lines 52-53  - ``condition`` being a *type* (converted to an isinstance lambda)
* line 52 else - ``condition`` being a plain callable (no conversion)
* lines 54-55  - a matching condition short-circuits and returns its action
* line 54 else - a non-matching condition falls through to the next entry
* line 56      - no condition matches -> the builtin ``repr`` is returned

The tests are pure: they never mutate pysnooper state or any global, so no
monkeypatching / mocking cleanup is required.
"""

import pytest

from pysnooper.utils import get_repr_function


class Foo:
    """Arbitrary class used as a *type* condition."""


class Bar:
    """A second, distinct class used as a *type* condition."""


def test_matching_type_condition_returns_its_action():
    """A type condition that matches returns the paired action (lines 51-55)."""
    def action(item):
        return 'foo-repr'

    item = Foo()
    result = get_repr_function(item, [(Foo, action)])

    # Postconditions: the exact action is returned, and it works on the item.
    assert result is action
    assert result(item) == 'foo-repr'


def test_non_matching_type_condition_falls_through_to_later_entry():
    """A type condition that does not match is skipped (line 54 False branch)."""
    foo_action = lambda item: 'foo-repr'
    fallback_action = lambda item: 'fallback-repr'
    custom_repr = [(Foo, foo_action), (lambda item: True, fallback_action)]

    result = get_repr_function(Bar(), custom_repr)

    # Postconditions: the first (non-matching) action is NOT returned; the
    # later matching callable-condition entry wins.
    assert result is not foo_action
    assert result is fallback_action
    assert result(Bar()) == 'fallback-repr'


def test_matching_callable_condition_returns_its_action():
    """A plain-callable condition skips the isinstance-lambda conversion
    (line 52 False branch) and returns its action when it matches."""
    action = lambda item: 'callable-repr'
    condition = lambda item: item.startswith('a')

    result = get_repr_function('abc', [(condition, action)])

    assert result is action
    assert result('abc') == 'callable-repr'


def test_each_type_condition_is_bound_to_its_own_type():
    """Exercises line 53's ``lambda x, y=condition`` default-argument trick:
    two type conditions must each test against their own class, not the last
    one iterated (late-binding bug guard)."""
    foo_action = lambda item: 'foo-repr'
    bar_action = lambda item: 'bar-repr'
    custom_repr = [(Foo, foo_action), (Bar, bar_action)]

    assert get_repr_function(Foo(), custom_repr) is foo_action
    assert get_repr_function(Bar(), custom_repr) is bar_action
    assert get_repr_function(Foo(), custom_repr)(Foo()) == 'foo-repr'
    assert get_repr_function(Bar(), custom_repr)(Bar()) == 'bar-repr'


def test_no_matching_condition_returns_builtin_repr():
    """When every condition rejects the item, the builtin ``repr`` is
    returned (line 56)."""
    custom_repr = [
        (Foo, lambda item: 'foo-repr'),          # type condition, won't match
        (lambda item: False, lambda item: 'never'),  # callable condition, won't match
    ]

    result = get_repr_function(42, custom_repr)

    # Postconditions: builtin repr is returned and behaves like repr.
    assert result is repr
    assert result(42) == '42'
    assert result('abc') == "'abc'"


def test_empty_custom_repr_returns_builtin_repr():
    """An empty ``custom_repr`` iterates zero times (line 51 with an empty
    loop) and falls straight through to ``return repr`` (line 56)."""
    sentinel = object()

    result = get_repr_function(sentinel, [])

    assert result is repr
    assert result(sentinel) == repr(sentinel)
