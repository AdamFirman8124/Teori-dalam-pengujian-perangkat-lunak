# file: project/pysnooper/utils.py:90-95
# asked: {"lines": [91, 92, 93, 95], "branches": [[91, 93], [91, 95]]}
# gained: {"lines": [91, 92, 93, 95], "branches": [[91, 93], [91, 95]]}

"""Tests targeting the uncovered lines 91-95 of pysnooper/utils.py (ensure_tuple).

Coverage plan:
- Lines 91-93 (if-branch taken): pass an Iterable that is NOT a string
  (a list and a lazy iterable/range), so ``tuple(x)`` executes.
- Lines 91-92 + 95 (else-branch via second condition): pass a string,
  which IS Iterable but also a string_type, so ``(x,)`` is returned.
- Line 91 short-circuit + 95 (else-branch via first condition): pass a
  non-iterable object (int / None), so the ``and`` short-circuits.

``ensure_tuple`` is a pure function: it creates no files, mutates no
module-level state and performs no I/O, so no monkeypatching/teardown
is required and no state can leak between tests.
"""

from pysnooper import utils


def test_ensure_tuple_iterable_non_string_returns_tuple_of_items():
    """Lines 91-93: Iterable + not a string -> elements are unpacked."""
    result = utils.ensure_tuple([1, 2, 3])
    assert result == (1, 2, 3)
    assert isinstance(result, tuple)


def test_ensure_tuple_lazy_iterable_returns_tuple_of_items():
    """Lines 91-93 again, using a non-sequence iterable (range)."""
    result = utils.ensure_tuple(range(4))
    assert result == (0, 1, 2, 3)
    assert isinstance(result, tuple)


def test_ensure_tuple_string_is_wrapped_not_unpacked():
    """Lines 91-92 (second condition True) and line 95: strings stay whole."""
    result = utils.ensure_tuple('abc')
    assert result == ('abc',)
    assert isinstance(result, tuple)


def test_ensure_tuple_non_iterable_is_wrapped():
    """Line 91 short-circuit (not Iterable) and line 95: value is wrapped."""
    result = utils.ensure_tuple(42)
    assert result == (42,)
    assert isinstance(result, tuple)


def test_ensure_tuple_none_is_wrapped():
    """Line 91 short-circuit and line 95: None is not Iterable either."""
    result = utils.ensure_tuple(None)
    assert result == (None,)
    assert isinstance(result, tuple)
