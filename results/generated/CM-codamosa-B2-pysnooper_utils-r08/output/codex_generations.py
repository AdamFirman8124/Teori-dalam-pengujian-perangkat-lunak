

# Generated at 2026-10-25 01:49:58.884207
# Unit test for function ensure_tuple
def test_ensure_tuple():
    # Non-iterables are wrapped in a one-item tuple.
    assert module_0.ensure_tuple(42) == (42,)
    assert module_0.ensure_tuple(None) == (None,)

    # Strings are treated as scalar values, not iterables.
    assert module_0.ensure_tuple('hello') == ('hello',)
    assert module_0.ensure_tuple('') == ('',)

    # Other iterables are converted to tuples.
    assert module_0.ensure_tuple([1, 2, 3]) == (1, 2, 3)
    assert module_0.ensure_tuple((1, 2, 3)) == (1, 2, 3)
    assert module_0.ensure_tuple(range(3)) == (0, 1, 2)
    assert module_0.ensure_tuple(x for x in [1, 2, 3]) == (1, 2, 3)
    assert module_0.ensure_tuple([]) == ()

# Generated at 2026-10-25 01:50:00.284398
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

# Generated at 2026-10-25 01:50:08.735557
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    # The abstract class cannot be instantiated directly.
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError("WritableStream should not be instantiable")

    class MemoryStream(WritableStream):
        def __init__(self):
            self.contents = []

        def module_0.write(self, s):
            self.contents.append(s)
            return len(s)

    stream = MemoryStream()

    assert stream.write("hello") == 5
    assert stream.write(" world") == 6
    assert stream.contents == ["hello", " world"]
    assert isinstance(stream, WritableStream)

# Generated at 2026-10-25 01:50:11.378391
# Unit test for constructor of class WritableStream

# Generated at 2026-10-25 01:50:25.016204
# Unit test for constructor of class WritableStream

# Generated at 2026-10-25 01:50:26.360483
# Unit test for constructor of class WritableStream

# Generated at 2026-10-25 01:50:34.545256
# Unit test for function get_repr_function
def test_get_repr_function():
    def string_repr(item):
        return '<string: {}>'.format(item)

    def answer_repr(item):
        return '<answer>'

    def fallback_custom_repr(item):
        return '<custom>'

    custom_repr = (
        (str, string_repr),
        (lambda item: item == 42, answer_repr),
        (lambda item: True, fallback_custom_repr),
    )

    # Type-based condition.
    assert module_0.get_repr_function('hello', custom_repr) is string_repr

    # Callable condition.
    assert module_0.get_repr_function(42, custom_repr) is answer_repr

    # First matching condition wins.
    assert module_0.get_repr_function('42', custom_repr) is string_repr

    # Generic custom fallback.
    assert module_0.get_repr_function(None, custom_repr) is fallback_custom_repr

    # Built-in repr is returned when no condition matches.
    assert module_0.get_repr_function(3.14, ()) is repr

# Generated at 2026-10-25 01:50:43.159891
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    # WritableStream cannot be instantiated without implementing module_0.write().
    with pytest.raises(TypeError):
        WritableStream()

    class BufferStream(WritableStream):
        def __init__(self):
            self.contents = []

        def module_0.write(self, s):
            self.contents.append(s)
            return len(s)

    stream = BufferStream()

    assert stream.write("hello") == 5
    assert stream.contents == ["hello"]

# Generated at 2026-10-25 01:50:50.629236
# Unit test for function get_repr_function
def test_get_repr_function():
    def integer_repr(item):
        return 'integer: {}'.format(item)

    def special_repr(item):
        return 'special: {}'.format(item)

    custom_repr = (
        (int, integer_repr),
        (lambda item: item == 'special', special_repr),
    )

    # Type-based condition.
    assert module_0.get_repr_function(42, custom_repr) is integer_repr

    # Callable condition.
    assert module_0.get_repr_function('special', custom_repr) is special_repr

    # No matching condition falls back to the built-in repr.
    assert module_0.get_repr_function('ordinary', custom_repr) is repr

# Generated at 2026-10-25 01:50:57.375177
# Unit test for function truncate

