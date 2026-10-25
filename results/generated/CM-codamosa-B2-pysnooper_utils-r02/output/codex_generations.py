

# Generated at 2026-10-25 00:19:33.626755
# Unit test for function ensure_tuple
def test_ensure_tuple():
    # Non-iterables are wrapped in a tuple.
    assert module_0.ensure_tuple(None) == (None,)
    assert module_0.ensure_tuple(42) == (42,)

    # Strings are treated as single values.
    assert module_0.ensure_tuple('hello') == ('hello',)
    assert module_0.ensure_tuple(u'hello') == (u'hello',)

    # Iterables are converted to tuples.
    assert module_0.ensure_tuple([]) == ()
    assert module_0.ensure_tuple([1, 2, 3]) == (1, 2, 3)
    assert module_0.ensure_tuple((1, 2, 3)) == (1, 2, 3)
    assert module_0.ensure_tuple(range(3)) == (0, 1, 2)

    # One-shot iterables are also supported.
    generator = (x for x in range(3))
    assert module_0.ensure_tuple(generator) == (0, 1, 2)

# Generated at 2026-10-25 00:19:39.723019
# Unit test for function ensure_tuple
def test_ensure_tuple():
    assert module_0.ensure_tuple([1, 2, 3]) == (1, 2, 3)
    assert module_0.ensure_tuple((1, 2, 3)) == (1, 2, 3)
    assert module_0.ensure_tuple(iter([1, 2, 3])) == (1, 2, 3)

    # Strings should be treated as single values, not iterables.
    assert module_0.ensure_tuple('hello') == ('hello',)

    # Non-iterable values should be wrapped in a tuple.
    assert module_0.ensure_tuple(42) == (42,)
    assert module_0.ensure_tuple(None) == (None,)

    # Empty iterables should produce an empty tuple.
    assert module_0.ensure_tuple([]) == ()

# Generated at 2026-10-25 00:19:46.936735
# Unit test for function truncate

# Generated at 2026-10-25 00:19:48.269287
# Unit test for function truncate
def test_truncate():# No truncation when string fits within max_length
    assert module_0.truncate('abcdefghij', 10) == 'abcdefghij'

    # No truncation when string is shorter than max_length
    assert module_0.truncate('abc', 10) == 'abc'

    # max_length=None means never truncate
    assert module_0.truncate('a' * 100, None) == 'a' * 100

    # Even-length max_length: left=(8-3)//2=2, right=8-3-2=3
    assert module_0.truncate('abcdefghijkl', 8) == 'ab...jkl'

    # Odd-length max_length: left=(7-3)//2=2, right=7-3-2=2
    assert module_0.truncate('abcdefgh', 7) == 'ab...gh'

    # Minimum split: max_length=4 -> left=0, right=1
    assert module_0.truncate('abcdef', 4) == '...f'

    # Ellipsis accounts for exactly 3 characters
    result = module_0.truncate('a' * 50, 20)
    assert len(result) == 20
    assert result.startswith('a' * 8) and result.endswith('a' * 9) and '...' in result

# Generated at 2026-10-25 00:20:23.609296
# Unit test for function truncate
def test_truncate():
    # No truncation needed
    assert module_0.truncate('abc', None) == 'abc'
    assert module_0.truncate('', 5) == ''
    assert module_0.truncate('abcdefghij', 10) == 'abcdefghij'
    assert module_0.truncate('abcdefghij', 11) == 'abcdefghij'

    # Truncation: head + '...' + tail, exactly max_length chars
    assert module_0.truncate('abcdefghij', 4) == '...j'
    assert module_0.truncate('abcdefghij', 5) == 'a...j'
    assert module_0.truncate('abcdefghij', 6) == 'a...ij'
    assert module_0.truncate('abcdefghij', 7) == 'ab...ij'
    assert module_0.truncate('abcdefghij', 8) == 'ab...hij'
    assert module_0.truncate('abcdefghij', 9) == 'abc...hij'

    # Unicode is preserved
    assert module_0.truncate(u'\u03b1\u03b2\u03b3\u03b4\u03b5\u03b6\u03b7\u03b8', 5) == u'\u03b1...\u03b8'

    # Property: for any max_length >= 4, result length == max_length
    s = 'abcdefghij'
    for max_length in range(4, len(s)):
        result = module_0.truncate(s, max_length)
        assert len(result) == max_length
        assert result.startswith('a')
        assert result.endswith('j')
        assert '...' in result

# Generated at 2026-10-25 00:20:24.953829
# Unit test for constructor of class WritableStream
def test_WritableStream():
    # WritableStream is abstract; direct instantiation must fail.
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise Exception("WritableStream() should not be instantiable.")

    # A class with a `write` method counts as a subclass via __subclasshook__.
    class WithWrite:
        def write(self, s):
            pass

    assert issubclass(WithWrite, WritableStream)
    WithWrite()  # Constructor works fine.

    # A class without `write` is not a subclass.
    class WithoutWrite:
        pass

    assert not issubclass(WithoutWrite, WritableStream)
    try:
        WithoutWrite()  # Sanity: constructor itself is fine, just not a WritableStream.
    except TypeError:
        raise Exception("WithoutWrite() should be instantiable.")

