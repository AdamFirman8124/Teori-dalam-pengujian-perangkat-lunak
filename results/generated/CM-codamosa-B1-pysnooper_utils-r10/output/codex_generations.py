

# Generated at 2026-10-25 03:57:26.273595
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

# Generated at 2026-10-25 03:57:27.631936
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

# Generated at 2026-10-25 03:57:29.009843
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

# Generated at 2026-10-25 03:57:30.474143
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

# Generated at 2026-10-25 03:57:38.256563
# Unit test for function get_repr_function
def test_get_repr_function():
    type_action = lambda item: 'type action'
    condition_action = lambda item: 'condition action'
    first_action = lambda item: 'first action'
    second_action = lambda item: 'second action'

    class Parent:
        pass

    class Child(Parent):
        pass

    # Type conditions use isinstance, including subclasses.
    assert module_0.get_repr_function(
        Child(),
        ((Parent, type_action),)
    ) is type_action

    # Callable conditions are supported.
    assert module_0.get_repr_function(
        42,
        ((lambda item: item == 42, condition_action),)
    ) is condition_action

    # The first matching condition wins.
    assert module_0.get_repr_function(
        42,
        (
            (lambda item: True, first_action),
            (int, second_action),
        )
    ) is first_action

    # Fall back to the built-in repr when nothing matches.
    assert module_0.get_repr_function(
        42,
        ((str, type_action),)
    ) is repr

# Generated at 2026-10-25 03:57:46.008152
# Unit test for function get_repr_function

# Generated at 2026-10-25 03:57:48.427135
# Unit test for function get_repr_function

# Generated at 2026-10-25 03:57:49.825809
# Unit test for function get_repr_function
def test_get_repr_function():f = lambda x: 'C'

# Generated at 2026-10-25 03:57:51.265434
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

# Generated at 2026-10-25 03:57:52.694097
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

# Generated at 2026-10-25 03:58:03.240766
# Unit test for function ensure_tuple

# Generated at 2026-10-25 03:58:06.824553
# Unit test for function ensure_tuple
def test_ensure_tuple():
    assert module_0.ensure_tuple((1, 2, 3)) == (1, 2, 3)
    assert module_0.ensure_tuple([1, 2, 3]) == (1, 2, 3)
    assert module_0.ensure_tuple(x for x in range(3)) == (0, 1, 2)
    assert module_0.ensure_tuple('abc') == ('abc',)
    assert module_0.ensure_tuple(5) == (5,)
    assert module_0.ensure_tuple(None) == (None,)

# Generated at 2026-10-25 03:58:17.576676
# Unit test for function ensure_tuple

# Generated at 2026-10-25 03:58:18.909121
# Unit test for function ensure_tuple
def test_ensure_tuple():
    assert module_0.ensure_tuple((1, 2, 3)) == (1, 2, 3)
    assert module_0.ensure_tuple([1, 2, 3]) == (1, 2, 3)
    assert module_0.ensure_tuple(x for x in range(3)) == (0, 1, 2)
    assert module_0.ensure_tuple('abc') == ('abc',)
    assert module_0.ensure_tuple(5) == (5,)
    assert module_0.ensure_tuple(None) == (None,)

# Generated at 2026-10-25 03:58:20.342323
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

# Generated at 2026-10-25 03:58:29.764424
# Unit test for function get_repr_function
def test_get_repr_function():
    class Parent:
        pass

    class Child(Parent):
        pass

    def special_repr(item):
        return 'special'

    def parent_repr(item):
        return 'parent'

    custom_repr = (
        (lambda item: item == 'special', special_repr),
        (Parent, parent_repr),
    )

    # Callable conditions are supported.
    assert module_0.get_repr_function('special', custom_repr) is special_repr

    # Type conditions use isinstance(), including subclasses.
    assert module_0.get_repr_function(Parent(), custom_repr) is parent_repr
    assert module_0.get_repr_function(Child(), custom_repr) is parent_repr

    # Items that match no condition fall back to repr().
    assert module_0.get_repr_function(42, custom_repr) is repr

    # The first matching rule takes precedence.
    assert module_0.get_repr_function(
        'special',
        ((str, parent_repr), (lambda item: item == 'special', special_repr)),
    ) is parent_repr

