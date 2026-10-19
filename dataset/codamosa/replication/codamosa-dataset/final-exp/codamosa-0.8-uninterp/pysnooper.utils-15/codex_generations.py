

# Generated at 2022-06-12 19:58:42.299861
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class DummyWritableStream(WritableStream):
        def __init__(self):
            self.written_chunks = []

        def write(self, s):
            self.written_chunks.append(s)

    my_writable_stream = DummyWritableStream()
    my_writable_stream.write('aaa')
    my_writable_stream.write('bbb')
    assert my_writable_stream.written_chunks == ['aaa', 'bbb']

# Generated at 2022-06-12 19:58:47.111389
# Unit test for function shitcode
def test_shitcode():
    def check(s, result):
        assert shitcode(s) == result
    check('abc', 'abc')
    check('', '')
    check('¡', '?')
    check('\uFFFF', '?')
    check('\u0456', '?')
    check('\u0480', '?')



# Generated at 2022-06-12 19:58:49.284425
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def write(self, s):
            pass

    assert issubclass(MyWritableStream, WritableStream)



# Generated at 2022-06-12 19:58:59.444832
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    from .exact_type_checking import type_checked_values
    from .exact_type_checking import exact_type_values

    assert get_shortish_repr('hey', max_length=3) == 'he...'
    assert get_shortish_repr('hey', max_length=5) == 'hey'
    assert get_shortish_repr('hey', max_length=4) == 'hey'
    assert get_shortish_repr('hey') == 'hey'
    assert get_shortish_repr((1, 2, 3), max_length=5) == '(1, 2, 3)'
    assert get_shortish_repr((1, 2, 3), max_length=4) == '(1, 2,...)'

# Generated at 2022-06-12 19:59:05.837700
# Unit test for function get_repr_function
def test_get_repr_function():

    def test_type(x):
        return get_repr_function(x, [])

    assert test_type(3j) == repr
    assert test_type(3.5+5) == repr
    assert test_type(str) == repr
    assert test_type(test_type) != repr
    assert test_type(test_type) == test_type

    def custom_repr(obj):
        return 'Custom repr!'

    class CustomReprClass(object):
        __repr__ = custom_repr

    assert test_type(CustomReprClass()) == custom_repr

# Generated at 2022-06-12 19:59:07.560161
# Unit test for function get_repr_function
def test_get_repr_function():

    assert get_repr_function([1, 2, 3], (int, lambda _: 'int')) == repr

# Generated at 2022-06-12 19:59:11.359417
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def __init__(self):
            self.datas = []
        def write(self, data):
            self.datas.append(data)

    my_writable_stream1 = MyWritableStream()
    assert isinstance(my_writable_stream1, WritableStream)
    my_writable_stream2 = MyWritableStream()
    my_writable_stream2.write = None # This will make it not WritableStream
    assert not isinstance(my_writable_stream2, WritableStream)



# Generated at 2022-06-12 19:59:20.435081
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class WritableStream_(object):
        def write(self, s):
            pass

    assert issubclass(WritableStream_, WritableStream)

    class WritableStream_WithExtraMethod(WritableStream):
        def extra_method(self):
            pass

    assert issubclass(WritableStream_WithExtraMethod, WritableStream)

    class WritableStream_WithExtraAbstractMethod(WritableStream):
        @abc.abstractmethod
        def extra_method(self):
            pass

    assert not issubclass(WritableStream_WithExtraAbstractMethod,
                          WritableStream)

# Generated at 2022-06-12 19:59:29.560971
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('abcd', max_length=100) == 'abcd'
    assert get_shortish_repr('abcd', max_length=4) == 'abc...'
    assert get_shortish_repr('abcd', max_length=2) == 'a...'
    assert get_shortish_repr(1, max_length=4) == '1'
    assert get_shortish_repr(1, max_length=2) == '1'
    assert get_shortish_repr((1, 2, 3), max_length=8) == '(1, 2, 3)'
    assert get_shortish_repr((1, 2, 3), max_length=7) == '(1, 2...'

# Generated at 2022-06-12 19:59:38.942399
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    from .test_tools import assert_equal
    from .test_tools import assert_is
    from .test_tools import assert_reprs_equal
    from .test_tools import assert_raises
    from .test_tools import assert_not_raises
    from .test_tools import assert_is_instance
    
    assert_equal(
        get_shortish_repr(1, (), 10),
        repr(1)
    )
    assert_equal(
        get_shortish_repr('spam', (), 10),
        repr('spam')
    )
    assert_equal(
        get_shortish_repr(b'eggs', (), 10),
        repr(b'eggs')
    )

# Generated at 2022-06-12 19:59:50.197492
# Unit test for function get_repr_function
def test_get_repr_function():
    a = object()
    assert get_repr_function(a, (
        (lambda x: True, repr),
        (lambda x: False, str)
    )) is repr
    class Foo: pass
    foo = Foo()
    assert get_repr_function(foo, (
        (lambda x: True, repr),
        (Foo, str)
    )) is str
    assert get_repr_function(a, ((Foo, str),)) is repr
    assert get_repr_function(foo, ((Foo, str),)) is str



