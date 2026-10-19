

# Generated at 2022-06-12 19:58:37.868831
# Unit test for function shitcode
def test_shitcode():
    def assert_shitcode(s, expected_shitcode):
        assert shitcode(s) == expected_shitcode

    assert_shitcode('abcäåèæ', 'abc????')
    assert_shitcode('øªƒ', '???')
    assert_shitcode('ÉÉÉ', '???É')

# Generated at 2022-06-12 19:58:41.547626
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class Dummy(WritableStream):
        def write(self, s):
            pass

    assert isinstance(Dummy(), WritableStream)

    class NotDummy(Dummy):
        pass

    assert not isinstance(NotDummy(), WritableStream)

    class AlsoDummy(WritableStream):
        def write(self, s):
            pass
        def foo(self):
            pass

    assert isinstance(AlsoDummy(), WritableStream)

# Generated at 2022-06-12 19:58:44.375410
# Unit test for function shitcode
def test_shitcode():
    assert shitcode(u'abc') == u'abc'
    assert shitcode(u'abc\n\r') == u'abc\n\r'
    assert shitcode(u'abc\u135cdef') == u'abc?def'
    assert shitcode(u'\xab\xcd\xef') == u'\xab\xcd\xef'



# Generated at 2022-06-12 19:58:52.661474
# Unit test for function get_repr_function
def test_get_repr_function():
    class MyClass:
        pass
    class MyClass2(MyClass):
        pass

    my_class = MyClass()
    my_class2 = MyClass2()
    assert get_repr_function(my_class, ()) == repr
    assert get_repr_function(my_class2, ()) == repr
    assert get_repr_function(my_class, [(MyClass, lambda x: 'the repr')]) == repr
    assert get_repr_function(my_class, [(MyClass2, lambda x: 'the repr')]) == repr
    assert get_repr_function(my_class2, [(MyClass, lambda x: 'the repr')]) == repr

# Generated at 2022-06-12 19:59:02.305221
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(3) == '3'
    assert get_shortish_repr('abc', max_length=2) == 'ab'
    assert get_shortish_repr('abc', max_length=3) == 'abc'
    assert get_shortish_repr('abc', max_length=4) == 'abc'
    assert get_shortish_repr('abc', max_length=5) == 'abc'
    assert get_shortish_repr('abc', max_length=6) == 'abc'
    assert get_shortish_repr('abc', max_length=7) == 'abc'
    assert get_shortish_repr('abc', max_length=8) == 'abc'

# Generated at 2022-06-12 19:59:09.996346
# Unit test for function get_repr_function
def test_get_repr_function():
    class A: pass
    class B: pass
    a = A()
    b = B()
    custom_repr = (
        (A, lambda x: 'A!'),
        (lambda item: isinstance(item, int), lambda x: 'ITS INT')
    )
    assert get_repr_function(a, custom_repr)() == 'A!'
    assert get_repr_function(b, custom_repr)() == repr(b)
    assert get_repr_function(4, custom_repr) == 'ITS INT'



# Generated at 2022-06-12 19:59:15.148801
# Unit test for function shitcode
def test_shitcode():
    assert shitcode('אאאאא') == '????????'
    assert shitcode('hello') == 'hello'
    assert shitcode('hello\nworld') == 'hello\nworld'
    assert shitcode('hello\r\nworld') == 'hello\nworld'
    assert shitcode('hello\nworld\r\n') == 'hello\nworld\n'
    assert shitcode('hello\r\nworld\r\n') == 'hello\nworld\n'

    assert shitcode(chr(0xFFF0)) == '?'
    assert shitcode(chr(0x0FF0)) == chr(0x0FF0)

    # Test unicode invisible character
    assert shitcode(chr(0xFEFF)) == chr(0xFFFD) # Unicode replace char



# Generated at 2022-06-12 19:59:20.227243
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(WritableStream):
        def write(self, s):
            assert False

    class B(WritableStream):
        def write(self, s):
            pass

    assert not issubclass(A, WritableStream)
    assert issubclass(B, WritableStream)

# Generated at 2022-06-12 19:59:29.427693
# Unit test for function get_repr_function
def test_get_repr_function():
    from .datastructuretools import SmartTuple
    from .magic_methods import Null
    assert get_repr_function(SmartTuple(1, 2, 3), ()) == SmartTuple.__repr__
    assert get_repr_function(1, ()) == repr
    assert get_repr_function(int, ((type, 1), (type, 1.0))) == repr

# Generated at 2022-06-12 19:59:34.411854
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(
        [1, 2, 3], ()
    ) is repr
    assert get_repr_function(
        [1, 2, 3], ((list, lambda x: 'list object' + str(id(x))))
    ) == 'list object' + str(id([]))
    assert get_repr_function(
        [1, 2, 3], ((list, lambda x: 'list object' + str(id(x))), (tuple,
                                                                             tuple.__repr__))
    ) == list.__repr__([])





# Generated at 2022-06-12 19:59:41.044014
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    repr_function = get_repr_function(1)
    assert repr_function(1) == '1'
    repr_function = get_repr_function(1, custom_repr=[(int, lambda x: '*')])
    assert repr_function(1) == '*'



