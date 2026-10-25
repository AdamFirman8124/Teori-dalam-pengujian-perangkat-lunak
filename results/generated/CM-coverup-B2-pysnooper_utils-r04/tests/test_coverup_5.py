# file: project/pysnooper/utils.py:23-32
# asked: {"lines": [26, 30, 31, 32], "branches": [[30, 31], [30, 32]]}
# gained: {"lines": [26, 30, 31, 32], "branches": [[30, 31], [30, 32]]}

from pysnooper.utils import WritableStream


def test_writable_stream_abstract_write_body_executes_via_super():
    class ConcreteStream(WritableStream):
        def __init__(self):
            self.values = []

        def write(self, s):
            result = super().write(s)
            self.values.append(s)
            return result

    stream = ConcreteStream()

    assert stream.write("hello") is None
    assert stream.values == ["hello"]
    assert isinstance(stream, WritableStream)
    assert issubclass(ConcreteStream, WritableStream)


def test_subclasshook_returns_true_for_class_with_write():
    class HasWrite:
        def write(self, s):
            return s

    assert WritableStream.__subclasshook__(HasWrite) is True
    assert issubclass(HasWrite, WritableStream) is True
    assert isinstance(HasWrite(), WritableStream) is True


def test_subclasshook_returns_notimplemented_for_class_without_write():
    class NoWrite:
        pass

    assert WritableStream.__subclasshook__(NoWrite) is NotImplemented
    assert issubclass(NoWrite, WritableStream) is False
    assert isinstance(NoWrite(), WritableStream) is False


def test_subclasshook_returns_notimplemented_for_write_is_none():
    class WriteIsNone:
        write = None

    assert WritableStream.__subclasshook__(WriteIsNone) is NotImplemented
    assert issubclass(WriteIsNone, WritableStream) is False
    assert isinstance(WriteIsNone(), WritableStream) is False


def test_subclasshook_returns_notimplemented_when_cls_is_not_writablestream():
    class SubStream(WritableStream):
        def write(self, s):
            return s

    class Candidate:
        def write(self, s):
            return s

    assert SubStream.__subclasshook__(Candidate) is NotImplemented
    assert WritableStream.__subclasshook__(Candidate) is True
    assert issubclass(Candidate, SubStream) is False
    assert issubclass(SubStream, WritableStream) is True
