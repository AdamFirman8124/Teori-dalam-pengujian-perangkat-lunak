

# Generated at 2026-11-03 06:18:50.498039
# Unit test for function get_repr_function
def test_get_repr_function():
    # With no custom_repr entries, falls back to builtin repr
    assert module_0.get_repr_function(123, ()) is repr
    assert module_0.get_repr_function('abc', []) is repr

    # Type condition is converted to an isinstance check
    int_repr = lambda x: 'INT:{}'.format(x)
    custom_repr = ((int, int_repr),)
    assert module_0.get_repr_function(123, custom_repr) is int_repr
    assert module_0.get_repr_function('abc', custom_repr) is repr

    # Callable (non-type) condition is used directly
    big_repr = lambda x: 'BIG'
    custom_repr = ((lambda x: x > 10, big_repr),)
    assert module_0.get_repr_function(100, custom_repr) is big_repr
    assert module_0.get_repr_function(5, custom_repr) is repr

    # First matching condition wins
    first = lambda x: 'FIRST'
    second = lambda x: 'SECOND'
    custom_repr = ((int, first), (lambda x: True, second))
    assert module_0.get_repr_function(5, custom_repr) is first
    assert module_0.get_repr_function('x', custom_repr) is second

    # Non-matching conditions fall back to repr
    custom_repr = ((str, first), (dict, second))
    assert module_0.get_repr_function(5, custom_repr) is repr

    # Works with user-defined classes as type conditions
    class Foo(object):
        pass
    foo_repr = lambda x: 'FOO'
    custom_repr = ((Foo, foo_repr),)
    assert module_0.get_repr_function(Foo(), custom_repr) is foo_repr
    assert module_0.get_repr_function(object(), custom_repr) is repr

# Generated at 2026-11-03 06:20:08.833732
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    # A concrete subclass implementing write should work normally
    class MyWritableStream(WritableStream):
        def __init__(self):
            self.written = []

        def module_0.write(self, s):
            self.written.append(s)

    stream = MyWritableStream()
    result = stream.write('hello')
    assert stream.written == ['hello']
    assert result is None

    # Any class with a `write` method is recognized as a WritableStream
    # subclass via __subclasshook__ (structural typing / duck typing)
    class DuckStream:
        def module_0.write(self, s):
            return s

    assert issubclass(DuckStream, WritableStream)
    duck = DuckStream()
    assert duck.write('quack') == 'quack'

    # A class without a `write` method is not a WritableStream subclass
    class NotWritable:
        pass

    assert not issubclass(NotWritable, WritableStream)

    # A class with `write = None` does not satisfy the interface
    class NoneWrite:
        write = None

    assert not issubclass(NoneWrite, WritableStream)

    # WritableStream itself is abstract and cannot be instantiated
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError(
            "WritableStream should not be instantiable without write"
        )

# Generated at 2026-11-03 06:20:48.152333
# Unit test for function shitcode
def test_shitcode():
    # Empty string stays empty
    assert module_0.shitcode('') == ''

    # ASCII characters pass through unchanged
    assert module_0.shitcode('abc') == 'abc'
    assert module_0.shitcode('hello world 123!') == 'hello world 123!'

    # Characters with ord in (0, 256) are kept
    assert module_0.shitcode('\x01') == '\x01'
    assert module_0.shitcode('\x7f') == '\x7f'
    assert module_0.shitcode('\xff') == '\xff'
    assert module_0.shitcode('é') == 'é'  # ord 233 < 256

    # Characters with ord 0 are replaced with '?'
    assert module_0.shitcode('\x00') == '?'

    # Characters with ord >= 256 are replaced with '?'
    assert module_0.shitcode('Ā') == '?'  # ord 256
    assert module_0.shitcode('€') == '?'  # ord 8364
    assert module_0.shitcode('א') == '?'  # ord 1488

    # Mixed strings
    assert module_0.shitcode('a\x00b€c') == 'a?b?c'
    assert module_0.shitcode('héllo€') == 'héllo?'
    assert module_0.shitcode('\x00€\x00') == '???'

# Generated at 2026-11-03 06:21:51.270111
# Unit test for function get_repr_function

# Generated at 2026-11-03 06:22:42.332690
# Unit test for function get_repr_function

# Generated at 2026-11-03 06:24:00.156632
# Unit test for function get_repr_function
def test_get_repr_function():item = 3

# Generated at 2026-11-03 06:24:30.061185
# Unit test for function shitcode
def test_shitcode():
    # Plain ASCII passes through unchanged
    assert module_0.shitcode('abc') == 'abc'
    assert module_0.shitcode('') == ''
    assert module_0.shitcode('hello world 123!@#') == 'hello world 123!@#'

    # Characters with ord == 0 are replaced with '?'
    assert module_0.shitcode('\x00') == '?'
    assert module_0.shitcode('a\x00b') == 'a?b'

    # Characters with 0 < ord < 256 are kept (including extended latin)
    assert module_0.shitcode('\x01') == '\x01'
    assert module_0.shitcode('\xff') == '\xff'
    assert module_0.shitcode('a\xffb\x01c') == 'a\xffb\x01c'

    # Characters with ord >= 256 are replaced with '?'
    assert module_0.shitcode('\u0100') == '?'
    assert module_0.shitcode('\u2603') == '?'
    assert module_0.shitcode('\U0001F600') == '?'

    # Mixed content
    assert module_0.shitcode('a\x00b\u0100c\u00ffd') == 'a?b?c\u00ffd'
    assert module_0.shitcode('\u4e2d\u6587abc') == '??abc'

    # Result is always a string of same length
    s = 'x\x00y\u0100z'
    result = module_0.shitcode(s)
    assert isinstance(result, str)
    assert len(result) == len(s)