# Generated at 2026-10-25 00:20:34.556275
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    with pytest.raises(TypeError):
        WritableStream()

    class ConcreteWritableStream(WritableStream):
        def __init__(self):
            self.written = []

        def module_0.write(self, s):
            self.written.append(s)

    stream = ConcreteWritableStream()
    stream.write('hello')

    assert stream.written == ['hello']

# Generated at 2026-10-25 00:20:42.643783
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    with pytest.raises(TypeError):
        WritableStream()

    class MemoryStream(WritableStream):
        def __init__(self):
            self.value = ''

        def module_0.write(self, s):
            self.value += s
            return len(s)

    stream = MemoryStream()

    assert stream.write('hello') == 5
    assert stream.write(' world') == 6
    assert stream.value == 'hello world'
    assert isinstance(stream, WritableStream)

# Generated at 2026-10-25 00:20:52.678811
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class ConcreteWritableStream(WritableStream):
        def __init__(self):
            self.contents = []

        def module_0.write(self, s):
            self.contents.append(s)
            return len(s)

    class StructuralWritableStream:
        def module_0.write(self, s):
            return len(s)

    class NotWritableStream:
        pass

    stream = ConcreteWritableStream()

    assert stream.write('hello') == 5
    assert stream.contents == ['hello']
    assert isinstance(stream, WritableStream)

    # Verify the structural subclass check implemented by __subclasshook__.
    assert issubclass(StructuralWritableStream, WritableStream)
    assert isinstance(StructuralWritableStream(), WritableStream)
    assert not issubclass(NotWritableStream, WritableStream)

    # The abstract base class itself cannot be instantiated.
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError('WritableStream should not be instantiable')

# Generated at 2026-10-25 00:20:54.000031
# Unit test for function shitcode
def test_shitcode():
    assert module_0.shitcode('') == ''
    assert module_0.shitcode('abc XYZ 123 !@#') == 'abc XYZ 123 !@#'
    assert module_0.shitcode('\x01\xff') == '\x01\xff'  # 1 and 255: kept
    assert module_0.shitcode('Ã©Ã¿') == 'Ã©Ã¿'              # 233 and 255: kept
    assert module_0.shitcode('\x00') == '?'             # 0: replaced
    assert module_0.shitcode('Äâð') == '???'           # 256, 9731, 128512: replaced
    assert module_0.shitcode('a\x00bÄc') == 'a?b?c'
    assert isinstance(module_0.shitcode('abc'), str)

# Generated at 2026-10-25 00:21:01.180385
# Unit test for function get_repr_function
def test_get_repr_function():
    class Example:
        pass

    example = Example()

    type_repr = lambda item: 'type match'
    predicate_repr = lambda item: 'predicate match'
    first_repr = lambda item: 'first match'
    second_repr = lambda item: 'second match'

    # Matches a type-based condition.
    assert module_0.get_repr_function(
        example,
        [(Example, type_repr)]
    ) is type_repr

    # Matches a callable predicate.
    assert module_0.get_repr_function(
        42,
        [(lambda item: item == 42, predicate_repr)]
    ) is predicate_repr

    # Returns the first matching action.
    assert module_0.get_repr_function(
        example,
        [
            (Example, first_repr),
            (lambda item: True, second_repr),
        ]
    ) is first_repr

    # Falls back to the built-in repr when nothing matches.
    assert module_0.get_repr_function(
        example,
        [(str, type_repr)]
    ) is repr

    # Also falls back when no custom representations are supplied.
    assert module_0.get_repr_function(example, ()) is repr

# Generated at 2026-10-25 00:21:03.605992
# Unit test for function get_repr_function

# Generated at 2026-10-25 00:21:06.031193
# Unit test for function get_repr_function

# Generated at 2026-10-25 00:21:08.554086
# Unit test for function get_repr_function

# Generated at 2026-10-25 00:21:10.979540
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 00:21:13.415785
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 00:21:15.831086
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 00:21:18.269190
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:21:20.693387
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:21:23.108298
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:21:25.525059
# Unit test for function get_repr_function

# Generated at 2026-10-25 00:21:27.940990
# Unit test for function get_repr_function

# Generated at 2026-10-25 00:21:30.357104
# Unit test for function get_repr_function

# Generated at 2026-10-25 00:21:32.773672
# Unit test for function get_repr_function

# Generated at 2026-10-25 00:21:35.196873
# Unit test for function get_repr_function

# Generated at 2026-10-25 00:21:37.611363
# Unit test for function get_repr_function