# Generated at 2026-10-25 03:58:31.199499
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

# Generated at 2026-10-25 03:58:32.843716
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

# Generated at 2026-10-25 03:58:41.337013
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    assert getattr(WritableStream.write, '__isabstractmethod__', False)

    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError("WritableStream must not be directly instantiable")

    class ConcreteWritableStream(WritableStream):
        def __init__(self):
            self.contents = []

        def module_0.write(self, s):
            self.contents.append(s)
            return len(s)

    stream = ConcreteWritableStream()

    assert stream.write("hello") == 5
    assert stream.write(" world") == 6
    assert stream.contents == ["hello", " world"]
    assert isinstance(stream, WritableStream)

# Generated at 2026-10-25 03:58:49.240329
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    with pytest.raises(TypeError):
        WritableStream()

    class ConcreteWritableStream(WritableStream):
        def __init__(self):
            self.data = []

        def module_0.write(self, s):
            self.data.append(s)

    stream = ConcreteWritableStream()
    result = stream.write("hello")

    assert stream.data == ["hello"]
    assert result is None

# Generated at 2026-10-25 03:58:58.300309
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class TestStream(WritableStream):
        def __init__(self):
            self.written = []

        def module_0.write(self, s):
            self.written.append(s)
            return len(s)

    stream = TestStream()

    assert stream.write('hello') == 5
    assert stream.write(' world') == 6
    assert stream.written == ['hello', ' world']

# Generated at 2026-10-25 03:59:05.401650
# Unit test for function get_repr_function
def test_get_repr_function():
    def int_repr(item):
        return 'integer: {}'.format(item)

    def special_repr(item):
        return 'special: {}'.format(item)

    def fallback_repr(item):
        return 'fallback: {}'.format(item)

    custom_repr = (
        (int, int_repr),
        (lambda item: item == 'special', special_repr),
        (lambda item: True, fallback_repr),
    )

    assert module_0.get_repr_function(42, custom_repr) is int_repr
    assert module_0.get_repr_function('special', custom_repr) is special_repr
    assert module_0.get_repr_function('ordinary', custom_repr) is fallback_repr

    # With no matching condition, the built-in repr is returned.
    assert module_0.get_repr_function(object(), ()) is repr

    # The first matching condition takes precedence.
    assert module_0.get_repr_function(
        42,
        ((int, int_repr), (lambda item: True, fallback_repr)),
    ) is int_repr

# Generated at 2026-10-25 03:59:06.832558
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

# Generated at 2026-10-25 03:59:08.172163
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

# Generated at 2026-10-25 03:59:17.584888
# Unit test for function truncate
def test_truncate():
    assert module_0.truncate('abcdefghij', None) == 'abcdefghij'
    assert module_0.truncate('abcdefghij', 10) == 'abcdefghij'
    assert module_0.truncate('abcdefghij', 20) == 'abcdefghij'

    assert module_0.truncate('abcdefghij', 9) == 'abc...hij'
    assert module_0.truncate('abcdefghij', 8) == 'ab...hij'
    assert module_0.truncate('abcdefghij', 7) == 'ab...ij'

    result = module_0.truncate('abcdefghij', 6)
    assert result == 'a...ij'
    assert len(result) == 6

# Generated at 2026-10-25 03:59:26.902815
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    # WritableStream cannot be instantiated without implementing module_0.write().
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

# Generated at 2026-10-25 03:59:33.866805
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class TestWritableStream(WritableStream):
        def __init__(self):
            self.contents = []

        def module_0.write(self, s):
            self.contents.append(s)
            return len(s)

    stream = TestWritableStream()

    assert stream.write('hello') == 5
    assert stream.write(' world') == 6
    assert stream.contents == ['hello', ' world']
    assert isinstance(stream, WritableStream)

# Generated at 2026-10-25 03:59:40.508150
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class TestWritableStream(WritableStream):
        def __init__(self):
            self.written = []

        def module_0.write(self, s):
            self.written.append(s)
            return len(s)

    stream = TestWritableStream()

    result = stream.write('hello')

    assert result == 5
    assert stream.written == ['hello']
    assert isinstance(stream, WritableStream)

