

# Generated at 2022-06-12 19:58:45.954009
# Unit test for function get_repr_function
def test_get_repr_function():
    class A: pass
    class B(A): pass
    class C: pass
    a = A()
    b = B()
    c = C()
    assert get_repr_function(a, ((A, lambda x: 'A'))) == (lambda x: 'A')
    assert get_repr_function(a, ((B, lambda x: 'B'))) == repr
    assert get_repr_function(a, ((C, lambda x: 'C'))) == repr
    assert get_repr_function(a, ((type, lambda x: 'type'))) == (
        lambda x: 'type'
    )
    assert get_repr_function(a, ((type, lambda x: 'type'), (A, lambda x: 'A'))) == (
        lambda x: 'A'
    )
    assert get_

# Generated at 2022-06-12 19:58:47.917216
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class TestClass(WritableStream):
        def write(self, s):
            pass
    isinstance(TestClass(), WritableStream)


# Generated at 2022-06-12 19:58:55.723194
# Unit test for function get_repr_function
def test_get_repr_function():
    class Foo(object):
        pass
    assert get_repr_function(None) == repr
    assert get_repr_function(0) == repr
    assert get_repr_function(0.0) == repr
    assert get_repr_function('') == repr
    assert get_repr_function(()) == repr
    assert get_repr_function([]) == repr
    assert get_repr_function({}) == repr
    assert get_repr_function(Foo()) == repr
    assert get_repr_function(object()) == repr

    def custom_repr(x):
        return '<custom {}>'.format(x)
    assert get_repr_function(None, custom_repr=((object, custom_repr),)) == repr

# Generated at 2022-06-12 19:59:03.992607
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    class Foo:
        def __repr__(self):
            return 'Foo'
        def __str__(self):
            return 'foo'

    foo = Foo()
    class Bar:
        def __repr__(self):
            return 'Bar'
        def __str__(self):
            return 'bar'

    bar = Bar()

    assert get_shortish_repr("abcde") == "abcde"
    assert get_shortish_repr("abcde", max_length=10) == "abcde"
    assert get_shortish_repr("abcde", max_length=5) == "abcde"
    assert get_shortish_repr("abcde", max_length=4) == "a..."

# Generated at 2022-06-12 19:59:12.127038
# Unit test for function get_repr_function
def test_get_repr_function():
    class A: pass
    class B(A): pass
    assert get_repr_function(A(), ())(A()) == '<__main__.A object at 0x'
    assert get_repr_function(B(), ())(B()) == '<__main__.B object at 0x'
    assert get_repr_function(A(), ((A, lambda x: x.__class__.__name__)))(A()) == 'A'
    assert get_repr_function(B(), ((A, lambda x: x.__class__.__name__)))(B()) == 'B'
    assert get_repr_function(A(), ((B, lambda x: 'xxx')))(A()) == '<__main__.A object at 0x'

# Generated at 2022-06-12 19:59:24.132846
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(1) == '1'
    assert get_shortish_repr(1, max_length=1) == '1'
    assert get_shortish_repr(1, max_length=0) == ''
    assert get_shortish_repr('abc', max_length=2) == 'ab...'
    assert get_shortish_repr('abc', max_length=1) == 'a...'
    assert get_shortish_repr(set(), max_length=1) == '{...}'
    assert get_shortish_repr([], max_length=1) == '[]'
    assert get_shortish_repr((), max_length=1) == '()'

# Generated at 2022-06-12 19:59:35.215420
# Unit test for function shitcode
def test_shitcode():
    from python_toolbox import cute_testing
    assert shitcode(u'\u2603') == u'?'
    assert shitcode(u'\u2100') == u'?'
    assert shitcode(u'\u20ac') == u'\u20ac'
    assert shitcode(u'\u2603\u2100') == u'??'
    assert shitcode(u'\u2603\u20ac') == u'?\u20ac'
    assert shitcode(u'\u2100\u20ac') == u'?\u20ac'
    assert shitcode(u'\u9055\u3044') == u'\u9055\u3044'
    assert shitcode(u'\U0001f6ad') == u'\U0001f6ad'



# Generated at 2022-06-12 19:59:38.134539
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def write(self, s):
            pass

    assert issubclass(MyWritableStream, WritableStream)
    assert not issubclass(WritableStream, MyWritableStream)



# Generated at 2022-06-12 19:59:45.573044
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(3, [(lambda x: False, lambda x: x)]) == repr
    assert get_repr_function(3.5, [(lambda x: False, lambda x: x)]) == repr
    assert get_repr_function('3', [(lambda x: False, lambda x: x)]) == repr

    assert get_repr_function(3, [(lambda x: True, lambda x: 1)]) == \
                                                                   (lambda x: 1)
    assert get_repr_function(3.5, [(lambda x: True, lambda x: 1)]) == \
                                                                   (lambda x: 1)
    assert get_repr_function('3', [(lambda x: True, lambda x: 1)]) == \
                                                                   (lambda x: 1)

    assert get_repr