# Generated at 2026-10-25 00:21:48.557805
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    # Default repr
    assert module_0.get_shortish_repr(42) == '42'
    assert module_0.get_shortish_repr('foo') == "'foo'"

    # Newlines and carriage returns are stripped
    class WithNewlines:
        def __repr__(self):
            return 'line1\r\nline2'
    assert module_0.get_shortish_repr(WithNewlines()) == 'line1line2'

    # Repr that raises -> 'REPR FAILED'
    class BadRepr:
        def __repr__(self):
            raise RuntimeError('nope')
    assert module_0.get_shortish_repr(BadRepr()) == 'REPR FAILED'

    # custom_repr: type condition overrides repr
    class Custom:
        def __repr__(self):
            return 'default'
    assert module_0.get_shortish_repr(
        Custom(), custom_repr=((Custom, lambda x: 'custom'),)
    ) == 'custom'

    # custom_repr: callable condition overrides repr
    assert module_0.get_shortish_repr(
        Custom(), custom_repr=((lambda x: isinstance(x, Custom),
                                lambda x: 'callable-condition'),)
    ) == 'callable-condition'

    # custom_repr entry that doesn't match falls back to repr
    assert module_0.get_shortish_repr(
        Custom(), custom_repr=((int, lambda x: 'int!'),)
    ) == 'default'

    # normalize=True removes memory addresses
    class WithAddress:
        def __repr__(self):
            return '<WithAddress object at 0x7f3a1b2c4d5e>'
    assert module_0.get_shortish_repr(WithAddress(), normalize=True) == \
        '<WithAddress object>'
    assert module_0.get_shortish_repr(WithAddress(), normalize=False).startswith(
        '<WithAddress object at 0x'
    )

    # max_length truncates, keeping both head and tail
    long_string = 'a' * 100 + 'b' * 100
    result = module_0.get_shortish_repr(long_string, max_length=20)
    assert len(result) == 20
    assert result == ('a' * 8) + '...' + ('b' * 9)

    # max_length=None or short strings: unchanged
    assert module_0.get_shortish_repr('short', max_length=100) == 'short'
    assert module_0.get_shortish_repr('short') == 'short'

# Generated at 2026-10-25 00:21:57.516482
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    # The base class cannot be instantiated because write is abstract.
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError("WritableStream should require a write implementation")

    class MemoryStream(WritableStream):
        def __init__(self):
            self.contents = []

        def module_0.write(self, s):
            self.contents.append(s)

    stream = MemoryStream()
    stream.write("hello")

    assert stream.contents == ["hello"]
    assert isinstance(stream, WritableStream)

# Generated at 2026-10-25 00:22:06.206644
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    # WritableStream must not be instantiated without implementing module_0.write().
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError("WritableStream should be abstract")

    class TestStream(WritableStream):
        def __init__(self):
            self.output = []

        def module_0.write(self, s):
            self.output.append(s)
            return len(s)

    stream = TestStream()

    assert isinstance(stream, WritableStream)
    assert stream.write("hello") == 5
    assert stream.output == ["hello"]

    # The subclass hook should also recognize compatible duck-typed classes.
    class DuckTypedStream:
        def module_0.write(self, s):
            return s

    assert issubclass(DuckTypedStream, WritableStream)

# Generated at 2026-10-25 00:22:08.737361
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 00:22:11.164579
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 00:22:13.741024
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 00:22:16.155630
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 00:22:18.569863
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 00:22:20.986356
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 00:22:23.410699
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 00:22:25.827279
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 00:22:28.240570
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 00:22:30.655857
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 00:22:33.075494
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 00:22:35.503092
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 00:22:37.916751
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 00:22:40.331605
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 00:22:42.772639
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 00:22:45.204328
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:22:47.619247
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:22:50.033430
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:22:52.464378
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:22:54.882545
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:22:57.310984
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:22:59.724811
# Unit test for function get_repr_function

# Generated at 2026-10-25 00:23:02.141363
# Unit test for function get_repr_function

# Generated at 2026-10-25 00:23:04.567637
# Unit test for function get_repr_function

# Generated at 2026-10-25 00:23:06.983557
# Unit test for function get_repr_function

# Generated at 2026-10-25 00:23:09.397715
# Unit test for function get_repr_function

# Generated at 2026-10-25 00:23:11.812807
# Unit test for function get_repr_function

# Generated at 2026-10-25 00:23:14.227852
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:23:16.643210
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:23:19.058624
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:23:21.473455
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 00:23:23.890765
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 00:23:26.310657
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 00:23:28.727852
# Unit test for function get_repr_function

# Generated at 2026-10-25 00:23:31.142054
# Unit test for function get_repr_function

# Generated at 2026-10-25 00:23:33.557570
# Unit test for function get_repr_function

