# file: project/pysnooper/utils.py:10-20
# asked: {"lines": [11, 12, 13, 14, 15, 16, 17, 19, 20], "branches": [[12, 13], [12, 20], [13, 14], [13, 19], [14, 13], [14, 15], [15, 16], [15, 17]]}
# gained: {"lines": [11, 12, 13, 14, 15, 16, 17, 19, 20], "branches": [[12, 13], [12, 20], [13, 14], [13, 19], [14, 13], [14, 15], [15, 16], [15, 17]]}

from pysnooper import utils


def test_no_methods_returns_true():
    """With no requested methods the outer loop never runs -> True (line 20)."""
    class Anything:
        pass

    result = utils._check_methods(Anything)
    assert result is True


def test_all_methods_present_returns_true():
    """Every requested method exists as a real (non-None) attribute -> True.

    Covers: line 11, outer loop (12), inner MRO loop (13), hit branch of
    line 14, false branch of line 15, break (17), and final return (20),
    including the outer loop continuing after a break.
    """
    class WithMethods:
        def foo(self):
            return 'foo'

        def bar(self):
            return 'bar'

    result = utils._check_methods(WithMethods, 'foo', 'bar')
    assert result is True


def test_method_found_in_base_class_via_mro():
    """Method absent from the class dict but present in a base -> True.

    Covers the inner loop continuing past line 14's false branch before
    finding the method further along the MRO.
    """
    class Base:
        def foo(self):
            pass

    class Derived(Base):
        pass

    result = utils._check_methods(Derived, 'foo')
    assert result is True


def test_abstract_method_returns_not_implemented():
    """A method whose value is None (abstract) -> NotImplemented (line 16)."""
    class Abstract:
        foo = None

    result = utils._check_methods(Abstract, 'foo')
    assert result is NotImplemented


def test_missing_method_returns_not_implemented():
    """Method found nowhere in the MRO -> for-else fires -> NotImplemented.

    Covers lines 18-19 (the else clause of the inner loop).
    """
    class Empty:
        pass

    result = utils._check_methods(Empty, 'foo')
    assert result is NotImplemented


def test_first_method_found_second_missing():
    """Break on the first method (17), then the second is missing (18-19)."""
    class Partial:
        def foo(self):
            pass

    result = utils._check_methods(Partial, 'foo', 'bar')
    assert result is NotImplemented


def test_first_method_found_second_abstract():
    """Break on the first method (17), then hit a None method (15-16)."""
    class Mixed:
        def foo(self):
            pass

        bar = None

    result = utils._check_methods(Mixed, 'foo', 'bar')
    assert result is NotImplemented


def test_abstract_method_short_circuits_before_later_methods():
    """A None method returns immediately, never inspecting later methods."""
    class Abstract:
        foo = None

        def bar(self):
            pass

    result = utils._check_methods(Abstract, 'foo', 'bar')
    assert result is NotImplemented


def test_concrete_method_shadows_abstract_base_method():
    """A concrete override earlier in the MRO wins over None in a base."""
    class Base:
        foo = None

    class Derived(Base):
        def foo(self):
            pass

    result = utils._check_methods(Derived, 'foo')
    assert result is True


def test_abstract_override_in_derived_class_wins():
    """A None earlier in the MRO wins over a concrete base implementation."""
    class Base:
        def foo(self):
            pass

    class Derived(Base):
        foo = None

    result = utils._check_methods(Derived, 'foo')
    assert result is NotImplemented