# Generated at 2026-11-03 06:24:51.868864
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    # Test with a concrete subclass of WritableStream
    class MyStream(WritableStream):
        def __init__(self):
            self.output = ''

        def module_0.write(self, s):
            self.output += s

    stream = MyStream()
    stream.write('hello')
    stream.write(' world')
    assert stream.output == 'hello world'

    # Test structural typing via __subclasshook__: any class
    # with a `write` method counts as a WritableStream
    class DuckStream(object):
        def module_0.write(self, s):
            return len(s)

    assert issubclass(DuckStream, WritableStream)
    assert isinstance(DuckStream(), WritableStream)

    duck = DuckStream()
    assert duck.write('test') == 4

    # A class without a `write` method is not a WritableStream
    class NoWrite(object):
        pass

    assert not issubclass(NoWrite, WritableStream)
    assert not isinstance(NoWrite(), WritableStream)

    # A class with `write = None` should not qualify either
    class NoneWrite(object):
        write = None

    assert not issubclass(NoneWrite, WritableStream)

    # Subclasshook only applies to WritableStream itself
    class OtherABC(ABC):
        pass

    assert OtherABC.__subclasshook__(DuckStream) is NotImplemented

# Generated at 2026-11-03 06:25:20.241518
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
# nonce:163052b3
    # Default repr behavior
    assert module_0.get_shortish_repr(123) == '123'
    assert module_0.get_shortish_repr('foo') == "'foo'"

    # Newlines and carriage returns are stripped from the repr
    class MultiLine:
        def __repr__(self):
            return 'line1\nline2\rline3'
    assert module_0.get_shortish_repr(MultiLine()) == 'line1line2line3'

    # custom_repr with a type condition takes precedence
    class Custom:
        def __repr__(self):
            return 'original'
    custom_repr = ((Custom, lambda x: 'custom repr'),)
    assert module_0.get_shortish_repr(Custom(), custom_repr=custom_repr) == 'custom repr'

    # custom_repr with a callable condition also works
    custom_repr = ((lambda x: isinstance(x, Custom), lambda x: 'callable repr'),)
    assert module_0.get_shortish_repr(Custom(), custom_repr=custom_repr) == 'callable repr'

    # custom_repr conditions that don't match fall back to plain repr
    assert module_0.get_shortish_repr(42, custom_repr=custom_repr) == '42'

    # A repr function that raises results in 'REPR FAILED'
    class Bad:
        def __repr__(self):
            raise ValueError('nope')
    assert module_0.get_shortish_repr(Bad()) == 'REPR FAILED'

    # normalize=True removes memory addresses from the repr
    class WithAddress:
        def __repr__(self):
            return '<WithAddress object at 0xdeadbeef1234>'
    assert module_0.get_shortish_repr(WithAddress()) == '<WithAddress object at 0xdeadbeef1234>'
    assert module_0.get_shortish_repr(WithAddress(), normalize=True) == '<WithAddress object>'

    # max_length truncates long reprs, keeping both ends
    class Long:
        def __repr__(self):
            return 'x' * 20
    result = module_0.get_shortish_repr(Long(), max_length=10)
    assert result == 'xxx...xxxx'
    assert len(result) == 10

    # max_length=None disables truncation
    assert module_0.get_shortish_repr(Long(), max_length=None) == 'x' * 20

    # Short reprs are unaffected by max_length
    assert module_0.get_shortish_repr('abc', max_length=100) == "'abc'"

    # All options combined: newline removal, normalization, truncation
    class LongAddress:
        def __repr__(self):
            return 'A' * 10 + ' at 0x1234567890ab'
    assert module_0.get_shortish_repr(LongAddress(), normalize=True) == 'A' * 10
    result = module_0.get_shortish_repr(LongAddress(), normalize=True, max_length=8)
    assert result == 'AA...AAA'

# Generated at 2026-11-03 06:25:47.111826
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    # A class defining a `write` method is recognized as a WritableStream
    # subclass via __subclasshook__.
    class FakeStream:
        def module_0.write(self, s):
            return s

    class NoWrite:
        pass

    assert issubclass(FakeStream, WritableStream)
    assert isinstance(FakeStream(), WritableStream)
    assert FakeStream().write('abc') == 'abc'

    # A class without a `write` method is not a WritableStream subclass.
    assert not issubclass(NoWrite, WritableStream)
    assert not isinstance(NoWrite(), WritableStream)

    # WritableStream itself is abstract and cannot be instantiated.
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError("WritableStream should not be instantiable")

    # A concrete subclass implementing write works normally.
    class ConcreteStream(WritableStream):
        def module_0.write(self, s):
            self.buffer = s
            return len(s)

    stream = ConcreteStream()
    assert stream.write('hello') == 5
    assert stream.buffer == 'hello'