# Generated at 2026-10-25 01:50:58.707254
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

# Generated at 2026-10-25 01:51:06.416595
# Unit test for function get_repr_function
def test_get_repr_function():
    class Parent:
        pass

    class Child(Parent):
        pass

    item = Child()

    parent_repr = lambda obj: 'parent'
    predicate_repr = lambda obj: 'predicate'
    fallback_repr = lambda obj: 'fallback'

    # Type conditions use isinstance(), including subclasses.
    assert module_0.get_repr_function(item, (
        (Parent, parent_repr),
    )) is parent_repr

    # Callable conditions are supported.
    assert module_0.get_repr_function(item, (
        (lambda obj: False, fallback_repr),
        (lambda obj: obj is item, predicate_repr),
    )) is predicate_repr

    # The first matching condition wins.
    assert module_0.get_repr_function(item, (
        (lambda obj: True, predicate_repr),
        (Parent, parent_repr),
    )) is predicate_repr

    # Fall back to the built-in repr when nothing matches.
    assert module_0.get_repr_function(item, (
        (str, fallback_repr),
        (lambda obj: False, predicate_repr),
    )) is repr

# Generated at 2026-10-25 01:51:08.834685
# Unit test for function shitcode

# Generated at 2026-10-25 01:51:11.489654
# Unit test for function shitcode

# Generated at 2026-10-25 01:51:13.906396
# Unit test for function shitcode

# Generated at 2026-10-25 01:51:16.322010
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 01:51:37.311475
# Unit test for function get_shortish_repr
def test_get_shortish_repr():assert module_0.get_shortish_repr("abcdefghij", max_length=7) == "'a...j'"

# Generated at 2026-10-25 01:51:38.746059
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

# Generated at 2026-10-25 01:51:48.576155
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class IncompleteStream(WritableStream):
        pass

    with pytest.raises(TypeError):
        IncompleteStream()

    class ConcreteStream(WritableStream):
        def __init__(self):
            self.contents = ''

        def module_0.write(self, s):
            self.contents += s
            return len(s)

    stream = ConcreteStream()

    assert stream.write('hello') == 5
    assert stream.contents == 'hello'

    class StructuralStream:
        def module_0.write(self, s):
            return s

    assert issubclass(StructuralStream, WritableStream)
    assert isinstance(StructuralStream(), WritableStream)

# Generated at 2026-10-25 01:51:50.008664
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 01:51:51.441999
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 01:51:52.767228
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

# Generated at 2026-10-25 01:51:54.126130
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

# Generated at 2026-10-25 01:52:02.713382
# Unit test for function get_repr_function

# Generated at 2026-10-25 01:52:04.087843
# Unit test for function get_repr_function
def test_get_repr_function():f = lambda x: 'C'

# Generated at 2026-10-25 01:52:06.717171
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 01:52:09.131800
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 01:52:11.662358
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 01:52:14.077118
# Unit test for function shitcode

# Generated at 2026-10-25 01:52:16.489956
# Unit test for function shitcode

# Generated at 2026-10-25 01:52:18.905658
# Unit test for function shitcode

# Generated at 2026-10-25 01:52:21.320520
# Unit test for function get_repr_function

# Generated at 2026-10-25 01:52:23.734881
# Unit test for function get_repr_function

# Generated at 2026-10-25 01:52:29.744900
# Unit test for function get_repr_function
def test_get_repr_function():custom_repr = (
        (int, lambda value: "integer:{}".format(value)),
        (lambda value: value == "special", lambda value: "SPECIAL"),
    )

# Generated at 2026-10-25 01:52:31.379662
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

# Generated at 2026-10-25 01:52:32.817060
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

# Generated at 2026-10-25 01:52:42.438302
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class IncompleteStream(WritableStream):
        pass

    with pytest.raises(TypeError):
        IncompleteStream()

    class ConcreteStream(WritableStream):
        def __init__(self):
            self.contents = ''

        def module_0.write(self, s):
            self.contents += s
            return len(s)

    stream = ConcreteStream()

    assert stream.write('hello') == 5
    assert stream.contents == 'hello'

