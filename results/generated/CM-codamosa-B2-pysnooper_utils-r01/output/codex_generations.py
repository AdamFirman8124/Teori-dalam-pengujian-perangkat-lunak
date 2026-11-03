

# Generated at 2026-11-02 00:25:10.197868
# Unit test for constructor of class WritableStream
def test_WritableStream():
    # Cannot instantiate the abstract class directly
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError("WritableStream should not be instantiable")

    # A subclass implementing `write` can be instantiated
    class MyWritableStream(WritableStream):
        def write(self, s):
            self.written = s

    stream = MyWritableStream()
    assert isinstance(stream, WritableStream)
    assert issubclass(MyWritableStream, WritableStream)
    stream.write('foo')
    assert stream.written == 'foo'

    # Virtual subclass: any class with a `write` method is recognized
    class DuckStream:
        def write(self, s):
            pass

    assert issubclass(DuckStream, WritableStream)
    assert isinstance(DuckStream(), WritableStream)

    # Class without a `write` method is not a subclass
    class NotWritable:
        pass

    assert not issubclass(NotWritable, WritableStream)

    # Subclasshook only applies to WritableStream itself, not subclasses
    class OtherHook(WritableStream):
        def write(self, s):
            pass

    try:
        issubclass(DuckStream, OtherHook)
    except TypeError:
        pass
    else:
        raise AssertionError("Subclass check against non-ABC should fail")

# Generated at 2026-11-02 00:27:47.778722
# Unit test for constructor of class WritableStream
def test_WritableStream():
    import io
    import pytest

    class MyStream(object):
        def write(self, s):
            pass

    class NotAStream(object):
        pass

    class IncompleteStream(WritableStream):
        pass

    # WritableStream itself counts as a subclass of itself
    assert issubclass(WritableStream, WritableStream)

    # Classes with a `write` method are recognized as subclasses
    # via __subclasshook__, even without inheriting from it
    assert issubclass(MyStream, WritableStream)
    assert issubclass(io.StringIO, WritableStream)

    # Classes without a `write` method are not subclasses
    assert not issubclass(NotAStream, WritableStream)

    # Cannot instantiate the abstract base class directly
    with pytest.raises(TypeError):
        WritableStream()

    # Cannot instantiate a subclass that doesn't implement `write`
    with pytest.raises(TypeError):
        IncompleteStream()

    # A proper subclass implementing `write` can be instantiated
    class GoodStream(WritableStream):
        def write(self, s):
            pass

    GoodStream()

# Generated at 2026-11-02 00:28:49.029657
# Unit test for function get_repr_function
def test_get_repr_function():
    import builtins

    # With no custom repr entries, falls back to builtin repr
    assert module_0.get_repr_function(1, ()) is builtins.repr
    assert module_0.get_repr_function('foo', []) is builtins.repr

    # Condition given as a type that matches the item -> returns its action
    action_int = lambda x: 'INT'
    assert module_0.get_repr_function(5, [(int, action_int)]) is action_int

    # Condition given as a type that does NOT match -> falls through
    assert module_0.get_repr_function('hello', [(int, action_int)]) is builtins.repr

    # Condition given as a callable
    action_odd = lambda x: 'ODD'
    assert module_0.get_repr_function(3, [(lambda x: x % 2 == 1, action_odd)]) is action_odd
    assert module_0.get_repr_function(4, [(lambda x: x % 2 == 1, action_odd)]) is builtins.repr

    # First matching entry wins (order matters)
    action_str = lambda x: 'STR'
    assert module_0.get_repr_function('a', [(str, action_str), (int, action_int)]) is action_str
    assert module_0.get_repr_function(1, [(str, action_str), (int, action_int)]) is action_int

    # Non-matching earlier entries don't shadow later matching ones
    assert module_0.get_repr_function('a', [(int, action_int), (str, action_str)]) is action_str

    # Type conditions are bound correctly per-entry (late-binding bug avoided)
    class Foo(object):
        pass

    class Bar(object):
        pass

    foo = Foo()
    assert module_0.get_repr_function(foo, [(Foo, lambda x: 'FOO'), (Bar, lambda x: 'BAR')])() == 'FOO'
    assert module_0.get_repr_function(Bar(), [(Foo, lambda x: 'FOO'), (Bar, lambda x: 'BAR')])() == 'BAR'

    # Subclass instances match a parent-type condition
    class SubFoo(Foo):
        pass
    assert module_0.get_repr_function(SubFoo(), [(Foo, lambda x: 'FOO')])() == 'FOO'

