# file: project/pysnooper/utils.py:50-56
# asked: {"lines": [51, 52, 53, 54, 55, 56], "branches": [[51, 52], [51, 56], [52, 53], [52, 54], [54, 51], [54, 55]]}
# gained: {"lines": [51, 52, 53, 54, 55, 56], "branches": [[51, 52], [51, 56], [52, 53], [52, 54], [54, 51], [54, 55]]}

from pysnooper.utils import get_repr_function


def test_type_condition_match():
    """A condition that is a type is converted to an isinstance check (lines 52-53),
    matches the item, and its action is returned (lines 54-55)."""
    action = lambda x: 'custom str repr'
    custom_repr = [(str, action)]
    result = get_repr_function('hello', custom_repr)
    assert result is action
    assert result('hello') == 'custom str repr'


def test_callable_condition_match():
    """A condition that is a plain callable (not a type) is used as-is
    (line 52 False branch), matches, and its action is returned."""
    action = lambda x: 'big number'
    custom_repr = [(lambda x: x > 3, action)]
    result = get_repr_function(5, custom_repr)
    assert result is action
    assert result(5) == 'big number'


def test_callable_condition_no_match():
    """A callable condition that returns False does not match (line 54 False
    branch), so the builtin repr is returned (line 56)."""
    action = lambda x: 'big number'
    custom_repr = [(lambda x: x > 3, action)]
    result = get_repr_function(2, custom_repr)
    assert result is repr
    assert result(2) == '2'


def test_type_condition_no_match_returns_repr():
    """A type condition that does not match falls through and the builtin
    repr is returned (line 56)."""
    custom_repr = [(int, lambda x: 'int repr')]
    result = get_repr_function('hello', custom_repr)
    assert result is repr
    assert result('hello') == "'hello'"


def test_empty_custom_repr_returns_repr():
    """An empty custom_repr list means the loop body never runs (line 51
    zero-iteration branch) and builtin repr is returned (line 56)."""
    item = object()
    result = get_repr_function(item, [])
    assert result is repr
    assert result(item) == repr(item)


def test_multiple_type_conditions_late_binding():
    """Each type condition is bound correctly via the default argument in the
    generated lambda (line 53), so earlier entries do not shadow later ones."""
    int_action = lambda x: 'int repr'
    str_action = lambda x: 'str repr'
    custom_repr = [(int, int_action), (str, str_action)]
    assert get_repr_function('hello', custom_repr) is str_action
    assert get_repr_function(42, custom_repr) is int_action
    # An item matching neither type falls through to builtin repr.
    assert get_repr_function(3.5, custom_repr) is repr
    assert get_repr_function(3.5, custom_repr)(3.5) == '3.5'