# Generated at 2022-06-12 19:59:48.960255
# Unit test for function get_repr_function
def test_get_repr_function():
    from copy import copy
    assert get_repr_function(None) == repr
    assert get_repr_function(None, custom_repr=[(lambda s: True, str)]) == str
    assert get_repr_function(object, custom_repr=[(object, str)]) == str
    assert get_repr_function(object, [(object, str),
                                      (None, str)]) == str
    assert get_repr_function(object, [(int, str),
                                      (None, str)]) == repr



# Generated at 2022-06-12 20:00:00.961761
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    import random

    assert get_shortish_repr(1) == '1'
    assert get_shortish_repr([1, 2]) == '[1, 2]'
    assert get_shortish_repr((1, 2)) == '(1, 2)'
    assert get_shortish_repr(object) == "<type 'object'>"
    assert get_shortish_repr(object(), max_length=7) == 'object()'
    assert get_shortish_repr(object(), max_length=7, normalize=True) == \
                                                                    'object'
    assert get_shortish_repr([1, 2], max_length=7) == '[1, 2]'
    assert get_shortish_repr([1, 2, 3, 4], max_length=7) == '[1, ...]'


# Generated at 2022-06-12 20:00:05.034643
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class StringIO(WritableStream):
        def __init__(self):
            self.s = ''
        def write(self, c):
            self.s += c
    string_io = StringIO()
    string_io.write('hello')
    assert string_io.s == 'hello'

# Generated at 2022-06-12 20:00:13.190089
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('12345678901234567890') == '12345678901234567890'
    assert get_shortish_repr('12345678901234567890', max_length=10) == '1234567...67890'
    assert get_shortish_repr('12345678901234567890', max_length=20) == '12345678901234567890'
    assert get_shortish_repr('12345678901234567890', max_length=15) == '123456789012345'
    assert get_shortish_repr('12345678901234567890', max_length=16) == '1234567890123456'

# Generated at 2022-06-12 20:00:15.311903
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function('abc', ()) is repr
    assert get_repr_function('abc', ((str, str), (int, str))) is repr
    assert get_repr_function(5, ((str, str), (int, str))) == str



# Generated at 2022-06-12 20:00:20.599059
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def __init__(self, out):
            self.out = out
        def write(self, s):
            self.out.write(s)
    writable_stream = MyWritableStream(sys.stdout)
    writable_stream.write('spam')

# Generated at 2022-06-12 20:00:29.376711
# Unit test for function get_shortish_repr
def test_get_shortish_repr():

    class Test(object):
        def __repr__(self):
            return '<Test>'

    print(get_shortish_repr('abcde'))
    print(get_shortish_repr('abcde', max_length=3))
    print(get_shortish_repr('abcde', max_length=4))
    print(get_shortish_repr('abcde', max_length=5))
    print(get_shortish_repr('abcde', max_length=6))
    print(get_shortish_repr(Test(), custom_repr=((bool, lambda x: '<yes>'),)))

# Generated at 2022-06-12 20:00:33.246107
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, custom_repr=[]) is repr
    assert get_repr_function(1, custom_repr=[(1, str), (3, lambda x: 'hi')]) is str
    assert get_repr_function(2, custom_repr=[(1, str), (3, lambda x: 'hi')]) is repr
    assert get_repr_function(4, custom_repr=[(1, str), (3, lambda x: 'hi')]) == 'hi'
    assert get_repr_function('a', custom_repr=[(str, str), (3, lambda x: 'hi')]) is str
    assert get_repr_function(2, custom_repr=[(str, str), (3, lambda x: 'hi')]) is repr
    assert get_repr_

# Generated at 2022-06-12 20:00:45.050929
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, custom_repr=[]) is repr
    assert get_repr_function(1, custom_repr=[(1, '1')]) == '1'
    assert get_repr_function(2, custom_repr=[(1, '1')]) is repr
    assert get_repr_function(2, custom_repr=[(int, '1')]) == '1'
    assert get_repr_function(2, custom_repr=[(lambda x: False, '1')]) is repr
    assert get_repr_function(2, custom_repr=[(lambda x: True, '1')]) == '1'

# Generated at 2022-06-12 20:00:52.693841
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(2) == '2'
    assert get_shortish_repr(5, max_length=2) == '5'
    assert get_shortish_repr(5, max_length=1) == '5'
    assert get_shortish_repr(5, max_length=0) == '5'
    assert get_shortish_repr(5, max_length=None) == '5'
    assert get_shortish_repr(42, max_length=4) == '42'
    assert get_shortish_repr(42, max_length=3) == '4...'
    assert get_shortish_repr(42, max_length=2) == '4...'

# Generated at 2022-06-12 20:01:03.227450
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    items = [
        '123456789',
        '123456789',
        '123456789',
        '123456789',
        '123456789',
        '123456789',
        '123456789',
        '123456789',
        '123456789',
        '123456789',
    ]
    assert get_shortish_repr(items,
                             normalize=True) == repr(items)
    assert get_shortish_repr(items,
                             max_length=None,
                             normalize=True) == repr(items)
    assert get_shortish_repr(items,
                             max_length=50,
                             normalize=True) == repr(items)

# Generated at 2022-06-12 20:01:11.065256
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(WritableStream):
        def write(self, *whatever):
            pass
    A()



