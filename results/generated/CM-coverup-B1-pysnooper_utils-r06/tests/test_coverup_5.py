# file: project/pysnooper/utils.py:23-32
# asked: {"lines": [26, 30, 31, 32], "branches": [[30, 31], [30, 32]]}
# gained: {"lines": [26, 30, 31, 32], "branches": [[30, 31], [30, 32]]}

from pysnooper.utils import WritableStream


def test_writable_stream_write_pass_executes():
    class Concrete(WritableStream):
        def __init__(self):
            self.written = []

        def write(self, s):
            result = super().write(s)
            assert result is None
            self.written.append(s)

    obj = Concrete()
    assert isinstance(obj, WritableStream)
    obj.write("hello")
    assert obj.written == ["hello"]
    # Directly exercise base implementation (line 26: pass)
    assert WritableStream.write(obj, "hi") is None


def test_subclasshook_duck_type_with_write_returns_true():
    class DuckWithWrite:
        def write(self, s):
            pass

    # Direct call exercises lines 30-31
    assert WritableStream.__subclasshook__(DuckWithWrite) is True
    # issubclass / isinstance go through ABCMeta -> __subclasshook__
    assert issubclass(DuckWithWrite, WritableStream) is True
    assert isinstance(DuckWithWrite(), WritableStream) is True


def test_subclasshook_missing_write_returns_notimplemented():
    class NoWrite:
        pass

    assert WritableStream.__subclasshook__(NoWrite) is NotImplemented
    assert issubclass(NoWrite, WritableStream) is False
    assert isinstance(NoWrite(), WritableStream) is False


def test_subclasshook_none_write_returns_notimplemented():
    class NoneWrite:
        write = None

    assert WritableStream.__subclasshook__(NoneWrite) is NotImplemented
    assert issubclass(NoneWrite, WritableStream) is False


def test_subclasshook_cls_is_not_writablestream_returns_notimplemented():
    class SubStream(WritableStream):
        def write(self, s):
            super().write(s)

    class Dummy:
        def write(self, s):
            pass

    # cls is SubStream, not WritableStream -> exercises line 32
    assert SubStream.__subclasshook__(Dummy) is NotImplemented
    # Normal inheritance still works for real subclass
    assert issubclass(SubStream, WritableStream) is True
    assert isinstance(SubStream(), WritableStream) is True
