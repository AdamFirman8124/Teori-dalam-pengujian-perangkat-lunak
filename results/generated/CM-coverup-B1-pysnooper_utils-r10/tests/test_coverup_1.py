# file: project/pysnooper/utils.py:10-20
# asked: {"lines": [11, 12, 13, 14, 15, 16, 17, 19, 20], "branches": [[12, 13], [12, 20], [13, 14], [13, 19], [14, 13], [14, 15], [15, 16], [15, 17]]}
# gained: {"lines": [11, 12, 13, 14, 15, 16, 17, 19, 20], "branches": [[12, 13], [12, 20], [13, 14], [13, 19], [14, 13], [14, 15], [15, 16], [15, 17]]}

from pysnooper.utils import _check_methods


def test_no_methods_returns_true():
    class A:
        pass
    result = _check_methods(A)
    assert result is True


def test_present_methods_returns_true():
    class A:
        def foo(self):
            pass

        def bar(self):
            pass

    result = _check_methods(A, "foo", "bar")
    assert result is True


def test_missing_method_returns_not_implemented():
    class A:
        def foo(self):
            pass

    result = _check_methods(A, "nonexistent_method_xyz")
    assert result is NotImplemented


def test_none_method_returns_not_implemented():
    class A:
        foo = None

    result = _check_methods(A, "foo")
    assert result is NotImplemented


def test_inherited_method_returns_true():
    class Base:
        def foo(self):
            pass

    class Derived(Base):
        pass

    result = _check_methods(Derived, "foo")
    assert result is True


def test_object_method_requires_full_mro_traversal():
    class A:
        pass

    # '__str__' is defined on `object`, so loop must miss A then hit object
    assert "__str__" not in A.__dict__
    result = _check_methods(A, "__str__")
    assert result is True


def test_none_in_base_returns_not_implemented():
    class Base:
        foo = None

    class Derived(Base):
        pass

    assert "foo" not in Derived.__dict__
    result = _check_methods(Derived, "foo")
    assert result is NotImplemented


def test_multiple_methods_second_missing_returns_not_implemented():
    class A:
        def foo(self):
            pass

    result = _check_methods(A, "foo", "missing_xyz")
    assert result is NotImplemented


def test_multiple_methods_second_is_none_returns_not_implemented():
    class A:
        def foo(self):
            pass

        bar = None

    result = _check_methods(A, "foo", "bar")
    assert result is NotImplemented
