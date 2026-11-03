

# Generated at 2026-11-01 23:48:20.708331
# Unit test for function normalize_repr
def test_normalize_repr():
    # A typical default object repr contains a memory address like 'at 0x...'
    class Foo:
        pass

    foo = Foo()
    original_repr = repr(foo)
    assert ' at 0x' in original_repr
    normalized = module_0.normalize_repr(original_repr)
    assert ' at 0x' not in normalized
    assert normalized == '<{}.{} object>'.format(Foo.__module__, Foo.__name__)

    # Explicit examples with different hex address lengths / cases
    assert module_0.normalize_repr('<Foo object at 0x7f8b2c3d4e5f>') == '<Foo object>'
    assert module_0.normalize_repr('<Foo object at 0xABCD>') == '<Foo object>'
    assert module_0.normalize_repr('<Foo object at 0xabcd1234>') == '<Foo object>'

    # Addresses shorter than 4 hex digits are not matched by the pattern
    assert module_0.normalize_repr('<Foo object at 0xabc>') == '<Foo object at 0xabc>'

    # Reprs without an address remain untouched
    plain_repr = '<Foo object>'
    assert module_0.normalize_repr(plain_repr) == plain_repr

    # Multiple occurrences are all removed
    multi = '[<A object at 0x12345678>, <B object at 0x9abcdef0>]'
    assert module_0.normalize_repr(multi) == '[<A object>, <B object>]'

# Generated at 2026-11-01 23:49:20.697820
# Unit test for constructor of class WritableStream
def test_WritableStream():
    # The abstract base class cannot be instantiated directly.
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError("WritableStream should be abstract and "
                             "not instantiable")

    # A proper subclass implementing `write` constructs successfully.
    class MyStream(WritableStream):
        def write(self, s):
            pass

    my_stream = MyStream()
    assert isinstance(my_stream, WritableStream)

    # Any class with a `write` method is registered as a virtual subclass
    # via `__subclasshook__`.
    class DuckTypedStream(object):
        def write(self, s):
            pass

    class NotAStream(object):
        pass

    class HasNoneWrite(object):
        write = None

    assert issubclass(DuckTypedStream, WritableStream)
    assert isinstance(DuckTypedStream(), WritableStream)
    assert not issubclass(NotAStream, WritableStream)
    assert not issubclass(HasNoneWrite, WritableStream)

    # The subclasshook only applies to WritableStream itself.
    class OtherABC(ABC):
        pass

    OtherABC.__subclasshook__ = WritableStream.__subclasshook__.__func__
    assert OtherABC.__subclasshook__(OtherABC, DuckTypedStream) is NotImplemented

# Generated at 2026-11-01 23:50:29.101984
# Unit test for function normalize_repr
def test_normalize_repr():
    # A typical default repr with a memory address should have it removed
    assert module_0.normalize_repr('<foo.Foo object at 0x7f0e8d4b3a90>') == '<foo.Foo object at>'

    # Lowercase hex address
    assert module_0.normalize_repr('<object at 0xabc1234>') == '<object at>'

    # Uppercase hex address is matched too
    assert module_0.normalize_repr('<object at 0xDEADBEEF>') == '<object at>'

    # Short addresses (4 hex digits) are matched
    assert module_0.normalize_repr('<object at 0xabcd>') == '<object at>'

    # Addresses shorter than 4 hex digits are not matched
    assert module_0.normalize_repr('<object at 0xabc>') == '<object at 0xabc>'

    # Strings without a memory address are returned unchanged
    assert module_0.normalize_repr('no address here') == 'no address here'

    # Only the address is removed; surrounding text is preserved
    assert module_0.normalize_repr('start 0x1234 end') == 'start  end'

    # Empty string stays empty
    assert module_0.normalize_repr('') == ''

    # Multiple addresses are all removed
    assert module_0.normalize_repr('0x1111 and 0x2222') == ' and '
# nonce:264a8d59

# Generated at 2026-11-01 23:51:45.433233
# Unit test for function get_repr_function
def test_get_repr_function():

    # Test with a condition specified as a type (isinstance check).
    class Foo(object):
        pass

    foo = Foo()
    custom_repr = ((Foo, lambda x: 'foo repr'),)
    assert module_0.get_repr_function(foo, custom_repr)('anything') == 'foo repr'

    # Item that isn't an instance of the given type should fall back
    # through the loop (and eventually to builtin repr if nothing matches).
    assert module_0.get_repr_function(1, custom_repr) is repr

    # Test with a condition specified as a callable.
    custom_repr = ((lambda x: x > 5, lambda x: 'big number'),)
    assert module_0.get_repr_function(10, custom_repr)(10) == 'big number'
    assert module_0.get_repr_function(3, custom_repr) is repr

    # Test that the first matching condition wins.
    custom_repr = (
        (lambda x: x > 5, lambda x: 'first'),
        (lambda x: x > 1, lambda x: 'second'),
    )
    assert module_0.get_repr_function(10, custom_repr)(10) == 'first'

    # Test that no matching conditions yields builtin repr.
    custom_repr = ((lambda x: False, lambda x: 'never'),)
    assert module_0.get_repr_function('bar', custom_repr) is repr

    # Test with empty custom_repr.
    assert module_0.get_repr_function('bar', ()) is repr

    # Test mixed types/callables in custom_repr.
    custom_repr = (
        (int, lambda x: 'an int'),
        (str, lambda x: 'a str'),
    )
    assert module_0.get_repr_function(7, custom_repr)(7) == 'an int'
    assert module_0.get_repr_function('baz', custom_repr)('baz') == 'a str'
    assert module_0.get_repr_function(1.5, custom_repr) is repr