# Generated at 2022-06-12 20:01:21.833780
# Unit test for function get_shortish_repr
def test_get_shortish_repr():

    class SomethingWithLongRepr(object):
        def __init__(self, x):
            self.x = x
        def __repr__(self):
            return 'something with long repr: %s' % self.x

    r = get_shortish_repr(SomethingWithLongRepr('reallylongstring'))
    assert r == 'something with long repr: reallylongstring'
    r = get_shortish_repr(SomethingWithLongRepr('reallylongstring'),
                          max_length=15)
    assert r == 'som...gstring'
    r = get_shortish_repr(SomethingWithLongRepr('reallylongstring'),
                          max_length=1)
    assert r == 's'

# Generated at 2022-06-12 20:01:28.391741
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function('r', ((str, lambda x: 'hi'),)) == 'hi'
    assert get_repr_function('r', ((lambda x: True, lambda x: 'hi'),)) == 'hi'

    assert get_repr_function('r', ((str, 'hi'),)) == 'hi'
    assert get_repr_function('r', ((lambda x: True, 'hi'),)) == 'hi'

    assert get_repr_function(1, ((str, 'hi'),)) == repr

# Generated at 2022-06-12 20:01:35.673288
# Unit test for function get_repr_function
def test_get_repr_function():
    from .python_toolbox import get_repr_function
    class A(object): pass
    class B(A): pass
    assert get_repr_function(A(), []) is repr
    assert get_repr_function(A(), [(A, str)]) is str
    assert get_repr_function(A(), [(B, str)]) is repr
    assert get_repr_function(A(), [(A, str), (B, str)]) is str
    assert get_repr_function(A(), [(B, str), (A, str)]) is str
    assert get_repr_function(A(), [(A, str), (B, str), (A, str)]) is str
    assert get_repr_function(A(), [(A, str), (B, str), (A, str)]) is str

# Generated at 2022-06-12 20:01:45.242898
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(None, max_length=4) == 'None'
    assert get_shortish_repr(None, max_length=None) == 'None'
    assert get_shortish_repr(1, max_length=4) == '1'
    assert get_shortish_repr(1, max_length=1) == '1'
    assert get_shortish_repr(1, max_length=2) == '1'
    assert get_shortish_repr(1, max_length=3) == '1'
    assert get_shortish_repr(1, max_length=4) == '1'
    assert get_shortish_repr(12345678, max_length=4) == '1...8'

# Generated at 2022-06-12 20:01:47.167893
# Unit test for function get_repr_function
def test_get_repr_function():
    import math
    assert get_repr_function(3, ((int, str.upper),)) == str.upper
    assert get_repr_function(math.pi, ((int, str.upper),)) == repr



# Generated at 2022-06-12 20:01:57.446703
# Unit test for function shitcode
def test_shitcode():
    for u, s in (
        ('©', '?'),
        ('ಠ_ಠ', '????_??'),
        ('abc', 'abc'),
    ):
        r = shitcode(u)
        assert isinstance(r, str)
        assert len(r) == len(s)
        assert r == s
    if sys.platform == 'cli':
        return
    for u in (
        u'\U0001F61E \U0001F61E \U0001F61E',
        u'\U0001F63B \U0001F61E \U0001F63B',
        u'\U0001F63B \U0001F63B \U0001F63B',
    ):
        r = shitcode(u)
        assert isinstance(r, str)

# Generated at 2022-06-12 20:02:05.114225
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(1) == '1'
    assert get_shortish_repr(1, max_length=1) == '1'
    assert get_shortish_repr(1, max_length=2) == '1'
    assert get_shortish_repr(1, max_length=3) == '1'
    assert get_shortish_repr(1, max_length=4) == '1'
    assert get_shortish_repr(1, max_length=100) == '1'
    assert get_shortish_repr(123456789111111111111111222, max_length=30) ==\
                           '123456789111111111111111222'

# Generated at 2022-06-12 20:02:10.812319
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def __init__(self):
            self.written_text = ''
        def write(self, s):
            self.written_text += s

    writable_stream = MyWritableStream()

    writable_stream.write('hello')
    writable_stream.write(' there!')
    assert writable_stream.written_text == 'hello there!'

    writable_stream.write(5)
    assert writable_stream.written_text == 'hello there!5'





# Generated at 2022-06-12 20:02:17.784641
# Unit test for function get_repr_function
def test_get_repr_function():

    assert get_repr_function(1, [(int, repr)]) == repr

    assert get_repr_function(1.0, [(int, repr)]) == repr

    assert get_repr_function(1.0, [(int, repr), (float, str)]) == str

    assert get_repr_function(1, [(int, repr), (float, str)]) == repr

    assert get_repr_function(1, [(int, repr), (float, str)]) == repr

    assert get_repr_function(1, [(bool, repr), (int, str), (float, str)]) == \
                                                                           str



