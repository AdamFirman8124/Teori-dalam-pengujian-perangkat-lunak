

# Generated at 2026-11-02 21:48:23.879949
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    from io import StringIO

    # A concrete subclass implementing write should work
    class MyWritable(WritableStream):
        def module_0.write(self, s):
            self.written = s
            return len(s)

    my_stream = MyWritable()
    result = my_stream.write('hello')
    assert result == 5
    assert my_stream.written == 'hello'

    # StringIO should be recognized as a virtual subclass
    # because it has a `write` method
    assert issubclass(StringIO, WritableStream)
    assert isinstance(StringIO(), WritableStream)

    # A class without a `write` method should not be a subclass
    class NotWritable:
        pass

    assert not issubclass(NotWritable, WritableStream)

    # A class with write explicitly set to None should not be a subclass
    class NoneWrite:
        write = None

    assert not issubclass(NoneWrite, WritableStream)

    # Subclasshook only applies to WritableStream itself
    class OtherABC(ABC):
        pass

    assert OtherABC.__subclasshook__(NotWritable) is NotImplemented

    # WritableStream itself cannot be instantiated (abstract)
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError("WritableStream should be abstract")

# Generated at 2026-11-02 21:49:35.778214
# Unit test for function ensure_tuple
def test_ensure_tuple():
    # Non-iterable values get wrapped in a single-element tuple
    assert module_0.ensure_tuple(1) == (1,)
    assert module_0.ensure_tuple(1.5) == (1.5,)
    assert module_0.ensure_tuple(None) == (None,)
    assert module_0.ensure_tuple(object) == (object,)

    # Strings are iterable but should be treated as single items
    assert module_0.ensure_tuple('abc') == ('abc',)
    assert module_0.ensure_tuple('') == ('',)
    assert module_0.ensure_tuple(u'hello') == (u'hello',)

    # Bytes are also string-like
    assert module_0.ensure_tuple(b'abc') == (b'abc',)

    # Iterables get converted to tuples
    assert module_0.ensure_tuple([1, 2, 3]) == (1, 2, 3)
    assert module_0.ensure_tuple((1, 2, 3)) == (1, 2, 3)
    assert module_0.ensure_tuple([]) == ()
    assert module_0.ensure_tuple(()) == ()
    assert module_0.ensure_tuple({1, 2}) in ((1, 2), (2, 1))
    assert module_0.ensure_tuple({'a': 1, 'b': 2}) in (('a', 'b'), ('b', 'a'))
    assert module_0.ensure_tuple(range(3)) == (0, 1, 2)

    # Generators are consumed into a tuple
    assert module_0.ensure_tuple(x for x in range(3)) == (0, 1, 2)

    # Result is always a tuple
    assert isinstance(module_0.ensure_tuple(1), tuple)
    assert isinstance(module_0.ensure_tuple('abc'), tuple)
    assert isinstance(module_0.ensure_tuple([1, 2]), tuple)

# Generated at 2026-11-02 21:51:11.475905
# Unit test for constructor of class WritableStream
def test_WritableStream():
    # A class with a `write` method is considered a subclass via the
    # __subclasshook__ mechanism
    class WithWrite:
        def write(self, s):
            pass

    assert issubclass(WithWrite, WritableStream)
    assert isinstance(WithWrite(), WritableStream)

    # Inherited `write` methods are detected through the MRO
    class SubWithWrite(WithWrite):
        pass

    assert issubclass(SubWithWrite, WritableStream)
    assert isinstance(SubWithWrite(), WritableStream)

    # A class without a `write` method is not considered a subclass
    class WithoutWrite:
        pass

    assert not issubclass(WithoutWrite, WritableStream)
    assert not isinstance(WithoutWrite(), WritableStream)

    # A class whose `write` attribute is None is not considered a subclass
    class WriteIsNone:
        write = None

    assert not issubclass(WriteIsNone, WritableStream)

    # A real subclass implementing the abstract `write` method can be
    # instantiated and used
    class MyWritableStream(WritableStream):
        def write(self, s):
            return s

    stream = MyWritableStream()
    assert stream.write('foo') == 'foo'
    assert isinstance(stream, WritableStream)

    # The abstract base class itself cannot be instantiated
    try:
        WritableStream()
    except TypeError:
        pass
    else:
        raise AssertionError('WritableStream should be abstract and not '
                             'instantiable')

# Generated at 2026-11-02 21:52:23.397508
# Unit test for function ensure_tuple
def test_ensure_tuple():
    # nonce:08325069
    # Strings are not treated as iterables, so they get wrapped in a tuple.
    assert module_0.ensure_tuple('foo') == ('foo',)
    # Lists and tuples are converted to tuples.
    assert module_0.ensure_tuple(['foo', 'bar']) == ('foo', 'bar')
    assert module_0.ensure_tuple(('foo', 'bar')) == ('foo', 'bar')
    # Generators (and other one-shot iterables) are exhausted into a tuple.
    assert module_0.ensure_tuple(x for x in range(3)) == (0, 1, 2)
    # Non-iterable objects are wrapped in a single-element tuple.
    assert module_0.ensure_tuple(3) == (3,)
    assert module_0.ensure_tuple(None) == (None,)

