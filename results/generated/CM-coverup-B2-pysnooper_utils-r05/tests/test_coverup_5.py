# file: project/pysnooper/utils.py:23-32
# asked: {"lines": [26, 30, 31, 32], "branches": [[30, 31], [30, 32]]}
# gained: {"lines": [26, 30, 31, 32], "branches": [[30, 31], [30, 32]]}

from pysnooper.utils import WritableStream


def test_write_body_returns_none():
    # Line 26: execute the `pass` body of the abstract `write`.
    assert WritableStream.__dict__["write"](object(), "hello") is None


def test_subclasshook_accepts_writer():
    # Lines 30-31: cls is WritableStream -> _check_methods returns True.
    class WithWrite:
        def write(self, s):
            return s

    assert WritableStream.__subclasshook__(WithWrite) is True
    assert issubclass(WithWrite, WritableStream) is True
    assert isinstance(WithWrite(), WritableStream) is True


def test_subclasshook_rejects_missing_write():
    # Lines 30-31 with the NotImplemented branch of _check_methods.
    class WithoutWrite:
        pass

    assert WritableStream.__subclasshook__(WithoutWrite) is NotImplemented
    assert issubclass(WithoutWrite, WritableStream) is False
    assert isinstance(WithoutWrite(), WritableStream) is False


def test_subclasshook_rejects_none_write():
    # Lines 30-31 with write = None -> _check_methods returns NotImplemented.
    class NoneWrite:
        write = None

    assert WritableStream.__subclasshook__(NoneWrite) is NotImplemented
    assert issubclass(NoneWrite, WritableStream) is False


def test_subclasshook_other_cls_returns_notimplemented():
    # Line 32: cls is not WritableStream -> return NotImplemented.
    class Concrete(WritableStream):
        def write(self, s):
            return s

    class WithWrite:
        def write(self, s):
            return s

    assert Concrete.__subclasshook__(WithWrite) is NotImplemented
    # Sanity: concrete subclass itself still works as a WritableStream.
    assert isinstance(Concrete(), WritableStream) is True
    assert Concrete().write("abcd") == "abcd"
