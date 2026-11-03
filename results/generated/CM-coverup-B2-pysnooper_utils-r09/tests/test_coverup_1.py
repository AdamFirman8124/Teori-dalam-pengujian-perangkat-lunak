# file: project/pysnooper/utils.py:10-20
# asked: {"lines": [11, 12, 13, 14, 15, 16, 17, 19, 20], "branches": [[12, 13], [12, 20], [13, 14], [13, 19], [14, 13], [14, 15], [15, 16], [15, 17]]}
# gained: {"lines": [11, 12, 13, 14, 15, 16, 17, 19, 20], "branches": [[12, 13], [12, 20], [13, 14], [13, 19], [14, 13], [14, 15], [15, 16], [15, 17]]}

import pytest

from pysnooper import utils


def test_check_methods_all_methods_present():
    """All requested methods are defined and not None -> True.

    Covers: line 11 (mro lookup), line 12 (methods loop), line 13 (mro loop),
    line 14 True branch, line 15 False branch, line 17 (break), line 20.
    """

    class Base:
        def foo(self):
            return 'foo'

    class Derived(Base):
        def bar(self):
            return 'bar'

    result = utils._check_methods(Derived, 'foo', 'bar')
    assert result is True


def test_check_methods_method_is_none_in_base():
    """A method explicitly set to None in a base class -> NotImplemented.

    Covers: line 14 False branch (skipped over Derived.__dict__),
    line 14 True branch, line 15 True branch, line 16 (return NotImplemented).
    """

    class Base:
        foo = None

    class Derived(Base):
        pass

    result = utils._check_methods(Derived, 'foo')
    assert result is NotImplemented


def test_check_methods_method_missing_entirely():
    """A method absent from every class in the MRO -> NotImplemented.

    Covers: line 14 False branch repeatedly, and the for/else on
    lines 18-19 (return NotImplemented when the inner loop exhausts).
    """

    class A:
        def foo(self):
            pass

    result = utils._check_methods(A, 'foo', 'missing')
    assert result is NotImplemented


def test_check_methods_found_in_later_mro_class():
    """Method missing from the subclass dicts but present in a base -> True.

    Covers: line 14 False branch (Derived and Middle dicts), then the
    True branch on Base, line 15 False branch, line 17, line 20.
    """

    class Base:
        def foo(self):
            pass

    class Middle(Base):
        pass

    class Derived(Middle):
        pass

    result = utils._check_methods(Derived, 'foo')
    assert result is True


def test_check_methods_no_methods_requested():
    """With no methods requested, the loop body never runs -> True.

    Covers: line 11, line 12 (loop entered but not iterated), line 20.
    """

    class A:
        pass

    result = utils._check_methods(A)
    assert result is True


def test_check_methods_none_shadows_defined_method():
    """A None in the subclass shadows a real definition in a base.

    Covers: line 14 True branch on the first MRO class, line 15 True
    branch, line 16 (return NotImplemented before reaching the base).
    """

    class Base:
        def foo(self):
            pass

    class Derived(Base):
        foo = None

    result = utils._check_methods(Derived, 'foo')
    assert result is NotImplemented


def test_check_methods_multiple_methods_mixed_outcomes():
    """First method found (break taken), second method is None.

    Exercises re-entry into the inner mro loop for a second method and
    both outcomes of the None check across iterations.
    """

    class Base:
        foo = None

    class Derived(Base):
        def bar(self):
            pass

    # 'bar' is found on Derived (break, line 17); 'foo' is None on Base
    # (line 16) after skipping Derived's dict (line 14 False branch).
    result = utils._check_methods(Derived, 'bar', 'foo')
    assert result is NotImplemented
