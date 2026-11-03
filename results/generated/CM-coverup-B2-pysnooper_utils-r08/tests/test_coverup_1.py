# file: project/pysnooper/utils.py:10-20
# asked: {"lines": [11, 12, 13, 14, 15, 16, 17, 19, 20], "branches": [[12, 13], [12, 20], [13, 14], [13, 19], [14, 13], [14, 15], [15, 16], [15, 17]]}
# gained: {"lines": [11, 12, 13, 14, 15, 16, 17, 19, 20], "branches": [[12, 13], [12, 20], [13, 14], [13, 19], [14, 13], [14, 15], [15, 16], [15, 17]]}

import pytest

from pysnooper import utils


def test_check_methods_no_methods_returns_true():
    """No methods requested: the outer loop body never runs, returns True.

    Covers line 11 (mro lookup) and line 20 (return True).
    """

    class A:
        pass

    assert utils._check_methods(A) is True


def test_check_methods_method_defined_on_class():
    """Method found on the class itself and not None: returns True.

    Covers lines 11-14, the break on line 17, and line 20.
    """

    class A:
        def foo(self):
            pass

    assert utils._check_methods(A, 'foo') is True


def test_check_methods_method_found_in_base_class():
    """Method found on a base class via the MRO: returns True.

    Covers the MRO traversal on line 13 finding the method on a non-first
    class in the MRO.
    """

    class Base:
        def foo(self):
            pass

    class Child(Base):
        pass

    assert utils._check_methods(Child, 'foo') is True


def test_check_methods_method_found_on_object():
    """Method found on `object` (last MRO entry): returns True.

    Ensures the inner loop can run to the last MRO entry before breaking.
    """

    class A:
        pass

    assert utils._check_methods(A, '__repr__') is True


def test_check_methods_method_is_none_on_class():
    """Method present but set to None: returns NotImplemented.

    Covers lines 11-16 (the `is None` branch returning NotImplemented).
    """

    class A:
        foo = None

    assert utils._check_methods(A, 'foo') is NotImplemented


def test_check_methods_method_is_none_in_base_class():
    """Method present but None on a base class: returns NotImplemented.

    Covers lines 11-16 reached through MRO traversal.
    """

    class Base:
        foo = None

    class Child(Base):
        pass

    assert utils._check_methods(Child, 'foo') is NotImplemented


def test_check_methods_method_missing():
    """Method absent from the entire MRO: returns NotImplemented.

    Covers lines 11-14 and the for-else on lines 18-19.
    """

    class A:
        pass

    assert utils._check_methods(A, 'foo') is NotImplemented


def test_check_methods_first_found_then_missing():
    """After a successful lookup the outer loop continues; a later missing
    method still yields NotImplemented.

    Covers the break on line 17 followed by another iteration of the outer
    loop (line 12) that ends in the for-else (lines 18-19).
    """

    class A:
        def foo(self):
            pass

    assert utils._check_methods(A, 'foo', 'bar') is NotImplemented


def test_check_methods_all_methods_found():
    """All requested methods found and not None: returns True.

    Covers multiple iterations of the outer loop, each ending in a break
    (line 17), then falling through to line 20.
    """

    class A:
        def foo(self):
            pass

        def bar(self):
            pass

    assert utils._check_methods(A, 'foo', 'bar') is True


def test_check_methods_mro_order_decides_outcome():
    """The first class in the MRO that defines the method decides the result,
    regardless of what later classes define.
    """

    # Subclass defines a real method, base has None: subclass wins -> True.
    class BaseNone:
        foo = None

    class ChildReal(BaseNone):
        def foo(self):
            pass

    assert utils._check_methods(ChildReal, 'foo') is True

    # Subclass sets None, base has a real method: subclass wins -> NotImplemented.
    class BaseReal:
        def foo(self):
            pass

    class ChildNone(BaseReal):
        foo = None

    assert utils._check_methods(ChildNone, 'foo') is NotImplemented