# Generated at 2022-06-12 19:59:42.407490
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    f = sys.stdout
    print('foo', file=f)
    assert isinstance(f, WritableStream)

# Generated at 2022-06-12 19:59:51.949243
# Unit test for function shitcode
def test_shitcode():
    assert shitcode('bar \xff') == 'bar ?'
    assert shitcode('bar \xffff') == 'bar ??'
    assert shitcode('bar \xffff\xff') == 'bar ???\xff'
    assert shitcode('\x00') == '\x00'
    assert shitcode('\x01') == '\x01'
    assert shitcode('\xff') == '\xff'
    assert shitcode(u'\x00') == '\x00'
    assert shitcode(u'\x01') == '\x01'
    assert shitcode(u'\xff') == '\xff'
    assert shitcode(u'\u2345') == '\u2345'
    assert shitcode('\x80') == '\x80'
    assert shitcode(u'\u2345\xff')

# Generated at 2022-06-12 19:59:56.609002
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def __init__(self):
            self.output = ''

        def write(self, s):
            self.output += s

    wstream = MyWritableStream()
    wstream.write('Zeppeli')
    assert wstream.output == 'Zeppeli'



# Generated at 2022-06-12 20:00:07.837328
# Unit test for function get_repr_function
def test_get_repr_function():
    import re
    import numbers
    class A(object):
        pass

    class B(object):
        pass

    class C(A):
        pass

    class D(B):
        pass

    class E(C, D):
        pass

    a = A()
    c = C()
    d = D()
    e = E()

    custom_repr = [
        (A, lambda x: 'A'),
        (D, lambda x: 'D'),
        (re.Match, lambda x: 'match'),
        (lambda x: isinstance(x, numbers.Number) and x % 2 == 0,
         lambda x: 'even'),
        (lambda x: isinstance(x, numbers.Number) and x % 2 == 1,
         lambda x: 'odd'),
    ]

    repr_function = get_repr

# Generated at 2022-06-12 20:00:11.715320
# Unit test for function get_repr_function
def test_get_repr_function():
    from .hints import int_repr
    assert get_repr_function(1, custom_repr=[(int, int_repr)]) is int_repr
    assert get_repr_function(1.0, []) is repr
    assert get_repr_function(1, custom_repr=[(float, int_repr)]) is repr

# Generated at 2022-06-12 20:00:15.164419
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function('abc', ((str, str), (type(None), None))) is str
    assert get_repr_function(None, ((str, str), (type(None), None))) is None

# Generated at 2022-06-12 20:00:20.597355
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(5, custom_repr=[(lambda x: True, lambda x: 49)]) \
                                                                       == 49
    assert get_repr_function(
        5, custom_repr=[(lambda x: False, lambda x: 49)]
    ) == repr



# Generated at 2022-06-12 20:00:26.361021
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Logger(WritableStream):
        def __init__(self):
            self.messages = set()

        def write(self, message):
            self.messages.add(message)

    logger = Logger()
    logger.write('hi')
    assert len(logger.messages) == 1
    assert 'hi' in logger.messages



# Generated at 2022-06-12 20:00:33.518000
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    custom_repr = (
        (lambda x: isinstance(x, tuple), lambda x: 'tuple!'),
        (lambda x: isinstance(x, dict), lambda x: 'dict!'),
    )

    assert get_shortish_repr(3, custom_repr=custom_repr) == '3'
    assert get_shortish_repr((3, 4), custom_repr=custom_repr) == 'tuple!'
    assert get_shortish_repr({3, 4}, custom_repr=custom_repr) == "{3, 4}"


# Generated at 2022-06-12 20:00:47.825884
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(1) == '1'
    assert get_shortish_repr('Hello') == 'Hello'
    assert get_shortish_repr('Hello', max_length=2) == 'He...'
    assert get_shortish_repr('Hello', max_length=3) == 'Hel...'
    assert get_shortish_repr('Hello', max_length=4) == 'Hell...'
    assert get_shortish_repr('Hello', max_length=5) == 'Hello'

    def my_repr(x):
        return 'my_repr({})'.format(x)

    bad_repr = (1, my_repr)

    assert get_shortish_repr('foo', custom_repr=bad_repr) == \
                                                  get_

# Generated at 2022-06-12 20:00:54.783765
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(object) == repr

# Generated at 2022-06-12 20:01:04.590592
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('1234567', max_length=4) == '123...'
    assert get_shortish_repr('1234567', max_length=5) == '12345'
    assert get_shortish_repr('1234567', max_length=6) == '12345...'
    assert get_shortish_repr('1234567', max_length=7) == '1234567'
    assert get_shortish_repr('1234567', max_length=8) == '1234567'
    assert get_shortish_repr('1234567', max_length=9) == '1234567'

    assert get_shortish_repr('12345678', max_length=4) == '1...'