# Generated at 2026-10-25 00:23:43.278168
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    # The abstract base class cannot be instantiated directly.
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError("WritableStream should be abstract")

    class RecordingStream(WritableStream):
        def __init__(self):
            self.writes = []

        def module_0.write(self, s):
            self.writes.append(s)

    stream = RecordingStream()
    stream.write('hello')
    stream.write(' world')

    assert stream.writes == ['hello', ' world']
    assert isinstance(stream, WritableStream)

    # Structural subclass detection accepts classes that implement module_0.write().
    class DuckTypedStream:
        def module_0.write(self, s):
            pass

    assert issubclass(DuckTypedStream, WritableStream)
    assert isinstance(DuckTypedStream(), WritableStream)

    class NonWritable:
        pass

    assert not issubclass(NonWritable, WritableStream)

# Generated at 2026-10-25 00:23:44.609209
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    # Default repr
    assert module_0.get_shortish_repr(42) == '42'
    assert module_0.get_shortish_repr('foo') == "'foo'"

    # Newlines and carriage returns are stripped
    class WithNewlines:
        def __repr__(self):
            return 'line1\r\nline2'
    assert module_0.get_shortish_repr(WithNewlines()) == 'line1line2'

    # Repr that raises -> 'REPR FAILED'
    class BadRepr:
        def __repr__(self):
            raise RuntimeError('nope')
    assert module_0.get_shortish_repr(BadRepr()) == 'REPR FAILED'

    # custom_repr: type condition overrides repr
    class Custom:
        def __repr__(self):
            return 'default'
    assert module_0.get_shortish_repr(
        Custom(), custom_repr=((Custom, lambda x: 'custom'),)
    ) == 'custom'

    # custom_repr: callable condition overrides repr
    assert module_0.get_shortish_repr(
        Custom(), custom_repr=((lambda x: isinstance(x, Custom),
                                lambda x: 'callable-condition'),)
    ) == 'callable-condition'

    # custom_repr entry that doesn't match falls back to repr
    assert module_0.get_shortish_repr(
        Custom(), custom_repr=((int, lambda x: 'int!'),)
    ) == 'default'

    # normalize=True removes memory addresses
    class WithAddress:
        def __repr__(self):
            return '<WithAddress object at 0x7f3a1b2c4d5e>'
    assert module_0.get_shortish_repr(WithAddress(), normalize=True) == \
        '<WithAddress object>'
    assert module_0.get_shortish_repr(WithAddress(), normalize=False).startswith(
        '<WithAddress object at 0x'
    )

    # max_length truncates, keeping both head and tail
    long_string = 'a' * 100 + 'b' * 100
    result = module_0.get_shortish_repr(long_string, max_length=20)
    assert len(result) == 20
    assert result == ('a' * 8) + '...' + ('b' * 9)

    # max_length=None or short strings: unchanged
    assert module_0.get_shortish_repr('short', max_length=100) == 'short'
    assert module_0.get_shortish_repr('short') == 'short'

# Generated at 2026-10-25 00:23:45.930643
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    # Default repr
    assert module_0.get_shortish_repr(42) == '42'
    assert module_0.get_shortish_repr('foo') == "'foo'"

    # Newlines and carriage returns are stripped
    class WithNewlines:
        def __repr__(self):
            return 'line1\r\nline2'
    assert module_0.get_shortish_repr(WithNewlines()) == 'line1line2'

    # Repr that raises -> 'REPR FAILED'
    class BadRepr:
        def __repr__(self):
            raise RuntimeError('nope')
    assert module_0.get_shortish_repr(BadRepr()) == 'REPR FAILED'

    # custom_repr: type condition overrides repr
    class Custom:
        def __repr__(self):
            return 'default'
    assert module_0.get_shortish_repr(
        Custom(), custom_repr=((Custom, lambda x: 'custom'),)
    ) == 'custom'

    # custom_repr: callable condition overrides repr
    assert module_0.get_shortish_repr(
        Custom(), custom_repr=((lambda x: isinstance(x, Custom),
                                lambda x: 'callable-condition'),)
    ) == 'callable-condition'

    # custom_repr entry that doesn't match falls back to repr
    assert module_0.get_shortish_repr(
        Custom(), custom_repr=((int, lambda x: 'int!'),)
    ) == 'default'

    # normalize=True removes memory addresses
    class WithAddress:
        def __repr__(self):
            return '<WithAddress object at 0x7f3a1b2c4d5e>'
    assert module_0.get_shortish_repr(WithAddress(), normalize=True) == \
        '<WithAddress object>'
    assert module_0.get_shortish_repr(WithAddress(), normalize=False).startswith(
        '<WithAddress object at 0x'
    )

    # max_length truncates, keeping both head and tail
    long_string = 'a' * 100 + 'b' * 100
    result = module_0.get_shortish_repr(long_string, max_length=20)
    assert len(result) == 20
    assert result == ('a' * 8) + '...' + ('b' * 9)

    # max_length=None or short strings: unchanged
    assert module_0.get_shortish_repr('short', max_length=100) == 'short'
    assert module_0.get_shortish_repr('short') == 'short'

