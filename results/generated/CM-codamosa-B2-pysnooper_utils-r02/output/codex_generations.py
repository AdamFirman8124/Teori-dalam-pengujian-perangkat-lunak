

# Generated at 2026-11-02 20:53:19.929916
# Unit test for function ensure_tuple
def test_ensure_tuple():
# nonce:6b120b5f
    # Non-iterable values get wrapped in a single-element tuple
    assert module_0.ensure_tuple(1) == (1,)
    assert module_0.ensure_tuple(3.14) == (3.14,)
    assert module_0.ensure_tuple(None) == (None,)

    class Foo(object):
        pass
    foo = Foo()
    result = module_0.ensure_tuple(foo)
    assert isinstance(result, tuple)
    assert result == (foo,)

    # Strings are iterable, but should be wrapped, not unpacked
    assert module_0.ensure_tuple('abc') == ('abc',)
    assert module_0.ensure_tuple(u'abc') == (u'abc',)
    assert module_0.ensure_tuple('') == ('',)

    # Iterables get converted to tuples
    assert module_0.ensure_tuple([1, 2, 3]) == (1, 2, 3)
    assert module_0.ensure_tuple((1, 2, 3)) == (1, 2, 3)
    assert module_0.ensure_tuple(()) == ()
    assert module_0.ensure_tuple([]) == ()
    assert module_0.ensure_tuple(range(3)) == (0, 1, 2)
    assert module_0.ensure_tuple(i for i in range(3)) == (0, 1, 2)
    assert module_0.ensure_tuple({1: 'a', 2: 'b'}) == (1, 2)
    assert module_0.ensure_tuple({'a', 'b'}) in (('a', 'b'), ('b', 'a'))

    # Result is always a tuple
    assert isinstance(module_0.ensure_tuple(1), tuple)
    assert isinstance(module_0.ensure_tuple([1, 2]), tuple)
    assert isinstance(module_0.ensure_tuple('abc'), tuple)

# Generated at 2026-11-02 20:54:32.430810
# Unit test for function ensure_tuple
def test_ensure_tuple():
    # Non-iterable objects get wrapped in a single-element tuple.
    assert module_0.ensure_tuple(1) == (1,)
    assert module_0.ensure_tuple(3.5) == (3.5,)
    assert module_0.ensure_tuple(None) == (None,)
    assert module_0.ensure_tuple(True) == (True,)
    assert module_0.ensure_tuple(object) == (object,)

    class Foo(object):
        pass
    foo = Foo()
    assert module_0.ensure_tuple(foo) == (foo,)

    # Strings (and other string types) are treated as single items,
    # not as iterables of characters.
    assert module_0.ensure_tuple('abc') == ('abc',)
    assert module_0.ensure_tuple(u'abc') == (u'abc',)
    assert module_0.ensure_tuple('') == ('',)

    # Iterables are converted to tuples.
    assert module_0.ensure_tuple(()) == ()
    assert module_0.ensure_tuple([]) == ()
    assert module_0.ensure_tuple((1, 2, 3)) == (1, 2, 3)
    assert module_0.ensure_tuple([1, 2, 3]) == (1, 2, 3)
    assert module_0.ensure_tuple(range(3)) == (0, 1, 2)
    assert module_0.ensure_tuple(x * 2 for x in range(3)) == (0, 2, 4)
    assert tuple(sorted(module_0.ensure_tuple({'a': 1, 'b': 2}))) == ('a', 'b')

    # Sets are converted, though iteration order isn't guaranteed.
    result = module_0.ensure_tuple({1, 2, 3})
    assert isinstance(result, tuple)
    assert set(result) == {1, 2, 3}

    # Custom iterable classes are converted too.
    class MyIterable(object):
        def __iter__(self):
            return iter((7, 8))
    assert module_0.ensure_tuple(MyIterable()) == (7, 8)

    if sys.version_info[0] >= 3:
        # In Python 3, bytes is an iterable distinct from str.
        assert module_0.ensure_tuple(b'ab') == (97, 98)

    # The result is always a tuple.
    for x in (1, 'a', [1, 2], (1, 2), None, {1: 2}):
        assert isinstance(module_0.ensure_tuple(x), tuple)