# Generated at 2026-11-01 23:52:49.699205
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def __init__(self):
            self.written = []

        def module_0.write(self, s):
            self.written.append(s)
            return len(s)

    stream = MyWritableStream()
    result = stream.write('hello world')
    assert result == 11
    assert stream.written == ['hello world']

    # Writing multiple times appends
    stream.write('foo')
    stream.write('bar')
    assert stream.written == ['hello world', 'foo', 'bar']

    # Writing an empty string
    stream.write('')
    assert stream.written[-1] == ''

    # A duck-typed class with a `write` method is a virtual subclass
    class DuckStream:
        def module_0.write(self, s):
            pass

    assert issubclass(DuckStream, WritableStream)
    assert isinstance(DuckStream(), WritableStream)

    # A class without a `write` method is not a virtual subclass
    class NotAStream:
        pass

    assert not issubclass(NotAStream, WritableStream)
    assert not isinstance(NotAStream(), WritableStream)

    # Cannot instantiate the abstract base class directly
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError("WritableStream should be abstract and not instantiable")

# Generated at 2026-11-01 23:54:51.354050
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    from .py3k_repr import get_shortish_repr

    # Basic repr of a string
    assert module_0.get_shortish_repr('foo') == repr('foo')

    # Newlines and carriage returns are removed
    assert module_0.get_shortish_repr('foo\r\nbar\nbaz\r') == "'foobarbaz'"

    # Custom repr function is used when condition matches
    custom_repr = ((lambda x: isinstance(x, str), lambda x: 'CUSTOM'),)
    assert module_0.get_shortish_repr('foo', custom_repr=custom_repr) == 'CUSTOM'

    # Custom repr with a type condition
    custom_repr = ((str, lambda x: 'CUSTOM'),)
    assert module_0.get_shortish_repr('foo', custom_repr=custom_repr) == 'CUSTOM'

    # Custom repr that doesn't match falls back to default repr
    custom_repr = ((int, lambda x: 'CUSTOM'),)
    assert module_0.get_shortish_repr('foo', custom_repr=custom_repr) == repr('foo')

    # max_length truncates the output
    long_string = 'a' * 100
    result = module_0.get_shortish_repr(long_string, max_length=20)
    assert len(result) == 20
    assert '...' in result
    assert result == "''...'"  # left=8, right=9 for repr of 100 a's
    # More precisely: repr is 102 chars, truncate to 20: left=8, right=9
    r = repr(long_string)
    expected = r[:8] + '...' + r[-9:]
    assert result == expected

    # max_length larger than string leaves it unchanged
    assert module_0.get_shortish_repr('foo', max_length=100) == repr('foo')

    # max_length of None leaves it unchanged
    assert module_0.get_shortish_repr('foo', max_length=None) == repr('foo')

    # Repr failure results in 'REPR FAILED'
    class BadRepr:
        def __repr__(self):
            raise Exception('nope')
    assert module_0.get_shortish_repr(BadRepr()) == 'REPR FAILED'

    # Repr failure with max_length still respects max_length
    result = module_0.get_shortish_repr(BadRepr(), max_length=5)
    assert len(result) == 5
    assert result == 'RE...ED'

    # normalize=True removes memory addresses from default reprs
    class ObjectWithAddr:
        pass
    repr_output = repr(ObjectWithAddr())
    if ' at 0x' in repr_output:
        normalized = module_0.get_shortish_repr(ObjectWithAddr(), normalize=True)
        assert '0x' not in normalized or ' at 0x' not in normalized

    # normalize=True with a literal memory address pattern
    custom_repr = ((object, lambda x: 'Foo at 0xdeadbeef1234'),)
    assert module_0.get_shortish_repr(object(), custom_repr=custom_repr,
                             normalize=True) == 'Foo '

    # normalize=False keeps the memory address
    custom_repr = ((object, lambda x: 'Foo at 0xdeadbeef1234'),)
    assert module_0.get_shortish_repr(object(), custom_repr=custom_repr,
                             normalize=False) == 'Foo at 0xdeadbeef1234'

    # Combination: normalize + max_length
    custom_repr = ((object, lambda x: 'A' * 50 + ' at 0xdeadbeef1234'),)
    result = module_0.get_shortish_repr(object(), custom_repr=custom_repr,
                               normalize=True, max_length=20)
    assert len(result) == 20
    assert '0x' not in result

    # Newline removal happens before truncation
    result = module_0.get_shortish_repr('a\nb', max_length=4)
    assert result == "'ab'"

    # max_length=0 is falsy, so no truncation
    assert module_0.get_shortish_repr('foo', max_length=0) == repr('foo')

# Generated at 2026-11-01 23:56:35.495587
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def __init__(self):
            self.output = []

        def module_0.write(self, s):
            self.output.append(s)

    stream = MyWritableStream()
    stream.write('hello')
    stream.write(' world')
    assert stream.output == ['hello', ' world']

    # A class defining a `write` method is recognized as a WritableStream
    # via the duck-typing __subclasshook__.
    class DuckTypedStream(object):
        def module_0.write(self, s):
            pass

    assert issubclass(DuckTypedStream, WritableStream)

    # A class without a `write` method is not a WritableStream.
    class NotAStream(object):
        pass

    assert not issubclass(NotAStream, WritableStream)

    # The abstract base class itself cannot be instantiated.
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError('WritableStream should be abstract')

    # Standard file-like objects qualify as WritableStream as well.
    import io
    string_stream = io.StringIO()
    assert isinstance(string_stream, WritableStream)
    string_stream.write(u'abc')
    assert string_stream.getvalue() == u'abc'