# Generated at 2026-10-25 03:59:50.083226
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class ConcreteWritableStream(WritableStream):
        def __init__(self):
            self.received = []

        def module_0.write(self, s):
            self.received.append(s)
            return len(s)

    stream = ConcreteWritableStream()

    assert stream.write("hello") == 5
    assert stream.received == ["hello"]

    # Classes that do not implement write remain abstract.
    class IncompleteWritableStream(WritableStream):
        pass

    try:
        IncompleteWritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError(
            "WritableStream subclasses without module_0.write() must not be instantiable"
        )

# Generated at 2026-10-25 04:00:00.144881
# Unit test for function get_repr_function
def test_get_repr_function():
    class Foo:
        pass

    def foo_repr(item):
        return 'foo'

    def special_repr(item):
        return 'special'

    custom_repr = (
        (Foo, foo_repr),
        (lambda item: item == 'special', special_repr),
    )

    assert module_0.get_repr_function(Foo(), custom_repr) is foo_repr
    assert module_0.get_repr_function('special', custom_repr) is special_repr
    assert module_0.get_repr_function('other', custom_repr) is repr

# Generated at 2026-10-25 04:00:07.249568
# Unit test for function get_repr_function
def test_get_repr_function():
    int_repr = lambda item: 'integer'
    positive_repr = lambda item: 'positive'
    str_repr = lambda item: 'string'

    custom_repr = (
        (str, str_repr),
        (lambda item: isinstance(item, int) and item > 0, positive_repr),
        (int, int_repr),
    )

    assert module_0.get_repr_function('hello', custom_repr) is str_repr
    assert module_0.get_repr_function(42, custom_repr) is positive_repr
    assert module_0.get_repr_function(-1, custom_repr) is int_repr
    assert module_0.get_repr_function(3.14, custom_repr) is repr

# Generated at 2026-10-25 04:00:16.499764
# Unit test for function get_repr_function
def test_get_repr_function():
    class Parent:
        pass

    class Child(Parent):
        pass

    parent_repr = lambda item: 'parent'
    special_repr = lambda item: 'special'
    fallback_repr = lambda item: 'fallback'

    special_item = object()

    custom_repr = (
        (Parent, parent_repr),
        (lambda item: item is special_item, special_repr),
        (lambda item: True, fallback_repr),
    )

    # Type conditions also match subclasses.
    assert module_0.get_repr_function(Parent(), custom_repr) is parent_repr
    assert module_0.get_repr_function(Child(), custom_repr) is parent_repr

    # Callable conditions are supported.
    assert module_0.get_repr_function(special_item, custom_repr) is special_repr

    # The first matching condition wins.
    assert module_0.get_repr_function(Parent(), (
        (Parent, parent_repr),
        (lambda item: True, fallback_repr),
    )) is parent_repr

    # A catch-all condition can provide a custom fallback.
    assert module_0.get_repr_function(42, custom_repr) is fallback_repr

    # Without a match, the built-in repr function is returned.
    assert module_0.get_repr_function(42, ()) is repr

# Generated at 2026-10-25 04:00:26.061585
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class ConcreteWritableStream(WritableStream):
        def __init__(self):
            self.contents = []

        def module_0.write(self, s):
            self.contents.append(s)

    stream = ConcreteWritableStream()

    result = stream.write('hello')

    assert result is None
    assert stream.contents == ['hello']
    assert isinstance(stream, WritableStream)

    # WritableStream itself must remain abstract.
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError('WritableStream should not be instantiable')

# Generated at 2026-10-25 04:00:28.604167
# Unit test for function get_repr_function

# Generated at 2026-10-25 04:00:31.022547
# Unit test for function get_repr_function

# Generated at 2026-10-25 04:00:33.439288
# Unit test for function get_repr_function

# Generated at 2026-10-25 04:00:35.854092
# Unit test for function shitcode

# Generated at 2026-10-25 04:00:38.271126
# Unit test for function shitcode

# Generated at 2026-10-25 04:00:40.930740
# Unit test for function shitcode

# Generated at 2026-10-25 04:00:43.459084
# Unit test for function get_repr_function

# Generated at 2026-10-25 04:00:45.873738
# Unit test for function get_repr_function

# Generated at 2026-10-25 04:00:48.288846
# Unit test for function get_repr_function

