# file: project/pysnooper/utils.py:23-32
# asked: {"lines": [26, 30, 31, 32], "branches": [[30, 31], [30, 32]]}
# gained: {"lines": [26, 30, 31, 32], "branches": [[30, 31], [30, 32]]}

from pysnooper.utils import WritableStream


def test_writable_stream_abstract_write_body_returns_none():
    assert WritableStream.write(object(), "value") is None


def test_writable_stream_subclasshook_accepts_class_with_write():
    class Writer:
        def write(self, value):
            return value

    assert WritableStream.__subclasshook__(Writer) is True


def test_writable_stream_subclasshook_rejects_class_without_write():
    class NotWriter:
        pass

    assert WritableStream.__subclasshook__(NotWriter) is NotImplemented


def test_writable_stream_subclasshook_returns_not_implemented_for_derived_cls():
    class SpecializedWritableStream(WritableStream):
        def write(self, value):
            return value

    class Writer:
        def write(self, value):
            return value

    assert SpecializedWritableStream.__subclasshook__(Writer) is NotImplemented