# Generated at 2026-11-02 00:29:27.213207
# Unit test for function shitcode
def test_shitcode():
    assert module_0.shitcode('foo') == 'foo'
    assert module_0.shitcode('') == ''
    assert module_0.shitcode(u'\u05d0') == '?'  # Hebrew character, non-latin
    assert module_0.shitcode(u'a\u05d0b') == 'a?b'
    assert module_0.shitcode(u'\u20ac') == '?'  # Euro sign
    assert module_0.shitcode(u'caf\u00e9') == u'caf\xe9'  # Latin-1 chars preserved
    assert module_0.shitcode(chr(0)) == '?'  # Null char gets replaced
    assert module_0.shitcode(chr(255)) == chr(255)  # Upper boundary of latin-1
    assert module_0.shitcode(chr(256)) == '?'  # Just above boundary
    assert module_0.shitcode(u'\u4e2d\u6587') == '??'  # Chinese characters
    assert all(c == '?' or 0 < ord(c) < 256 for c in module_0.shitcode(u'mixed\u1234text\u2603'))

# Generated at 2026-11-02 00:30:12.882095
# Unit test for function get_repr_function
def test_get_repr_function():
    class A(object):
        pass

    class B(A):
        pass

    a = A()
    b = B()

    # Empty custom_repr falls back to built-in repr
    assert module_0.get_repr_function(a, ()) is repr
    assert module_0.get_repr_function(b, ()) is repr

    # Type condition matches instances of that type...
    custom_repr = ((A, lambda x: 'A-repr'),)
    action = module_0.get_repr_function(a, custom_repr)
    assert action is custom_repr[0][1]
    assert action(a) == 'A-repr'

    # ...including subclasses
    assert module_0.get_repr_function(b, custom_repr) is custom_repr[0][1]

    # Type condition does not match instances of superclasses
    custom_repr = ((B, lambda x: 'B-repr'),)
    assert module_0.get_repr_function(a, custom_repr) is repr
    assert module_0.get_repr_function(b, custom_repr) is custom_repr[0][1]

    # Unrelated types don't match
    custom_repr = ((dict, lambda x: 'dict-repr'),)
    assert module_0.get_repr_function(a, custom_repr) is repr

    # Callable (non-type) conditions are used directly
    custom_repr = ((lambda x: x == 42, lambda x: 'forty-two'),)
    assert module_0.get_repr_function(42, custom_repr)(42) == 'forty-two'
    assert module_0.get_repr_function(43, custom_repr) is repr

    # First matching entry wins
    custom_repr = (
        (int, lambda x: 'int-repr'),
        (object, lambda x: 'object-repr'),
    )
    assert module_0.get_repr_function(42, custom_repr) is custom_repr[0][1]

    custom_repr = (
        (str, lambda x: 'str-repr'),
        (object, lambda x: 'object-repr'),
    )
    assert module_0.get_repr_function(42, custom_repr) is custom_repr[1][1]

    # Non-matching earlier entries are skipped
    custom_repr = (
        (dict, lambda x: 'never'),
        (type(None), lambda x: 'none-repr'),
    )
    assert module_0.get_repr_function(None, custom_repr) is custom_repr[1][1]