# Generated at 2026-10-25 04:00:56.092596
# Unit test for function get_repr_function
def test_get_repr_function():int_repr = lambda item: f'int:{item}'

# Generated at 2026-10-25 04:00:57.531354
# Unit test for function get_repr_function
def test_get_repr_function():f = lambda x: 'C'

# Generated at 2026-10-25 04:01:04.286786
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

    # WritableStream itself cannot be instantiated because write is abstract.
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError('WritableStream should not be directly instantiable')

# Generated at 2026-10-25 04:01:11.864016
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    assert getattr(WritableStream.write, '__isabstractmethod__', False)

    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError(
            'WritableStream should not be instantiable without module_0.write()'
        )

    class BufferStream(WritableStream):
        def __init__(self):
            self.contents = ''

        def module_0.write(self, s):
            self.contents += s
            return len(s)

    stream = BufferStream()

    assert stream.write('hello') == 5
    assert stream.write(' world') == 6
    assert stream.contents == 'hello world'

# Generated at 2026-10-25 04:01:13.492902
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

# Generated at 2026-10-25 04:01:14.936271
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

# Generated at 2026-10-25 04:01:22.206727
# Unit test for function get_repr_function
def test_get_repr_function():
    class Example:
        pass

    class ExampleSubclass(Example):
        pass

    example_repr = lambda item: 'example'
    special_int_repr = lambda item: 'special integer'

    custom_repr = (
        (Example, example_repr),
        (lambda item: item == 42, special_int_repr),
    )

    # Type conditions use isinstance, including subclasses.
    assert module_0.get_repr_function(Example(), custom_repr) is example_repr
    assert module_0.get_repr_function(ExampleSubclass(), custom_repr) is example_repr

    # Callable conditions are evaluated directly.
    assert module_0.get_repr_function(42, custom_repr) is special_int_repr

    # If no condition matches, the built-in repr is returned.
    assert module_0.get_repr_function('unmatched', custom_repr) is repr

# Generated at 2026-10-25 04:01:23.639385
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

# Generated at 2026-10-25 04:01:35.007173
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    # The abstract base class cannot be instantiated directly.
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError("WritableStream should be abstract")

    class MemoryStream(WritableStream):
        def __init__(self):
            self.data = []

        def module_0.write(self, s):
            self.data.append(s)
            return len(s)

    stream = MemoryStream()
    assert stream.write("hello") == 5
    assert stream.data == ["hello"]

    # WritableStream also supports structural subclass detection.
    class DuckTypedStream:
        def module_0.write(self, s):
            return len(s)

    class NonWritable:
        pass

    assert issubclass(DuckTypedStream, WritableStream)
    assert isinstance(DuckTypedStream(), WritableStream)
    assert not issubclass(NonWritable, WritableStream)

# Generated at 2026-10-25 04:01:37.425560
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 04:01:40.018342
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 04:01:42.434943
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 04:01:44.848663
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 04:01:47.266117
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 04:01:49.681410
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 04:01:52.097897
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 04:01:54.514230
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 04:02:02.862505
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 04:02:12.154785
# Unit test for function get_repr_function
def test_get_repr_function():
    int_repr = lambda item: 'integer: {}'.format(item)
    positive_repr = lambda item: 'positive: {}'.format(item)
    first_repr = lambda item: 'first'
    second_repr = lambda item: 'second'

    # Type conditions use isinstance().
    assert module_0.get_repr_function(42, [(int, int_repr)]) is int_repr
    assert module_0.get_repr_function(True, [(int, int_repr)]) is int_repr

    # Callable conditions are supported.
    assert module_0.get_repr_function(
        5,
        [(lambda item: item > 0, positive_repr)]
    ) is positive_repr

    # The first matching rule wins.
    assert module_0.get_repr_function(
        5,
        [
            (lambda item: item > 0, first_repr),
            (int, second_repr),
        ]
    ) is first_repr

    # Fall back to the built-in repr when nothing matches.
    assert module_0.get_repr_function('text', [(int, int_repr)]) is repr
    assert module_0.get_repr_function('text', ()) is repr