# Generated at 2022-06-12 20:01:08.664210
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(123, max_length=None) == '123'
    assert get_shortish_repr(123, max_length=10) == '123'
    assert get_shortish_repr(123, max_length=3) == '123'

    assert get_shortish_repr(123, max_length=2) == '1...'
    assert get_shortish_repr(123, max_length=1) == '...'
    assert get_shortish_repr(123, max_length=0) == '...'

    assert get_shortish_repr('hello', max_length=4) == 'h...'

# Generated at 2022-06-12 20:01:14.819053
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class Test(WritableStream):

        def __init__(self, capture):
            self.capture = capture

        def write(self, s):
            self.capture.append(s)

    capture = []
    test = Test(capture)
    test.write('yo')
    assert capture == ['yo']

# Generated at 2022-06-12 20:01:20.764028
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(object(), max_length=3) == 'REPR FAILED'
    assert get_shortish_repr(object(), max_length=6) == 'REPR FAILED'
    assert get_shortish_repr(object(), max_length=7) == 'REPR FAILED'

    try:
        get_shortish_repr(object(), max_length=-1)
        assert False
    except AssertionError:
        pass

    assert get_shortish_repr(object()) == '<object object at 0x...>'
    assert get_shortish_repr(object(), max_length=None) == \
                                                 '<object object at 0x...>'

# Generated at 2022-06-12 20:01:30.634071
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(2, [(lambda x: True, id)]) == id
    assert get_repr_function(2, []) == repr
    assert get_repr_function(2, [(int, id)]) == id
    assert get_repr_function(2.0, [(int, id)]) == repr
    assert get_repr_function(2, [(int, id), (float, str)]) == id
    assert get_repr_function(2.0, [(int, id), (float, str)]) == str
    assert get_repr_function(2.0, [(int, id), (lambda x: True, str)]) == str
    assert get_repr_function(2.0, [(int, id), (None, str)]) == str



# Generated at 2022-06-12 20:01:37.281937
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    from .testing.test_lazy_repr import get_shortish_repr
    from .testing import (assert_equal, assert_same)

    a = 'a' * 10
    assert_equal(get_shortish_repr(a), a)
    assert_equal(get_shortish_repr(a, (str, str)), a)
    assert_equal(get_shortish_repr(a, [(str, 2, str)]), a)
    assert_equal(get_shortish_repr(a, [(str, 3, str)]), 'aaa...aaa')

    a = 'a'
    assert_equal(get_shortish_repr(a), a)
    assert_equal(get_shortish_repr(a, (str, str)), a)

# Generated at 2022-06-12 20:01:41.510759
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    # Try write on a file-like object:
    WritableStream.register(file)
    assert isinstance(sys.stdout, WritableStream)

    # Try write on a non-filelike object:
    WritableStream.register(str)
    assert not isinstance('bla', WritableStream)

# Generated at 2022-06-12 20:01:46.794804
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert truncate('abcdefghijklmnoprstuvwxyz', max_length=20) == \
                                                           'abcdefghijklmnoprs...'
    assert truncate('abcdefghijklmnoprstu', max_length=20) == \
                                                           'abcdefghijklmnoprstu'
    assert truncate('abcdefghijklmnoprstuvwxyz', max_length=6) == \
                                                                 'abc...'

# Generated at 2022-06-12 20:01:55.795389
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Logger(WritableStream):
        def __init__(self):
            self.lines = []
        def write(self, s):
            self.lines.append(s)
    logger = Logger()
    assert (logger.lines == [])
    logger.write('hello')
    assert (logger.lines == ['hello'])

# Generated at 2022-06-12 20:01:59.054881
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def write(self, s):
            self.written_string = s

    my_writable_stream = MyWritableStream()
    my_writable_stream.write('hi')
    assert my_writable_stream.written_string == 'hi'

# Generated at 2022-06-12 20:02:05.837120
# Unit test for function get_repr_function
def test_get_repr_function():

    assert get_repr_function(None) == repr
    assert get_repr_function(1) == repr
    assert get_repr_function(True) == repr
    assert get_repr_function(4.5) == repr
    assert get_repr_function('a') == repr
    assert get_repr_function((1, 2, 3)) == repr
    assert get_repr_function(set((1, 2, 3))) == repr
    assert get_repr_function({1: 2, 3: 4}) == repr


    class Thing: pass
    instance = Thing()
    assert get_repr_function(instance) == repr

    class Thing:
        def __repr__(self):
            return '<reprred>'

    instance = Thing()
    assert get_repr_function(instance)

# Generated at 2022-06-12 20:02:13.279371
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('#' * 100, max_length=5) == u'#####...#####'
    assert get_shortish_repr('#' * 100, max_length=None) == u'#' * 100
    assert get_shortish_repr('#' * 100, max_length=50) == u'#' * 100
    assert get_shortish_repr('#' * 100, max_length=101) == u'#' * 100
    assert get_shortish_repr('#' * (101), max_length=100) == u'#####...#####'



# Generated at 2022-06-12 20:02:15.581898
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Foo:
        def write(self, s):
            pass

    foo = Foo()
    assert isinstance(foo, WritableStream)