# Generated at 2022-06-12 19:59:59.842036
# Unit test for function get_repr_function
def test_get_repr_function():
    foo = self = None
    _custom_repr = (
        (lambda x: x is foo, lambda x: 'foo was here'),
        (lambda x: x is self, lambda x: 'self was here'),
        (str, lambda x: 'str was here'),
        (int, lambda x: 'int was here'),
    )
    assert get_repr_function('hello', _custom_repr) == 'str was here'
    assert get_repr_function(6, _custom_repr) == 'int was here'
    assert get_repr_function(foo, _custom_repr) == 'foo was here'
    assert get_repr_function(self, _custom_repr) == 'self was here'



# Generated at 2022-06-12 20:00:09.829181
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(set('abc')) == "{'a', 'c', 'b'}"
    assert get_shortish_repr(set('abc'), custom_repr=(
        (lambda x: isinstance(x, set), lambda x: '1234'),
    )) == "1234"
    assert get_shortish_repr(set('abc'), custom_repr=(
        (lambda x: isinstance(x, set), lambda x: '1234'),
    ), max_length=4) == "1234"
    assert get_shortish_repr(set('abc'), custom_repr=(
        (lambda x: isinstance(x, set), lambda x: '1234'),
    ), max_length=3) == "12..."

# Generated at 2022-06-12 20:00:12.022555
# Unit test for function shitcode
def test_shitcode():
    try:
        shitcode('אבג')
    except TypeError:
        pass
    else:
        raise Exception("Shouldn't be able to shitcode() non-ASCII strings.")



# Generated at 2022-06-12 20:00:20.856223
# Unit test for function get_shortish_repr
def test_get_shortish_repr():

    assert get_shortish_repr(5) == '5'
    assert get_shortish_repr(5, custom_repr=((lambda x: x > 10,
                                              lambda x: '> 10'),)) == '> 10'

    assert get_shortish_repr(5,
                             custom_repr=((lambda x: x > 10,
                                           lambda x: '> 10'),)) == '> 10'
    assert get_shortish_repr(5,
                             custom_repr=((lambda x: x > 10,
                                           lambda x: '> 10'),
                                          (lambda x: True,
                                           lambda x: 'always'))) == 'always'


# Generated at 2022-06-12 20:00:24.193566
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def write(self, s):
            pass

    assert issubclass(MyWritableStream, WritableStream)

# Generated at 2022-06-12 20:00:32.923013
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(['a'], None) is repr
    assert get_repr_function(['a'], [[type, lambda x: x[0][0]]]) == 'a'
    assert get_repr_function(['a'], ((type, lambda x: x[0]))).__name__ == \
                                                                  '<lambda>'
    assert get_repr_function(['a'], [[lambda x: True, lambda x: x[0][0]]]) == 'a'
    assert get_repr_function(
        (1, 2, 3),
        [[lambda x: x[0] == 1, lambda x: x[1]]]
    ) == 2



# Generated at 2022-06-12 20:00:44.567578
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(None) == 'None'
    assert get_shortish_repr(1) == '1'
    assert get_shortish_repr('a') == "'a'"
    assert get_shortish_repr('abc') == "'abc'"
    assert get_shortish_repr('abc', max_length=1) == "'a'"
    assert get_shortish_repr('abc', max_length=2) == "'ab'"
    assert get_shortish_repr('abc', max_length=3) == "'abc'"
    assert get_shortish_repr('abc', max_length=4) == "'abc'"
    assert get_shortish_repr('abc', max_length=5) == "'abc'"

# Generated at 2022-06-12 20:00:47.598125
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class WriteableList(list):
        def write(self, obj):
            self.append(obj)

    writeable_list = WriteableList()
    assert isinstance(writeable_list, WritableStream)
    writeable_list.write('test')
    assert writeable_list == ['test']

# Generated at 2022-06-12 20:00:55.195848
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function([], []) == repr
    assert get_repr_function(set(), []) == repr
    assert get_repr_function([], [(lambda x: True, lambda x: 'foo')]) == (
        lambda x: 'foo'
    )
    assert get_repr_function([], [(set, lambda x: 'foo')]) == (
        lambda x: 'foo'
    )
    assert get_repr_function(False, [(set, lambda x: 'foo')]) == (
        repr
    )

# Generated at 2022-06-12 20:01:03.198802
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class C:
        data = ''
        def write(self, s):
            self.data += s
    c = C()
    assert issubclass(C, WritableStream)
    c.write('puppy')
    assert c.data == 'puppy'
    c.write('noodle')
    assert c.data == 'puppynoodle'

# Generated at 2022-06-12 20:01:11.233181
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(u'a' * 100, max_length=10) == \
                                                        u'aaaaaaaaaa\u2026aaaaaa'
    assert get_shortish_repr(u'a' * 100, max_length=None) == u'aaaaaaaaaa' * 10
    assert get_shortish_repr(u'a' * 100, max_length=0) == u'aaaaaaaaaa' * 10
    assert get_shortish_repr(u'a' * 100, max_length=100) == u'aaaaaaaaaa' * 10
    assert get_shortish_repr(u'a' * 100, max_length=101) == u'aaaaaaaaaa' * 10
    assert get_shortish_repr(u'a' * 100, max_length=102) == u