# Generated at 2026-11-02 00:35:32.085776
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    # nonce:10dc6094
    # Basic usage: falls back to the built-in repr.
    assert module_0.get_shortish_repr(7) == '7'
    assert module_0.get_shortish_repr('foo') == "'foo'"

    # Newlines and carriage returns are stripped from the repr.
    class MultilineRepr(object):
        def __repr__(self):
            return 'line1\r\nline2\nline3'
    assert module_0.get_shortish_repr(MultilineRepr()) == 'line1line2line3'

    # A broken __repr__ results in 'REPR FAILED'.
    class BrokenRepr(object):
        def __repr__(self):
            raise RuntimeError('broken')
    assert module_0.get_shortish_repr(BrokenRepr()) == 'REPR FAILED'

    # custom_repr entry matched by type.
    custom_repr = ((int, lambda item: 'AN INT!'),)
    assert module_0.get_shortish_repr(42, custom_repr=custom_repr) == 'AN INT!'

    # Type-based custom_repr matches subclasses (isinstance semantics).
    class Base(object):
        pass
    class Sub(Base):
        pass
    custom_repr = ((Base, lambda item: 'BASE!'),)
    assert module_0.get_shortish_repr(Sub(), custom_repr=custom_repr) == 'BASE!'

    # custom_repr entry matched by an arbitrary predicate.
    custom_repr = ((lambda item: item == 'me', lambda item: 'ITS ME!'),)
    assert module_0.get_shortish_repr('me', custom_repr=custom_repr) == 'ITS ME!'

    # First matching custom_repr entry wins.
    custom_repr = (
        (lambda item: True, lambda item: 'FIRST'),
        (lambda item: True, lambda item: 'SECOND'),
    )
    assert module_0.get_shortish_repr('anything', custom_repr=custom_repr) == 'FIRST'

    # Non-matching custom_repr falls back to the regular repr.
    custom_repr = ((str, lambda item: 'A STRING'),)
    assert module_0.get_shortish_repr(42, custom_repr=custom_repr) == '42'

    # Exceptions raised by a custom repr function are caught.
    def bad_custom_repr(item):
        raise ValueError('nope')
    custom_repr = ((int, bad_custom_repr),)
    assert module_0.get_shortish_repr(42, custom_repr=custom_repr) == 'REPR FAILED'

    # max_length truncates long reprs, keeping both ends.
    assert module_0.get_shortish_repr('abcdefghijklmnopqrstuvwxyz',
                             max_length=11) == 'abcd...wxyz'

    # Short reprs are not truncated.
    assert module_0.get_shortish_repr('short', max_length=100) == "'short'"

    # max_length=None (the default) never truncates.
    long_string = 'a' * 500
    assert module_0.get_shortish_repr(long_string) == ("'%s'" % long_string)

    # normalize=True strips memory addresses from default object reprs.
    class SomeObject(object):
        pass
    unnormalized = module_0.get_shortish_repr(SomeObject())
    assert ' at 0x' in unnormalized
    normalized = module_0.get_shortish_repr(SomeObject(), normalize=True)
    assert '0x' not in normalized
    assert normalized.endswith('SomeObject object>')

    # normalize also works on custom reprs containing addresses.
    class AddressRepr(object):
        def __repr__(self):
            return ('<some.long.module.SomeClass object '
                    'at 0xdeadbeef1234>')
    normalized = module_0.get_shortish_repr(AddressRepr(), normalize=True)
    assert normalized == '<some.long.module.SomeClass object>'

    # normalize and max_length work together.
    result = module_0.get_shortish_repr(AddressRepr(), max_length=30,
                               normalize=True)
    assert len(result) == 30
    assert '0x' not in result
    assert '...' in result
    assert result.startswith('<some.long.')
    assert result.endswith('>')

    # Truncation applies after newline stripping and normalization.
    class WeirdRepr(object):
        def __repr__(self):
            return 'aaaa\r\nbbbb' + 'c' * 50
    result = module_0.get_shortish_repr(WeirdRepr(), max_length=20)
    assert len(result) == 20
    assert '\n' not in result and '\r' not in result