# Generated at 2022-06-12 20:02:20.026952
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class WritableStreamImpl(object):
        def __init__(self):
            self.text = ''
        def write(self, s):
            self.text += s
    writable_stream_impl = WritableStreamImpl()
    assert isinstance(writable_stream_impl, WritableStream)
    writable_stream_impl.write('hello')
    writable_stream_impl.write('there')
    assert writable_stream_impl.text == 'hellothere'



# Generated at 2022-06-12 20:02:29.990893
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    items = [
        lambda: (1,),
        lambda: [1],
        lambda: {1},
        lambda: {1: 2},
        lambda: str(1),
        lambda: int(1),
        lambda: float(1),
        lambda: object(),
        lambda: object(),
        lambda: object(),
    ]

# Generated at 2022-06-12 20:02:39.003633
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('hi') == "'hi'"
    assert get_shortish_repr(custom_repr=[(lambda x: True, lambda x: 'yo')]) == 'yo'
    assert get_shortish_repr(1, max_length=5) == '1'
    assert get_shortish_repr([1, 2, 3], max_length=6) == '[1, 2]'
    assert get_shortish_repr([1, 2, 3], max_length=5) == '[...]'
    assert get_shortish_repr(3, max_length=1) == '...'
    assert get_shortish_repr(3, max_length=0) == '...'

# Generated at 2022-06-12 20:02:47.598721
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyStream(WritableStream):
        def __init__(self):
            self.written_lines = []
        def write(self, s):
            self.written_lines.extend(s.splitlines(True))

    stream = MyStream()

    assert isinstance(stream, WritableStream)

    stream.write('This is a test')

    assert stream.written_lines == ['This is a test']

    assert len(stream.__class__.__mro__) == 2
    assert stream.__class__.__mro__[0] == MyStream
    assert stream.__class__.__mro__[1] == object
    assert stream.__class__.__mro__[1].__class__ == type

    class MyStream(object):
        def write(self, s):
            self.written_lines

# Generated at 2022-06-12 20:02:57.367608
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(WritableStream):
        pass
    assert isinstance(A, ABC)
    assert issubclass(A, WritableStream)

    class B(WritableStream):
        def write(self, s):
            pass
    assert issubclass(B, WritableStream)

    class C(WritableStream):
        def write(self, s):
            pass
    assert issubclass(C, WritableStream)
    assert not issubclass(C, B)

    class D(B):
        def something_else(self):
            pass
    assert issubclass(D, WritableStream)
    assert issubclass(D, B)
    assert not issubclass(D, C)

    class E(B):
        def write(self):
            pass

# Generated at 2022-06-12 20:03:07.316953
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(2, ()) is repr
    assert get_repr_function((1, 2, 3), ()) is repr
    assert get_repr_function(
        [2, 3, 4],
        (
            (lambda x: isinstance(x, tuple), lambda x: 'tuple!'),
            (lambda x: True, lambda x: 'silly'),
        )
    ) == 'silly'
    assert get_repr_function(
        (2, 3, 4),
        (
            (lambda x: isinstance(x, tuple), lambda x: 'tuple!'),
            (lambda x: True, lambda x: 'silly'),
        )
    ) == 'tuple!'
    assert get_repr_function('spam', ()) is repr

# Generated at 2022-06-12 20:03:13.699379
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class WritableStreamImpl(WritableStream):

        def __init__(self):
            self.written = []

        def write(self, s):
            self.written.append(s)

    ws = WritableStreamImpl()
    ws.write('abc')
    assert ws.written == ['abc']



# Generated at 2022-06-12 20:03:23.529552
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class TestStream(WritableStream):
        def write(self, s):
            if isinstance(s, bytes):
                decoded = s.decode()
            else:
                decoded = s
            if decoded == 'fail':
                raise IOError()
            else:
                sys.stdout.write(decoded)

    stream = TestStream()
    # Fails:
    for write_type in (list, dict, set, frozenset, range, tuple):
        try:
            stream.write(write_type(range(10)))
            raise Exception('Should have raised TypeError')
        except TypeError:
            pass
    # Works:
    for write_type in (bytes, bytearray, memoryview, str):
        stream.write(write_type(b'hello world'))

# Generated at 2022-06-12 20:03:32.634421
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('abc', max_length=4) == 'abc'
    assert get_shortish_repr('abcde', max_length=4) == 'a...e'
    assert get_shortish_repr('ab', max_length=4) == 'ab'
    assert get_shortish_repr('abcde', max_length=2) == 'a...'
    assert get_shortish_repr('abcde', max_length=1) == '...'
    assert get_shortish_repr('abcde', max_length=0) == '...'
    assert get_shortish_repr('abcde', max_length=-1) == '...'
    assert get_shortish_repr('abcde', max_length=None) == 'abcde'
    assert get_short

# Generated at 2022-06-12 20:03:43.296186
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert normalize_repr('hello world') == 'hello world'
    assert normalize_repr('hello world at 0x12345') == 'hello world'
    assert normalize_repr('hello world at 0x1234567890abc') == 'hello world'
    assert normalize_repr('hello world at 0x1234567890abcde') == \
                                                               'hello world'
    assert normalize_repr('hello world at 0x1234567890abcdef') == \
                                                               'hello world'


    assert get_shortish_repr('c' * 50) == repr('c' * 50)
    assert get_shortish_repr('c' * 50, max_length=10) == truncate(repr('c' * 50), 10)