# Generated at 2022-06-12 20:01:13.742100
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    try:
        with open(sys.argv[0]) as f:
            assert isinstance(f, WritableStream) # Make sure we're in a file
    except IndexError:
        raise AssertionError()
    except IOError:
        raise AssertionError()

# Generated at 2022-06-12 20:01:19.879595
# Unit test for function get_shortish_repr
def test_get_shortish_repr():

    class MyClass(object):
        def __init__(self, name):
            self.name = name

        def __repr__(self):
            return self.name

    def my_repr(item):
        return 'MyRepr: ' + repr(item.name)

    normalize_repr(repr(MyClass('xx' * 100)))
    assert normalize_repr(repr(MyClass('xx' * 100))) == repr(MyClass('xx' * 100))
    assert normalize_repr(
        repr(MyClass('xx' * 100))
    ).startswith('MyClass')

    assert get_shortish_repr(MyClass('abc'),
                             normalize=True) == 'MyClass(abc)'

# Generated at 2022-06-12 20:01:24.160260
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class C:
        pass
    c = C()
    c.write = lambda s: sys.stdout.write(s)
    assert issubclass(c.__class__, WritableStream)
    c.write('hi')

# Generated at 2022-06-12 20:01:25.892269
# Unit test for function shitcode
def test_shitcode():
    assert shitcode('abcd') == 'abcd'
    assert shitcode('abcd\xfc') == 'abcd?'

# Generated at 2022-06-12 20:01:29.158179
# Unit test for function shitcode
def test_shitcode():
    assert shitcode(u'\u2190') == '?'
    assert shitcode(u'\u2190' * 20) == '?' * 20
    assert shitcode(u'abc') == 'abc'



# Generated at 2022-06-12 20:01:36.455756
# Unit test for function get_repr_function
def test_get_repr_function():
    class Custom(object): pass
    assert get_repr_function(Custom(), ()) is repr
    assert get_repr_function(Custom(), (None, None)) is None
    assert get_repr_function(Custom(), ((None, None), (None, None))) is None
    assert get_repr_function(Custom(), ((str, None), (None, None))) is repr
    assert get_repr_function(Custom(), ((None, None), (str, None))) is None
    assert get_repr_function(Custom(), ((Custom, None), (None, None))) is repr
    assert get_repr_function(Custom(), ((None, None), (Custom, None))) is None
    assert get_repr_function(Custom(), ((Custom, None))) is repr

# Generated at 2022-06-12 20:01:45.827344
# Unit test for function get_repr_function
def test_get_repr_function():
    from .typing import FrozenSet
    assert callable(get_repr_function(1, []))
    assert get_repr_function(1, [(int, str)])(1) == '1'
    assert get_repr_function(1, [(FrozenSet, str)])(1) == '1'
    assert get_repr_function((1, 2), [(FrozenSet, str)])((1, 2)) == '(1, 2)'
    assert get_repr_function(1, [(lambda x: not isinstance(x, int), str)])(1) == '1'
    assert get_repr_function(1, [(lambda x: isinstance(x, int), str)])(1) == '1'

# Generated at 2022-06-12 20:01:55.879898
# Unit test for function get_repr_function
def test_get_repr_function():
    class A: pass
    class B: pass
    class C: pass
    class D: pass
    class E: pass
    class F: pass
    class G: pass

    custom_repr = [
        (int, shitcode),
        (float, shitcode),
        (str, shitcode),
        (lambda item: item.__class__.__name__ in 'A B'.split(), lambda item: 'Funny'),
        ((A, B), lambda item: 'Lucky'),
        ((C, D), lambda item: 'Lucky'),
        (E, lambda item: 'Lucky'),
        ((C, D, E), lambda item: 'Wow!'),
        ((F, G), lambda item: 'Wow!'),
    ]

    assert get_repr_function(5, custom_repr) == shitcode
    assert get

# Generated at 2022-06-12 20:02:01.108781
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    assert hasattr(WritableStream, 'write')
    assert isinstance(WritableStream.write, collections_abc.Callable)



# Generated at 2022-06-12 20:02:08.352384
# Unit test for function get_repr_function
def test_get_repr_function():
    class Thing(object): pass
    thing = Thing()
    assert get_repr_function(thing, ((type(thing), thing),)) is thing
    assert get_repr_function(thing, ()) == repr
    assert get_repr_function(thing) == repr
    assert get_repr_function(thing, ((lambda x: True, 'hi'),)) == 'hi'
    assert get_repr_function(thing, ((lambda x: False, 'hi'),)) == repr



# Generated at 2022-06-12 20:02:11.137252
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Stream(WritableStream):
        def write(self, s):
            self.written = s
    
    stream = Stream()
    stream.write('foo')
    assert stream.written == 'foo'

# Generated at 2022-06-12 20:02:16.847388
# Unit test for function shitcode
def test_shitcode():
    assert shitcode('abc') == 'abc'
    assert shitcode('abc\x01') == 'abc?'
    assert shitcode('\xc5\x99\xc5\xbe\xc3\xa1\xc3\xa9\xc3\xad\xc3\xb3\xc5'
                    '\x99\xc5\xbe\xc3\xba\xc5\xaf\xc5\xa1\xc5\xa5') == '??aéíó?ú????'