# Generated at 2026-10-25 01:52:43.770673
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 01:52:45.096398
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 01:52:51.859323
# Unit test for function get_repr_function
def test_get_repr_function():
    string_repr = lambda item: f'string: {item}'
    positive_int_repr = lambda item: f'positive integer: {item}'

    custom_repr = (
        (str, string_repr),
        (lambda item: isinstance(item, int) and item > 0, positive_int_repr),
    )

    # Type conditions use isinstance().
    assert module_0.get_repr_function('hello', custom_repr) is string_repr

    # Callable conditions are evaluated directly.
    assert module_0.get_repr_function(42, custom_repr) is positive_int_repr

    # Fall back to the built-in repr when no condition matches.
    assert module_0.get_repr_function(-1, custom_repr) is repr
    assert module_0.get_repr_function(object(), custom_repr) is repr

# Generated at 2026-10-25 01:52:53.292241
# Unit test for function get_repr_function
def test_get_repr_function():f = lambda x: 'C'

# Generated at 2026-10-25 01:53:00.768285
# Unit test for function get_repr_function
def test_get_repr_function():
    def integer_repr(item):
        return 'integer: {}'.format(item)

    def positive_repr(item):
        return 'positive: {}'.format(item)

    custom_repr = (
        (lambda item: isinstance(item, int) and item > 0, positive_repr),
        (int, integer_repr),
    )

    # Callable conditions are evaluated first.
    assert module_0.get_repr_function(5, custom_repr) is positive_repr

    # Type conditions use isinstance().
    assert module_0.get_repr_function(-5, custom_repr) is integer_repr

    # The built-in repr is returned when no condition matches.
    assert module_0.get_repr_function('hello', custom_repr) is repr

    # Matching respects declaration order.
    reversed_custom_repr = (
        (int, integer_repr),
        (lambda item: isinstance(item, int) and item > 0, positive_repr),
    )
    assert module_0.get_repr_function(5, reversed_custom_repr) is integer_repr

# Generated at 2026-10-25 01:53:02.212483
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

# Generated at 2026-10-25 01:53:03.566182
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

# Generated at 2026-10-25 01:53:10.807743
# Unit test for function get_repr_function
def test_get_repr_function():
    class Parent:
        pass

    class Child(Parent):
        pass

    type_repr = lambda item: 'type match'
    predicate_repr = lambda item: 'predicate match'

    custom_repr = (
        (Parent, type_repr),
        (lambda item: item == 42, predicate_repr),
    )

    # Type conditions use isinstance, including subclasses.
    assert module_0.get_repr_function(Parent(), custom_repr) is type_repr
    assert module_0.get_repr_function(Child(), custom_repr) is type_repr

    # Callable conditions are evaluated directly.
    assert module_0.get_repr_function(42, custom_repr) is predicate_repr

    # The default is the built-in repr function.
    assert module_0.get_repr_function('unmatched', custom_repr) is repr

    # The first matching condition wins.
    first_repr = lambda item: 'first'
    second_repr = lambda item: 'second'
    matches_everything = (
        (lambda item: True, first_repr),
        (lambda item: True, second_repr),
    )
    assert module_0.get_repr_function(object(), matches_everything) is first_repr

# Generated at 2026-10-25 01:53:13.337372
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 01:53:15.751272
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 01:53:18.166160
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 01:53:20.581660
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 01:53:22.996128
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 01:53:25.411264
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 01:53:26.804109
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

# Generated at 2026-10-25 01:53:34.662907
# Unit test for function get_repr_function
def test_get_repr_function():
    def repr_int(item):
        return 'integer: {}'.format(item)

    def repr_negative(item):
        return 'negative: {}'.format(item)

    custom_repr = (
        (lambda item: isinstance(item, int) and item < 0, repr_negative),
        (int, repr_int),
    )

    # Callable conditions are evaluated in order.
    assert module_0.get_repr_function(-1, custom_repr) is repr_negative

    # Type conditions match using isinstance().
    assert module_0.get_repr_function(1, custom_repr) is repr_int

    # Fall back to the built-in repr when no condition matches.
    assert module_0.get_repr_function('text', custom_repr) is repr

# Generated at 2026-10-25 01:53:36.302793
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