# Generated at 2022-06-12 20:02:30.119416
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(10) == '10'
    assert get_shortish_repr(10, max_length=2) == '10'
    assert get_shortish_repr(10, max_length=3) == '10'
    assert get_shortish_repr(10, max_length=4) == '10'
    assert get_shortish_repr(10, max_length=5) == '10'
    assert get_shortish_repr(10, max_length=6) == '10'
    assert get_shortish_repr(10, max_length=7) == '10'
    assert get_shortish_repr(10, max_length=8) == '10'

# Generated at 2022-06-12 20:02:37.220837
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function('p', ()) is repr
    assert get_repr_function('p', ((str, 'c'),)) == 'c'
    assert get_repr_function('p', ((str, 'c'), ('g', 'd'))) == 'c'
    assert get_repr_function('p', (('g', 'b'),
                                   (str, 'c')
                                  )) == 'c'
    assert get_repr_function(3, ((str, 'c'),
                                 (str, 'c'),
                                )) is repr



# Generated at 2022-06-12 20:02:39.815218
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(WritableStream):
        write_output = ''
        def write(self, s):
            self.write_output += s
    a = A()
    a.write('bla')
    assert a.write_output == 'bla'



# Generated at 2022-06-12 20:02:44.995720
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def __init__(self):
            self.written_items = []

        def write(self, item):
            self.written_items.append(item)

    my_writable_stream = MyWritableStream()
    my_writable_stream.write('spam')
    my_writable_stream.write('eggs')
    assert my_writable_stream.written_items == ['spam', 'eggs']



# Generated at 2022-06-12 20:02:46.049057
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    from six.moves import StringIO

    assert isinstance(StringIO(), WritableStream)

# Generated at 2022-06-12 20:02:52.490369
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(1) == '1'
    assert get_shortish_repr('abc') == "'abc'"
    assert get_shortish_repr('abc', custom_repr=((
        lambda x: isinstance(x, str) and len(x) > 2,
        lambda x: '***' + x,
    ), (
        lambda x: isinstance(x, int),
        lambda x: '{:,}'.format(x),
    ))) == '***abc'

# Generated at 2022-06-12 20:03:02.096590
# Unit test for function shitcode
def test_shitcode():
    def assert_shitcode(s, expected):
        assert shitcode(s) == expected
    assert_shitcode('foo', 'foo')
    assert_shitcode('f\x00o\xffo', 'f?o?')
    assert_shitcode('f\x00o\xffo', 'f?o?')
    assert_shitcode('\x00\x01\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19', '?' * 25)

# Generated at 2022-06-12 20:03:04.266861
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyStream(WritableStream):
        def write(self, s):
            return s
    assert issubclass(MyStream, WritableStream)



# Generated at 2022-06-12 20:03:08.506814
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(WritableStream):
        def __init__(self):
            self.x = ''
        def write(self, s):
            self.x += s
    assert issubclass(A, WritableStream)
    a = A()
    a.write('hi')
    assert a.x == 'hi'
    a.write(' there')
    assert a.x == 'hi there'
    assert not hasattr(a, 'writte')



# Generated at 2022-06-12 20:03:09.847185
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class TempClass:
        def write(self, x):
            return x

    assert isinstance(TempClass(), WritableStream)



# Generated at 2022-06-12 20:03:20.570492
# Unit test for function shitcode
def test_shitcode():
    assert shitcode('') == ''
    assert shitcode('a') == 'a'
    assert shitcode('b') == 'b'
    assert shitcode('abc') == 'abc'
    assert shitcode('abcdefghijk') == 'abcdefghijk'
    assert shitcode('abcd' * 1000) == 'abcd' * 1000
    assert shitcode('\x00') == '?'
    assert shitcode('\x01') == '?'
    assert shitcode('\x02') == '?'
    assert shitcode('\xFF') == '?'
    assert shitcode('\xFF' * 1000) == '?' * 1000
    assert shitcode('\x00\xFF') == '?\xFF'
    assert shitcode('\xFF\x00') == '\xFF?'

# Generated at 2022-06-12 20:03:24.258681
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(1) == '1'
    assert get_shortish_repr(1, max_length=3) == '1'
    assert get_shortish_repr(1, max_length=2) == '1'
    assert get_shortish_repr('hi', max_length=2) == 'hi'

# Generated at 2022-06-12 20:03:33.259027
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(None) is repr
    assert get_repr_function(1) is repr
    mock = Mock()
    assert callable(get_repr_function(mock))
    assert get_repr_function(mock)() == 'mock'
    assert get_repr_function(mock, custom_repr=(
        (lambda x: x is mock, lambda x: 'mock2'),
    ))() == 'mock2'

    assert get_repr_function(mock, custom_repr=(
        (lambda x: x is mock, lambda x: 'mock2'),
        (lambda x: x is mock, lambda x: 'mock3'),
    ))() == 'mock2'


# Generated at 2022-06-12 20:03:43.888131
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(1) == '1'
    assert get_shortish_repr(1, max_length=2) == '1'
    assert get_shortish_repr(1, max_length=1) == '1'
    assert get_shortish_repr(1, max_length=0) == ''
    assert get_shortish_repr(1.0, max_length=5) == '1.0'
    assert get_shortish_repr(None, max_length=5) == 'None'
    assert get_shortish_repr('asdf', max_length=7) == 'asdf'
    assert get_shortish_repr('asdf', max_length=6) == 'asdf'