# Generated at 2022-06-12 20:03:50.214976
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(WritableStream):
        def write(self, s): pass

    assert issubclass(A, WritableStream)

    class B(A): pass

    assert issubclass(B, WritableStream)

    class C(B):
        def write(self, s): pass

    assert issubclass(C, WritableStream)

    class D(C): pass

    assert issubclass(D, WritableStream)

    class D2(C):
        def write(self, s):
            pass

    assert issubclass(D2, WritableStream)

    class E(B):
        def write(self, s):
            pass

    assert issubclass(E, WritableStream)

    class F(B): pass

    assert not issubclass(F, WritableStream)


# Generated at 2022-06-12 20:03:55.029207
# Unit test for function get_repr_function
def test_get_repr_function():

    assert get_repr_function(1, custom_repr=((int, str),)) == str
    assert get_repr_function(1.0, custom_repr=((int, str),)) == repr
    assert get_repr_function(1.0, custom_repr=((int, str),) + repr_specs) == str



default_encoding = 'UTF-8'


# Generated at 2022-06-12 20:03:56.740943
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class FakeFile:
        def write(self, s):
            return

    stream = FakeFile()

    assert issubclass(FakeFile, WritableStream)
    assert isinstance(stream, WritableStream)

# Generated at 2022-06-12 20:03:58.891373
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyStream(WritableStream):
        def write(self, s):
            return s

    assert isinstance(MyStream(), WritableStream)



# Generated at 2022-06-12 20:04:04.218780
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Foo:
        def write(self, s):
            pass
        def write_foo(self, s):
            pass
    for i in (Foo(), object()):
        WritableStream.register(i.__class__)
        assert issubclass(i.__class__, WritableStream)
        assert isinstance(i, WritableStream)


if __name__ == '__main__':
    test_WritableStream_write()

# Generated at 2022-06-12 20:04:17.774337
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(u'asdf') == u"u'asdf'"
    assert get_shortish_repr(u'asdf', max_length=2) == u"u'as..."
    assert get_shortish_repr(u'asdf', max_length=2, normalize=True) == u"'as..."
    assert get_shortish_repr(u'asdf', max_length=3) == u"u'asd'"
    assert get_shortish_repr(u'asdf', max_length=3, normalize=True) == u"'asd'"
    assert get_shortish_repr(u'asdf', max_length=4) == u"u'asdf'"

# Generated at 2022-06-12 20:04:27.073186
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('meow') == "'meow'"
    assert get_shortish_repr('meow', max_length=3) == "'me...'"
    assert get_shortish_repr('meow', max_length=4) == "'meo...'"
    assert get_shortish_repr('meow', max_length=5) == "'meow'"
    assert get_shortish_repr('meow', max_length=6) == "'meow'"
    assert get_shortish_repr(['meow'], max_length=5) == "['meow']"
    assert get_shortish_repr(['meow'], max_length=8) == "['meow']"
    assert get_shortish_repr(['meow'], max_length=9)

# Generated at 2022-06-12 20:04:34.317866
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    from .python_toolbox import sequence_tools
    assert get_shortish_repr((1, 2, 3), max_length=10) == '(1, 2...'
    assert get_shortish_repr((1, 2, 3), max_length=None) == '(1, 2, 3)'
    assert get_shortish_repr((1, 2, 3), max_length=0) == '...'
    assert get_shortish_repr((1, 2, 3), max_length=2) == '...'
    assert get_shortish_repr((1, 2, 3), max_length=-1) == '...'
    assert get_shortish_repr('some string', max_length=None) == "'some string'"

# Generated at 2022-06-12 20:04:45.127100
# Unit test for function get_shortish_repr
def test_get_shortish_repr():

    class T(object):

        def __repr__(self):
            return 'This string is long'

    class S(object):

        def __repr__(self):
            return 'This is short'

    assert get_shortish_repr(T()) == 'This string is long'
    assert get_shortish_repr(T(), max_length=10) == 'This stri...g'
    assert get_shortish_repr(T(), max_length=None) == 'This string is long'
    assert get_shortish_repr(T(), max_length=100) == 'This string is long'
    assert get_shortish_repr(T(), max_length=21) == 'This string is long'

# Generated at 2022-06-12 20:04:52.455260
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        pass
    try:
        WritableStream.register(MyWritableStream)
    except:
        pass
    else:
        assert issubclass(MyWritableStream, WritableStream)
    class MyWritableStream:
        def write(self, s):
            pass
    try:
        WritableStream.register(MyWritableStream)
    except:
        pass
    else:
        assert issubclass(MyWritableStream, WritableStream)

if __name__ == '__main__':
    test_WritableStream_write()

# Generated at 2022-06-12 20:04:56.616461
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(['hi', 'there'], max_length=5) == "[...]"
    assert get_shortish_repr(['hi', 'there'], max_length=20) == "['hi', 'there']"