# Generated at 2026-10-25 01:53:46.234738
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class ConcreteWritableStream(WritableStream):
        def __init__(self):
            self.written = []

        def module_0.write(self, s):
            self.written.append(s)
            return len(s)

    stream = ConcreteWritableStream()

    assert isinstance(stream, WritableStream)
    assert stream.write('hello') == 5
    assert stream.written == ['hello']

    class DuckTypedStream:
        def module_0.write(self, s):
            return s

    assert issubclass(DuckTypedStream, WritableStream)
    assert isinstance(DuckTypedStream(), WritableStream)

# Generated at 2026-10-25 01:53:54.918134
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    assert getattr(WritableStream.write, '__isabstractmethod__', False)

    class ConcreteWritableStream(WritableStream):
        def __init__(self):
            self.contents = ''

        def module_0.write(self, s):
            self.contents += s

    stream = ConcreteWritableStream()
    stream.write('hello')
    stream.write(' world')

    assert stream.contents == 'hello world'
    assert isinstance(stream, WritableStream)

# Generated at 2026-10-25 01:53:56.563649
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

# Generated at 2026-10-25 01:54:05.261420
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    # WritableStream cannot be instantiated without implementing module_0.write().
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError("WritableStream should be abstract")

    class BufferStream(WritableStream):
        def __init__(self):
            self.contents = []

        def module_0.write(self, s):
            self.contents.append(s)
            return len(s)

    stream = BufferStream()

    assert stream.write("hello") == 5
    assert stream.contents == ["hello"]
    assert isinstance(stream, WritableStream)

    # The subclass hook should also recognize structural implementations.
    class DuckTypedStream:
        def module_0.write(self, s):
            return len(s)

    assert issubclass(DuckTypedStream, WritableStream)

# Generated at 2026-10-25 01:54:13.268513
# Unit test for function get_repr_function
def test_get_repr_function():
    def repr_for_int(item):
        return 'integer: {}'.format(item)

    def repr_for_even(item):
        return 'even: {}'.format(item)

    custom_repr = (
        (lambda item: isinstance(item, int) and item % 2 == 0, repr_for_even),
        (int, repr_for_int),
    )

    # Predicate conditions are supported, and the first match wins.
    assert module_0.get_repr_function(2, custom_repr) is repr_for_even

    # Types are treated as isinstance checks.
    assert module_0.get_repr_function(3, custom_repr) is repr_for_int

    # repr is returned when no custom condition matches.
    assert module_0.get_repr_function('hello', custom_repr) is repr

# Generated at 2026-10-25 01:54:14.611340
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

# Generated at 2026-10-25 01:54:17.285635
# Unit test for function shitcode

# Generated at 2026-10-25 01:54:19.699322
# Unit test for function shitcode

# Generated at 2026-10-25 01:54:22.246980
# Unit test for function shitcode

# Generated at 2026-10-25 01:54:24.662745
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 01:54:27.080449
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 01:54:29.496092
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 01:54:31.910829
# Unit test for function shitcode

# Generated at 2026-10-25 01:54:34.324964
# Unit test for function shitcode

# Generated at 2026-10-25 01:54:36.739413
# Unit test for function shitcode

# Generated at 2026-10-25 01:54:39.156669
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 01:54:41.572095
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 01:54:51.261935
# Unit test for function get_shortish_repr
def test_get_shortish_repr():result = module_0.get_shortish_repr(
        'abcdefgh',
        custom_repr=((str, lambda value: '<' + value + '>\n'),),
        max_length=9,
    )

# Generated at 2026-10-25 01:54:57.710048
# Unit test for function get_repr_function
def test_get_repr_function():
    class Foo:
        pass

    foo = Foo()

    def foo_repr(item):
        return 'foo'

    def predicate_repr(item):
        return 'predicate'

    def never_matches(item):
        return False

    def matches_foo(item):
        return isinstance(item, Foo)

    # A type can be used as a condition.
    assert module_0.get_repr_function(foo, ((Foo, foo_repr),)) is foo_repr

    # A predicate can be used as a condition.
    assert module_0.get_repr_function(
        foo,
        ((never_matches, foo_repr), (matches_foo, predicate_repr))
    ) is predicate_repr

    # The first matching rule wins.
    assert module_0.get_repr_function(
        foo,
        ((Foo, foo_repr), (matches_foo, predicate_repr))
    ) is foo_repr

    # Fall back to the built-in repr when no rule matches.
    assert module_0.get_repr_function(foo, ((never_matches, foo_repr),)) is repr
    assert module_0.get_repr_function(foo, ()) is repr