# Generated at 2022-06-12 20:03:47.409458
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class FakeStream(WritableStream):
        def __init__(self):
            self.content = ''
        def write(self, s):
            self.content += s

    stream = FakeStream()
    stream.write('spam')
    assert stream.content == 'spam'




# Generated at 2022-06-12 20:03:56.878544
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    # Check that builtin streams are WritableStreams:
    assert issubclass(sys.stdout.__class__, WritableStream)
    assert isinstance(sys.stdout, WritableStream)
    # Check that random streams aren't WritableStreams:
    assert not issubclass(int.__class__, WritableStream)
    assert not isinstance(7, WritableStream)
    # Check that a custom class that properly implements write is a
    # WritableStream:
    class Foo(object):
        def write(self, s):
            pass
    assert issubclass(Foo, WritableStream)
    assert isinstance(Foo(), WritableStream)
    # Check that a custom class that doesn't implement write isn't a
    # WritableStream:
    class Bar(object):
        pass
    assert not issub

# Generated at 2022-06-12 20:03:58.711193
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Foo:
        def write(self, s):
            pass
    assert issubclass(Foo, WritableStream)



# Generated at 2022-06-12 20:04:02.362594
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyStream(WritableStream):
        def __init__(self) -> None:
            self.data = b''
        def write(self, s: bytes) -> None:
            self.data += s

    stream = MyStream()
    stream.write(b'one')
    assert stream.data == b'one'
    stream.write(b'two')
    assert stream.data == b'onetwo'

# Generated at 2022-06-12 20:04:04.529288
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def write(self, s):
            pass

    assert issubclass(MyWritableStream, WritableStream)



# Generated at 2022-06-12 20:04:11.798747
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(1) == '1'
    assert get_shortish_repr(1, max_length=1) == '1'
    assert get_shortish_repr(1, max_length=2) == '1'
    assert get_shortish_repr(1, max_length=3) == '1'
    assert get_shortish_repr(12, max_length=3) == '12'
    assert get_shortish_repr(123, max_length=3) == '123'
    assert get_shortish_repr(1234, max_length=3) == '...'
    assert get_shortish_repr(12345, max_length=3) == '...'
    assert get_shortish_repr(123456, max_length=3)

# Generated at 2022-06-12 20:04:19.032953
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class TestStream(WritableStream):
        def write(self, s):
            pass
    TestStream().write('hi')



# Generated at 2022-06-12 20:04:24.035406
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class F(object):
        def write(self, s):
            assert isinstance(s, str)
    assert isinstance(F(), WritableStream)
    class F(object):
        def write(self, s):
            assert isinstance(s, bytes)
    assert isinstance(F(), WritableStream)


# Generated at 2022-06-12 20:04:28.416883
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class dummy_stream(object):
        def __init__(self):
            self.string = ''
        def write(self, s):
            self.string += s
        def __del__(self):
            self.string = ''

    assert issubclass(dummy_stream, WritableStream) # Unit test passed


if __name__ == '__main__':
    test_WritableStream_write()
    print('Everything is fine.')

# Generated at 2022-06-12 20:04:33.181204
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    from . import assert_equal
    assert_equal(get_shortish_repr('hello'), "'hello'")
    assert_equal(get_shortish_repr('hello', max_length=2), "...")
    assert_equal(get_shortish_repr('hello', max_length=10), "'hello'")
    assert_equal(get_shortish_repr('hello', max_length=5), "'he...")
    assert_equal(get_shortish_repr([1, 2, 3], max_length=5), "[1, ...")
    assert_equal(get_shortish_repr([1, 2, 3], max_length=15), "[1, 2, 3]")
    assert_equal(get_shortish_repr(i for i in range(3)), "<gen...")
    assert_

# Generated at 2022-06-12 20:04:43.870805
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('abc', max_length=1) == 'a...'
    assert get_shortish_repr('abc', max_length=2) == 'a...'
    assert get_shortish_repr('abc', max_length=3) == 'a...'
    assert get_shortish_repr('abc', max_length=4) == 'ab...'
    assert get_shortish_repr('abc', max_length=5) == 'ab...'
    assert get_shortish_repr('abc', max_length=6) == 'abc...'
    assert get_shortish_repr('abc', max_length=7) == 'abc...'

    assert get_shortish_repr('abcdefghijklmn', max_length=3) == 'a...n'
   

# Generated at 2022-06-12 20:04:45.190432
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class WriteableStreamTest(WritableStream):
        def write(self, s):
            pass

    assert issubclass(WriteableStreamTest, WritableStream)



# Generated at 2022-06-12 20:04:54.398730
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(lambda x: x) == '<function test_get_shortish_repr.<locals>.<lambda> at 0x000001F8A9F2F488>'
    assert get_shortish_repr(lambda x: x, custom_repr=((lambda x: True, 'oops'),)) == 'oops'
    assert get_shortish_repr(lambda x: x, custom_repr=((lambda x: False, 'oops'),)) == '<function test_get_shortish_repr.<locals>.<lambda> at 0x000001F8A9F2F488>'
    assert get_shortish_repr(lambda x: x, custom_repr=((lambda x: False, 'oops'), (lambda x: True, 'oops2'))) == 'oops2'

   

