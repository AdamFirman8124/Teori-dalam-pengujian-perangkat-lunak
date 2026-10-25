# file: project/pysnooper/utils.py:23-32
# asked: {"lines": [26, 30, 31, 32], "branches": [[30, 31], [30, 32]]}
# gained: {"lines": [26, 30, 31, 32], "branches": [[30, 31], [30, 32]]}

from pysnooper.utils import WritableStream


def test_writable_stream_abstract_write_body_executes():
    class Concrete(WritableStream):
        def write(self, s):
            return super().write(s)

    obj = Concrete()
    assert isinstance(obj, WritableStream)
    assert obj.write("hello") is None
    # direct unbound call also executes the `pass` body on line 26
    assert WritableStream.write(obj, "hello") is None


def test_writable_stream_subclasshook_duck_type_with_write():
    class HasWrite:
        def write(self, s):
            pass

    # direct call executes lines 30-31 with True result
    assert WritableStream.__subclasshook__(HasWrite) is True
    # integration via ABC machinery also executes lines 30-31
    assert issubclass(HasWrite, WritableStream)
    assert isinstance(HasWrite(), WritableStream)


def test_writable_stream_subclasshook_duck_type_without_write():
    class NoWrite:
        pass

    # direct call executes lines 30-31 with NotImplemented result
    assert WritableStream.__subclasshook__(NoWrite) is NotImplemented
    # integration via ABC machinery also executes lines 30-31
    assert not issubclass(NoWrite, WritableStream)
    assert not isinstance(NoWrite(), WritableStream)


def test_writable_stream_subclasshook_cls_is_not_writable_stream():
    class SubStream(WritableStream):
        def write(self, s):
            pass

    class Dummy:
        pass

    # cls is SubStream, not WritableStream, so executes line 32
    assert SubStream.__subclasshook__(Dummy) is NotImplemented
    assert WritableStream.__subclasshook__.__func__(SubStream, Dummy) is NotImplemented
    # integration via ABC machinery also executes line 32
    assert not issubclass(Dummy, SubStream)