# Generated at 2022-06-12 20:02:27.300865
# Unit test for function get_repr_function
def test_get_repr_function():
    class A(object): pass
    a = A()

    assert get_repr_function(a, custom_repr=[]) is repr
    assert get_repr_function(a, custom_repr=[(A, str)]) is str

    assert get_repr_function(a, custom_repr=[(lambda x: False, str)]) is repr
    assert get_repr_function(a, custom_repr=[(lambda x: True, str)]) is str
    assert get_repr_function(a, custom_repr=[(lambda x, y=a: x is y, str)]) \
                                                                    is str
    assert get_repr_function(a, custom_repr=[(A, str), (A, repr)]) is str



# Generated at 2022-06-12 20:02:31.346879
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(object):
        def write(self, x):
            pass

    assert issubclass(A, WritableStream)
    assert not issubclass(str, WritableStream)
    assert not issubclass(int, WritableStream)



# Generated at 2022-06-12 20:02:35.696178
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def write(self, s):
            pass
    assert issubclass(MyWritableStream, WritableStream)
    assert isinstance(MyWritableStream(), WritableStream)
    assert not issubclass(int, WritableStream)


# Generated at 2022-06-12 20:02:41.466965
# Unit test for function get_repr_function
def test_get_repr_function():
    class ExampleClass:
        pass

    repr_function = get_repr_function(ExampleClass(), [
        (lambda x: True, lambda x: 'hei'),
        (ExampleClass, lambda x: 'hoi'),
    ])
    assert repr_function(ExampleClass()) == 'hoi'

    repr_function = get_repr_function(ExampleClass(), [
        (ExampleClass, lambda x: 'hoi'),
    ])
    assert repr_function(ExampleClass()) == 'hoi'

    repr_function = get_repr_function(ExampleClass(), [
        (lambda x: True, lambda x: 'hei'),
    ])
    assert repr_function(ExampleClass()) == 'hei'


# Generated at 2022-06-12 20:02:51.826991
# Unit test for function get_repr_function
def test_get_repr_function():
    class A(object): pass
    class B(A): pass

    repr_int = get_repr_function(1, ())
    repr_a = get_repr_function(A(), ())
    repr_b = get_repr_function(B(), ())
    repr_none = get_repr_function(None, ())

    assert repr_int(0) == '0'
    assert repr_a(A()) == '<tests.test_tools.test_misc.A object at 0x'
    assert repr_b(B()) == '<tests.test_tools.test_misc.B object at 0x'
    assert repr_none(None) == 'None'



    def a_repr(x):
        return 'a!'

    def b_repr(x):
        return 'b!'

    custom_re

# Generated at 2022-06-12 20:02:54.499461
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A:
        def write(self, s):
            pass
    assert isinstance(A(), WritableStream)
    assert 'write' in WritableStream.__dict__



# Generated at 2022-06-12 20:03:03.045223
# Unit test for function get_repr_function
def test_get_repr_function():
    class A(): pass
    class B(A): pass
    class C(): pass

    class X():
        def __repr__(self):
            return 'hello'

    assert get_repr_function(A(), ((type, normalize_repr),)) == normalize_repr
    assert get_repr_function(B(), ((type, normalize_repr),)) == normalize_repr
    assert get_repr_function(C(), ((type, normalize_repr),)) == repr
    assert get_repr_function(X(), ((type, normalize_repr),)) == normalize_repr



# Generated at 2022-06-12 20:03:09.026390
# Unit test for function get_repr_function
def test_get_repr_function():
    from .custom_repr import custom_repr, new_custom_repr
    from .bug_handling import BugHandler

    assert get_repr_function('hello', new_custom_repr) == repr
    assert get_repr_function((3,), new_custom_repr) == repr
    assert get_repr_function([3], new_custom_repr) == repr

    assert get_repr_function('hello', custom_repr) == repr
    assert get_repr_function((3,), custom_repr) == repr
    assert get_repr_function([3], custom_repr) == repr

    b = BugHandler()
    assert get_repr_function(b, custom_repr) == b.__repr__

# Generated at 2022-06-12 20:03:13.821101
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(5) == '5'
    assert get_shortish_repr('a', max_length=0) == ''
    assert get_shortish_repr('a', max_length=1) == 'a'
    assert get_shortish_repr('a', max_length=2) == 'a'
    assert get_shortish_repr('a', max_length=3) == 'a'
    assert get_shortish_repr('abc', max_length=2) == 'ab...'
    assert get_shortish_repr('abc', max_length=3) == 'abc'
    assert get_shortish_repr('abc', max_length=4) == 'abc'
    assert get_shortish_repr('abc', max_length=5) == 'abc'