# Generated at 2022-06-12 20:05:05.450363
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    from .objects import get_shortish_repr

    assert get_shortish_repr('apple') == "'apple'"
    assert get_shortish_repr(1) == '1'
    assert get_shortish_repr([1, 2, 3]) == '[1, 2, 3]'

    assert get_shortish_repr('apple', max_length=4) == "'app'..."
    assert get_shortish_repr([1, 2, 3], max_length=4) == '[1, 2'

    assert get_shortish_repr([1, 2, 3], max_length=8) == '[1, 2, 3]'

    class A(object):
        def __repr__(self):
            return 'r'*100
    assert get_shortish_repr(A(), max_length=10)

# Generated at 2022-06-12 20:05:07.701395
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A:
        def write(self, s):
            pass

    assert isinstance(A(), WritableStream)




# Generated at 2022-06-12 20:05:15.624398
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(5, ()) is repr
    assert get_repr_function(5.5, ()) is repr

    def custom_repr_float(x):
        return 'float {}'.format(x)
    assert get_repr_function(5.5,
                    ((type(5.5), custom_repr_float),)) is custom_repr_float
    assert get_repr_function(5.5,
                    ((lambda x: isinstance(x, type(5.5)), custom_repr_float),)) \
                                                          is custom_repr_float

# Generated at 2022-06-12 20:05:24.123226
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Foo(WritableStream):
        def write(self, s):
            pass

    assert issubclass(Foo, WritableStream)
    Foo()

    with pytest.raises(TypeError):
        class Bar(Foo):
            pass

    class Baz(Foo):
        def __init__(self):
            pass

    assert issubclass(Baz, WritableStream)
    Baz()

    class Quux(Foo):
        def write(self):
            pass

    assert not issubclass(Quux, WritableStream)
    with pytest.raises(TypeError):
        Quux()

    class Corge(Foo):
        def write(self, s, t):
            pass

    assert not issubclass(Corge, WritableStream)

# Generated at 2022-06-12 20:05:29.112644
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, ((int, str), str)) == str
    assert get_repr_function('a', ((int, str), str)) == str
    assert get_repr_function(1, ((int, str), type)) == type
    assert get_repr_function('a', ((int, str), type)) == type

# Generated at 2022-06-12 20:05:34.590354
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Y(WritableStream):
        def write(self, s):
            pass

    class Z(WritableStream):
        def foo(self, s):
            pass

    assert issubclass(Y, WritableStream)
    assert not issubclass(Z, WritableStream)



# Generated at 2022-06-12 20:05:36.641770
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A:
        def write(self, s):
            pass

    assert issubclass(A, WritableStream)

# Generated at 2022-06-12 20:05:44.849236
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import os, sys
    import collections
    import tempfile
    import io
    import textwrap
    import contextlib

    class TextIOWrapper(WritableStream):

        def __init__(self, text_io_stream):
            self.text_io_stream = text_io_stream

        def write(self, s):
            return self.text_io_stream.write(s)

    class Queue(collections.deque):

        def write(self, s):
            self.append(s)

    class List(list):

        def write(self, s):
            self.append(s)


# Generated at 2022-06-12 20:05:49.672311
# Unit test for function get_repr_function
def test_get_repr_function():
    assert (
        get_repr_function(None, ((lambda x: x is not None, None),)) is None
    )

# Generated at 2022-06-12 20:05:51.523735
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Class(WritableStream):
        def write(self, s):
            pass

    assert issubclass(Class, WritableStream)
    Class()

# Generated at 2022-06-12 20:05:53.854130
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class WritableStreamSubclass(WritableStream):
        def write(self, s):
            pass

    assert issubclass(WritableStreamSubclass, WritableStream)

# Generated at 2022-06-12 20:06:02.899011
# Unit test for function get_repr_function
def test_get_repr_function():

    # Make sure we can handle tuples and classes
    assert get_repr_function((), [(tuple, 'tuple_repr')]) == 'tuple_repr'
    assert get_repr_function((), [(list, 'list_repr')]) == repr

    # Make sure we run the last chosen repr when multiple reprs are applicable
    assert get_repr_function((), [(list, 'list_repr'), (tuple, 'tuple_repr')]) == 'tuple_repr'

    # Make sure we can handle non-class conditions
    assert get_repr_function(1, [(lambda x: x==1, 'x==1_repr')]) == 'x==1_repr'

# Generated at 2022-06-12 20:06:11.650340
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, []) is repr
    assert str(get_repr_function('', [])) == '<built-in function repr>'
    assert get_repr_function(1, [(int, str)]) is str
    assert get_repr_function(1.5, [(int, str)]) is repr
    assert get_repr_function(1.5, [(float, str)]) is str

    assert get_repr_function(
        'foo',
        [
            (lambda x: len(x) > 1, lambda x: '>1'),
            (lambda x: len(x) < 2, lambda x: '<2'),
            (lambda x: len(x) == 2, lambda x: '==2'),
        ]
    ) == '>1'

    assert get_re