# Generated at 2026-10-25 00:23:55.711748
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class RecordingStream:
        def __init__(self):
            self.data = []

        def module_0.write(self, s):
            self.data.append(s)
            return len(s)

    assert issubclass(RecordingStream, WritableStream)

    stream = RecordingStream()
    assert isinstance(stream, WritableStream)
    assert stream.write('hello') == 5
    assert stream.data == ['hello']

    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError('WritableStream must not be directly instantiable')

# Generated at 2026-10-25 00:24:04.216569
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class TestStream(WritableStream):
        def __init__(self):
            self.data = ''

        def module_0.write(self, s):
            self.data += s
            return len(s)

    stream = TestStream()

    assert isinstance(stream, WritableStream)
    assert stream.write('hello') == 5
    assert stream.data == 'hello'

# Generated at 2026-10-25 00:24:06.637192
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:24:09.051163
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:24:11.469225
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:24:13.887175
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:24:16.304174
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:24:18.717898
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:24:21.134776
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 00:24:23.548279
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 00:24:25.963879
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 00:24:28.379649
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 00:24:30.792825
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 00:24:33.234559
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 00:24:35.675867
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:24:38.118459
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:24:40.560927
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:24:42.981396
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:24:45.400722
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:24:47.817258
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:24:50.234675
# Unit test for function get_repr_function

# Generated at 2026-10-25 00:24:52.660856
# Unit test for function get_repr_function

# Generated at 2026-10-25 00:24:55.103025
# Unit test for function get_repr_function

# Generated at 2026-10-25 00:24:57.543897
# Unit test for function get_repr_function

# Generated at 2026-10-25 00:24:59.986811
# Unit test for function get_repr_function

# Generated at 2026-10-25 00:25:02.429063
# Unit test for function get_repr_function

# Generated at 2026-10-25 00:25:04.845730
# Unit test for function shitcode

# Generated at 2026-10-25 00:25:07.263754
# Unit test for function shitcode

# Generated at 2026-10-25 00:25:09.678362
# Unit test for function shitcode

# Generated at 2026-10-25 00:25:12.105455
# Unit test for function shitcode

# Generated at 2026-10-25 00:25:14.517948
# Unit test for function shitcode

# Generated at 2026-10-25 00:25:16.943819
# Unit test for function shitcode

# Generated at 2026-10-25 00:25:19.358481
# Unit test for function get_repr_function

# Generated at 2026-10-25 00:25:25.282238
# Unit test for function get_repr_function
def test_get_repr_function():custom_repr = ((int, lambda value: 'integer:{}'.format(value)),)

# Generated at 2026-10-25 00:25:31.875892
# Unit test for function get_repr_function
def test_get_repr_function():
    class Base:
        pass

    class Child(Base):
        pass

    def base_repr(item):
        return 'base'

    def positive_int_repr(item):
        return 'positive integer'

    def fallback_number_repr(item):
        return 'number'

    custom_repr = (
        (Base, base_repr),
        (lambda item: isinstance(item, int) and item > 0, positive_int_repr),
        (int, fallback_number_repr),
    )

    # Type conditions use isinstance(), including subclasses.
    assert module_0.get_repr_function(Base(), custom_repr) is base_repr
    assert module_0.get_repr_function(Child(), custom_repr) is base_repr

    # The first matching condition wins.
    assert module_0.get_repr_function(1, custom_repr) is positive_int_repr

    # Later conditions are used when earlier ones do not match.
    assert module_0.get_repr_function(-1, custom_repr) is fallback_number_repr

    # Built-in repr is returned when no condition matches.
    assert module_0.get_repr_function('unmatched', custom_repr) is repr

# Generated at 2026-10-25 00:25:33.209765
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    # Default repr
    assert module_0.get_shortish_repr(42) == '42'
    assert module_0.get_shortish_repr('foo') == "'foo'"

    # Newlines and carriage returns are stripped
    class WithNewlines:
        def __repr__(self):
            return 'line1\r\nline2'
    assert module_0.get_shortish_repr(WithNewlines()) == 'line1line2'

    # Repr that raises -> 'REPR FAILED'
    class BadRepr:
        def __repr__(self):
            raise RuntimeError('nope')
    assert module_0.get_shortish_repr(BadRepr()) == 'REPR FAILED'

    # custom_repr: type condition overrides repr
    class Custom:
        def __repr__(self):
            return 'default'
    assert module_0.get_shortish_repr(
        Custom(), custom_repr=((Custom, lambda x: 'custom'),)
    ) == 'custom'

    # custom_repr: callable condition overrides repr
    assert module_0.get_shortish_repr(
        Custom(), custom_repr=((lambda x: isinstance(x, Custom),
                                lambda x: 'callable-condition'),)
    ) == 'callable-condition'

    # custom_repr entry that doesn't match falls back to repr
    assert module_0.get_shortish_repr(
        Custom(), custom_repr=((int, lambda x: 'int!'),)
    ) == 'default'

    # normalize=True removes memory addresses
    class WithAddress:
        def __repr__(self):
            return '<WithAddress object at 0x7f3a1b2c4d5e>'
    assert module_0.get_shortish_repr(WithAddress(), normalize=True) == \
        '<WithAddress object>'
    assert module_0.get_shortish_repr(WithAddress(), normalize=False).startswith(
        '<WithAddress object at 0x'
    )

    # max_length truncates, keeping both head and tail
    long_string = 'a' * 100 + 'b' * 100
    result = module_0.get_shortish_repr(long_string, max_length=20)
    assert len(result) == 20
    assert result == ('a' * 8) + '...' + ('b' * 9)

    # max_length=None or short strings: unchanged
    assert module_0.get_shortish_repr('short', max_length=100) == 'short'
    assert module_0.get_shortish_repr('short') == 'short'

