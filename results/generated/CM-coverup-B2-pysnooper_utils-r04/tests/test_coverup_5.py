# file: project/pysnooper/utils.py:23-32
# asked: {"lines": [26, 30, 31, 32], "branches": [[30, 31], [30, 32]]}
# gained: {"lines": [26, 30, 31, 32], "branches": [[30, 31], [30, 32]]}

"""Tests for pysnooper.utils.WritableStream.

Covers the previously-unexecuted lines:
  - line 26:  the ``pass`` body of the abstract ``write`` method
  - line 30:  the ``if cls is WritableStream`` check in ``__subclasshook__``
  - line 31:  the ``return _check_methods(C, 'write')`` branch
  - line 32:  the ``return NotImplemented`` branch
"""

from pysnooper.utils import WritableStream


def test_abstract_write_body_executes_directly():
    """Line 26: calling the abstract ``write`` itself runs its ``pass`` body."""
    class Dummy:
        pass

    # Invoke the abstract method (not an override) with a dummy self.
    result = WritableStream.write(Dummy(), 'some text')

    assert result is None


def test_abstract_write_body_executes_via_inherited_method(monkeypatch):
    """Line 26: ``write`` reached through an instance of a subclass."""
    class PartiallyConcrete(WritableStream):
        pass

    # Allow instantiation even though ``write`` is still abstract; the
    # attribute is restored by monkeypatch after the test.
    monkeypatch.setattr(PartiallyConcrete, '__abstractmethods__', frozenset())

    stream = PartiallyConcrete()

    # ``write`` is inherited from WritableStream, so line 26 executes.
    assert stream.write('hello') is None


def test_subclasshook_positive_branch():
    """Lines 30-31: hook taken when ``cls is WritableStream`` and method found."""
    class HasWrite:
        def write(self, s):
            return s

    # ``issubclass`` invokes WritableStream.__subclasshook__(WritableStream, C).
    assert issubclass(HasWrite, WritableStream) is True

    # Same branch exercised directly through the bound classmethod.
    assert WritableStream.__subclasshook__(HasWrite) is True


def test_subclasshook_negative_branch():
    """Lines 30-31: hook taken when ``cls is WritableStream`` but method missing."""
    class LacksWrite:
        pass

    # _check_methods returns NotImplemented, so issubclass falls back to the
    # normal (negative) result.
    assert issubclass(LacksWrite, WritableStream) is False
    assert WritableStream.__subclasshook__(LacksWrite) is NotImplemented


def test_subclasshook_notimplemented_branch_for_foreign_cls():
    """Line 32: hook returns NotImplemented when ``cls`` is not WritableStream."""
    class Concrete(WritableStream):
        def write(self, s):
            return s

    class HasWrite:
        def write(self, s):
            return s

    # Direct call with a foreign ``cls`` deterministically hits line 32.
    underlying = WritableStream.__subclasshook__.__func__
    assert underlying(Concrete, Concrete) is NotImplemented
    assert underlying(Concrete, HasWrite) is NotImplemented

    # Through the public API: the hook is found on Concrete via the MRO but
    # invoked with cls=Concrete, so line 32 runs and issubclass falls back to
    # the regular subclass mechanism.
    assert issubclass(Concrete, Concrete) is True
    assert issubclass(HasWrite, Concrete) is False
    assert issubclass(int, Concrete) is False
