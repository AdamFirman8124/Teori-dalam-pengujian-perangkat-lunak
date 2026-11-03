# file: project/pysnooper/utils.py:23-32
# asked: {"lines": [26, 30, 31, 32], "branches": [[30, 31], [30, 32]]}
# gained: {"lines": [26, 30, 31, 32], "branches": [[30, 31], [30, 32]]}

from pysnooper import utils


def test_subclasshook_true_for_class_with_write():
    """Lines 30 (True branch) and 31: cls is WritableStream, C provides 'write'."""

    class WithWrite:
        def write(self, s):
            return s

    # Direct hook call: cls is bound to WritableStream -> _check_methods -> True
    assert utils.WritableStream.__subclasshook__(WithWrite) is True
    # The natural issubclass() path consults the same hook (fresh class => cache miss)
    assert issubclass(WithWrite, utils.WritableStream) is True


def test_subclasshook_notimplemented_for_class_without_write():
    """Lines 30 (True branch) and 31: cls is WritableStream, C lacks 'write'."""

    class WithoutWrite:
        pass

    class NoneWrite:
        write = None  # _check_methods treats a None method as missing

    # Both cases make _check_methods return NotImplemented
    assert utils.WritableStream.__subclasshook__(WithoutWrite) is NotImplemented
    assert utils.WritableStream.__subclasshook__(NoneWrite) is NotImplemented
    # issubclass() falls back to the regular check and yields False
    assert issubclass(WithoutWrite, utils.WritableStream) is False
    assert issubclass(NoneWrite, utils.WritableStream) is False


def test_subclasshook_notimplemented_for_non_writablestream_cls():
    """Lines 30 (False branch) and 32: cls is a subclass, not WritableStream itself."""

    class Concrete(utils.WritableStream):
        def write(self, s):
            return s

    class Other:
        def write(self, s):
            return s

    # The inherited classmethod binds cls to Concrete, so the hook bails out
    assert Concrete.__subclasshook__(Other) is NotImplemented
    assert Concrete.__subclasshook__(Concrete) is NotImplemented
    # issubclass() falls back to the regular MRO-based check
    assert issubclass(Other, Concrete) is False
    assert issubclass(Concrete, Concrete) is True
    # Concrete still qualifies as a WritableStream through the hook (lines 30-31)
    assert issubclass(Concrete, utils.WritableStream) is True


def test_abstract_write_body_executes():
    """Line 26: the body (pass) of the abstract write method runs when called."""

    class Dummy:
        pass

    # Abstractness only blocks instantiation; the method itself is callable
    assert utils.WritableStream.write(Dummy(), 'hello') is None