# Generated at 2026-10-25 00:25:41.550494
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class ConcreteWritableStream(WritableStream):
        def __init__(self):
            self.contents = []

        def module_0.write(self, s):
            self.contents.append(s)

    # The abstract base class cannot be instantiated directly.
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError(
            'WritableStream should not be directly instantiable'
        )

    stream = ConcreteWritableStream()
    stream.write('hello')

    assert stream.contents == ['hello']
    assert isinstance(stream, WritableStream)

# Generated at 2026-10-25 00:25:50.605918
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    # WritableStream cannot be instantiated without implementing module_0.write().
    with pytest.raises(TypeError):
        WritableStream()

    class BufferStream(WritableStream):
        def __init__(self):
            self.data = []

        def module_0.write(self, s):
            self.data.append(s)
            return len(s)

    stream = BufferStream()

    assert isinstance(stream, WritableStream)
    assert stream.write('hello') == 5
    assert stream.data == ['hello']

    # The subclass hook also accepts classes that provide module_0.write()
    # without explicitly inheriting from WritableStream.
    class DuckStream:
        def module_0.write(self, s):
            return s

    assert issubclass(DuckStream, WritableStream)
    assert isinstance(DuckStream(), WritableStream)

# Generated at 2026-10-25 00:25:53.023391
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:25:55.437919
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:25:57.852521
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:26:00.267009
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:26:02.682051
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:26:05.097362
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:26:07.511399
# Unit test for function get_repr_function

# Generated at 2026-10-25 00:26:09.925953
# Unit test for function get_repr_function

# Generated at 2026-10-25 00:26:12.341988
# Unit test for function get_repr_function

# Generated at 2026-10-25 00:26:14.757737
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:26:17.171594
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:26:19.589207
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:26:22.010114
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:26:28.039939
# Unit test for method write of class WritableStream
def test_WritableStream_write():result = WritableStream.write(object(), "hello")

# Generated at 2026-10-25 00:26:39.201511
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    assert WritableStream.write.__isabstractmethod__

    class IncompleteStream(WritableStream):
        pass

    with pytest.raises(TypeError):
        IncompleteStream()

    class MemoryStream(WritableStream):
        def __init__(self):
            self.contents = []

        def module_0.write(self, s):
            self.contents.append(s)
            return len(s)

    stream = MemoryStream()

    assert isinstance(stream, WritableStream)
    assert stream.write("hello") == 5
    assert stream.contents == ["hello"]

# Generated at 2026-10-25 00:26:40.637358
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:26:41.968802
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:26:48.301781
# Unit test for function get_repr_function
def test_get_repr_function():
    class Example:
        pass

    type_repr = lambda item: 'type match'
    predicate_repr = lambda item: 'predicate match'

    custom_repr = (
        (Example, type_repr),
        (lambda item: item == 42, predicate_repr),
    )

    # Matches a type condition, including subclasses.
    assert module_0.get_repr_function(Example(), custom_repr) is type_repr

    class ExampleSubclass(Example):
        pass

    assert module_0.get_repr_function(ExampleSubclass(), custom_repr) is type_repr

    # Matches a callable condition.
    assert module_0.get_repr_function(42, custom_repr) is predicate_repr

    # Falls back to the built-in repr when no condition matches.
    assert module_0.get_repr_function('unmatched', custom_repr) is repr

# Generated at 2026-10-25 00:26:56.916823
# Unit test for function get_repr_function
def test_get_repr_function():
    class Parent:
        pass

    class Child(Parent):
        pass

    parent_repr = lambda item: 'parent'
    predicate_repr = lambda item: 'predicate'
    first_repr = lambda item: 'first'
    second_repr = lambda item: 'second'

    # Type conditions use isinstance(), including subclasses.
    assert module_0.get_repr_function(
        Child(),
        ((Parent, parent_repr),)
    ) is parent_repr

    # Callable conditions are evaluated directly.
    assert module_0.get_repr_function(
        42,
        ((lambda item: item == 42, predicate_repr),)
    ) is predicate_repr

    # The first matching rule wins.
    assert module_0.get_repr_function(
        Child(),
        (
            (Parent, first_repr),
            (Child, second_repr),
        )
    ) is first_repr

    # Fall back to the built-in repr when no condition matches.
    assert module_0.get_repr_function(
        'unmatched',
        ((Parent, parent_repr),)
    ) is repr

    # An empty configuration also falls back to repr.
    assert module_0.get_repr_function('anything', ()) is repr

