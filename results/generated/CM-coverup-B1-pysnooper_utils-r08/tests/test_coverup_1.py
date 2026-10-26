# file: project/pysnooper/utils.py:10-20
# asked: {"lines": [11, 12, 13, 14, 15, 16, 17, 19, 20], "branches": [[12, 13], [12, 20], [13, 14], [13, 19], [14, 13], [14, 15], [15, 16], [15, 17]]}
# gained: {"lines": [11, 12, 13, 14, 15, 16, 17, 19, 20], "branches": [[12, 13], [12, 20], [13, 14], [13, 19], [14, 13], [14, 15], [15, 16], [15, 17]]}

import pytest

from pysnooper import utils


def test_check_methods_all_present_returns_true():
    class A:
        def foo(self):
            pass

        def bar(self):
            pass

    class B(A):
        pass

    assert utils._check_methods(B, "foo", "bar") is True


def test_check_methods_method_is_none_returns_not_implemented():
    class A:
        foo = None

    class B(A):
        pass

    assert utils._check_methods(B, "foo") is NotImplemented


def test_check_methods_method_missing_returns_not_implemented():
    class A:
        pass

    assert utils._check_methods(A, "foo") is NotImplemented


def test_check_methods_found_in_mro_base_class():
    class Base:
        def foo(self):
            pass

    class Derived(Base):
        pass

    assert utils._check_methods(Derived, "foo") is True


def test_check_methods_none_in_mro_shadows_missing_method():
    class A:
        foo = None

    class B(A):
        pass

    class C(B):
        pass

    # 'foo' is found in A.__dict__ as None -> NotImplemented,
    # exercising the break + None branch rather than the for-else.
    assert utils._check_methods(C, "foo") is NotImplemented


def test_check_methods_multiple_methods_first_missing():
    class A:
        def bar(self):
            pass

    # 'foo' missing -> NotImplemented returned before 'bar' is checked
    assert utils._check_methods(A, "foo", "bar") is NotImplemented