# Generated at 2022-06-12 20:06:18.730527
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function('a', ())('a') == "'a'"
    assert get_repr_function('a', ((str, str),))('a') == "'a'"
    assert get_repr_function(1, ((str, str),))(1) == '1'



# Generated at 2022-06-12 20:06:20.795435
# Unit test for function get_repr_function
def test_get_repr_function():
    def f(x):
        return x + 1
    assert get_repr_function(2, custom_repr=((lambda x: True, f))) == f



# Generated at 2022-06-12 20:06:28.057930
# Unit test for function get_repr_function
def test_get_repr_function():
    from .let import let

    assert get_repr_function(None, []) is repr

    def my_repr(x):
        return 'my_repr({})'.format(repr(x))

    one = let(1)
    assert get_repr_function(one, [(int, my_repr)]) is my_repr

    assert get_repr_function(int, [(int, my_repr)]) is repr
    assert get_repr_function(int, [(int, None), (int, my_repr)]) is my_repr

    def class_based_repr(x):
        return 'class_based_repr({})'.format(repr(x))

    def my_lambda(x):
        return 'my_lambda({})'.format(repr(x))


# Generated at 2022-06-12 20:06:34.084054
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(3, ()) is repr
    assert get_repr_function(3, ((type(3), lambda x: '42!'))) == '42!'
    assert get_repr_function(3, ((lambda x: True, lambda x: '42!'))) == '42!'

    import fractions
    assert get_repr_function(fractions.Fraction(1, 2), (
        (type(3), lambda x: '42!'),
        (lambda x: isinstance(x, fractions.Fraction),
                                                     str)
    )) == '1/2'

    assert get_repr_function(fractions.Fraction(1, 2), (
        (type(3), lambda x: '42!'),
    )) == '42!'





# Generated at 2022-06-12 20:06:39.218655
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class SubclassOfWritableStream(WritableStream):
        def write(self, s):
            pass
    assert issubclass(SubclassOfWritableStream, WritableStream)
    assert issubclass(SubclassOfWritableStream, WritableStream)
    assert not issubclass(str, WritableStream)



# Generated at 2022-06-12 20:06:48.688904
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    from collections import namedtuple
    try:
        import threading
    except ImportError:
        threading = None

    class MockThreading(object):
        class Lock():
            def __init__(self):
                self.acquired = False
            def acquire(self):
                assert not self.acquired
                self.acquired = True
            def release(self):
                assert self.acquired
                self.acquired = False
        Lock = Lock

    class FileLike(object):
        def __init__(self):
            self.data = []

        def write(self, s):
            self.data.append(s)

    class FileLikeThreadSafe(object):
        def __init__(self):
            self.data = []
            if threading:
                self.lock = threading.Lock()

# Generated at 2022-06-12 20:06:54.216220
# Unit test for function get_repr_function
def test_get_repr_function():

    custom_repr = [
        (lambda x: hasattr(x, 'foo'), lambda x: 'bar')
    ]

    class Foo(object):
        def __init__(self):
            self.foo = 'foo'

    assert get_repr_function(Foo(), custom_repr)('hello') == 'hello'
    assert get_repr_function(Foo(), custom_repr)(Foo()) == 'bar'
    assert get_repr_function(Foo(), custom_repr)(Foo().foo) == 'foo'



# Generated at 2022-06-12 20:06:55.965957
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A:
        def write(self, s):
            pass
    assert issubclass(A, WritableStream)



# Generated at 2022-06-12 20:07:03.927001
# Unit test for function get_repr_function
def test_get_repr_function():
    # type: () -> None

    class MyObj(object):
        pass

    class MyObjChild(MyObj):
        pass

    obj = MyObjChild()

    assert get_repr_function(obj, ((str, 'foo'), (MyObj, 'bar'))) == 'foo'
    assert get_repr_function(obj, ((int, 'foo'), (MyObj, 'bar'))) == 'bar'
    assert get_repr_function(obj, ((int, 'foo'), (MyObj, 'bar'),
                                   (lambda x: True, 'baz'))) == 'baz'



# Generated at 2022-06-12 20:07:07.910044
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def write(self, s):
            pass
    MyWritableStream().write('')
    MyWritableStream().write(u'')
    MyWritableStream.__subclasshook__(MyWritableStream)



# Generated at 2022-06-12 20:07:15.572543
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class DummyWritableStream(WritableStream):
        def write(self, s):
            print(s)

    dummy = DummyWritableStream()
    dummy.write('hi')



# Generated at 2022-06-12 20:07:26.946527
# Unit test for function get_repr_function
def test_get_repr_function():
    class SomeClass(object):
        def __repr__(self):
            return 'SomeClass()'

    class SomeOtherClass(SomeClass):
        def __repr__(self):
            return 'SomeOtherClass()'

    class SomeOtherOtherClass(SomeClass):
        def __repr__(self):
            return 'SomeOtherOtherClass()'

    class SomeSubclass(SomeClass):
        pass

    class SomeSubclassOfSomeOtherClass(SomeOtherClass):
        pass

    def some_repr(x):
        return 'some_repr({})'.format(x)

    assert get_repr_function(object(), ()) == repr
    assert get_repr_function('some string', ()) == repr
    assert get_repr_function(SomeClass(), ()) == repr