# Generated at 2022-06-12 20:05:07.213758
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    from .testing.mock import Mock, mock_me
    assert get_shortish_repr('hello') == "'hello'"
    assert get_shortish_repr('hello', max_length=10) == "'hello'"
    assert get_shortish_repr('hello', max_length=5) == "'hel...'"

    class A(object):
        def __repr__(self):
            return 'A=10'

    assert get_shortish_repr(A(), max_length=3) == "'A=10'"

    class B(object):
        def __repr__(self):
            return 'B=10'

    assert get_shortish_repr(B(), max_length=8, custom_repr=((A, lambda x: 'A'),))\
        == "'A=10'"
    assert get

# Generated at 2022-06-12 20:05:14.753821
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A:
        def write(self, s):
            pass

    class A2:
        def write(self):
            pass

    class B:
        pass

    class B2:
        def write(self, s, t):
            pass

    assert WritableStream.__subclasshook__(A) is True
    assert WritableStream.__subclasshook__(A2) is NotImplemented
    assert WritableStream.__subclasshook__(B) is NotImplemented
    assert WritableStream.__subclasshook__(B2) is NotImplemented

# Generated at 2022-06-12 20:05:21.985484
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(u'hello', max_length=4) == u'hell...'
    assert get_shortish_repr(u'hello', max_length=5) == u'hello'
    assert get_shortish_repr(u'hello', max_length=6) == u'hello'
    assert get_shortish_repr(u'hello', max_length=7) == u'hello'
    assert get_shortish_repr(u'hello', max_length=8) == u'hello'
    assert get_shortish_repr(u'hello', max_length=9) == u'hello'
    assert get_shortish_repr(u'hello', max_length=17) == u'hello'

# Generated at 2022-06-12 20:05:26.925262
# Unit test for function get_repr_function
def test_get_repr_function():
    from .abc import CustomType
    from .abc import CustomInstance
    from .abc import CustomOtherInstance

    assert get_repr_function(3, custom_repr=((CustomType, str),)) is str

    assert get_repr_function(
        CustomInstance(),
        custom_repr=((CustomType, str),)
    ) is str

    assert get_repr_function(
        CustomOtherInstance(),
        custom_repr=((CustomType, str),)
    ) is repr

    assert get_repr_function(
        CustomInstance(),
        custom_repr=((lambda x: x.magic_number == 2, str),)
    ) is repr


# Generated at 2022-06-12 20:05:43.750181
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(int, custom_repr=[(int, None)]) is None
    assert get_repr_function(int, custom_repr=[(int, lambda _: 'Yay')])() == 'Yay'
    assert get_repr_function(int, custom_repr=[(str, 'Yay')])() == 'Yay'
    assert get_repr_function(5, custom_repr=[(lambda x: x % 2, 'Yay')]) == \
        'Yay'
    assert get_repr_function(5, custom_repr=[(lambda x: x % 2 == 0, 'Yay')]) == \
        repr



# Generated at 2022-06-12 20:05:53.698243
# Unit test for function get_repr_function
def test_get_repr_function():
    class A: pass
    class B: pass
    a = A()
    b = B()
    assert get_repr_function(a, ((A, None),)) is None
    assert get_repr_function(b, ((A, None),)) == repr
    assert get_repr_function(a, (A, None)) is None
    assert get_repr_function(b, (A, None)) == repr
    assert get_repr_function(a, ((A, 'blah'),)) == 'blah'
    assert get_repr_function(b, ((A, 'blah'),)) == repr
    assert get_repr_function(a, (A, 'blah')) == 'blah'
    assert get_repr_function(b, (A, 'blah')) == repr
    assert get

# Generated at 2022-06-12 20:05:56.793474
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class FakeFile(WritableStream):
        def __init__(self):
            self.s = ''

        def write(self, s):
            self.s += s

    fake_file = FakeFile()
    fake_file.write('abc')
    assert fake_file.s == 'abc'



# Generated at 2022-06-12 20:06:01.246249
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, [])(1) == '1'
    assert get_repr_function(1, [(lambda x: True, lambda x: '123')])(1) == '123'
    assert get_repr_function(1, [(int, lambda x: '123')])(1) == '123'



# Generated at 2022-06-12 20:06:07.008799
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class MockWritableStream(WritableStream):
        def write(self, s):
            pass

    mock_writable_stream = MockWritableStream()
    assert isinstance(mock_writable_stream, WritableStream)

    class MockNonWritableStream(object):
        pass

    mock_non_writable_stream = MockNonWritableStream()
    assert not isinstance(mock_non_writable_stream, WritableStream)

# Generated at 2022-06-12 20:06:14.397407
# Unit test for function get_repr_function
def test_get_repr_function():
    class A(object): pass
    class B(object): pass
    class C(A): pass
    class D(A): pass
    assert get_repr_function(A(), ()) is repr
    assert get_repr_function(A(), ((lambda x: True, lambda x: 'A'))) == 'A'
    assert get_repr_function(A(), ((lambda x: False, lambda x: 'A'),
                                   (lambda x: True, lambda x: 'B'))) == 'B'
    assert get_repr_function(C(), ((A, lambda x: 'A!'))) == 'A!'
    assert get_repr_function(C(), ((D, lambda x: 'A!'))) == repr
    assert get_repr_function(A(), ((A, lambda x: 'A!'))) == 'A!'
    assert get

