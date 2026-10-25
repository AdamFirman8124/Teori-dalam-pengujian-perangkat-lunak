# file: project/pysnooper/utils.py:23-32
# asked: {"lines": [26, 30, 31, 32], "branches": [[30, 31], [30, 32]]}
# gained: {"lines": [26, 30, 31, 32], "branches": [[30, 31], [30, 32]]}

from pysnooper.utils import WritableStream


def test_writable_stream_abstract_write_body():
    assert WritableStream.write(object(), "payload") is None


def test_writable_stream_subclasshook_recognizes_write_method():
    class HasWrite:
        def write(self, value):
            return value

    assert WritableStream.__subclasshook__(HasWrite) is True


def test_writable_stream_subclasshook_for_derived_class():
    class DerivedWritableStream(WritableStream):
        def write(self, value):
            return value

    class Candidate:
        def write(self, value):
            return value

    assert DerivedWritableStream.__subclasshook__(Candidate) is NotImplemented