# Generated at 2022-06-12 20:07:36.639321
# Unit test for function get_repr_function
def test_get_repr_function():
    from pytest import raises

    from . import example_object
    e = example_object.ExampleObject

    assert get_repr_function('', ()) == repr
    assert get_repr_function('', ((bool, str),)) == str
    assert get_repr_function('', ((lambda x: False, str),)) == repr
    assert get_repr_function('', ((type(None), str),)) == repr

    assert get_repr_function(True, ((bool, str),)) == str
    assert get_repr_function(False, ((bool, str),)) == str
    assert get_repr_function(None, ((bool, str),)) == repr

    assert get_repr_function(e, ((bool, str),)) == repr

# Generated at 2022-06-12 20:07:41.926214
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io

    def write_to_stdout(something):
        sys.stdout.write(something)

    assert issubclass(io.StringIO, WritableStream)
    assert not hasattr(sys.stdout, 'write')
    assert not issubclass(object, WritableStream)
    assert not issubclass(list, WritableStream)
    assert issubclass(object, WritableStream)


if __name__ == '__main__':
    test_WritableStream_write()

# Generated at 2022-06-12 20:07:43.960456
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(WritableStream):
        pass
    assert isinstance(A(), WritableStream)
    assert not isinstance(float, WritableStream)

# Generated at 2022-06-12 20:07:53.241036
# Unit test for function get_repr_function
def test_get_repr_function():
    class Foo: pass

    class TheAnswer(int):
        def __repr__(self):
            return 'the answer'

    assert get_repr_function(object(), []) is repr
    assert get_repr_function(Foo(), [(Foo, lambda x: 'yes')]) == 'yes'

    assert get_repr_function(42, [(Foo, lambda x: 'yes')]) == repr
    assert get_repr_function(TheAnswer(42), []) == 'the answer'
    assert get_repr_function(TheAnswer(42), [(int, lambda x: 'no')]) == 'no'



# Generated at 2022-06-12 20:08:03.097279
# Unit test for function get_repr_function
def test_get_repr_function():

    for item, expected_output in (
                                ([], '[]'),
                                ((), '()'),
                                ({}, '{}'),
                                (1, '1'),
                                (1.5, '1.5'),
                                ('hello', "'hello'"),
                                (slice(1, 2), 'slice(1, 2, None)'),
                                (slice(1, 2, 3), 'slice(1, 2, 3)'),
                                ):
        assert get_repr_function(item, custom_repr=()) == expected_output

    class MyClass(object):
        pass
    assert (get_repr_function(
        MyClass(), custom_repr=((MyClass, lambda obj: 'foo'),)
    ) == 'foo')


# Generated at 2022-06-12 20:08:11.203106
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(None) == 'None'
    assert get_shortish_repr(3) == '3'
    assert get_shortish_repr('a' * 100) == 'a' * 100
    assert get_shortish_repr('a' * 100, max_length=10) == 'aaaaaaaaaa...'
    assert get_shortish_repr('a' * 100, max_length=20) == 'aaaaaaaaaaaaaaaaaa...'
    assert get_shortish_repr('a' * 100, max_length=100) == 'a' * 100
    assert get_shortish_repr('a' * 100, max_length=101) == 'a' * 100

    custom_repr = [(lambda item: item == 3, (lambda item: '3?')),]
    assert get

# Generated at 2022-06-12 20:08:15.037182
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function([1, 2, 3], ()) is repr
    assert get_repr_function(1, ((int, id),)) == id
    assert get_repr_function(
        [1, 2, 3],
        ((list, sorted),)
    ) == sorted

# Generated at 2022-06-12 20:08:21.810969
# Unit test for function get_repr_function
def test_get_repr_function():
    from .test_python_toolbox import assert_equal
    assert_equal(
        get_repr_function(1, ()),
        repr
    )
    assert_equal(
        get_repr_function(2.7, ((lambda x: True, lambda x: 'qa'))),
        lambda x: 'qa'
    )
    assert_equal(
        get_repr_function(3, ((int, lambda x: 'q'))),
        lambda x: 'q'
    )
    assert_equal(
        get_repr_function(4.1, ((int, lambda x: 'qa'))),
        repr
    )





# Generated at 2022-06-12 20:08:42.454610
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    from .temp_file_tools import make_temp_file, with_temp_file
    from .cross_version import print_, flush_stdout_stdin_stderr

    def inner(f):
        with f.open('wb') as fp:
            class WritableStreamThrowingIOError(WritableStream):
                def write(self, s):
                    raise IOError()
            class WritableStreamThatWorks(WritableStream):
                def write(self, s):
                    fp.write(s.encode('utf-8'))
            class WritableStreamThrowingValueError(WritableStream):
                def write(self, s):
                    raise ValueError()
            class WritableStreamThrowingKeyboardInterrupt(WritableStream):
                def write(self, s):
                    raise KeyboardInterrupt()