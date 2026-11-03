# file: project/pysnooper/utils.py:10-20
# asked: {"lines": [11, 12, 13, 14, 15, 16, 17, 19, 20], "branches": [[12, 13], [12, 20], [13, 14], [13, 19], [14, 13], [14, 15], [15, 16], [15, 17]]}
# gained: {"lines": [11, 12, 13, 14, 15, 16, 17, 19, 20], "branches": [[12, 13], [12, 20], [13, 14], [13, 19], [14, 13], [14, 15], [15, 16], [15, 17]]}

"""Tests for pysnooper.utils._check_methods, targeting full line and
branch coverage of the function (lines 11-20)."""

from pysnooper.utils import _check_methods


def test_all_methods_present_returns_true():
    """Lines 11-15 (False branch), 17, 20: every requested method is found
    and none of them is None, so the function returns True."""

    class C:
        def foo(self):
            pass

        def bar(self):
            pass

    result = _check_methods(C, 'foo', 'bar')
    assert result is True


def test_method_is_none_returns_not_implemented():
    """Lines 11-16: a requested method is present in the class __dict__ but
    its value is None (abstract), so the function returns NotImplemented."""

    class C:
        foo = None

    result = _check_methods(C, 'foo')
    assert result is NotImplemented


def test_method_absent_returns_not_implemented():
    """Lines 11-14 (False branch) and 19: the requested method is not found
    anywhere in the MRO, so the for-else clause returns NotImplemented."""

    class C:
        pass

    result = _check_methods(C, 'foo')
    assert result is NotImplemented


def test_method_found_in_base_class_returns_true():
    """Lines 13-14 (False for the class itself, True for the base), 17, 20:
    the method is not defined on the class but is found in a base class via
    the MRO."""

    class Base:
        def foo(self):
            pass

    class Child(Base):
        pass

    result = _check_methods(Child, 'foo')
    assert result is True


def test_none_method_in_base_class_returns_not_implemented():
    """Lines 13-16: the method is absent from the child class but present
    with a None value in a base class, so the function returns
    NotImplemented."""

    class Base:
        foo = None

    class Child(Base):
        pass

    result = _check_methods(Child, 'foo')
    assert result is NotImplemented


def test_first_method_found_second_missing_returns_not_implemented():
    """Lines 12-14, 17 (break after finding the first method) and 19 (else
    clause reached for the second method): a mixed outcome returns
    NotImplemented."""

    class C:
        def foo(self):
            pass

    result = _check_methods(C, 'foo', 'bar')
    assert result is NotImplemented


def test_no_methods_requested_returns_true():
    """Lines 11-12 (zero iterations of the methods loop) and 20: with no
    methods requested the function trivially returns True."""

    class C:
        pass

    result = _check_methods(C)
    assert result is True