# nonce:1e895807

# Generated at 2026-11-02 20:55:23.507714
# Unit test for function truncate
def test_truncate():
    # max_length is None: string returned unchanged
    assert module_0.truncate('0123456789', None) == '0123456789'

    # string length <= max_length: string returned unchanged
    assert module_0.truncate('', 10) == ''
    assert module_0.truncate('0123456789', 10) == '0123456789'
    assert module_0.truncate('0123456789', 11) == '0123456789'

    # string length > max_length: truncated with '...' in the middle
    assert module_0.truncate('0123456789', 7) == '01...89'
    assert module_0.truncate('0123456789', 8) == '012...89'
    assert module_0.truncate('0123456789', 9) == '0123...89'
    assert module_0.truncate('0123456789', 4) == '0...9'
    assert module_0.truncate('0123456789', 3) == '...'

    # result length never exceeds max_length
    for max_length in range(3, 12):
        result = module_0.truncate('0123456789', max_length)
        assert len(result) == max_length

# Generated at 2026-11-02 20:56:00.864909
# Unit test for function truncate
def test_truncate():
    # nonce:042cd863
    # max_length is None -> string returned unchanged
    assert module_0.truncate('hello world', None) == 'hello world'

    # len(string) <= max_length -> string returned unchanged
    assert module_0.truncate('hello', 10) == 'hello'
    assert module_0.truncate('hello', 5) == 'hello'
    assert module_0.truncate('', 5) == ''

    # len(string) > max_length -> truncated with '...' in the middle
    assert module_0.truncate('abcdefghijkl', 10) == 'abc...ijkl'
    assert module_0.truncate('abcdefghijk', 10) == 'abc...hijk'

    # Odd max_length: right side gets the extra character
    assert module_0.truncate('0123456789', 8) == '01...789'

    # Even max_length: left and right sides are equal
    assert module_0.truncate('0123456789', 7) == '01...89'

    # Truncated output always has exactly max_length characters,
    # preserving the first `left` and last `right` characters.
    for max_length in range(4, 20):
        for length in range(max_length + 1, max_length + 30):
            string = 'x' * length
            result = module_0.truncate(string, max_length)
            assert len(result) == max_length
            left = (max_length - 3) // 2
            right = max_length - 3 - left
            assert result == 'x' * left + '...' + 'x' * right

# Generated at 2026-11-02 20:56:46.130398
# Unit test for constructor of class WritableStream
def test_WritableStream():
    # WritableStream is abstract, so it cannot be instantiated directly
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise Exception("WritableStream should be abstract and not instantiable")

    # A subclass implementing write() can be instantiated
    class MyWritableStream(WritableStream):
        def write(self, s):
            pass

    my_stream = MyWritableStream()
    assert isinstance(my_stream, WritableStream)

    # A class with a `write` method is registered as a subclass via
    # __subclasshook__, even without inheriting from WritableStream
    class DuckStream:
        def write(self, s):
            pass

    assert issubclass(DuckStream, WritableStream)
    assert isinstance(DuckStream(), WritableStream)

    # A class without a `write` method is not a subclass
    class NonWriter:
        pass

    assert not issubclass(NonWriter, WritableStream)
    assert not isinstance(NonWriter(), WritableStream)

    # A class with a None `write` attribute is not a subclass
    class NoneWriter:
        write = None

    assert not issubclass(NoneWriter, WritableStream)

    # Subclasshook only applies to WritableStream itself
    class OtherABC(ABC):
        pass

    assert OtherABC.__subclasshook__(OtherABC) is NotImplemented \
        if hasattr(OtherABC, '__subclasshook__') else True

# Generated at 2026-11-02 20:57:47.878961
# Unit test for function shitcode
def test_shitcode():
    assert module_0.shitcode('foo') == 'foo'
    assert module_0.shitcode(u'foo') == 'foo'
    assert module_0.shitcode(u'foo\u05f0') == 'foo?'
    assert module_0.shitcode(u'\u05f0foo') == '?foo'
    assert module_0.shitcode(u'\u05f0') == '?'
    assert module_0.shitcode(u'\u05f0\u05f0') == '??'
    assert module_0.shitcode(chr(1)) == chr(1)
    assert module_0.shitcode(chr(255)) == chr(255)
    assert module_0.shitcode(chr(256)) == '?'
    assert module_0.shitcode(chr(0)) == '?'
    assert module_0.shitcode('') == ''