# Generated at 2022-06-12 20:03:19.813111
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(5, ()) == repr
    assert get_repr_function(5, (lambda x: x > 10, lambda x: 'foo')) == repr
    assert get_repr_function(5, ((lambda x: x > 10, lambda x: 'foo'))) == repr
    assert get_repr_function(5, (lambda x: x < 10, lambda x: 'foo'))(5) == 'foo'
    assert get_repr_function(5, ((lambda x: x < 10, lambda x: 'foo')))(5) == 'foo'
    assert get_repr_function(5, (int, lambda x: 'foo'))(5) == 'foo'
    assert get_repr_function(5, ((int, lambda x: 'foo')))(5) == 'foo'


# Generated at 2022-06-12 20:03:26.138279
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWriteObject(WritableStream):
        def write(self, s):
            self.s = s

    assert isinstance(MyWriteObject(), WritableStream)
    assert not isinstance(object(), WritableStream)
    assert not isinstance(5, WritableStream)
    assert not isinstance(3.14, WritableStream)
    assert not isinstance(MyWriteObject, WritableStream)

# Generated at 2022-06-12 20:03:31.039929
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Stream(WritableStream):
        def __init__(self):
            self.written_items = []
        def write(self, s):
            self.written_items.append(s)
    stream = Stream()
    assert isinstance(stream, WritableStream)
    stream.write('a')
    stream.write('b')
    assert stream.written_items == ['a', 'b']

# Generated at 2022-06-12 20:03:40.927898
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    import pytest

    assert get_shortish_repr(1) == '1'
    assert get_shortish_repr(1.0) == '1'
    assert get_shortish_repr(1, max_length=1) == '1'
    assert get_shortish_repr(1, max_length=2) == '1'
    assert get_shortish_repr(1, max_length=2, normalize=True) == '1'
    assert get_shortish_repr(1, max_length=3) == '1'
    assert get_shortish_repr(1, max_length=3, normalize=True) == '1'
    assert get_shortish_repr(1, max_length=4) == '1'

# Generated at 2022-06-12 20:03:49.216819
# Unit test for function get_repr_function

# Generated at 2022-06-12 20:03:53.230111
# Unit test for function get_repr_function
def test_get_repr_function():
    custom_repr = [(lambda x: True, lambda x: 'custom'), (list, lambda x: 'list')]
    assert get_repr_function('abc', custom_repr) == 'custom'
    assert get_repr_function([1, 2, 3], custom_repr) == 'list'



# Generated at 2022-06-12 20:03:54.755326
# Unit test for function shitcode
def test_shitcode():
    assert shitcode('תשובה נכונה') == '?????????????'



# Generated at 2022-06-12 20:04:04.365116
# Unit test for function get_repr_function
def test_get_repr_function():

    lst = [1, 2, 3]


# Generated at 2022-06-12 20:04:06.184629
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(WritableStream):
        def write(self, s):
            pass
    assert issubclass(A, WritableStream)



# Generated at 2022-06-12 20:04:16.946063
# Unit test for function get_repr_function
def test_get_repr_function():
    def get_shortish_repr_with_custom_repr(item):
        return get_shortish_repr(item, custom_repr=((type(item), repr),))
    assert get_shortish_repr_with_custom_repr(1) == '1'
    assert get_shortish_repr_with_custom_repr('1') == "'1'"
    assert get_shortish_repr_with_custom_repr((1,)) == '(1,)'
    assert get_shortish_repr_with_custom_repr([1]) == '[1]'
    assert get_shortish_repr_with_custom_repr({1}) == '{1}'
    assert get_shortish_repr_with_custom_repr({1: 2}) == '{1: 2}'

# Generated at 2022-06-12 20:04:26.488338
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(13, [(int, lambda x: str(x) + ' is an int')]) == \
                                                                      '13 is an int'
    assert get_repr_function(13, [(str, lambda x: str(x) + ' is a str')]) == \
                                                                        repr
    assert get_repr_function('hey', [(int, lambda x: str(x) + ' is an int')]) == \
                                                                        repr
    assert get_repr_function('hey', [(str, lambda x: str(x) + ' is a str')]) == \
                                                            'hey is a str'
    assert get_repr_function('hey', [(type(None), lambda x: str(x))]) == repr

# Generated at 2022-06-12 20:04:33.892152
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('123456789') == '123456789'
    assert get_shortish_repr('123456789', max_length=100) == '123456789'
    assert get_shortish_repr(1.234568, max_length=100) == '1.234568'
    assert get_shortish_repr('123456789', max_length=5) == '12345'
    assert get_shortish_repr(1.234568, max_length=5) == '1.234'
    assert get_shortish_repr([[1, 2], [3, 4]], max_length=5) == '[[1, ...'

# Generated at 2022-06-12 20:04:37.075882
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class SampleWritableStream(WritableStream):
        def write(self, s):
            assert isinstance(s, bytes)
    x = SampleWritableStream()

# Generated at 2022-06-12 20:04:40.001607
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def __init__(self):
            self.all_strings = ''
        def write(self, s):
            self.all_strings += s
    mws = MyWritableStream()
    mws.write('hi')
    assert mws.all_strings == 'hi'
    mws.write('world')
    assert mws.all_strings == 'hiworld'