# Generated at 2026-10-25 04:02:20.727188
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import pytest

    # WritableStream cannot be instantiated without implementing module_0.write().
    with pytest.raises(TypeError):
        WritableStream()

    class TestStream(WritableStream):
        def __init__(self):
            self.contents = []

        def module_0.write(self, s):
            self.contents.append(s)
            return len(s)

    stream = TestStream()

    assert stream.write('hello') == 5
    assert stream.contents == ['hello']
    assert isinstance(stream, WritableStream)

# Generated at 2026-10-25 04:02:31.730272
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    # The abstract base class cannot be instantiated directly.
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError("WritableStream should not be directly instantiable")

    class ConcreteWritableStream(WritableStream):
        def __init__(self):
            self.contents = []

        def module_0.write(self, s):
            self.contents.append(s)
            return len(s)

    stream = ConcreteWritableStream()

    assert isinstance(stream, WritableStream)
    assert stream.write("hello") == 5
    assert stream.contents == ["hello"]

    # A duck-typed class with module_0.write() is recognized by __subclasshook__.
    class DuckTypedStream:
        def module_0.write(self, s):
            return s

    assert issubclass(DuckTypedStream, WritableStream)
    assert isinstance(DuckTypedStream(), WritableStream)

# Generated at 2026-10-25 04:02:40.071423
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class ConcreteWritableStream(WritableStream):
        def __init__(self):
            self.contents = []

        def module_0.write(self, s):
            self.contents.append(s)
            return len(s)

    stream = ConcreteWritableStream()

    assert isinstance(stream, WritableStream)
    assert stream.write('hello') == 5
    assert stream.contents == ['hello']

    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError(
            'WritableStream should not be instantiable without implementing write'
        )

# Generated at 2026-10-25 04:02:49.554742
# Unit test for function get_repr_function
def test_get_repr_function():
    class Parent:
        pass

    class Child(Parent):
        pass

    def parent_repr(item):
        return 'parent'

    def child_repr(item):
        return 'child'

    def special_repr(item):
        return 'special'

    custom_repr = (
        (lambda item: item == 'special', special_repr),
        (Child, child_repr),
        (Parent, parent_repr),
    )

    assert module_0.get_repr_function('special', custom_repr) is special_repr
    assert module_0.get_repr_function(Child(), custom_repr) is child_repr
    assert module_0.get_repr_function(Parent(), custom_repr) is parent_repr
    assert module_0.get_repr_function(42, custom_repr) is repr

    # The first matching rule should take precedence.
    reversed_types = (
        (Parent, parent_repr),
        (Child, child_repr),
    )
    assert module_0.get_repr_function(Child(), reversed_types) is parent_repr

# Generated at 2026-10-25 04:02:57.950629
# Unit test for method write of class WritableStream
def test_WritableStream_write():
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

# Generated at 2026-10-25 04:02:59.334133
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

# Generated at 2026-10-25 04:03:06.653970
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class ConcreteWritableStream(WritableStream):
        def __init__(self):
            self.written = []

        def module_0.write(self, s):
            self.written.append(s)
            return len(s)

    stream = ConcreteWritableStream()

    assert stream.write('hello') == 5
    assert stream.written == ['hello']
    assert isinstance(stream, WritableStream)

    # WritableStream also accepts structural subclasses that define module_0.write().
    class DuckTypedStream:
        def module_0.write(self, s):
            return s

    assert issubclass(DuckTypedStream, WritableStream)
    assert isinstance(DuckTypedStream(), WritableStream)

# Generated at 2026-10-25 04:03:16.485014
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    # WritableStream cannot be instantiated without implementing module_0.write().
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError(
            "WritableStream should require an implementation of module_0.write()"
        )

    class ConcreteWritableStream(WritableStream):
        def __init__(self):
            self.contents = []

        def module_0.write(self, s):
            self.contents.append(s)
            return len(s)

    stream = ConcreteWritableStream()

    assert stream.write('hello') == 5
    assert stream.contents == ['hello']

    # The subclass hook should also recognize compatible duck-typed classes.
    class DuckTypedStream:
        def module_0.write(self, s):
            return s

    assert issubclass(DuckTypedStream, WritableStream)
    assert isinstance(DuckTypedStream(), WritableStream)

# Generated at 2026-10-25 04:03:17.918026
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