# Generated at 2026-11-02 20:59:34.942980
# Unit test for method write of class WritableStream
def test_WritableStream_write():
# nonce:7f1afb86
    class MyStream(WritableStream):
        def __init__(self):
            self.written = []

        def module_0.write(self, s):
            self.written.append(s)

    stream = MyStream()
    stream.write('hello')
    stream.write('world')
    assert stream.written == ['hello', 'world']

    # WritableStream itself is abstract and must not be instantiable
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError('WritableStream should not be instantiable')

    # Any class with a `write` method is recognized as a virtual subclass
    class DuckStream(object):
        def module_0.write(self, s):
            pass

    assert issubclass(DuckStream, WritableStream)
    assert isinstance(DuckStream(), WritableStream)

    # Classes without a `write` method are not subclasses
    class NoWrite(object):
        pass

    assert not issubclass(NoWrite, WritableStream)
    assert not isinstance(NoWrite(), WritableStream)

# Generated at 2026-11-02 20:59:57.937189
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def __init__(self):
            self.output = []

        def module_0.write(self, s):
            self.output.append(s)

    stream = MyWritableStream()
    stream.write('hello')
    stream.write('world')
    assert stream.output == ['hello', 'world']

    # A class with a 'write' method is recognized as a subclass
    # via __subclasshook__ (structural typing / duck typing)
    class DuckTypedStream(object):
        def module_0.write(self, s):
            self.last = s

    assert issubclass(DuckTypedStream, WritableStream)

    duck_stream = DuckTypedStream()
    duck_stream.write('quack')
    assert duck_stream.last == 'quack'

    # A class without a 'write' method is not a subclass
    class NotWritable(object):
        pass

    assert not issubclass(NotWritable, WritableStream)

    # Subclasshook only applies for WritableStream itself
    class OtherABC(WritableStream):
        pass

    class HasWrite(object):
        def module_0.write(self, s):
            pass

    assert OtherABC.__subclasshook__(HasWrite) is NotImplemented

# Generated at 2026-11-02 21:00:23.735798
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    # A concrete subclass implementing write works normally
    class MyWritableStream(WritableStream):
        def __init__(self):
            self.content = ''

        def module_0.write(self, s):
            self.content += s

    stream = MyWritableStream()
    stream.write('hello')
    stream.write(' world')
    assert stream.content == 'hello world'

    # Any class with a `write` method is treated as a subclass (structural typing)
    class DuckStream:
        def module_0.write(self, s):
            self.last = s

    assert issubclass(DuckStream, WritableStream)
    duck = DuckStream()
    duck.write('quack')
    assert duck.last == 'quack'

    # A class without a `write` method is not a subclass
    class NotAStream:
        pass

    assert not issubclass(NotAStream, WritableStream)

    # `write = None` does not count as an implementation
    class NoneStream:
        write = None

    assert not issubclass(NoneStream, WritableStream)

    # The abstract base class itself cannot be instantiated
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError('WritableStream should not be instantiable')

    # A subclass that does not implement write also cannot be instantiated
    class IncompleteStream(WritableStream):
        pass

    try:
        IncompleteStream()
    except TypeError:
        pass
    else:
        raise AssertionError('IncompleteStream should not be instantiable')