# Generated at 2022-06-12 20:04:49.855231
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, []) is repr
    assert get_repr_function(1., []) is repr

    assert get_repr_function(1, [(int, str)]) is str
    assert get_repr_function(1., [(int, str)]) is repr

    assert get_repr_function(int, [(int, str)]) is str
    assert get_repr_function(float, [(int, str)]) is repr

    class CustomRepr(object):
        __repr__ = lambda self: 'cust'
    assert get_repr_function(CustomRepr(), [(CustomRepr, lambda x: x.x)]) is id

# Generated at 2022-06-12 20:04:54.178228
# Unit test for function shitcode
def test_shitcode():
    assert (shitcode(u'\u2602') == '?')
    assert (shitcode(u'\u2601') == u'\u2601')
    assert (shitcode(u'foo\u2601bar') == u'foo\u2601bar')
    assert (shitcode(u'foo\u2602bar') == u'foo?bar')



# Generated at 2022-06-12 20:05:00.012423
# Unit test for function get_repr_function
def test_get_repr_function():
    class A: pass
    class B(A): pass
    class C(A): pass
    class D: pass
    class E: pass
    class F: pass
    class G: pass

    def repr_factory(test_type):
        return lambda x: '<{}>'.format(test_type)

    assert get_repr_function(A(), (
        (A, repr_factory('A')),
        (B, repr_factory('B')),
        (C, repr_factory('C')),
    ))(A()) == '<A>'

# Generated at 2022-06-12 20:05:11.576420
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(123456789, max_length=8) == '1234567...'
    assert get_shortish_repr(123456789, max_length=9) == '123456789'
    assert get_shortish_repr(
        123456789,
        max_length=9,
        custom_repr=[(lambda x: x == 123456789, lambda _: 'my favorite')]
    ) == 'my favori'




# Generated at 2022-06-12 20:05:15.361786
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyClass(object):
        pass

    assert _check_methods(MyClass, 'write') is NotImplemented
    MyClass.write = lambda self, s: sys.stdout.write(s)
    assert _check_methods(MyClass, 'write') is True

# Generated at 2022-06-12 20:05:25.180078
# Unit test for function get_repr_function
def test_get_repr_function():
    # Let's test that it returns the identity function for strings
    assert get_repr_function('hello', custom_repr=[]) is repr
    from . import misc_tools
    import string
    def custom_repr(x):
        return 'custom repr for "{}"'.format(x)
    custom_repr_for_int = lambda x: 'int repr for {}'.format(x)
    # Let's test that it returns the custom repr for ints
    assert get_repr_function(5, custom_repr=[(int, custom_repr_for_int)]) \
                                                            is custom_repr_for_int
    # Let's test that it returns the identity function for a function

# Generated at 2022-06-12 20:05:29.694627
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def write(self, s):
            pass
    assert issubclass(MyWritableStream, WritableStream)
    assert not issubclass(int, WritableStream)
    assert not issubclass(list, WritableStream)




# Generated at 2022-06-12 20:05:33.475717
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('abc', max_length=100) == 'abc'
    assert get_shortish_repr('abc', max_length=2) == '...'
    assert get_shortish_repr('abcdef', max_length=5) == 'ab...f'
    assert get_shortish_repr('abcdef', max_length=6) == 'abc...f'
    assert get_shortish_repr('abcdef', max_length=7) == 'abcdef'
    assert get_shortish_repr('abcdef', max_length=8) == 'abcdef'


# Generated at 2022-06-12 20:05:43.290002
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(b'a b') == "b'a b'"
    assert get_shortish_repr(b'a b', max_length=5) == "b'...'"
    assert get_shortish_repr(b'a b', max_length=6) == "b'a ...'"
    assert get_shortish_repr(b'a b', max_length=7) == "b'a b '"
    assert get_shortish_repr(b'a b', max_length=8) == "b'a b \\xc2\\xa0'"
    assert get_shortish_repr(b'a b', max_length=9) == "b'a b \\xc2\\xa0'"

# Generated at 2022-06-12 20:05:53.160703
# Unit test for function get_repr_function
def test_get_repr_function():
    import nose_parameterized
    from .with_assertions import assert_equal

    def condition1(x):
        return x == 1
        
    def condition2(x):
        return x == 2
        
    def action1(x):
        return 'repr1'
        
    def action2(x):
        return 'repr2'
        
    def action3(x):
        return 'repr3'
        

# Generated at 2022-06-12 20:06:02.211095
# Unit test for function get_repr_function
def test_get_repr_function():
    from .testing.test_tools import assert_equal
    from .testing.test_tools import assert_not_equal
    class A(object): pass
    class B(A): pass
    
    r1 = get_repr_function(A())
    r2 = get_repr_function(B())
    assert_equal(r1('anything'), r2('anything'))
    
    r1 = get_repr_function(A(), ((type(A), lambda x: 'A!'),))
    r2 = get_repr_function(B(), ((type(B), lambda x: 'B!'),))
    r3 = get_repr_function(B(), ((type(A), lambda x: 'A!'),))
    assert_equal(r1('anything'), 'A!')

