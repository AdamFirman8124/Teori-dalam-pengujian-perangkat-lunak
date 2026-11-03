# file: project/pysnooper/utils.py:50-56
# asked: {"lines": [51, 52, 53, 54, 55, 56], "branches": [[51, 52], [51, 56], [52, 53], [52, 54], [54, 51], [54, 55]]}
# gained: {"lines": [51, 52, 53, 54, 55, 56], "branches": [[51, 52], [51, 56], [52, 53], [52, 54], [54, 51], [54, 55]]}

"""
Tests for pysnooper.utils.get_repr_function, targeting the previously
uncovered lines 51-56:

    def get_repr_function(item, custom_repr):
        for condition, action in custom_repr:          # 51
            if isinstance(condition, type):            # 52
                condition = lambda x, y=condition: isinstance(x, y)  # 53
            if condition(item):                        # 54
                return action                          # 55
        return repr                                    # 56
"""

import pytest

from pysnooper import utils


class Foo:
    pass


class Bar:
    pass


def action_for_foo(item):
    return '<Foo custom repr>'


def action_for_bar(item):
    return '<Bar custom repr>'


def always_false(_):
    return False


def test_type_condition_matches_returns_action():
    """A type condition whose class matches the item yields its action
    (covers lines 51, 52-True, 53, 54-True, 55)."""
    custom_repr = ((Foo, action_for_foo),)
    item = Foo()
    result = utils.get_repr_function(item, custom_repr)
    assert result is action_for_foo
    # The returned function is what would be used to repr the item:
    assert result(item) == '<Foo custom repr>'


def test_type_condition_does_not_match_returns_repr():
    """A type condition whose class does not match the item is skipped and
    the builtin repr is returned (covers lines 51, 52-True, 53, 54-False,
    56)."""
    custom_repr = ((Foo, action_for_foo),)
    item = Bar()
    result = utils.get_repr_function(item, custom_repr)
    assert result is repr
    assert result(item) == repr(item)


def test_callable_condition_matches_returns_action():
    """A plain callable condition returning True yields its action
    (covers lines 51, 52-False, 54-True, 55)."""
    condition = lambda item: item == 42
    action = lambda item: 'the answer'
    custom_repr = ((condition, action),)
    result = utils.get_repr_function(42, custom_repr)
    assert result is action
    assert result(42) == 'the answer'


def test_callable_condition_does_not_match_returns_repr():
    """A plain callable condition returning False is skipped and the
    builtin repr is returned (covers lines 51, 52-False, 54-False, 56)."""
    custom_repr = ((always_false, action_for_foo),)
    item = 'anything'
    result = utils.get_repr_function(item, custom_repr)
    assert result is repr
    assert result(item) == repr(item)


def test_empty_custom_repr_returns_repr():
    """With no custom entries at all, the builtin repr is returned
    (covers line 51 with an exhausted loop, then 56)."""
    item = object()
    result = utils.get_repr_function(item, ())
    assert result is repr
    assert result(item) == repr(item)


def test_later_entry_matches_after_earlier_misses():
    """Iteration continues past non-matching entries until one matches
    (covers line 51 looping more than once, then 54-True/55)."""
    custom_repr = (
        (always_false, action_for_foo),
        (Foo, action_for_bar),
    )
    item = Foo()
    result = utils.get_repr_function(item, custom_repr)
    assert result is action_for_bar
    assert result(item) == '<Bar custom repr>'


def test_type_condition_lambda_binding():
    """Each type condition becomes its own isinstance check via the
    default-argument trick (no late-binding bug), and non-instances of any
    conditioned type fall back to repr (covers 53 for multiple types and
    54-False for the generated lambdas)."""
    custom_repr = ((Foo, action_for_foo), (Bar, action_for_bar))
    foo_item = Foo()
    bar_item = Bar()
    assert utils.get_repr_function(foo_item, custom_repr) is action_for_foo
    assert utils.get_repr_function(bar_item, custom_repr) is action_for_bar
    # An item that is an instance of neither type falls back to repr:
    neither = object()
    assert utils.get_repr_function(neither, custom_repr) is repr
    assert utils.get_repr_function(neither, custom_repr)(neither) == repr(neither)


def test_none_item_with_type_condition():
    """None is not an instance of the conditioned type, so repr is
    returned (covers 53-created lambda evaluating False)."""
    custom_repr = ((Foo, action_for_foo),)
    result = utils.get_repr_function(None, custom_repr)
    assert result is repr
    assert result(None) == 'None'


def test_integration_with_get_shortish_repr():
    """get_shortish_repr uses get_repr_function, so a matching custom
    entry changes the produced string (postcondition of the helper's
    contract)."""
    item = Foo()
    result = utils.get_shortish_repr(item, custom_repr=((Foo, action_for_foo),))
    assert result == '<Foo custom repr>'
    # Without a matching entry, the normal repr is used:
    result = utils.get_shortish_repr(item, custom_repr=((Bar, action_for_bar),))
    assert result == repr(item)