# Generated at 2026-11-02 21:00:38.187926
# Unit test for function shitcode
def test_shitcode():
    assert module_0.shitcode('') == ''
    assert module_0.shitcode('abc') == 'abc'
    assert module_0.shitcode('foo bar') == 'foo bar'
    assert module_0.shitcode('foo\nbar') == 'foo\nbar'
    # ASCII characters (ord between 1 and 255) are kept
    assert module_0.shitcode('a\x00b') == 'a?b'
    assert module_0.shitcode('\x01\x02\x03') == '\x01\x02\x03'
    # Non-ASCII characters are replaced with '?'
    assert module_0.shitcode('Rémy') == 'R?my'
    assert module_0.shitcode('שלום') == '????'
    assert module_0.shitcode('你好') == '??'
    assert module_0.shitcode('🦎') == '?'
    # Mixed content
    assert module_0.shitcode('foo\nbar\x00baz\ufeff') == 'foo\nbar?baz?'
    # Every character with ord 1-255 is kept, others replaced
    assert module_0.shitcode(''.join(chr(i) for i in range(1, 256))) == \
           ''.join(chr(i) for i in range(1, 256))
    assert module_0.shitcode(chr(256)) == '?'

# Generated at 2026-11-02 21:01:19.046859
# Unit test for function normalize_repr
def test_normalize_repr():
# nonce:2e9b4a09
    # Typical object repr with a memory address gets it removed
    assert module_0.normalize_repr('<foo.Bar object at 0x7f2a12345678>') == '<foo.Bar object>'

    # Minimum of 4 hex digits is matched
    assert module_0.normalize_repr('<object at 0xabcd>') == '<object>'

    # Uppercase hex digits are matched too
    assert module_0.normalize_repr('<object at 0xDEADBEEF>') == '<object>'

    # Mixed-case hex digits
    assert module_0.normalize_repr('<object at 0xAbCdEf12>') == '<object>'

    # String without a memory address is unchanged
    assert module_0.normalize_repr('no memory address here') == 'no memory address here'

    # Empty string is unchanged
    assert module_0.normalize_repr('') == ''

    # Address must be preceded by a space to be removed
    assert module_0.normalize_repr('at 0x1234 without leading space') == \
           'at 0x1234 without leading space'

    # Multiple addresses are all removed
    assert module_0.normalize_repr('<A at 0x1111> and <B at 0x2222>') == '<A> and <B>'

# Generated at 2026-11-02 21:01:41.279111
# Unit test for function normalize_repr
def test_normalize_repr():
    # Repr with a typical memory address gets it removed
    assert module_0.normalize_repr('<Foo object at 0x7f1b2c3d4e5f>') == '<Foo object>'
    assert module_0.normalize_repr('<Foo object at 0x7f1b2c3d4e5f6a7b>') == '<Foo object>'
    # Uppercase hex digits are matched too
    assert module_0.normalize_repr('<Bar object at 0xABCD>') == '<Bar object>'
    assert module_0.normalize_repr('<Bar object at 0xAbCdEf12>') == '<Bar object>'
    # Minimum length of 4 hex digits is required
    assert module_0.normalize_repr('<Baz at 0x123>') == '<Baz at 0x123>'
    # Repr without a memory address is unchanged
    assert module_0.normalize_repr('just a string') == 'just a string'
    assert module_0.normalize_repr('<Foo object>') == '<Foo object>'
    # Multiple addresses are all removed
    assert module_0.normalize_repr('a at 0x1234 b at 0x5678') == 'a b'
    # Address in the middle of a string is removed, surrounding text kept
    assert module_0.normalize_repr('object at 0xdeadbeef is here') == 'object is here'

# Generated at 2026-11-02 21:02:09.146758
# Unit test for function shitcode
def test_shitcode():
    assert module_0.shitcode('') == ''
    assert module_0.shitcode('abc') == 'abc'
    assert module_0.shitcode('Hello, world!') == 'Hello, world!'
    # Characters with ord in (0, 256) are kept as-is:
    assert module_0.shitcode('héllo') == 'héllo'  # é is 233, kept
    assert module_0.shitcode('\x01\x7f\xff') == '\x01\x7f\xff'
    # Characters with ord == 0 or ord >= 256 are replaced with '?':
    assert module_0.shitcode('\x00') == '?'
    assert module_0.shitcode('א') == '?'
    assert module_0.shitcode('€') == '?'
    assert module_0.shitcode('hello אבג world') == 'hello ??? world'
    assert module_0.shitcode('a\x00b') == 'a?b'
    # Mixed string with newlines and tabs (both < 256, kept):
    assert module_0.shitcode('a\nb\tc') == 'a\nb\tc'