# Generated at 2022-06-12 20:06:11.117212
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(sys.maxint) == '9223372036854775807'
    assert get_shortish_repr(sys.maxint, max_length=10) == '9223372036...'
    assert get_shortish_repr((7, 8, 9), max_length=15) == '(7, 8, 9)'
    assert get_shortish_repr((7, 8, 9), max_length=6) == '(7, ...)'
    assert get_shortish_repr((7, 8), max_length=5) == '(7, ...)'
    assert get_shortish_repr((7, 8), max_length=6) == '(7, 8)'
    assert get_shortish_repr((7, 8), max_length=7) == '(7, 8)'

# Generated at 2022-06-12 20:06:18.553155
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(lambda x: x) == '<function <lambda> at 0x'
    assert (get_shortish_repr(lambda x: x,
                              custom_repr=((lambda x: x,
                                            lambda y: 'my lambda'),)) ==
            'my lambda')
    assert (get_shortish_repr(lambda x: x,
                              custom_repr=((lambda x: x,
                                            lambda y: 'my lambda'),),
                              normalize=True) ==
            'my lambda')
    assert (get_shortish_repr(lambda x: x, normalize=True) ==
            '<function <lambda>')
    assert (get_shortish_repr(lambda x: x, max_length=12) ==
            '<function <...>')

# Generated at 2022-06-12 20:06:26.603551
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(WritableStream): pass
    assert not issubclass(A, WritableStream)
    class B:
        def write(self, s):
            pass
    assert issubclass(B, WritableStream)
    class C:
        pass
    assert not issubclass(C, WritableStream)


test_WritableStream_write()

# Generated at 2022-06-12 20:06:33.346004
# Unit test for function shitcode
def test_shitcode():
    assert shitcode('abc') == 'abc'
    assert shitcode('abc\x00\x01\x02\x03') == 'abc\x03\x03\x03\x03'
    assert shitcode('\x00\x01\x02') == '\x03\x03\x03'
    assert shitcode('\x16\x00\x01') == '\x16\x03\x03'
    assert shitcode('\x00\x01\x02') == '\x03\x03\x03'

# Generated at 2022-06-12 20:06:43.342652
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('hello world!') == "'hello world!'"

    class A(object):
        def __init__(self):
            pass

        def __repr__(self):
            return 'hello world!'


    assert get_shortish_repr(A()) == 'hello world!'

    assert get_shortish_repr('hello world!',
                             max_length=12) == "'hello wo...'"

    assert get_shortish_repr('hello world!',
                             max_length=10) == "'hello ...'"

    assert get_shortish_repr('hello world!',
                             max_length=11) == "'hello w...'"

    assert get_shortish_repr('hello world!',
                             max_length=15) == "'hello world!'"


# Generated at 2022-06-12 20:06:48.017796
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyFileLikeObject(WritableStream):
        def __init__(self):
            self.content = ""
        def write(self, s):
            self.content += s

    f = MyFileLikeObject()
    f.write('a')
    f.write('b')
    assert f.content == 'ab'



# Generated at 2022-06-12 20:06:54.976497
# Unit test for function shitcode
def test_shitcode():
    assert shitcode('a') == 'a'
    assert shitcode('a\nb') == 'a?b'
    assert shitcode('a\x0bb') == 'a?b'
    assert shitcode('a\n\x0bb') == 'a??b'
    assert shitcode('a\u1234') == 'a?'
    assert shitcode('a\u1234b') == 'a?b'
    assert shitcode('a\u1234b\u4321') == 'a?b?'
    assert shitcode('a\u1234b\u4321c') == 'a?b?c'
    assert shitcode('a\u1234b\u4321c\x0d') == 'a?b?c?'

# Generated at 2022-06-12 20:06:57.500076
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def write(self, s):
            pass

    assert issubclass(MyWritableStream, WritableStream)

# Generated at 2022-06-12 20:06:59.844233
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream1(WritableStream):
        def write(self, s): pass
    assert issubclass(MyWritableStream1, WritableStream)
    #
    class MyWritableStream2(WritableStream): pass
    assert not issubclass(MyWritableStream2, WritableStream)

# Generated at 2022-06-12 20:07:10.445379
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(1) == '1'
    assert get_shortish_repr(1, normalize=True) == '1'
    assert get_shortish_repr(1, normalize=True, max_length=2) == '1'
    assert get_shortish_repr(1, normalize=False, max_length=2) == '1'
    assert get_shortish_repr(1, normalize=True, max_length=1) == '...'
    assert get_shortish_repr(1, normalize=True, max_length=0) == '...'
    assert get_shortish_repr(1, normalize=False, max_length=1) == '...'

# Generated at 2022-06-12 20:07:16.480657
# Unit test for function shitcode
def test_shitcode():
    assert shitcode('s') == 's'
    assert shitcode('s\x10') == 's?'
    assert shitcode('\x10s') == '?s'
    assert shitcode('\x10\x10 s') == '?? s'
    assert shitcode('\x10\x10 \x10') == '?? ?'
    assert shitcode('\x10\x10 s\x10') == '?? s?'
    assert shitcode('\x10\x10 s\x10\x10\x10') == '?? s???'

# Generated at 2022-06-12 20:07:20.422791
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class TestWritable(WritableStream):
        def write(self, x):
            pass

    x = TestWritable()
    with x:
        pass

