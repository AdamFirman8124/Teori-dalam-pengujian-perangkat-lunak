# file: project/pysnooper/utils.py:23-32
# asked: {"lines": [26, 30, 31, 32], "branches": [[30, 31], [30, 32]]}
# gained: {"lines": [26, 30, 31, 32], "branches": [[30, 31], [30, 32]]}

from pysnooper.utils import WritableStream


def test_writable_stream_abstract_write_body():
    class ConcreteWritableStream(WritableStream):
        def write(self, s):
            return s

    stream = ConcreteWritableStream()

    assert WritableStream.write(stream, "payload") is None


def test_writable_stream_subclasshook_detects_write_method():
    class Writer:
        def write(self, s):
            return s

    assert WritableStream.__subclasshook__(Writer) is True


def test_writable_stream_subclasshook_returns_not_implemented_for_subclass():
    class SpecializedWritableStream(WritableStream):
        def write(self, s):
            return s

    class Candidate:
        def write(self, s):
            return s

    assert (
        SpecializedWritableStream.__subclasshook__(Candidate)
        is NotImplemented
    )