# Generated at 2026-11-02 21:54:00.463768
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    # Basic repr behavior
    assert module_0.get_shortish_repr(1) == '1'
    assert module_0.get_shortish_repr(None) == 'None'
    assert module_0.get_shortish_repr([1, 2, 3]) == '[1, 2, 3]'

    # Newlines and carriage returns are removed
    assert module_0.get_shortish_repr('foo\r\nbar') == 'foobar'
    assert module_0.get_shortish_repr('a\nb\rc') == 'abc'

    class Foo:
        pass

    foo_repr = repr(Foo())

    # Normalization removes memory addresses
    normalized = module_0.get_shortish_repr(Foo(), normalize=True)
    assert normalized == re.sub(r' at 0x[a-f0-9A-F]{4,}', '', foo_repr)
    assert ' at 0x' not in normalized
    # Without normalization, the memory address is kept
    assert module_0.get_shortish_repr(Foo()) == foo_repr

    # max_length truncation keeps both head and tail
    assert module_0.get_shortish_repr('abcdefghijklmnopqrstuvwxyz',
                             max_length=10) == 'abc...wxyz'
    # No truncation when the string is short enough or max_length is None
    assert module_0.get_shortish_repr('abc', max_length=10) == 'abc'
    assert module_0.get_shortish_repr('abc') == 'abc'

    # Custom repr functions (type as condition)
    custom_repr = ((int, lambda x: 'int: {}'.format(x)),)
    assert module_0.get_shortish_repr(3, custom_repr=custom_repr) == 'int: 3'
    assert module_0.get_shortish_repr('3', custom_repr=custom_repr) == "'3'"

    # Custom repr functions (callable as condition)
    custom_repr = ((lambda x: isinstance(x, str), lambda x: 'a string!'),)
    assert module_0.get_shortish_repr('hello', custom_repr=custom_repr) == 'a string!'

    # The first matching custom repr wins
    custom_repr = ((int, lambda x: 'first'),
                   (object, lambda x: 'second'))
    assert module_0.get_shortish_repr(1, custom_repr=custom_repr) == 'first'
    assert module_0.get_shortish_repr(1.0, custom_repr=custom_repr) == 'second'

    # Broken reprs produce 'REPR FAILED'
    class Bad:
        def __repr__(self):
            raise ValueError('no')
    assert module_0.get_shortish_repr(Bad()) == 'REPR FAILED'
    assert module_0.get_shortish_repr(Bad(), max_length=5) == 'R...D'
    assert module_0.get_shortish_repr(Bad(), normalize=True) == 'REPR FAILED'

    # Newlines are stripped from custom repr output as well
    custom_repr = ((int, lambda x: 'line1\nline2\r\nline3'),)
    assert module_0.get_shortish_repr(7, custom_repr=custom_repr) == 'line1line2line3'

# Generated at 2026-11-02 21:55:31.556711
# Unit test for function get_repr_function
def test_get_repr_function():
    # No custom repr: falls back to built-in repr
    item = 123
    assert module_0.get_repr_function(item, ()) is repr

    # Condition is a type: uses isinstance check
    custom_repr = [(int, lambda x: 'INT')]
    assert module_0.get_repr_function(123, custom_repr)(123) == 'INT'

    # Condition is a callable
    custom_repr = [(lambda x: x > 100, lambda x: 'BIG')]
    assert module_0.get_repr_function(150, custom_repr)(150) == 'BIG'
    assert module_0.get_repr_function(5, custom_repr) is repr

    # First matching condition wins
    custom_repr = [
        (int, lambda x: 'INT'),
        (lambda x: True, lambda x: 'ALWAYS'),
    ]
    assert module_0.get_repr_function(123, custom_repr)(123) == 'INT'

    # Later entry matches when earlier doesn't
    custom_repr = [
        (str, lambda x: 'STR'),
        (int, lambda x: 'INT'),
    ]
    assert module_0.get_repr_function(123, custom_repr)(123) == 'INT'

    # Type condition does not match subclass check incorrectly
    class Foo(object):
        pass

    class Bar(Foo):
        pass

    custom_repr = [(Foo, lambda x: 'FOO')]
    assert module_0.get_repr_function(Bar(), custom_repr)(Bar()) == 'FOO'
    assert module_0.get_repr_function('not foo', custom_repr) is repr

    # Multiple entries with mixed condition types
    custom_repr = [
        (str, lambda x: 'STRING: %s' % x),
        (dict, repr),
    ]
    assert module_0.get_repr_function('abc', custom_repr)('abc') == 'STRING: abc'
    assert module_0.get_repr_function({'a': 1}, custom_repr)({'a': 1}) == repr({'a': 1})

    # None action is returned as-is (caller decides how to handle)
    custom_repr = [(int, None)]
    assert module_0.get_repr_function(1, custom_repr) is None

# Generated at 2026-11-02 21:57:17.398871
# Unit test for function get_repr_function
def test_get_repr_function():
    # With no custom repr entries, the built-in repr is returned
    item = object()
    assert module_0.get_repr_function(item, ()) is repr

    # When the condition is a type and the item is an instance of it,
    # the associated action is returned
    def custom_action(x):
        return 'CUSTOM'

    assert module_0.get_repr_function(3, ((int, custom_action),)) is custom_action

    # When the condition is a type but the item is not an instance,
    # fall through to the built-in repr
    assert module_0.get_repr_function('foo', ((int, custom_action),)) is repr

    # When the condition is a callable, it is called with the item
    condition = lambda x: x > 10
    assert module_0.get_repr_function(20, ((condition, custom_action),)) is custom_action
    assert module_0.get_repr_function(5, ((condition, custom_action),)) is repr

    # The first matching entry wins
    def another_action(x):
        return 'ANOTHER'

    assert module_0.get_repr_function(
        3, ((int, custom_action), (int, another_action))
    ) is custom_action

    # Type conditions use isinstance, so subclasses match
    class Base(object):
        pass

    class Derived(Base):
        pass

    assert module_0.get_repr_function(Derived(), ((Base, custom_action),)) is custom_action
    assert module_0.get_repr_function(object(), ((Base, custom_action),)) is repr