# Generated at 2022-06-12 20:06:17.829920
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Foo:
        def write(self, s):
            return len(s)
    assert WritableStream.__subclasshook__(Foo) is True



# Generated at 2022-06-12 20:06:25.588663
# Unit test for function get_repr_function
def test_get_repr_function():
    import unittest

    class FooError(Exception):
        pass
    class BarError(FooError):
        pass
    class Foo(object):
        def __repr__(self):
            return 'foo'
    class Bar(object):
        def __repr__(self):
            return 'bar'
    class Baz(object):
        def __repr__(self):
            return 'baz'

    class TestGetReprFunction(unittest.TestCase):
        def test_single_no_condition(self):
            self.assertEqual(
                get_repr_function(Foo(), ((str, lambda x: 'str'),)),
                str
            )
            self.assertEqual(
                get_repr_function(Bar(), ((str, lambda x: 'str'),)),
                str
            )

# Generated at 2022-06-12 20:06:28.663606
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class DummyFile(WritableStream):
        def __init__(self):
            self.content = ''

        def write(self, s):
            self.content += s

    file = DummyFile()
    file.write('hello world')
    assert file.content == 'hello world'

# Generated at 2022-06-12 20:06:39.935804
# Unit test for function get_repr_function
def test_get_repr_function():
    class A: pass
    class B(A): pass
    class C(A): pass
    x = A()
    y = B()
    z = C()

    assert get_repr_function(x, (
        (lambda item: isinstance(item, B), lambda x: 'B'),
        (lambda item: isinstance(item, A), lambda x: 'A'),
    ))(x) == 'A'

    assert get_repr_function(y, (
        (lambda item: isinstance(item, B), lambda x: 'B'),
        (lambda item: isinstance(item, A), lambda x: 'A'),
    ))(x) == 'B'


# Generated at 2022-06-12 20:06:52.419053
# Unit test for function get_repr_function
def test_get_repr_function():
    from . import tests
    from . import my_assertions

    class A: pass
    a = A()

    assert get_repr_function(a) is repr

    assert get_repr_function(a, custom_repr=((A, str),)) is str

    assert get_repr_function(a, custom_repr=((A, lambda x: str(x.__name__)),)) \
                                                                == A.__name__

    assert get_repr_function(a, custom_repr=((A, lambda x: str(x.__name__)),
                                             (object, str))) is str

# Generated at 2022-06-12 20:06:57.957304
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(metaclass=ABCMeta):
        @abc.abstractmethod
        def write(self, s):
            pass

    class B(A):
        pass

    class C(A):
        def write(self, s):
            pass

    class D(C):
        pass

    for x in (A, B, C, D):
        assert issubclass(x, WritableStream)

    class E(object):
        def write(self, s):
            pass

    assert issubclass(E, WritableStream)

    class F(E, C):
        pass

    assert issubclass(F, WritableStream)





if __name__ == '__main__':
    test_WritableStream_write()

# Generated at 2022-06-12 20:07:03.466296
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(3.14) == u'3.14'
    assert get_shortish_repr(3.14, max_length=5) == u'3.14'
    assert get_shortish_repr(3.14, max_length=4) == u'3.1'

    assert get_shortish_repr((1, 2, 3, 4), max_length=9) == u'(1, 2, 3, 4)'
    assert get_shortish_repr((1, 2, 3, 4), max_length=8) == u'(1, 2, 3, 4)'
    assert get_shortish_repr((1, 2, 3, 4), max_length=7) == u'(1, 2, ...)'

# Generated at 2022-06-12 20:07:13.325889
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(1) == '1'
    assert get_shortish_repr(1, max_length=5) == '1'
    assert get_shortish_repr(1, max_length=4) == '1'
    assert get_shortish_repr(1, max_length=3) == '1'
    assert get_shortish_repr(1, max_length=2) == '1'
    assert get_shortish_repr(1, max_length=1) == '1'
    assert get_shortish_repr(1, max_length=0) == '1'
    assert get_shortish_repr(1, max_length=None) == '1'

# Generated at 2022-06-12 20:07:20.130331
# Unit test for function get_repr_function
def test_get_repr_function():
    def assert_Callable(s):
        assert isinstance(s, collections_abc.Callable)
    def assert_NotCallable(s):
        assert not isinstance(s, collections_abc.Callable)

    assert_Callable(get_repr_function(None, []))
    assert_NotCallable(get_repr_function(None, custom_repr=[(None, None)]))
    assert_Callable(get_repr_function(None, custom_repr=[(lambda: True, None)]))
    assert_Callable(get_repr_function([], custom_repr=[(list, None)]))
    assert_Callable(get_repr_function([], custom_repr=[(list, lambda a: a)]))

# Generated at 2022-06-12 20:07:24.048388
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    c = 0
    class Something(WritableStream):
        def write(self, s):
            print(s)
            nonlocal c
            c += 1

    Something().write('hi')
    assert c == 1



