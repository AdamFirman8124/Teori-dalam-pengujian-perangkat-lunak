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

    assert utils._check_methods(A, "foo", "bar") is True


def test_check_methods_inherited_method_returns_true():
    class Base:
        def foo(self):
            pass

    class Child(Base):
        pass

    # 'foo' is not in Child.__dict__ but is found in the MRO
    assert utils._check_methods(Child, "foo") is True


def test_check_methods_missing_method_returns_not_implemented():
    class A:
        def foo(self):
            pass

    result = utils._check_methods(A, "foo", "bar")
    assert result is NotImplemented


def test_check_methods_none_value_returns_not_implemented():
    # A method explicitly set to None in the class body (e.g. an
    # abstract/undefined method) must trigger the NotImplemented branch.
    class A:
        foo = None

    result = utils._check_methods(A, "foo")
    assert result is NotImplemented


def test_check_methods_none_in_base_class_returns_not_implemented():
    class Base:
        foo = None

    class Child(Base):
        pass

    result = utils._check_methods(Child, "foo")
    assert result is NotImplemented


def test_check_methods_no_methods_requested_returns_true():
    class A:
        pass

    # With no methods to check, the outer loop body never runs and
    # the function falls through to the final return.
    assert utils._check_methods(A) is True
