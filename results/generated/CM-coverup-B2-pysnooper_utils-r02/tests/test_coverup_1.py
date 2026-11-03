# file: project/pysnooper/utils.py:10-20
# asked: {"lines": [11, 12, 13, 14, 15, 16, 17, 19, 20], "branches": [[12, 13], [12, 20], [13, 14], [13, 19], [14, 13], [14, 15], [15, 16], [15, 17]]}
# gained: {"lines": [11, 12, 13, 14, 15, 16, 17, 19, 20], "branches": [[12, 13], [12, 20], [13, 14], [13, 19], [14, 13], [14, 15], [15, 16], [15, 17]]}

"""Tests for pysnooper.utils._check_methods (the previously uncovered lines 11-20).

The helper implements the standard ``__subclasshook__`` logic:

* ``True``            -- every requested method is defined (not ``None``) somewhere in ``C``'s MRO;
* ``NotImplemented``  -- some requested method is explicitly set to ``None`` in the MRO;
* ``NotImplemented``  -- some requested method is missing from every class in the MRO.

The function under test is pure and every class used below is created inside
its own test function, so no global state is created and no monkeypatching is
required; everything is garbage-collected when each test ends.
"""

import abc

from pysnooper.utils import _check_methods


def test_all_methods_defined_directly_returns_true():
    # Covers: mro lookup, outer loop over several methods, inner loop
    # hitting the first MRO entry, non-None attribute -> break, final True.
    class Base:
        def foo(self):
            return 'foo'

        def bar(self):
            return 'bar'

    class Derived(Base):
        pass

    result = _check_methods(Derived, 'foo', 'bar')
    assert result is True


def test_method_found_only_in_base_class_returns_true():
    # Covers the inner loop skipping MRO entries that lack the method
    # (the False branch of `if method in B.__dict__`) before breaking.
    class Base:
        def foo(self):
            return 'foo'

    class Derived(Base):
        pass

    result = _check_methods(Derived, 'foo')
    assert result is True


def test_method_in_subclass_shadows_base_returns_true():
    # Covers `break` happening on the very first MRO entry.
    class Base:
        def foo(self):
            return 'base'

    class Derived(Base):
        def foo(self):
            return 'derived'

    result = _check_methods(Derived, 'foo')
    assert result is True


def test_method_is_none_on_class_itself_returns_not_implemented():
    # Covers the `B.__dict__[method] is None` -> return NotImplemented branch.
    class C:
        foo = None

    result = _check_methods(C, 'foo')
    assert result is NotImplemented


def test_method_is_none_in_base_class_returns_not_implemented():
    # None marker found in a *later* MRO entry: the inner loop must first
    # skip Derived (False branch) and then take the None branch in Base.
    class Base:
        foo = None

    class Derived(Base):
        pass

    result = _check_methods(Derived, 'foo')
    assert result is NotImplemented


def test_none_marker_in_earlier_mro_entry_wins():
    # The first MRO entry that has the attribute decides: a None marker in
    # Derived shadows the real method in Base -> NotImplemented.
    class Base:
        def foo(self):
            return 'foo'

    class Derived(Base):
        foo = None

    result = _check_methods(Derived, 'foo')
    assert result is NotImplemented


def test_real_method_in_earlier_mro_entry_wins():
    # Conversely, a real method in Derived means Base's None marker is never
    # consulted (break happens first) -> True.
    class Base:
        foo = None

    class Derived(Base):
        def foo(self):
            return 'foo'

    result = _check_methods(Derived, 'foo')
    assert result is True


def test_missing_method_returns_not_implemented():
    # Covers the for/else: the inner loop exhausts the whole MRO without
    # finding 'does_not_exist' -> return NotImplemented.
    class Base:
        def foo(self):
            return 'foo'

    class Derived(Base):
        pass

    result = _check_methods(Derived, 'foo', 'does_not_exist')
    assert result is NotImplemented


def test_later_method_is_none_returns_not_implemented():
    # Covers the outer loop continuing after a successful method ('foo')
    # and then hitting the None branch on the second method ('bar').
    class C:
        def foo(self):
            return 'foo'

        bar = None

    result = _check_methods(C, 'foo', 'bar')
    assert result is NotImplemented


def test_no_methods_requested_returns_true():
    # Covers the zero-iteration branch of the outer `for method in methods`
    # loop, falling straight through to `return True`.
    class C:
        pass

    result = _check_methods(C)
    assert result is True


def test_check_methods_through_subclasshook():
    # Exercises the function in its intended context: an ABCMeta
    # __subclasshook__, verifying real issubclass() outcomes.
    class Readable(metaclass=abc.ABCMeta):
        @classmethod
        def __subclasshook__(cls, other):
            if cls is Readable:
                return _check_methods(other, 'read', 'close')
            return NotImplemented

    class Good:
        def read(self):
            return 'data'

        def close(self):
            pass

    class MissingMethod:
        def read(self):
            return 'data'

    class NoneMethod:
        read = None

        def close(self):
            pass

    assert issubclass(Good, Readable) is True
    assert issubclass(MissingMethod, Readable) is False
    assert issubclass(NoneMethod, Readable) is False
    assert issubclass(int, Readable) is False