# Generated at 2026-11-03 06:25:52.693097
# Unit test for method write of class WritableStream

# Generated at 2026-11-03 06:26:04.471887
# Unit test for method write of class WritableStream

# Generated at 2026-11-03 06:26:22.188666
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    # Classes implementing `write` are recognized as subclasses via
    # the custom __subclasshook__.
    class DuckStream(object):
        def module_0.write(self, s):
            pass

    assert issubclass(DuckStream, WritableStream)

    # Classes without a `write` method are not.
    class NotAStream(object):
        pass

    assert not issubclass(NotAStream, WritableStream)

    # The abstract base class itself cannot be instantiated.
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError("WritableStream should be abstract")

    # A concrete subclass's write method works as expected.
    class MyStream(WritableStream):
        def __init__(self):
            self.written = []

        def module_0.write(self, s):
            self.written.append(s)

    stream = MyStream()
    stream.write('hello')
    stream.write('world')
    assert stream.written == ['hello', 'world']

# Generated at 2026-11-03 06:26:34.985771
# Unit test for method write of class WritableStream

# Generated at 2026-11-03 06:26:46.053671
# Unit test for method write of class WritableStream

# Generated at 2026-11-03 06:26:51.778505
# Unit test for function truncate
def test_truncate():
    # String shorter than max_length is returned unchanged
    assert module_0.truncate('12345', 10) == '12345'

    # String exactly max_length is returned unchanged
    assert module_0.truncate('12345', 5) == '12345'

    # max_length of None returns the string unchanged
    assert module_0.truncate('12345', None) == '12345'

    # String longer than max_length is truncated with '...' in the middle
    assert module_0.truncate('1234567890', 8) == '12...890'

    # Verify truncated result has exactly max_length characters
    result = module_0.truncate('abcdefghijklmnopqrstuvwxyz', 10)
    assert len(result) == 10
    assert '...' in result
    assert result == 'abcde...yz'

    # Odd max_length: left gets the smaller share
    result = module_0.truncate('abcdefghijklmnop', 7)
    assert result == 'ab...op'
    assert len(result) == 7

    # Very short max_length
    assert module_0.truncate('abcdef', 3) == '...'
    assert module_0.truncate('abcdef', 4) == 'a...f'

    # Works with unicode strings
    result = module_0.truncate(u'áéíóúáéíóúáéíóú', 8)
    assert len(result) == 8
    assert u'...' in result

# Generated at 2026-11-03 06:27:45.256246
# Unit test for function ensure_tuple
def test_ensure_tuple():
# nonce:2a4d7761
    # Non-iterable objects are wrapped in a single-element tuple.
    assert module_0.ensure_tuple(1) == (1,)
    assert module_0.ensure_tuple(3.5) == (3.5,)
    assert module_0.ensure_tuple(None) == (None,)
    assert module_0.ensure_tuple(True) == (True,)
    some_object = object()
    assert module_0.ensure_tuple(some_object) == (some_object,)
    assert module_0.ensure_tuple(object) == (object,)

    # Strings are treated as atomic values, not iterated over.
    assert module_0.ensure_tuple('abc') == ('abc',)
    assert module_0.ensure_tuple(u'abc') == (u'abc',)
    assert module_0.ensure_tuple('') == ('',)

    # Iterables (non-string) are converted to tuples.
    assert module_0.ensure_tuple([]) == ()
    assert module_0.ensure_tuple([1, 2, 3]) == (1, 2, 3)
    assert module_0.ensure_tuple(()) == ()
    assert module_0.ensure_tuple((1, 2, 3)) == (1, 2, 3)
    assert module_0.ensure_tuple(range(4)) == (0, 1, 2, 3)
    assert module_0.ensure_tuple(i for i in range(3)) == (0, 1, 2)

    result = module_0.ensure_tuple({'a', 'b'})
    assert isinstance(result, tuple)
    assert set(result) == {'a', 'b'}

    result = module_0.ensure_tuple({'x': 1, 'y': 2})
    assert isinstance(result, tuple)
    assert sorted(result) == ['x', 'y']

    # Only the top level is iterated.
    assert module_0.ensure_tuple([[1, 2], [3]]) == ([1, 2], [3])

    # Custom iterable classes are supported.
    class CustomIterable(object):
        def __iter__(self):
            return iter((10, 20))
    assert module_0.ensure_tuple(CustomIterable()) == (10, 20)

    # String subclasses are also treated as atomic values.
    class MyString(str):
        pass
    assert module_0.ensure_tuple(MyString('xyz')) == ('xyz',)

    # Elements are shared, not copied.
    my_list = [1, 2]
    result = module_0.ensure_tuple(my_list)
    assert isinstance(result, tuple)
    assert result == (1, 2)
    assert result[0] is my_list[0]