# Generated at 2022-06-12 20:07:27.378169
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class TestWritableStream(WritableStream):
        def write(self, s):
            print(s)

    writable_stream = TestWritableStream()
    writable_stream.write('hi')
    assert issubclass(TestWritableStream, WritableStream)
    assert isinstance(writable_stream, WritableStream)




# Generated at 2022-06-12 20:07:31.922699
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, ()) is repr
    assert get_repr_function(1, [(int, str)]) is str
    assert get_repr_function(1, [(lambda x: x == 1, str)]) is str
    assert get_repr_function(1, [(lambda x: x == 2, str)]) is repr
    assert get_repr_function(1, [(lambda x: x == 2, str),
                                 (str, lambda x: x),
                                 (lambda x: x == 1, str)]) is str



# Generated at 2022-06-12 20:07:40.721323
# Unit test for function get_repr_function
def test_get_repr_function():
    import pytest
    from .objects_with_nice_repr import MagicalObject, Spam
    assert get_repr_function(MagicalObject(), [])('') == 'I am magical'
    assert get_repr_function(Spam('foo'), [])('') == 'Spam("foo")'
    assert get_repr_function(MagicalObject(), [])('') == 'I am magical'
    assert get_repr_function(Spam('foo'), [(MagicalObject, lambda z: z.name)]) \
                              ('') == 'foo'
    assert get_repr_function(MagicalObject(), [(MagicalObject, lambda z: z.name)]) \
                              ('') == 'foo'

# Generated at 2022-06-12 20:07:47.873054
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    class A(object):
        def __repr__(self):
            return "A"*150
    class B(object):
        def __repr__(self):
            return "B"*150

    def repr_b(x):
        return 'caca'

    assert get_shortish_repr('aaa') == "aaa"
    assert get_shortish_repr('aaa', max_length=4) == "aaa"
    assert get_shortish_repr('aaa', max_length=3) == "aaa"
    assert get_shortish_repr('aaa', max_length=2) == "a..."
    assert get_shortish_repr('aaa', max_length=1) == "..."
    assert get_shortish_repr('aaa', max_length=0) == "..."


# Generated at 2022-06-12 20:08:03.023901
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('qwerty') == 'qwerty'
    assert get_shortish_repr('qwerty', max_length=10) == 'qwerty'
    assert get_shortish_repr('qwerty', max_length=5) == 'qwert...'
    assert get_shortish_repr('qwerty', max_length=6) == 'qwerty'
    assert get_shortish_repr('qwerty', max_length=4) == 'q...'
    assert get_shortish_repr('qwerty', max_length=3) == '...'
    assert get_shortish_repr(None) == 'None'
    assert get_shortish_repr(True) == 'True'

# Generated at 2022-06-12 20:08:08.788066
# Unit test for function get_repr_function
def test_get_repr_function():
    class Foo(object): pass
    def foo_repr(x):
        return 'foo%s' % x
    custom_repr = [
        (lambda x: 'bar' in x, lambda x: 'bar-%s' % x),
    ]
    assert get_repr_function('foo', custom_repr) is repr
    assert get_repr_function('bar', custom_repr) is foo_repr
    assert get_repr_function(Foo(), custom_repr) is repr



# Generated at 2022-06-12 20:08:17.875389
# Unit test for function get_repr_function
def test_get_repr_function():
    def repr_x(x):
        return 'repr_x %r' % x
    def repr_y(y):
        return 'repr_y %r' % y
    def repr_z(z):
        return 'repr_z %r' % z
    default_repr = lambda x: 'default_repr %r' % x

    custom_repr = ((str, repr_x),
                   (unicode, repr_y),
                   (lambda x: isinstance(x, int) and x < 0, repr_z))


# Generated at 2022-06-12 20:08:24.841187
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Foo(WritableStream):
        def __init__(self):
            self.strings = []

        def write(self, s):
            self.strings.append(s)

    a = Foo()
    a.write('hi')
    assert a.strings == ['hi']

    try:
        class Bar:
            pass

        a = Bar()
        assert isinstance(a, WritableStream)
    except:
        pass
    else:
        assert False, 'Exception should have been raised.'

    try:
        class Bar(WritableStream):
            pass

        a = Bar()
        assert isinstance(a, WritableStream)
    except:
        pass
    else:
        assert False, 'Exception should have been raised.'

    class Bar(WritableStream):
        write = None


# Generated at 2022-06-12 20:08:31.728522
# Unit test for function get_repr_function
def test_get_repr_function():
    from .testing.assertions import assert_equal
    class Foo(object):
        def my_repr(self):
            return 'my repr'
    assert_equal(get_repr_function(Foo(), []), repr)
    assert_equal(get_repr_function(Foo(), [(object, lambda x: 'hi')]),
                 lambda x: 'hi')
    assert_equal(get_repr_function(Foo(), [(object, lambda x: 'bye')]),
                 lambda x: 'bye')
    assert_equal(get_repr_function(Foo(), [(object, lambda x: 'bye'),
                                           (object, lambda x: 'hi')]),
                 lambda x: 'bye')