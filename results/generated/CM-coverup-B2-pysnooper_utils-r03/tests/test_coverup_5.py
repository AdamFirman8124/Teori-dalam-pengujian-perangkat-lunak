# file: project/pysnooper/utils.py:23-32
# asked: {"lines": [26, 30, 31, 32], "branches": [[30, 31], [30, 32]]}
# gained: {"lines": [26, 30, 31, 32], "branches": [[30, 31], [30, 32]]}

from pysnooper.utils import WritableStream


def test_writable_stream_abstract_write_body_executes():
    class ConcreteWritable(WritableStream):
        def write(self, s):
            return super().write(s)

    obj = ConcreteWritable()
    assert obj.write("hello") is None
    # direct call of the abstract base implementation hits `pass`
    assert WritableStream.write(obj, "hello") is None


def test_writable_stream_subclasshook_duck_type_true():
    class HasWrite:
        def write(self, s):
            pass

    result = WritableStream.__subclasshook__(HasWrite)
    assert result is True
    assert issubclass(HasWrite, WritableStream) is True


def test_writable_stream_subclasshook_missing_write():
    class HasNoWrite:
        pass

    result = WritableStream.__subclasshook__(HasNoWrite)
    assert result is NotImplemented
    assert issubclass(HasNoWrite, WritableStream) is False


def test_writable_stream_subclasshook_on_derived_cls_returns_not_implemented():
    class DerivedStream(WritableStream):
        def write(self, s):
            pass

    class DummyTarget:
        pass

    # cls is not WritableStream, so must return NotImplemented (line 32)
    assert DerivedStream.__subclasshook__(DummyTarget) is NotImplemented
    # sanity: base hook still works for the derived class itself
    assert WritableStream.__subclasshook__(DerivedStream) is True
