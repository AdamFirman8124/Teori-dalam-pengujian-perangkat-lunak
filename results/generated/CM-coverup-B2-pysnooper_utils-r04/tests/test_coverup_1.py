# file: project/pysnooper/utils.py:10-20
# asked: {"lines": [11, 12, 13, 14, 15, 16, 17, 19, 20], "branches": [[12, 13], [12, 20], [13, 14], [13, 19], [14, 13], [14, 15], [15, 16], [15, 17]]}
# gained: {"lines": [11, 12, 13, 14, 15, 16, 17, 19, 20], "branches": [[12, 13], [12, 20], [13, 14], [13, 19], [14, 13], [14, 15], [15, 16], [15, 17]]}

import pytest

from pysnooper.utils import _check_methods


def test_all_methods_defined_returns_true():
    """All requested methods are defined (not None) in the class itself:
    covers mro lookup, the 'found and not None' break path, and final True."""
    class Base:
        def foo(self):
            pass

        def bar(self):
            pass

    class Child(Base):
        pass

    result = _check_methods(Child, 'foo', 'bar')
    assert result is True


def test_method_missing_from_mro_returns_not_implemented():
    """Method appears in no class of the mro: covers the for-else
    (lines 18-19) returning NotImplemented."""
    class Empty:
        pass

    result = _check_methods(Empty, 'missing_method')
    assert result is NotImplemented


def test_method_is_none_returns_not_implemented():
    """Method found in the class dict but set to None: covers the
    'is None' branch returning NotImplemented (lines 15-16)."""
    class WithNone:
        foo = None

    result = _check_methods(WithNone, 'foo')
    assert result is NotImplemented


def test_method_none_in_base_class_returns_not_implemented():
    """None method found in a base class while scanning the mro:
    covers the mro loop continuing past classes that lack the method."""
    class Base:
        foo = None

    class Child(Base):
        pass

    result = _check_methods(Child, 'foo')
    assert result is NotImplemented


def test_inherited_concrete_method_returns_true():
    """Method defined only in a base class (not the queried class):
    the mro loop must skip Child's dict and break on Base's dict."""
    class Base:
        def foo(self):
            pass

    class Child(Base):
        pass

    result = _check_methods(Child, 'foo')
    assert result is True


def test_first_method_ok_second_is_none_returns_not_implemented():
    """Multiple methods: first one is found fine (break), second one is
    None, so the outer loop iterates more than once before failing."""
    class Mixed:
        def foo(self):
            pass

        bar = None

    result = _check_methods(Mixed, 'foo', 'bar')
    assert result is NotImplemented


def test_first_method_missing_second_ok_returns_not_implemented():
    """Multiple methods: first one is missing entirely (for-else fires),
    so the function must short-circuit before ever examining the second."""
    class Partial:
        def bar(self):
            pass

    result = _check_methods(Partial, 'missing', 'bar')
    assert result is NotImplemented


def test_no_methods_requested_returns_true():
    """Empty *methods: the outer loop body never runs, returning True
    directly (lines 11 and 20 only)."""
    class Whatever:
        pass

    result = _check_methods(Whatever)
    assert result is True


def test_child_override_shadows_none_in_base():
    """Child defines a real method that shadows a None entry in the base:
    the break must happen at Child before Base's None is ever seen."""
    class Base:
        foo = None

    class Child(Base):
        def foo(self):
            pass

    result = _check_methods(Child, 'foo')
    assert result is True


def test_none_found_before_concrete_in_mro_order():
    """Mro order matters: the first class in the mro holding the method
    wins, so a None earlier in the mro causes NotImplemented even though
    a later base defines it concretely."""
    class GrandBase:
        def foo(self):
            pass

    class Middle(GrandBase):
        foo = None

    class Child(Middle):
        pass

    result = _check_methods(Child, 'foo')
    assert result is NotImplemented