# Generated at 2026-10-25 01:55:05.392124
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class TestStream(WritableStream):
        def __init__(self):
            self.contents = []

        def module_0.write(self, s):
            self.contents.append(s)

    stream = TestStream()
    stream.write("hello")

    assert stream.contents == ["hello"]
    assert isinstance(stream, WritableStream)

    # The subclass hook should recognize classes that provide module_0.write().
    class DuckTypedStream:
        def module_0.write(self, s):
            return len(s)

    assert issubclass(DuckTypedStream, WritableStream)
    assert DuckTypedStream().write("hello") == 5

    # WritableStream itself cannot be instantiated because write is abstract.
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError("WritableStream should not be directly instantiable")

# Generated at 2026-10-25 01:55:06.830613
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

# Generated at 2026-10-25 01:55:08.256536
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

# Generated at 2026-10-25 01:55:09.691094
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

# Generated at 2026-10-25 01:55:19.318676
# Unit test for function get_repr_function
def test_get_repr_function():
    class Parent(object):
        pass

    class Child(Parent):
        pass

    def type_repr(item):
        return 'type repr'

    def predicate_repr(item):
        return 'predicate repr'

    custom_repr = (
        (Parent, type_repr),
        (lambda item: item == 42, predicate_repr),
    )

    assert module_0.get_repr_function(Child(), custom_repr) is type_repr
    assert module_0.get_repr_function(42, custom_repr) is predicate_repr
    assert module_0.get_repr_function('unmatched', custom_repr) is repr

# Generated at 2026-10-25 01:55:20.654444
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

# Generated at 2026-10-25 01:55:29.353582
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    assert 'write' in WritableStream.__abstractmethods__

    with pytest.raises(TypeError):
        WritableStream()

    class RecordingStream(WritableStream):
        def __init__(self):
            self.written = []

        def module_0.write(self, s):
            self.written.append(s)
            return len(s)

    stream = RecordingStream()

    assert stream.write('hello') == 5
    assert stream.written == ['hello']
    assert isinstance(stream, WritableStream)

# Generated at 2026-10-25 01:55:30.792563
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

# Generated at 2026-10-25 01:55:32.125311
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

# Generated at 2026-10-25 01:55:34.647963
# Unit test for function get_repr_function

# Generated at 2026-10-25 01:55:37.063499
# Unit test for function get_repr_function

# Generated at 2026-10-25 01:55:39.478288
# Unit test for function get_repr_function

# Generated at 2026-10-25 01:55:42.075715
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 01:55:44.492646
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 01:55:45.942107
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 01:55:53.620138
# Unit test for function get_repr_function
def test_get_repr_function():
    def int_repr(value):
        return 'integer: {}'.format(value)

    def even_repr(value):
        return 'even: {}'.format(value)

    def fallback_custom_repr(value):
        return 'custom: {}'.format(value)

    # A type condition matches via isinstance().
    assert module_0.get_repr_function(42, ((int, int_repr),)) is int_repr

    # Callable conditions are supported.
    assert module_0.get_repr_function(
        42,
        ((lambda value: value % 2 == 0, even_repr),)
    ) is even_repr

    # The first matching condition wins.
    assert module_0.get_repr_function(
        42,
        (
            (int, int_repr),
            (lambda value: True, fallback_custom_repr),
        )
    ) is int_repr

    # Subclasses also match type conditions.
    class CustomInt(int):
        pass

    assert module_0.get_repr_function(
        CustomInt(42),
        ((int, int_repr),)
    ) is int_repr

    # If no condition matches, the built-in repr is returned.
    assert module_0.get_repr_function(
        'hello',
        ((int, int_repr),)
    ) is repr

    # An empty customization list also falls back to repr.
    assert module_0.get_repr_function('hello', ()) is repr