# Generated at 2026-10-25 00:26:59.346140
# Unit test for function get_repr_function

# Generated at 2026-10-25 00:27:01.760364
# Unit test for function get_repr_function

# Generated at 2026-10-25 00:27:04.176054
# Unit test for function get_repr_function

# Generated at 2026-10-25 00:27:06.724674
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 00:27:09.140516
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 00:27:11.555845
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 00:27:13.968443
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:27:16.382618
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:27:18.797563
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:27:21.213466
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:27:23.629950
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:27:26.046840
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:27:28.461572
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:27:30.876022
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:27:33.295836
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:27:35.711175
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:27:38.124525
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:27:40.548088
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:27:42.962207
# Unit test for function get_repr_function

# Generated at 2026-10-25 00:27:45.376774
# Unit test for function get_repr_function

# Generated at 2026-10-25 00:27:47.790642
# Unit test for function get_repr_function

# Generated at 2026-10-25 00:27:51.592390
# Unit test for function get_repr_function

# Generated at 2026-10-25 00:27:54.006381
# Unit test for function get_repr_function

# Generated at 2026-10-25 00:28:05.738459
# Unit test for function get_repr_function
def test_get_repr_function():f = lambda x: 'C'

# Generated at 2026-10-25 00:28:13.347260
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    # WritableStream cannot be instantiated because write is abstract.
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError("WritableStream should not be directly instantiable")

    class TestStream(WritableStream):
        def __init__(self):
            self.contents = []

        def module_0.write(self, s):
            self.contents.append(s)
            return len(s)

    stream = TestStream()

    assert stream.write("hello") == 5
    assert stream.contents == ["hello"]
    assert isinstance(stream, WritableStream)

# Generated at 2026-10-25 00:28:14.739411
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    # Default repr
    assert module_0.get_shortish_repr(42) == '42'
    assert module_0.get_shortish_repr('foo') == "'foo'"

    # Newlines and carriage returns are stripped
    class WithNewlines:
        def __repr__(self):
            return 'line1\r\nline2'
    assert module_0.get_shortish_repr(WithNewlines()) == 'line1line2'

    # Repr that raises -> 'REPR FAILED'
    class BadRepr:
        def __repr__(self):
            raise RuntimeError('nope')
    assert module_0.get_shortish_repr(BadRepr()) == 'REPR FAILED'

    # custom_repr: type condition overrides repr
    class Custom:
        def __repr__(self):
            return 'default'
    assert module_0.get_shortish_repr(
        Custom(), custom_repr=((Custom, lambda x: 'custom'),)
    ) == 'custom'

    # custom_repr: callable condition overrides repr
    assert module_0.get_shortish_repr(
        Custom(), custom_repr=((lambda x: isinstance(x, Custom),
                                lambda x: 'callable-condition'),)
    ) == 'callable-condition'

    # custom_repr entry that doesn't match falls back to repr
    assert module_0.get_shortish_repr(
        Custom(), custom_repr=((int, lambda x: 'int!'),)
    ) == 'default'

    # normalize=True removes memory addresses
    class WithAddress:
        def __repr__(self):
            return '<WithAddress object at 0x7f3a1b2c4d5e>'
    assert module_0.get_shortish_repr(WithAddress(), normalize=True) == \
        '<WithAddress object>'
    assert module_0.get_shortish_repr(WithAddress(), normalize=False).startswith(
        '<WithAddress object at 0x'
    )

    # max_length truncates, keeping both head and tail
    long_string = 'a' * 100 + 'b' * 100
    result = module_0.get_shortish_repr(long_string, max_length=20)
    assert len(result) == 20
    assert result == ('a' * 8) + '...' + ('b' * 9)

    # max_length=None or short strings: unchanged
    assert module_0.get_shortish_repr('short', max_length=100) == 'short'
    assert module_0.get_shortish_repr('short') == 'short'

# Generated at 2026-10-25 00:28:25.289722
# Unit test for function get_repr_function
def test_get_repr_function():
    class Base:
        pass

    class Child(Base):
        pass

    base_repr = lambda item: 'base'
    special_repr = lambda item: 'special'

    custom_repr = (
        (lambda item: item == 'special', special_repr),
        (Base, base_repr),
    )

    assert module_0.get_repr_function('special', custom_repr) is special_repr
    assert module_0.get_repr_function(Base(), custom_repr) is base_repr
    assert module_0.get_repr_function(Child(), custom_repr) is base_repr
    assert module_0.get_repr_function('ordinary', custom_repr) is repr