# Generated at 2026-10-25 04:03:26.929704
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    assert getattr(WritableStream.write, '__isabstractmethod__', False)

    class TestStream(WritableStream):
        def __init__(self):
            self.contents = ''

        def module_0.write(self, s):
            self.contents += s
            return len(s)

    stream = TestStream()

    assert stream.write('hello') == 5
    assert stream.write(' world') == 6
    assert stream.contents == 'hello world'

    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError('WritableStream should not be directly instantiable')

# Generated at 2026-10-25 04:03:28.258576
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

# Generated at 2026-10-25 04:03:36.145413
# Unit test for function get_repr_function
def test_get_repr_function():
    def int_repr(item):
        return 'integer: {}'.format(item)

    def negative_repr(item):
        return 'negative: {}'.format(item)

    custom_repr = (
        (int, int_repr),
        (lambda item: isinstance(item, float) and item < 0, negative_repr),
    )

    # Type conditions use isinstance.
    assert module_0.get_repr_function(42, custom_repr) is int_repr
    assert module_0.get_repr_function(True, custom_repr) is int_repr

    # Callable conditions are evaluated directly.
    assert module_0.get_repr_function(-1.5, custom_repr) is negative_repr

    # Unmatched items fall back to the built-in repr.
    assert module_0.get_repr_function('hello', custom_repr) is repr

    # The first matching rule wins.
    first = lambda item: 'first'
    second = lambda item: 'second'
    assert module_0.get_repr_function(
        10,
        ((int, first), (lambda item: True, second)),
    ) is first

# Generated at 2026-10-25 04:03:48.231949
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    # The abstract base class cannot be instantiated directly.
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
            return len(s)

    stream = MemoryStream()

    assert stream.write("hello") == 5
    assert stream.write(" world") == 6
    assert stream.contents == ["hello", " world"]

# Generated at 2026-10-25 04:03:50.808319
# Unit test for function get_repr_function

# Generated at 2026-10-25 04:03:53.222561
# Unit test for function get_repr_function

# Generated at 2026-10-25 04:03:55.759048
# Unit test for function get_repr_function

# Generated at 2026-10-25 04:03:58.174402
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 04:04:00.750013
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 04:04:23.105337
# Unit test for function get_shortish_repr
def test_get_shortish_repr():assert module_0.get_shortish_repr("hello") == "'hello'"

# Generated at 2026-10-25 04:04:33.183842
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    # The abstract base class cannot be instantiated directly.
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError(
            "WritableStream should require a concrete module_0.write() implementation"
        )

    class BufferStream(WritableStream):
        def __init__(self):
            self.contents = []

        def module_0.write(self, s):
            self.contents.append(s)
            return len(s)

    stream = BufferStream()

    assert stream.write("hello") == 5
    assert stream.write(" world") == 6
    assert stream.contents == ["hello", " world"]

# Generated at 2026-10-25 04:04:34.540788
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

# Generated at 2026-10-25 04:04:42.977870
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class TestStream(WritableStream):
        def __init__(self):
            self.data = []

        def module_0.write(self, s):
            self.data.append(s)
            return len(s)

    stream = TestStream()

    assert isinstance(stream, WritableStream)
    assert stream.write("hello") == 5
    assert stream.data == ["hello"]

    # The abstract base class cannot be instantiated directly.
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError("WritableStream should not be directly instantiable")

    # Structural subclassing recognizes any class with a write method.
    class DuckTypedStream:
        def module_0.write(self, s):
            return s

    assert issubclass(DuckTypedStream, WritableStream)
    assert isinstance(DuckTypedStream(), WritableStream)

# Generated at 2026-10-25 04:04:45.395715
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 04:04:47.811137
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 04:04:50.224374
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 04:04:52.638916
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 04:04:55.054378
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 04:04:57.642786
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 04:05:00.058427
# Unit test for function get_repr_function

# Generated at 2026-10-25 04:05:02.480389
# Unit test for function get_repr_function

# Generated at 2026-10-25 04:05:04.899195
# Unit test for function get_repr_function

# Generated at 2026-10-25 04:05:07.317609
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 04:05:09.729695
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 04:05:12.146208
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 04:05:23.157036
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 04:05:31.037930
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 04:05:32.472029
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 04:05:33.803956
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