# Generated at 2026-10-25 01:56:02.631659
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class ConcreteWritableStream(WritableStream):
        def __init__(self):
            self.contents = []

        def module_0.write(self, s):
            self.contents.append(s)
            return len(s)

    stream = ConcreteWritableStream()

    result = stream.write("hello")

    assert result == 5
    assert stream.contents == ["hello"]
    assert isinstance(stream, WritableStream)

# Generated at 2026-10-25 01:56:04.066040
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

# Generated at 2026-10-25 01:56:15.636676
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    # WritableStream cannot be instantiated until module_0.write() is implemented.
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError("WritableStream should be abstract")

    class MemoryStream(WritableStream):
        def __init__(self):
            self.contents = []

        def module_0.write(self, s):
            self.contents.append(s)
            return len(s)

    stream = MemoryStream()

    assert stream.write("hello") == 5
    assert stream.write(" world") == 6
    assert stream.contents == ["hello", " world"]

# Generated at 2026-10-25 01:56:23.827924
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MemoryStream(WritableStream):
        def __init__(self):
            self.data = []

        def module_0.write(self, s):
            self.data.append(s)
            return len(s)

    stream = MemoryStream()

    assert stream.write('hello') == 5
    assert stream.data == ['hello']

    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError(
            'WritableStream should not be instantiable without implementing write'
        )

# Generated at 2026-10-25 01:56:31.713509
# Unit test for function get_repr_function
def test_get_repr_function():
    int_repr = lambda item: 'integer: {}'.format(item)
    positive_repr = lambda item: 'positive: {}'.format(item)

    custom_repr = (
        (int, int_repr),
        (lambda item: isinstance(item, float) and item > 0, positive_repr),
    )

    # Type-based condition.
    assert module_0.get_repr_function(42, custom_repr) is int_repr

    # Callable condition.
    assert module_0.get_repr_function(3.14, custom_repr) is positive_repr

    # No matching condition falls back to built-in repr.
    assert module_0.get_repr_function('hello', custom_repr) is repr

# Generated at 2026-10-25 01:56:37.037483
# Unit test for function get_repr_function

# Generated at 2026-10-25 01:56:39.578778
# Unit test for function get_repr_function

# Generated at 2026-10-25 01:56:41.993557
# Unit test for function get_repr_function

# Generated at 2026-10-25 01:56:44.408887
# Unit test for function shitcode

# Generated at 2026-10-25 01:56:49.121469
# Unit test for function shitcode
def test_shitcode():assert module_0.shitcode("Hello, ä¸ç! cafÃ© \x00") == "Hello, ??! cafÃ© ?"

# Generated at 2026-10-25 01:56:50.494952
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

# Generated at 2026-10-25 01:57:01.513417
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class ConcreteWritableStream(WritableStream):
        def __init__(self):
            self.written = []

        def module_0.write(self, s):
            self.written.append(s)
            return len(s)

    # The abstract class cannot be instantiated directly.
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError("WritableStream should not be directly instantiable")

    stream = ConcreteWritableStream()

    assert stream.write("hello") == 5
    assert stream.written == ["hello"]
    assert isinstance(stream, WritableStream)

    # The subclass hook recognizes classes that provide module_0.write().
    class StructuralWritableStream:
        def module_0.write(self, s):
            return len(s)

    assert issubclass(StructuralWritableStream, WritableStream)

# Generated at 2026-10-25 01:57:10.933916
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    # The abstract class cannot be instantiated without implementing module_0.write().
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError("WritableStream should require module_0.write() to be implemented")

    class MemoryStream(WritableStream):
        def __init__(self):
            self.written = []

        def module_0.write(self, s):
            self.written.append(s)

    stream = MemoryStream()
    result = stream.write("hello")

    assert result is None
    assert stream.written == ["hello"]
    assert isinstance(stream, WritableStream)

# Generated at 2026-10-25 01:57:12.265052
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

# Generated at 2026-10-25 01:57:19.029302
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MemoryStream(WritableStream):
        def __init__(self):
            self.contents = []

        def module_0.write(self, s):
            self.contents.append(s)
            return len(s)

    stream = MemoryStream()

    result = stream.write("hello")

    assert result == 5
    assert stream.contents == ["hello"]
    assert isinstance(stream, WritableStream)

