# file: project/pysnooper/utils.py:23-32
# asked: {"lines": [26, 30, 31, 32], "branches": [[30, 31], [30, 32]]}
# gained: {"lines": [26, 30, 31, 32], "branches": [[30, 31], [30, 32]]}

from pysnooper.utils import WritableStream


def test_writable_stream_abstract_write_body_returns_none():
    assert WritableStream.write(object(), "payload") is None


def test_writable_stream_subclasshook_checks_for_write_method():
    class HasWrite:
        def write(self, s):
            return s

    class WithoutWrite:
        pass

    assert WritableStream.__subclasshook__(HasWrite) is True
    assert WritableStream.__subclasshook__(WithoutWrite) is NotImplemented


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
