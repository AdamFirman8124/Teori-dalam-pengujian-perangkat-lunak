# file: project/pysnooper/utils.py:10-20
# asked: {"lines": [11, 12, 13, 14, 15, 16, 17, 19, 20], "branches": [[12, 13], [12, 20], [13, 14], [13, 19], [14, 13], [14, 15], [15, 16], [15, 17]]}
# gained: {"lines": [11, 12, 13, 14, 15, 16, 17, 19, 20], "branches": [[12, 13], [12, 20], [13, 14], [13, 19], [14, 13], [14, 15], [15, 16], [15, 17]]}

"""Tests for pysnooper.utils._check_methods, covering lines 11-20 and all branches."""

from pysnooper.utils import _check_methods


class _Defined:
    """Class with all methods properly defined."""

    def foo(self):
        return 'foo'

    def bar(self):
        return 'bar'


class _Abstract:
    """Class with a method explicitly set to None (abstract-style)."""

    foo = None


class _ChildOfAbstract(_Abstract):
    """Inherits foo = None from _Abstract; defines its own bar."""

    def bar(self):
        return 'bar'


class _Parent:
    def foo(self):
        return 'foo'


class _Child(_Parent):
    """Does not define foo itself; it lives in _Parent.__dict__."""


def test_check_methods_all_defined_returns_true():
    """All requested methods are defined on the class itself: returns True.

    Covers: line 11 (mro), line 12 (outer loop), line 13 (inner loop),
    line 14 True branch, line 15 False branch, line 17 (break),
    and line 20 (return True).
    """
    result = _check_methods(_Defined, 'foo', 'bar')
    assert result is True


def test_check_methods_missing_method_returns_not_implemented():
    """A requested method missing from the entire MRO: for-else fires.

    Covers: line 14 False branch for every B in the MRO,
    and line 19 (return NotImplemented from the else clause).
    """
    result = _check_methods(_Defined, 'foo', 'definitely_not_defined')
    assert result is NotImplemented


def test_check_methods_none_attribute_returns_not_implemented():
    """A method explicitly set to None on the class itself.

    Covers: line 14 True branch, line 15 True branch,
    and line 16 (return NotImplemented).
    """
    result = _check_methods(_Abstract, 'foo')
    assert result is NotImplemented


def test_check_methods_none_inherited_returns_not_implemented():
    """A None method found on a base class while walking the MRO.

    Covers: line 14 False branch on the subclass itself, then True on the
    base, line 15 True branch, and line 16 (return NotImplemented).
    """
    result = _check_methods(_ChildOfAbstract, 'foo')
    assert result is NotImplemented


def test_check_methods_inherited_defined_method_returns_true():
    """Method defined only on a base class: inner loop breaks, returns True.

    Covers: line 14 False branch on the subclass, True branch on the base,
    line 15 False branch, line 17 (break), and line 20 (return True).
    """
    result = _check_methods(_Child, 'foo')
    assert result is True


def test_check_methods_no_methods_requested_returns_true():
    """Empty method list: outer loop never runs, returns True immediately.

    Covers: line 12 zero-iteration branch and line 20 (return True).
    """
    result = _check_methods(_Defined)
    assert result is True