# Generated at 2026-10-25 01:57:20.356110
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

# Generated at 2026-10-25 01:57:27.214512
# Unit test for function get_repr_function
def test_get_repr_function():
    def repr_string(item):
        return '<string: {}>'.format(item)

    def repr_positive(item):
        return '<positive: {}>'.format(item)

    custom_repr = (
        (str, repr_string),
        (lambda item: isinstance(item, int) and item > 0, repr_positive),
    )

    assert module_0.get_repr_function('hello', custom_repr) is repr_string
    assert module_0.get_repr_function(42, custom_repr) is repr_positive
    assert module_0.get_repr_function(-1, custom_repr) is repr
    assert module_0.get_repr_function([], custom_repr) is repr

# Generated at 2026-10-25 01:57:29.635567
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 01:57:32.150170
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 01:57:34.564200
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 01:57:36.979431
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 01:57:39.394505
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 01:57:41.818343
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 01:57:44.232828
# Unit test for function get_repr_function

# Generated at 2026-10-25 01:57:46.651010
# Unit test for function get_repr_function

# Generated at 2026-10-25 01:57:53.108125
# Unit test for function get_repr_function
def test_get_repr_function():item = [1, 2, 3]

# Generated at 2026-10-25 01:58:03.567385
# Unit test for function get_repr_function
def test_get_repr_function():
    class Example:
        pass

    example_repr = lambda item: 'example'
    string_repr = lambda item: 'string'

    custom_repr = (
        (Example, example_repr),
        (lambda item: isinstance(item, str), string_repr),
    )

    # A type condition matches instances of that type.
    assert module_0.get_repr_function(Example(), custom_repr) is example_repr

    # Callable conditions are supported.
    assert module_0.get_repr_function('hello', custom_repr) is string_repr

    # The default repr function is returned when nothing matches.
    assert module_0.get_repr_function(42, custom_repr) is repr

    # The first matching rule takes precedence.
    first = lambda item: 'first'
    second = lambda item: 'second'
    overlapping_rules = (
        (lambda item: True, first),
        (lambda item: True, second),
    )
    assert module_0.get_repr_function(example, overlapping_rules) is first

# Generated at 2026-10-25 01:58:13.399513
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MemoryStream(WritableStream):
        def __init__(self):
            self.data = []

        def module_0.write(self, s):
            self.data.append(s)
            return len(s)

    stream = MemoryStream()

    assert isinstance(stream, WritableStream)
    assert stream.write('hello') == 5
    assert stream.data == ['hello']

# Generated at 2026-10-25 01:58:23.023658
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    with pytest.raises(TypeError):
        WritableStream()

    class RecordingStream(WritableStream):
        def __init__(self):
            self.written = []

        def module_0.write(self, s):
            self.written.append(s)
            return len(s)

    stream = RecordingStream()

    assert stream.write("hello") == 5
    assert stream.written == ["hello"]
    assert isinstance(stream, WritableStream)

    class DuckTypedStream:
        def module_0.write(self, s):
            return s

    assert issubclass(DuckTypedStream, WritableStream)
    assert isinstance(DuckTypedStream(), WritableStream)

# Generated at 2026-10-25 01:58:31.936545
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    assert WritableStream.write.__isabstractmethod__

    with pytest.raises(TypeError):
        WritableStream()

    class ConcreteWritableStream(WritableStream):
        def __init__(self):
            self.written = []

        def module_0.write(self, s):
            self.written.append(s)

    stream = ConcreteWritableStream()
    result = stream.write("hello")

    assert stream.written == ["hello"]
    assert result is None

# Generated at 2026-10-25 01:58:34.352971
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 01:58:36.768856
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 01:58:39.447898
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 01:58:41.862993
# Unit test for function get_repr_function

# Generated at 2026-10-25 01:58:44.277802
# Unit test for function get_repr_function

# Generated at 2026-10-25 01:58:46.692418
# Unit test for function get_repr_function

