# file: project/pysnooper/utils.py:23-32
# asked: {"lines": [26, 30, 31, 32], "branches": [[30, 31], [30, 32]]}
# gained: {"lines": [26, 30, 31, 32], "branches": [[30, 31], [30, 32]]}

from pysnooper.utils import WritableStream


def test_writable_stream_write_body_executes():
    # Executes line 26 (`pass`) in WritableStream.write
    assert WritableStream.write(object(), "hello") is None

    class Concrete(WritableStream):
        def write(self, s):
            return super().write(s)

    c = Concrete()
    assert c.write("hi") is None
    assert isinstance(c, WritableStream)


def test_writable_stream_subclasshook_for_writable_stream():
    # Executes lines 30-31 (`if cls is WritableStream: return _check_methods(...)`)
    class WithWrite:
        def write(self, s):
            pass

    result = WritableStream.__subclasshook__(WithWrite)
    assert result is True

    class WithoutWrite:
        pass

    result2 = WritableStream.__subclasshook__(WithoutWrite)
    assert result2 is NotImplemented


def test_writable_stream_subclasshook_for_other_cls():
    # Executes line 32 (`return NotImplemented`) where cls is not WritableStream
    class SubStream(WritableStream):
        def write(self, s):
            pass

    class Dummy:
        def write(self, s):
            pass

    assert SubStream.__subclasshook__(Dummy) is NotImplemented
    assert SubStream.__subclasshook__(object) is NotImplemented