# Generated at 2022-06-12 20:07:28.399275
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    """Make sure that using `write` gives us what we expect it to give us."""
    import io
    from garlicsim.general_misc import string_tools
    output_stream = io.StringIO()
    writable_stream = string_tools.WritableStream(output_stream)
    writable_stream.write(u'Chicken')
    assert output_stream.getvalue() == 'Chicken'



# Generated at 2022-06-12 20:07:34.224906
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class WritableStreamSubclass(WritableStream):
        def __init__(self):
            self.data = ''
        def write(self, s):
            self.data += s
    wss = WritableStreamSubclass()
    wss.write('hello')
    wss.write('world')
    assert wss.data == 'helloworld'

# Generated at 2022-06-12 20:07:38.210809
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class DummyFile(WritableStream):
        def __init__(self):
            self.last_write = None
        def write(self, s):
            self.last_write = s

    dummy_file = DummyFile()
    dummy_file.write('foo bar')
    assert dummy_file.last_write == 'foo bar'



# Generated at 2022-06-12 20:07:45.985263
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr([1, 2, 3]) == '(1, 2, 3)'
    assert get_shortish_repr([1, 2, 3], max_length=3) == '(1,...'
    assert get_shortish_repr([1, 2, 3], max_length=7) == '(1, 2,...'
    assert get_shortish_repr([1, 2, 3], max_length=8) == '(1, 2,...)'
    assert get_shortish_repr([1, 2, 3], max_length=9) == '(1, 2, 3)'
    assert get_shortish_repr([1, 2, 3], max_length=10) == '(1, 2, 3)'


# Generated at 2022-06-12 20:07:50.509636
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class WritableStreamSubclass(WritableStream):
        def write(self, s):
            pass

    assert issubclass(WritableStreamSubclass, WritableStream)


test_WritableStream_write()

# Generated at 2022-06-12 20:07:57.274468
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert normalize_repr('x at 0x1234') == 'x'

    assert 'hello' == get_shortish_repr('hello', max_length=None,
                                        normalize=False)

    assert 'hello' == get_shortish_repr('hello', max_length=5, normalize=False)

    assert len('hello world') > 10

    assert 'hello...world' == get_shortish_repr('hello world', max_length=10,
                                        normalize=False)

    assert 'hello...world' == get_shortish_repr('hello world', max_length=11,
                                        normalize=False)

    assert 'hello...world' == get_shortish_repr('hello world', max_length=12,
                                        normalize=False)

    assert 'hello world' == get

# Generated at 2022-06-12 20:07:59.757754
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class MyWritableStream(WritableStream):
        def write(self, s):
           pass

    assert issubclass(MyWritableStream, WritableStream)



# Generated at 2022-06-12 20:08:01.966185
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def write(self, s):
            pass

    assert issubclass(MyWritableStream, WritableStream)



# Generated at 2022-06-12 20:08:03.770932
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import tempfile
    with tempfile.NamedTemporaryFile() as f:
        assert isinstance(f, WritableStream)

# Generated at 2022-06-12 20:08:11.778208
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class SomeWritableStream(WritableStream):
        pass

    class SomeUnwritableStream(object):
        pass

    assert issubclass(SomeWritableStream, WritableStream)
    assert not issubclass(SomeUnwritableStream, WritableStream)
    if sys.version_info[:2] == (3, 3):
        # For some reason, this is broken in v3.3.
        assert not issubclass(SomeUnwritableStream, WritableStream)

    class SomeWritableStream(WritableStream):
        def __init__(self):
            self.buffer = ''
        def write(self, s):
            assert isinstance(s, str)
            self.buffer += s
        def flush(self):
            pass

    some_writable_stream = SomeWritableStream()
    some_writable_

# Generated at 2022-06-12 20:08:25.613126
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    # Test a subclass that inherits from WritableStream:
    class MyWritableStream(WritableStream):
        def write(self, s):
            pass
    assert isinstance(MyWritableStream(), WritableStream)

    # Test a class that implements the right method but doesn't inherit from
    # WritableStream:
    class MyOtherWritableStream:
        def write(self, s):
            pass
    assert not isinstance(MyOtherWritableStream(), WritableStream)

    # Test a class that implements the right method but with a different name:
    class MyOtherWritableStream:
        def write_s(self, s):
            pass
    assert not isinstance(MyOtherWritableStream(), WritableStream)

# Generated at 2022-06-12 20:08:30.284631
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def __init__(self):
            self.contents = ''
        def write(self, s):
            self.contents += s

    my_writable_stream = MyWritableStream()
    my_writable_stream.write('spam')
    assert my_writable_stream.contents == 'spam'
    my_writable_stream.write('eggs')
    assert my_writable_stream.contents == 'spameggs'

# Generated at 2022-06-12 20:08:40.076455
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(3, max_length=3) == '3'
    assert get_shortish_repr(None, max_length=3) == 'None'
    assert get_shortish_repr(3, max_length=3, normalize=True) == '3'
    assert get_shortish_repr([1, 2, 3], max_length=3) == '[1, 2]'
    assert get_shortish_repr([1, 2, 3], max_length=3, normalize=True) == '[1, 2]'
    assert get_shortish_repr(('a', [1, 2, 3]), max_length=3) == "('a', [1, 2])"