# Generated at 2026-10-25 00:28:26.632511
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    # Default repr
    assert module_0.get_shortish_repr(42) == '42'
    assert module_0.get_shortish_repr('foo') == "'foo'"

    # Newlines and carriage returns are stripped
    class WithNewlines:
        def __repr__(self):
            return 'line1\r\nline2'
    assert module_0.get_shortish_repr(WithNewlines()) == 'line1line2'

    # Repr that raises -> 'REPR FAILED'
    class BadRepr:
        def __repr__(self):
            raise RuntimeError('nope')
    assert module_0.get_shortish_repr(BadRepr()) == 'REPR FAILED'

    # custom_repr: type condition overrides repr
    class Custom:
        def __repr__(self):
            return 'default'
    assert module_0.get_shortish_repr(
        Custom(), custom_repr=((Custom, lambda x: 'custom'),)
    ) == 'custom'

    # custom_repr: callable condition overrides repr
    assert module_0.get_shortish_repr(
        Custom(), custom_repr=((lambda x: isinstance(x, Custom),
                                lambda x: 'callable-condition'),)
    ) == 'callable-condition'

    # custom_repr entry that doesn't match falls back to repr
    assert module_0.get_shortish_repr(
        Custom(), custom_repr=((int, lambda x: 'int!'),)
    ) == 'default'

    # normalize=True removes memory addresses
    class WithAddress:
        def __repr__(self):
            return '<WithAddress object at 0x7f3a1b2c4d5e>'
    assert module_0.get_shortish_repr(WithAddress(), normalize=True) == \
        '<WithAddress object>'
    assert module_0.get_shortish_repr(WithAddress(), normalize=False).startswith(
        '<WithAddress object at 0x'
    )

    # max_length truncates, keeping both head and tail
    long_string = 'a' * 100 + 'b' * 100
    result = module_0.get_shortish_repr(long_string, max_length=20)
    assert len(result) == 20
    assert result == ('a' * 8) + '...' + ('b' * 9)

    # max_length=None or short strings: unchanged
    assert module_0.get_shortish_repr('short', max_length=100) == 'short'
    assert module_0.get_shortish_repr('short') == 'short'

# Generated at 2026-10-25 00:28:33.173249
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    assert WritableStream.write.__isabstractmethod__

    class ConcreteWritableStream(WritableStream):
        def __init__(self):
            self.output = []

        def module_0.write(self, s):
            self.output.append(s)
            return len(s)

    stream = ConcreteWritableStream()

    assert stream.write('hello') == 5
    assert stream.output == ['hello']

# Generated at 2026-10-25 00:28:35.593408
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 00:28:38.115590
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 00:28:40.644780
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 00:28:43.060138
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:28:45.475066
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:28:47.890938
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 00:28:50.495032
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 00:28:52.912054
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 00:28:55.328449
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 00:28:57.742816
# Unit test for function get_repr_function

# Generated at 2026-10-25 00:28:59.183960
# Unit test for function get_repr_function
def test_get_repr_function():f = lambda x: 'C'

# Generated at 2026-10-25 00:29:12.707276
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    # The abstract base class cannot be instantiated directly.
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError("WritableStream should be abstract")

    class Buffer(WritableStream):
        def __init__(self):
            self.data = []

        def module_0.write(self, s):
            self.data.append(s)

    stream = Buffer()
    stream.write("hello")
    stream.write(" world")

    assert stream.data == ["hello", " world"]

    # The subclass hook also accepts duck-typed classes with module_0.write().
    class DuckTypedStream:
        def module_0.write(self, s):
            return len(s)

    assert issubclass(DuckTypedStream, WritableStream)
    assert isinstance(DuckTypedStream(), WritableStream)

# Generated at 2026-10-25 00:29:20.585285
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class TestStream(WritableStream):
        def __init__(self):
            self.contents = []

        def module_0.write(self, s):
            self.contents.append(s)
            return len(s)

    stream = TestStream()

    assert isinstance(stream, WritableStream)
    assert stream.write('hello') == 5
    assert stream.contents == ['hello']

    # WritableStream also supports structural subclassing.
    class DuckTypedStream:
        def module_0.write(self, s):
            return len(s)

    assert issubclass(DuckTypedStream, WritableStream)
    assert isinstance(DuckTypedStream(), WritableStream)

    # The abstract base class itself cannot be instantiated.
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError('WritableStream should not be instantiable')

# Generated at 2026-10-25 00:29:28.367361
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class ConcreteWritableStream(WritableStream):
        def __init__(self):
            self.contents = ''

        def module_0.write(self, s):
            self.contents += s
            return len(s)

    stream = ConcreteWritableStream()

    assert stream.write('hello') == 5
    assert stream.contents == 'hello'
    assert isinstance(stream, WritableStream)

    # The subclass hook also accepts duck-typed classes with a write method.
    class DuckTypedStream:
        def module_0.write(self, s):
            return len(s)

    assert issubclass(DuckTypedStream, WritableStream)

    # WritableStream itself cannot be instantiated because write is abstract.
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError('WritableStream should not be instantiable')