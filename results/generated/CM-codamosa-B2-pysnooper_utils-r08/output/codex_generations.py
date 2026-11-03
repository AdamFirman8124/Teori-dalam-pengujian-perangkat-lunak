

# Generated at 2026-11-02 19:05:19.280220
# Unit test for function ensure_tuple
def test_ensure_tuple():
    # nonce:53b79a93
    # Iterables (non-string) get converted to tuples
    assert module_0.ensure_tuple([1, 2, 3]) == (1, 2, 3)
    assert module_0.ensure_tuple((1, 2)) == (1, 2)
    assert module_0.ensure_tuple([]) == ()
    assert module_0.ensure_tuple(range(3)) == (0, 1, 2)
    assert module_0.ensure_tuple(x for x in range(3)) == (0, 1, 2)
    assert module_0.ensure_tuple({'a': 1, 'b': 2}) == ('a', 'b')  # dict iterates keys
    assert module_0.ensure_tuple(tuple({1, 2, 3})) == (1, 2, 3)

    # Strings are treated as single items, not iterated
    assert module_0.ensure_tuple('abc') == ('abc',)
    assert module_0.ensure_tuple(u'abc') == (u'abc',)
    assert module_0.ensure_tuple('') == ('',)

    # Non-iterables get wrapped in a single-element tuple
    assert module_0.ensure_tuple(5) == (5,)
    assert module_0.ensure_tuple(3.5) == (3.5,)
    assert module_0.ensure_tuple(None) == (None,)
    assert module_0.ensure_tuple(object) == (object,)

    # Result is always a tuple
    assert isinstance(module_0.ensure_tuple([1]), tuple)
    assert isinstance(module_0.ensure_tuple('x'), tuple)
    assert isinstance(module_0.ensure_tuple(1), tuple)

# Generated at 2026-11-02 19:08:13.448733
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    item = 'fooo'
    # Basic behavior: returns repr of the item
    assert module_0.get_shortish_repr(item) == repr(item) == "'fooo'"

    # Custom repr function matched by type condition
    custom_repr = ((str, lambda x: 'meow'),)
    assert module_0.get_shortish_repr(item, custom_repr=custom_repr) == 'meow'

    # Custom repr function matched by arbitrary condition
    custom_repr = ((lambda x: x == 'fooo', lambda x: 'woof'),)
    assert module_0.get_shortish_repr(item, custom_repr=custom_repr) == 'woof'

    # Custom repr that is not matched falls back to default repr
    custom_repr = ((lambda x: False, lambda x: 'woof'),)
    assert module_0.get_shortish_repr(item, custom_repr=custom_repr) == "'fooo'"

    # Custom repr raising an exception results in 'REPR FAILED'
    custom_repr = ((lambda x: True, lambda x: 1 / 0),)
    assert module_0.get_shortish_repr(item, custom_repr=custom_repr) == 'REPR FAILED'

    # Newlines and carriage returns are stripped
    custom_repr = ((lambda x: True, lambda x: 'a\r\nb\nc'),)
    assert module_0.get_shortish_repr(item, custom_repr=custom_repr) == 'abc'

    # Normalization removes memory addresses from default-style reprs
    class Foo(object):
        def __repr__(self):
            return '<Foo object at 0xDEADBEEF>'

    assert module_0.get_shortish_repr(Foo()) == '<Foo object at 0xDEADBEEF>'
    assert module_0.get_shortish_repr(Foo(), normalize=True) == '<Foo object>'
    assert module_0.get_shortish_repr(Foo(), normalize=False) == \
                                                    '<Foo object at 0xDEADBEEF>'

    # Truncation
    long_item = 'a' * 30
    assert module_0.get_shortish_repr(long_item) == "'" + 'a' * 30 + "'"
    assert module_0.get_shortish_repr(long_item, max_length=100) == \
                                                  "'" + 'a' * 30 + "'"
    assert module_0.get_shortish_repr(long_item, max_length=None) == \
                                                  "'" + 'a' * 30 + "'"
    result = module_0.get_shortish_repr(long_item, max_length=10)
    assert result == "'aa...aaa'"
    assert len(result) == 10

    # Truncation combined with normalization
    class Bar(object):
        def __repr__(self):
            return ('<Bar object at 0xDEADBEEF>' + 'x' * 30)

    result = module_0.get_shortish_repr(Bar(), max_length=20, normalize=True)
    assert result == '<Bar object>xxxxxxxxx...'
    assert len(result) == 20

# Generated at 2026-11-02 19:10:13.889635
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import pytest

    class MockStream(WritableStream):
        def __init__(self):
            self.output = []

        def module_0.write(self, s):
            self.output.append(s)

    # A concrete subclass implementing the abstract `write` works normally.
    stream = MockStream()
    stream.write('hello')
    stream.write('world')
    assert stream.output == ['hello', 'world']

    # Any class defining `write` is recognized as a virtual subclass
    # via the custom __subclasshook__.
    class DuckStream(object):
        def module_0.write(self, s):
            pass

    assert issubclass(DuckStream, WritableStream)
    assert isinstance(DuckStream(), WritableStream)

    # A class without a `write` method is not a virtual subclass...
    class NotAStream(object):
        pass

    assert not issubclass(NotAStream, WritableStream)
    assert not isinstance(NotAStream(), WritableStream)

    # ...and a subclass that fails to implement the abstract `write`
    # cannot be instantiated.
    class IncompleteStream(WritableStream):
        pass

    with pytest.raises(TypeError):
        IncompleteStream()

# Generated at 2026-11-02 19:12:23.606437
# Unit test for constructor of class WritableStream
def test_WritableStream():
    # The abstract base class cannot be instantiated directly because
    # `write` is an abstract method.
    with pytest.raises(TypeError):
        WritableStream()

    # A subclass that implements `write` can be instantiated.
    class MyStream(WritableStream):
        def write(self, s):
            pass

    stream = MyStream()
    assert isinstance(stream, WritableStream)
    assert isinstance(stream, object)

    # Duck typing: any class with a `write` method is considered a
    # virtual subclass via __subclasshook__.
    class DuckWriter(object):
        def write(self, s):
            pass

    assert issubclass(DuckWriter, WritableStream)
    assert isinstance(DuckWriter(), WritableStream)

    # Classes lacking a `write` method are not considered subclasses.
    class NoWrite(object):
        pass

    assert not issubclass(NoWrite, WritableStream)
    with pytest.raises(TypeError):
        WritableStream.register(NoWrite)  # registration hook not needed, sanity check