# Generated at 2026-10-25 04:05:40.459662
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

    # No matching condition falls back to the built-in repr.
    assert module_0.get_repr_function('hello', custom_repr) is repr

    # The first matching condition takes precedence.
    first = lambda item: 'first'
    second = lambda item: 'second'
    assert module_0.get_repr_function(
        1,
        ((lambda item: True, first), (int, second)),
    ) is first

# Generated at 2026-10-25 04:05:46.705665
# Unit test for function get_repr_function
def test_get_repr_function():
    int_repr = lambda item: '<integer>'
    positive_repr = lambda item: '<positive>'
    fallback_repr = lambda item: '<fallback>'

    custom_repr = (
        (lambda item: item == 'special', fallback_repr),
        (int, int_repr),
        (lambda item: isinstance(item, (int, float)) and item > 0,
         positive_repr),
    )

    # Callable conditions are supported.
    assert module_0.get_repr_function('special', custom_repr) is fallback_repr

    # Types are treated as isinstance conditions.
    assert module_0.get_repr_function(42, custom_repr) is int_repr

    # The first matching condition wins.
    assert module_0.get_repr_function(3, custom_repr) is int_repr

    # Non-type callable conditions are evaluated.
    assert module_0.get_repr_function(2.5, custom_repr) is positive_repr

    # Built-in repr is returned when no condition matches.
    assert module_0.get_repr_function('ordinary', custom_repr) is repr

# Generated at 2026-10-25 04:05:49.241779
# Unit test for function get_repr_function

# Generated at 2026-10-25 04:05:51.663447
# Unit test for function get_repr_function

# Generated at 2026-10-25 04:05:54.192665
# Unit test for function get_repr_function

# Generated at 2026-10-25 04:05:56.720819
# Unit test for function get_repr_function

# Generated at 2026-10-25 04:05:59.137752
# Unit test for function get_repr_function

# Generated at 2026-10-25 04:06:01.552149
# Unit test for function get_repr_function

# Generated at 2026-10-25 04:06:03.967194
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 04:06:06.393696
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 04:06:08.808630
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 04:06:11.224081
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 04:06:13.653134
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 04:06:16.067738
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 04:06:18.482424
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 04:06:20.897397
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 04:06:23.317633
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 04:06:25.732852
# Unit test for function get_repr_function

# Generated at 2026-10-25 04:06:28.151414
# Unit test for function get_repr_function

# Generated at 2026-10-25 04:06:30.567251
# Unit test for function get_repr_function

# Generated at 2026-10-25 04:06:32.991827
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 04:06:35.405712
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 04:06:37.821016
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 04:06:40.263552
# Unit test for function shitcode

# Generated at 2026-10-25 04:06:42.681054
# Unit test for function shitcode

# Generated at 2026-10-25 04:06:45.097228
# Unit test for function shitcode

# Generated at 2026-10-25 04:06:47.510945
# Unit test for function get_repr_function

# Generated at 2026-10-25 04:06:49.925013
# Unit test for function get_repr_function

# Generated at 2026-10-25 04:06:52.339956
# Unit test for function get_repr_function

# Generated at 2026-10-25 04:06:54.754249
# Unit test for function get_repr_function

# Generated at 2026-10-25 04:06:57.168452
# Unit test for function get_repr_function

# Generated at 2026-10-25 04:06:59.584915
# Unit test for function get_repr_function

# Generated at 2026-10-25 04:07:01.999299
# Unit test for function get_repr_function

# Generated at 2026-10-25 04:07:04.414443
# Unit test for function get_repr_function

# Generated at 2026-10-25 04:07:06.829090
# Unit test for function get_repr_function

# Generated at 2026-10-25 04:07:09.253754
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 04:07:11.668489
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 04:07:14.083466
# Unit test for method write of class WritableStream

# Generated at 2026-10-25 04:07:16.505629
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 04:07:18.918597
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 04:07:21.333202
# Unit test for function get_shortish_repr

# Generated at 2026-10-25 04:07:23.748862
# Unit test for function shitcode

# Generated at 2026-10-25 04:07:26.164369
# Unit test for function shitcode

# Generated at 2026-10-25 04:07:28.585838
# Unit test for function shitcode