# Generated at 2026-10-25 01:58:49.113560
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 01:58:51.525205
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 01:58:53.939637
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 01:58:56.558005
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    output = []

    class MyWritableStream(WritableStream):
        def module_0.write(self, s):
            output.append(s)

    my_writable_stream = MyWritableStream()
    message = 'Me write lovely message!'
    my_writable_stream.write(message)
    assert output == [message]

    assert issubclass(MyWritableStream, WritableStream)
    assert isinstance(my_writable_stream, WritableStream)

    class MyNonWritableStream:
        pass

    assert not issubclass(MyNonWritableStream, WritableStream)
    assert not isinstance(MyNonWritableStream(), WritableStream)

# Generated at 2026-10-25 01:59:06.338055
# Unit test for function get_repr_function
def test_get_repr_function():
    int_repr = lambda item: f'int:{item}'
    positive_repr = lambda item: f'positive:{item}'
    fallback_repr = lambda item: f'fallback:{item}'

    custom_repr = (
        (int, int_repr),
        (lambda item: isinstance(item, float) and item > 0, positive_repr),
        (lambda item: True, fallback_repr),
    )

    # Type-based conditions use isinstance.
    assert module_0.get_repr_function(42, custom_repr) is int_repr
    assert module_0.get_repr_function(True, custom_repr) is int_repr

    # Callable conditions are supported.
    assert module_0.get_repr_function(1.5, custom_repr) is positive_repr

    # The first matching condition is returned.
    assert module_0.get_repr_function(-1.5, custom_repr) is fallback_repr

    # Built-in repr is returned when no condition matches.
    assert module_0.get_repr_function("hello", ()) is repr

# Generated at 2026-10-25 01:59:07.773336
# Unit test for function get_repr_function
def test_get_repr_function():f = lambda x: 'C'

# Generated at 2026-10-25 01:59:09.122362
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

# Generated at 2026-10-25 01:59:10.457495
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

# Generated at 2026-10-25 01:59:25.915758
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import pytest

    # WritableStream cannot be instantiated without implementing module_0.write().
    with pytest.raises(TypeError):
        WritableStream()

    class TestStream(WritableStream):
        def __init__(self):
            self.written = []

        def module_0.write(self, s):
            self.written.append(s)
            return len(s)

    stream = TestStream()

    assert stream.write('hello') == 5
    assert stream.written == ['hello']
    assert isinstance(stream, WritableStream)

# Generated at 2026-10-25 01:59:27.332695
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

# Generated at 2026-10-25 01:59:36.961544
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    # WritableStream cannot be instantiated without implementing module_0.write().
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError(
            "WritableStream should not be instantiable while module_0.write() is abstract"
        )

    class ConcreteWritableStream(WritableStream):
        def __init__(self):
            self.data = []

        def module_0.write(self, s):
            self.data.append(s)
            return len(s)

    stream = ConcreteWritableStream()

    assert stream.write("hello") == 5
    assert stream.data == ["hello"]

    # The subclass hook also accepts classes that provide module_0.write()
    # without explicitly inheriting from WritableStream.
    class DuckTypedStream:
        def module_0.write(self, s):
            return s

    assert issubclass(DuckTypedStream, WritableStream)
    assert isinstance(DuckTypedStream(), WritableStream)

# Generated at 2026-10-25 01:59:45.041313
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class ConcreteWritableStream(WritableStream):
        def __init__(self):
            self.written = []

        def module_0.write(self, s):
            self.written.append(s)

    stream = ConcreteWritableStream()
    stream.write("Hello")
    stream.write(" world")

    assert stream.written == ["Hello", " world"]
    assert isinstance(stream, WritableStream)

# Generated at 2026-10-25 01:59:52.304094
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    # WritableStream cannot be instantiated until module_0.write() is implemented.
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError(
            "WritableStream should not be instantiable without module_0.write()"
        )

    class ConcreteWritableStream(WritableStream):
        def __init__(self):
            self.contents = []

        def module_0.write(self, s):
            self.contents.append(s)
            return len(s)

    stream = ConcreteWritableStream()

    assert stream.write("hello") == 5
    assert stream.contents == ["hello"]
    assert isinstance(stream, WritableStream)