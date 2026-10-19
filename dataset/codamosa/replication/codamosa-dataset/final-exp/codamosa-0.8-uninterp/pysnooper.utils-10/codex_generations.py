

# Generated at 2022-06-12 19:58:52.466272
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    COUNT = 2
    message = 'dummy message'

    class WritableStreamStub(WritableStream):
        def __init__(self):
            self.calls = []
            self.call_count = 0
        def write(self, s):
            self.call_count += 1
            self.calls.append((self.call_count, s))
            if self.call_count == COUNT:
                raise Exception

    stream_stub = WritableStreamStub()
    try:
        stream_stub.write(message)
    except Exception:
        pass
    assert stream_stub.call_count == COUNT
    for i in range(1, COUNT + 1):
        assert stream_stub.calls[i - 1][0] == i

# Generated at 2022-06-12 19:58:57.030441
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    import tempfile
    text = 'spam\negg\n'
    f = io.TextIOWrapper(tempfile.TemporaryFile(), encoding='utf-8')
    f.write(text)
    f.close()
    assert isinstance(f, WritableStream)



# Generated at 2022-06-12 19:59:01.274324
# Unit test for function get_repr_function
def test_get_repr_function():
    class A(object):
        pass
    class B(A):
        pass

    for item, expected_repr_fn in ((A, repr), (B(), repr), (2, repr)):
        assert get_repr_function(item, custom_repr=((A, str), )) == expected_repr_fn




# Generated at 2022-06-12 19:59:10.686692
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('foobarbaz') == 'foobarbaz'
    assert get_shortish_repr(1) == '1'
    assert get_shortish_repr(1, max_length=3) == '1'
    assert get_shortish_repr(1, max_length=2) == '1'
    assert get_shortish_repr(1, max_length=1) == '...'
    assert get_shortish_repr(1, max_length=0) == '...'
    assert get_shortish_repr(1, max_length=20) == '1'
    assert get_shortish_repr('foobarbaz', max_length=10) == 'foobarbaz'

# Generated at 2022-06-12 19:59:22.341545
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyOpenFile(object):
        def __init__(self):
            self.written = ''

        def write(self, s):
            assert(isinstance(s, bytes))
            self.written += s.decode('utf-8')

    file_like = MyOpenFile()
    f = WritableStream()
    assert issubclass(f.__class__, WritableStream)

    # If the file_like is not a writable stream, this should fail.
    try:
        f = WritableStream(file_like)
        assert False # Shouldn't get here
    except TypeError:
        pass

    # If the file_like is a writable stream, this should succeed.
    f = WritableStream(sys.stdout)
    assert isinstance(f, WritableStream)

# Generated at 2022-06-12 19:59:26.145884
# Unit test for function get_repr_function
def test_get_repr_function():
    class X(object): pass
    class Y(object): pass
    class Z(object): pass
    x, y, z = X(), Y(), Z()

    assert get_repr_function(x, ()) is repr
    assert get_repr_function(x, ((X, str),)) is str
    assert get_repr_function(y, ((X, str),)) is repr
    assert get_repr_function(x, ((X, str), (Y, dict))) is str
    assert get_repr_function(y, ((X, str), (Y, dict))) is dict
    assert get_repr_function(z, ((X, str), (Y, dict))) is repr

    assert get_repr_function(x, ((type(x), str),)) is str

# Generated at 2022-06-12 19:59:35.415593
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, (
        (lambda x: True, lambda x: 'hello!'),
    )) == 'hello!'

    assert (
        get_repr_function(
            1, (
                (lambda x: False, lambda x: 'hello!'),
                (lambda x: True, lambda x: 'goodbye!'),
            )
        ) == 'goodbye!'
    )

    assert (
        get_repr_function(
            1, (
                (lambda x: False, lambda x: 'hello!'),
                (lambda x: False, lambda x: 'goodbye!'),
            )
        ) == repr
    )



# Generated at 2022-06-12 19:59:37.641300
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class WritableStreamSubclass(WritableStream):
        def write(self, s):
            pass
    assert isinstance(WritableStreamSubclass(), WritableStream)


# Generated at 2022-06-12 19:59:45.221734
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(1) == '1'
    assert get_shortish_repr(1, max_length=5) == '1'
    assert get_shortish_repr(1, max_length=1) == '1'

    assert get_shortish_repr(1, max_length=0) == ''
    assert get_shortish_repr(1, max_length=-1) == ''

    assert get_shortish_repr('123456') == '123456'
    assert get_shortish_repr('123456', max_length=5) == '...456'
    assert get_shortish_repr('123456', max_length=2) == '...'
    assert get_shortish_repr('123456', max_length=6) == '123456'

   

# Generated at 2022-06-12 19:59:48.818793
# Unit test for function get_repr_function
def test_get_repr_function():
    from .pretty import shortened_repr
    assert get_repr_function(42, ((int, shortened_repr),)) is shortened_repr
    assert get_repr_function(42., ((int, shortened_repr),)) is repr

# Generated at 2022-06-12 20:00:07.795123
# Unit test for function shitcode
def test_shitcode():
    assert shitcode('lié') == 'li?'


if sys.version_info[0] >= 3:

    def func_name(func):
        """Return the name of the function `func`."""
        return func.__name__

    def func_closure(func):
        """Return the closure of the function `func`."""
        return func.__closure__

    def func_defaults(func):
        """Return the default arguments of the function `func`."""
        return func.__defaults__

    def func_code(func):
        """Return the code object of the function `func`."""
        return func.__code__

    def func_globals(func):
        """Return the global namespace of the function `func`."""
        return func.__globals__

# Generated at 2022-06-12 20:00:14.726128
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    from .pycompat import class_type
    a_file = open('/dev/null', 'w')
    assert isinstance(a_file, WritableStream)
    class C(WritableStream):
        def write(self, s):
            assert isinstance(s, bytes)
            raise RuntimeError
    assert isinstance(C(), WritableStream)
    if sys.version_info[0] == 2:
        class C(object):
            def write(self, s):
                assert isinstance(s, bytes)
                raise RuntimeError
        assert isinstance(C(), WritableStream)
    class C(object):
        @classmethod
        def __subclasshook__(cls, C):
            return True
    assert isinstance(C(), WritableStream)
    class C(object):
        pass

# Generated at 2022-06-12 20:00:19.937693
# Unit test for function shitcode
def test_shitcode():
    assert shitcode('abcde') == 'abcde'
    assert shitcode('a¬b⚡c') == 'a?b?c'
    assert shitcode('a\x00b') == 'a?b'

# Generated at 2022-06-12 20:00:25.770639
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, (
        (int, lambda x: 'an integer'),
        (str, lambda x: 'a string')
    )) == 'an integer'
    assert get_repr_function('hi', (
        (int, lambda x: 'an integer'),
        (str, lambda x: 'a string')
    )) == 'a string'



# Generated at 2022-06-12 20:00:35.185667
# Unit test for function get_repr_function
def test_get_repr_function():
    class A: pass

    assert get_repr_function(A(), custom_repr=()) == repr
    assert get_repr_function(A(), custom_repr=(('', 'custom'))) == 'custom'
    assert get_repr_function(A(), custom_repr=(('', 'custom'), ('', 'custom2'))) == 'custom'
    assert get_repr_function(A(), custom_repr=(('', 'custom'), ('', 'custom2'))) == 'custom'
    assert get_repr_function(A(), custom_repr=((A, 'custom'), ('', 'custom2'))) == 'custom'
    assert get_repr_function(A(), custom_repr=(('', 'custom'), (A, 'custom2'))) == 'custom2'

# Generated at 2022-06-12 20:00:39.074537
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class X(WritableStream):
        def write(self, s):
            pass

    x = X()
    assert isinstance(x, WritableStream)



# Generated at 2022-06-12 20:00:44.417877
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    from .abc import abstractmethod, abstractproperty
    class X(object):
        @abstractmethod
        def write(self):
            pass
    assert issubclass(sys.stdout.__class__, WritableStream)
    assert not issubclass(X.__class__, WritableStream)


# Unit tests for method get_shortish_repr

# Generated at 2022-06-12 20:00:47.569084
# Unit test for function shitcode
def test_shitcode():
    assert shitcode('\x01\xff') == '?\xff'
    assert shitcode('\x01\xff') == '?\xff'
    assert shitcode('\x01\xff') == '?\xff'
    assert shitcode('\x01\xff') == '?\xff'



# Generated at 2022-06-12 20:00:57.810623
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, (lambda x: isinstance(x, int),
                                 lambda x: 'an int!')
                            )(1) == 'an int!'
    assert get_repr_function(1.0, (lambda x: isinstance(x, int),
                                   lambda x: 'an int!')
                              )(1.0) == '1.0'
    assert get_repr_function(1, ((int,), lambda x: 'an int!'))(1) == 'an int!'
    assert get_repr_function(1.0, ((int,), lambda x: 'an int!'))(1.0) == '1.0'



# Generated at 2022-06-12 20:01:05.023439
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('hello') == 'hello'
    assert get_shortish_repr(123) == '123'
    assert get_shortish_repr(1.23456789123456789) == '1.23456789123'
    assert get_shortish_repr(1.23456789123456789, max_length=4) == '1.2...9123'
    assert get_shortish_repr(1.23456789123456789, max_length=15) == '1.23456789123456789'
    assert get_shortish_repr('123456789123456789', max_length=15) == '123456789123456789'

# Generated at 2022-06-12 20:01:18.563391
# Unit test for function get_repr_function
def test_get_repr_function():
    custom_repr = (
        (lambda x: isinstance(x, int), int.__repr__),
        (lambda x: isinstance(x, str), lambda x: "s[{}]".format(repr(x)))
    )
    assert get_repr_function(4, custom_repr) == int.__repr__
    assert get_repr_function("abc", custom_repr) == custom_repr[1][1]
    assert get_repr_function(2.5, custom_repr) == repr



# Generated at 2022-06-12 20:01:26.423509
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Thing(WritableStream):
        def write(self, s):
            pass

    assert issubclass(Thing, WritableStream)

    class Thing2(object):
        def write(self, s):
            pass

    assert not issubclass(Thing2, WritableStream)

    class Thing3(object):
        def write(self, s):
            pass

    class Thing4(Thing3):
        write = None

    assert not issubclass(Thing4, WritableStream)

# Generated at 2022-06-12 20:01:31.848866
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyTextIOWrapper(WritableStream):
        def __init__(self):
            self.written = ''
        def write(self, s):
            self.written += s
    my_text_io_wrapper = MyTextIOWrapper()
    my_text_io_wrapper.write('hey')
    assert my_text_io_wrapper.written == 'hey'



# Unit tests for method __subclasshook__ of class WritableStream

# Generated at 2022-06-12 20:01:40.006079
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(Metaclass=ABCMeta):
        @abc.abstractmethod
        def write(self, s): pass
    class B(A): pass
    class C(A): pass
    class D(C): pass
    assert issubclass(B, A)
    assert issubclass(B, WritableStream)
    assert issubclass(C, A)
    assert issubclass(C, WritableStream)
    assert issubclass(D, A)
    assert issubclass(D, WritableStream)
    assert issubclass(D, C)

# Generated at 2022-06-12 20:01:48.118918
# Unit test for function get_repr_function
def test_get_repr_function():
    class A:
        def __init__(self, s):
            self.s = s
        def __repr__(self):
            return self.s

    assert get_repr_function(u'helloworld', ()) == repr
    assert get_repr_function(u'helloworld', [(lambda x: True, lambda x: x)]) == (
      lambda x: x
    )
    assert get_repr_function(u'helloworld', [(lambda x: True, str)]) == str
    assert get_repr_function(u'helloworld', [(lambda x: True, 222)]) == repr

    assert get_repr_function(A('whatever'), ()) == repr

# Generated at 2022-06-12 20:01:58.318869
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    try:
        from .testing_tools import assert_equal
    except ImportError:
        # If we don't have py.test, we won't be able to use `assert_equal`, so
        # we'll resort to `assert`
        def assert_equal(x, y):
            assert x == y
    def f(x):
        assert_equal(
            get_shortish_repr(x), repr(x)
        )
        assert_equal(
            get_shortish_repr(x, max_length=len(repr(x)) - 2),
            repr(x)
        )
        assert_equal(
            get_shortish_repr(x, max_length=len(repr(x)) - 1),
            repr(x)
        )

# Generated at 2022-06-12 20:02:01.612694
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Thing:
        def write(self, s):
            if isinstance(s, int):
                raise NotImplementedError
    assert WritableStream.__subclasshook__(Thing) is NotImplemented
    assert WritableStream.__subclasshook__(str) is NotImplemented

# Generated at 2022-06-12 20:02:11.331053
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    # Testing for the class itself:
    assert WritableStream.__subclasshook__(list) is NotImplemented
    # Testing for subclasses:
    class NotAStream(list): pass
    assert WritableStream.__subclasshook__(NotAStream) is NotImplemented

    class NotWritableStream(object): pass
    assert WritableStream.__subclasshook__(NotWritableStream) is NotImplemented

    class AStream(object): write = None
    assert WritableStream.__subclasshook__(AStream) is NotImplemented

    class AWritableStream(object):
        def write(self, s): pass
    assert WritableStream.__subclasshook__(AWritableStream) is True

    class AFileObject(file): pass

# Generated at 2022-06-12 20:02:17.107391
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(None, ()) is repr
    assert get_repr_function(None, (1, 2)) is repr
    assert get_repr_function(None, ((int, str), 2)) is repr
    assert get_repr_function(None, ((), str)) is repr
    assert get_repr_function(None, ((object,), str)) is repr
    assert get_repr_function(None, ((None,), len)) is len
    assert get_repr_function(int, ((int,), str)) is str



# Generated at 2022-06-12 20:02:27.912509
# Unit test for function get_repr_function
def test_get_repr_function():
    class A:
        pass
    class B(A):
        pass
    class C(A):
        pass
    assert get_repr_function(A(), (
        (A, lambda x: 'A'),
        (B, lambda x: 'B'),
        (C, lambda x: 'C'),
    )) == 'A'
    assert get_repr_function(B(), (
        (A, lambda x: 'A'),
        (B, lambda x: 'B'),
        (C, lambda x: 'C'),
    )) == 'B'
    assert get_repr_function(C(), (
        (A, lambda x: 'A'),
        (B, lambda x: 'B'),
        (C, lambda x: 'C'),
    )) == 'C'

# Generated at 2022-06-12 20:02:33.494019
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Foo:
        def write(self, s): pass
    f = Foo()
    assert issubclass(Foo, WritableStream)
    assert WritableStream.__subclasshook__(Foo)
    assert isinstance(f, WritableStream)

# Generated at 2022-06-12 20:02:35.241216
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('0' * 100, max_length=20) == '0' * 17 + '...'



# Generated at 2022-06-12 20:02:41.765850
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    from .python_toolbox.temp_value import TempValue
    with TempValue(sys.displayhook, None):
        for item in [
            7,
            (1, 2, 3),
            'hello',
            u'\u05d0\u05d1\u05d2',
            object(),
            object(),
            object(),
        ]:
            shortish_repr = get_shortish_repr(item, max_length=8)
            assert len(shortish_repr) <= 8
        assert get_shortish_repr(u'\u05d0\u05d1\u05d2', max_length=8) == '\ufffd\ufffd\ufffd'

# Generated at 2022-06-12 20:02:51.970982
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    # standard repr
    assert get_shortish_repr(1) == '1'
    assert get_shortish_repr(1.0) == '1.0'
    assert get_shortish_repr(1 + 1j) == '(1+1j)'
    assert get_shortish_repr(None) == 'None'
    assert get_shortish_repr(False) == 'False'
    assert get_shortish_repr(True) == 'True'
    assert get_shortish_repr('1') == "'1'"
    assert get_shortish_repr(b'1') == "b'1'"
    assert get_shortish_repr(u'1') == "u'1'"

# Generated at 2022-06-12 20:02:55.026600
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Good(WritableStream):
        def write(self, s):
            pass

    class Bad(WritableStream):
        pass

    assert issubclass(Good, WritableStream)
    assert not issubclass(Bad, WritableStream)

# Generated at 2022-06-12 20:02:59.301272
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class WritableStreamImpl(WritableStream):
        def __init__(self):
            self.written_lines = []
        def write(self, s):
            self.written_lines.append(s)
    writable_stream_impl = WritableStreamImpl()
    writable_stream_impl.write('hi\n')
    assert writable_stream_impl.written_lines == ['hi\n']



# Generated at 2022-06-12 20:03:06.639011
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(
        'o' * 200,
        custom_repr=((lambda x: len(x) > 100,
                      lambda x: 'long string with length {}'.format(len(x))))
    ) == 'long string with length 200'
    assert get_shortish_repr('o' * 200, max_length=10) == 'oooooooooo'
    assert get_shortish_repr(
        'o' * 200,
        custom_repr=((lambda x: len(x) > 100,
                      lambda x: 'long string with length {}'.format(len(x))),),
        max_length=20
    ) == 'long string with length...4'

# Generated at 2022-06-12 20:03:14.643124
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class FakeWritableStream(WritableStream):
        def __init__(self):
            self.buffer = ''
        def write(self, s):
            assert isinstance(s, str)
            self.buffer += s
    assert issubclass(FakeWritableStream, WritableStream)
    fws = FakeWritableStream()
    fws.write('hello')
    assert fws.buffer == 'hello'



# Generated at 2022-06-12 20:03:18.358731
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Super:
        def write(self, s): pass
    class GoodSub(Super):
        def write(self, s): pass
    class BadSub(Super):
        def write(self, s, t): pass
    assert issubclass(GoodSub, WritableStream)
    assert not issubclass(BadSub, WritableStream)



# Generated at 2022-06-12 20:03:25.292443
# Unit test for function get_repr_function
def test_get_repr_function():
    from .test_tools.asserting_tools import assert_equal

    class Foo(object): pass
    class Bar(object): pass
    class Baz(object): pass

    def repr_1(x): return 'yes'

    assert_equal(get_repr_function(5, (
        (lambda x: x % 2 == 0, repr_1),
        (lambda x: x % 2 == 1, lambda x: 'no'),
    )), repr_1)

    assert_equal(get_repr_function(Foo(), (
        (lambda x: isinstance(x, Foo), repr_1),
        (lambda x: isinstance(x, Bar), lambda x: 'no'),
    )), repr_1)


# Generated at 2022-06-12 20:03:35.356259
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function('ay',
                             custom_repr=((int, lambda n: str(n + 2)),)) == repr
    assert get_repr_function(1,
                             custom_repr=((int, lambda n: str(n + 2)),)) == (
                                                      lambda n: str(n + 2))



# Generated at 2022-06-12 20:03:46.113900
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(0, ()) == repr
    assert get_repr_function(0., ()) == repr
    assert get_repr_function(0j, ()) == repr
    assert get_repr_function('x', ()) == repr
    assert get_repr_function('', ()) == repr
    assert get_repr_function('', ((), lambda x: 'y')) == 'y'
    assert get_repr_function('', ((), lambda x: 'y', ())) == 'y'

    assert get_repr_function(0, ((0,), lambda x: x+1)) == 1

    assert get_repr_function(0j, ((0,), lambda x: x+1)) == 0j+1


# Generated at 2022-06-12 20:03:56.307754
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr((1, 2)) == '(1, 2)'
    assert get_shortish_repr((1, 2), max_length=7) == '(1, 2)'
    assert get_shortish_repr((1, 2), max_length=6) == '(1,...'
    assert get_shortish_repr((1, 2), max_length=5) == '(1...'
    assert get_shortish_repr((1, 2), max_length=4) == '(1..'
    assert get_shortish_repr((1, 2), max_length=3) == '(1.'
    assert get_shortish_repr((1, 2), max_length=2) == '(1'
    assert get_shortish_repr((1, 2), max_length=1) == '('

# Generated at 2022-06-12 20:03:59.324741
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    fake_stream = FakeStream()
    WritableStream.register(FakeStream)

    assert isinstance(fake_stream, WritableStream)

    fake_stream.write('hello, world!')
    assert fake_stream.got_data == 'hello, world!'



# Generated at 2022-06-12 20:04:08.083138
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class TestStream(WritableStream):
        def __init__(self):
            self.lines = []
        def write(self, s):
            self.lines.append(s)
    stream = TestStream()
    for i in range(10):
        stream.write('foo\n')
    assert stream.lines == ['foo\n'] * 10
    try:
        stream.write(3)
    except TypeError:
        pass
    else:
        assert False, '`write` should raise `TypeError` if it received ' \
                      'something other than a `str`'
    try:
        stream.write(b'hello')
    except TypeError:
        pass
    else:
        assert False, '`write` should raise `TypeError` if it received ' \
                      'something other than a `str`'

# Generated at 2022-06-12 20:04:18.380730
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(0, []) == repr
    assert get_repr_function(1, [(lambda x: True, str)]) == str
    assert get_repr_function(1, [(lambda x: False, str)]) == repr
    assert get_repr_function(0, [(int, str)]) == str
    assert get_repr_function(0, [(float, str)]) == repr
    assert get_repr_function(0.0, [(float, str)]) == str
    assert get_repr_function(0, [(int, str), (float, str)]) == str
    assert get_repr_function(0.0, [(int, str), (float, str)]) == str

# Generated at 2022-06-12 20:04:27.595049
# Unit test for function get_repr_function
def test_get_repr_function():
    class A(object): pass
    class B(A): pass
    class C(A): pass


# Generated at 2022-06-12 20:04:34.686363
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(5) == '5'
    assert get_shortish_repr(5.5) == '5.5'
    assert get_shortish_repr((5, 6)) == '(5, 6)'
    assert get_shortish_repr('hello') == "'hello'"
    assert get_shortish_repr('hello'[1:], max_length=2) == 'e...'
    assert get_shortish_repr('hello'[1:], max_length=4) == 'ell...'
    assert get_shortish_repr('hello'[1:], max_length=2,
                             normalize=True) == 'e...'

# Generated at 2022-06-12 20:04:45.506832
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    from python_toolbox.sequence_tools import peep

    def custom_repr_one(x):
        return '>' * x

    def custom_repr_two(x):
        return '<' * x

    for x in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 40, 50, 100):
        assert get_shortish_repr(x) == repr(x)
        assert get_shortish_repr(x, custom_repr=((x, custom_repr_one),)) == \
            custom_repr_one(x)
        assert get_shortish_repr(x, custom_repr=(
            (lambda y: y % 2, custom_repr_one),
        )) == custom_repr_

# Generated at 2022-06-12 20:04:47.068127
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyFile(WritableStream):
        pass

    verify_WritableStream(MyFile)




# Generated at 2022-06-12 20:04:58.803728
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class MyWritableStream(object):
        def write(self, s):
            self.s = s

    writable_stream = MyWritableStream()
    WritableStream.register(MyWritableStream)

    class MyUnwritableStream(object):
        pass

    unwritable_stream = MyUnwritableStream()

    assert isinstance(writable_stream, WritableStream)
    assert not isinstance(unwritable_stream, WritableStream)

# Generated at 2022-06-12 20:05:03.424280
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class TestStream(WritableStream):
        def __init__(self):
            pass

        def write(self, s):
            return s

    test_stream = TestStream()
    assert test_stream.write('hello') == 'hello'



# Generated at 2022-06-12 20:05:10.624895
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    from .testing.test_tools import assert_equal

    class _ReprTest(object):
        def __repr__(self):
            return 'long long long longlonglonglonglonglong long longlong'

    assert_equal(get_shortish_repr([1], max_length=10), '[1]')
    assert_equal(get_shortish_repr([1], max_length=10, normalize=True), '[1]')
    assert_equal(
        get_shortish_repr(_ReprTest(), max_length=10),
        'long long...'
    )
    assert_equal(
        get_shortish_repr(
            _ReprTest(),
            max_length=10,
            normalize=True
        ),
        'long long...'
    )


# Generated at 2022-06-12 20:05:18.195524
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, ((int, lambda x: str(x*1000)),))(1) == '1000'
    assert get_repr_function(1, ((lambda x: True, lambda x: '3'),))(1) == '3'
    assert get_repr_function([1], (
        (lambda x: len(x) == 1, lambda x: 'a list with one item'),
    ))([1]) == 'a list with one item'
    assert get_repr_function(1, ((lambda x: True, lambda x: '3'),
                                 (lambda x: True, lambda x: '2'))) == '2'

# Generated at 2022-06-12 20:05:23.889484
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A:
        def write(self, s):
            self.s = s

    assert A.__subclasshook__(A) is True
    a = A()
    a.write('hi')
    assert a.s == 'hi'

    assert A.__subclasshook__(list) is NotImplemented

# Generated at 2022-06-12 20:05:30.511844
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class MyFile(object):
        def __init__(self, write_function):
            self.write_function = write_function
        def write(self, x):
            self.write_function(x)

    result = []

    x = MyFile(lambda s: result.append(s))
    y = WritableStream()

    assert isinstance(x, WritableStream)
    assert not isinstance(y, WritableStream)

    y.write('hello') # should raise NotImplementedError

# Generated at 2022-06-12 20:05:42.079921
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(object): pass
    assert not issubclass(A, WritableStream)
    assert not isinstance(A(), WritableStream)
    class A(object):
        def write(self, s):
            pass
    assert issubclass(A, WritableStream)
    assert isinstance(A(), WritableStream)
    class A(object):
        def write(self):
            pass
    assert not issubclass(A, WritableStream)
    assert not isinstance(A(), WritableStream)
    class A(object):
        def write(self, s, extra=None):
            pass
    assert not issubclass(A, WritableStream)
    assert not isinstance(A(), WritableStream)
    class A(object):
        def write(self, extra=None, s=None):
            pass
   

# Generated at 2022-06-12 20:05:53.013671
# Unit test for function get_repr_function
def test_get_repr_function():
    class TestClass1(object):
        pass
    assert normalize_repr(get_shortish_repr(TestClass1())) == \
           normalize_repr(repr(TestClass1()))

    class TestClass2(object):
        def __repr__(self):
            return 'TestClass2'

    assert normalize_repr(get_shortish_repr(TestClass2())) == \
           normalize_repr(repr(TestClass2()))

    test_obj = TestClass1()
    assert normalize_repr(get_shortish_repr(test_obj)) == \
           normalize_repr(repr(test_obj))

    assert normalize_repr(get_shortish_repr(test_obj, custom_repr=[])) == \
           normal

# Generated at 2022-06-12 20:06:02.090774
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr([1, 2, 3, 4, 5]) == '[1, 2, 3, 4, 5]'
    assert get_shortish_repr([1, 2, 3, 4, 5], max_length=8) == '[1...5]'
    assert get_shortish_repr([1, 2, 3, 4, 5], max_length=1) == '[...'
    assert get_shortish_repr([1, 2, 3, 4, 5], max_length=0) == ''
    assert get_shortish_repr([1, 2, 3, 4, 5], max_length=None) == '[1, 2, 3, 4, 5]'

    assert get_shortish_repr(string_types, max_length=None) == \
                                                        "<type 'basestring'>"

# Generated at 2022-06-12 20:06:03.822627
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(1, max_length=2) == '1'



# Generated at 2022-06-12 20:06:20.796884
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(WritableStream):
        def write(self, s):
            pass

    class B(WritableStream):
        def write(self, s):
            return NotImplemented

    class C(WritableStream):
        def write(self, s):
            pass

        def write_to_disk(self, s):
            pass

    assert issubclass(A, WritableStream)
    assert not issubclass(B, WritableStream)
    assert issubclass(C, WritableStream)



# Generated at 2022-06-12 20:06:24.400852
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class BrokenFile(object):
        def write(self, s):
            raise IOError()

    assert _check_methods(BrokenFile, 'write') is NotImplemented

    class File(object):
        def write(self, s):
            pass

    assert _check_methods(File, 'write') is True



# Generated at 2022-06-12 20:06:31.135888
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(u'hey') == u"u'hey'"
    assert get_shortish_repr(u'H' * 1000) == \
           u"u'HHHHH...HHHH'"

# Generated at 2022-06-12 20:06:32.751828
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class Mock(WritableStream):

        def write(self, s):
            assert isinstance(s, str)

    Mock().write('')




# Generated at 2022-06-12 20:06:39.263484
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class WritableStream_write_checker(WritableStream):
        def __init__(self):
            self.written_string = ''

        def write(self, s):
            self.written_string += s

    writable_stream = WritableStream_write_checker()
    writable_stream.write('abc')
    writable_stream.write('def')
    assert writable_stream.written_string == 'abcdef'




# Generated at 2022-06-12 20:06:48.729254
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(3, []) is repr
    assert get_repr_function(3.5, []) is repr
    assert get_repr_function('hey', []) is repr
    assert get_repr_function([1, 2, 3], []) is repr
    assert get_repr_function({'a': 1}, []) is repr
    assert get_repr_function(set([1, 2, 3]), []) is repr
    assert get_repr_function(3, [
        (lambda x: (5 < x < 7), str),
    ]) is str
    assert get_repr_function(3, [
        (int, str),
    ]) is str
    assert get_repr_function(3.5, [
        (int, str),
    ]) is repr

# Generated at 2022-06-12 20:06:52.880794
# Unit test for function get_repr_function
def test_get_repr_function():
    def my_repr_for_int(x):
        return 'I am integer!'
    assert get_repr_function(1, ((int, my_repr_for_int),))(1) == \
                                                         'I am integer!'
    assert get_repr_function(1.0, ((int, my_repr_for_int),))(1.0) == '1.0'

# Generated at 2022-06-12 20:06:57.594359
# Unit test for function get_repr_function
def test_get_repr_function():
    assert normalize_repr(repr('hello world')) == 'hello world'
    assert normalize_repr(repr('hello at 0x12345678')) == 'hello'
    assert get_repr_function(1j + 0, [(complex, lambda x: 'c:' + str(x))]) \
                                                                     == 'c:1j'
    assert get_repr_function(1, [(complex, lambda x: 'c:' + str(x))]) == repr
    assert get_repr_function([0], []) == repr
    assert get_repr_function(
        [0], [(list, lambda x: ''.join(map(str, x)))]
    ) == ''.join(map(str, [0]))


if __name__ == '__main__':
    test_get_

# Generated at 2022-06-12 20:07:02.061159
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    from .fake_file import FakeFile
    from .fake_stream import FakeStream
    from .fake_socket import FakeSocket
    from . import stdin, stdout, stderr
    assert issubclass(FakeFile, WritableStream)
    assert not issubclass(FakeStream, WritableStream)
    assert not issubclass(FakeSocket, WritableStream)
    assert not issubclass(type(stdin), WritableStream)
    assert issubclass(type(stdout), WritableStream)
    assert issubclass(type(stderr), WritableStream)
    assert not issubclass(int, WritableStream)

# Generated at 2022-06-12 20:07:07.018255
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    class Good:
        def write(self, s):
            pass

    assert issubclass(Good, WritableStream)

    class Bad:
        def write(self, s):
            pass
        def writelines(self, s):
            pass

    assert not issubclass(Bad, WritableStream)

    class Bad:
        def write(self, s):
            pass
        def close(self):
            pass

    assert not issubclass(Bad, WritableStream)

    class Good:
        def write(self, s):
            pass
        def close(self):
            pass

    assert issubclass(Good, WritableStream)

    class Good2(io.TextIOBase):
        pass

    assert issubclass(Good2, WritableStream)


# Generated at 2022-06-12 20:07:37.345935
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def __init__(self):
            self.output = ''
        def write(self, s):
            self.output += s
    x = MyWritableStream()
    x.write('hey')
    assert x.output == 'hey'



# Generated at 2022-06-12 20:07:40.314615
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def write(self, s):
            return s + ' appended'

    writable_stream = MyWritableStream()
    assert writable_stream.write('hello ') == 'hello  appended'



# Generated at 2022-06-12 20:07:45.442899
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Foo(WritableStream):
        def write(self, s): pass

    class Bar(Foo):
        def write(self, s): pass

    class Baz(Foo):
        pass

    class Qux(Foo):
        def write(self): pass

    assert issubclass(Foo, WritableStream)
    assert issubclass(Bar, WritableStream)
    assert not issubclass(Baz, WritableStream)
    assert not issubclass(Qux, WritableStream)




# Generated at 2022-06-12 20:07:50.116726
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(str, ((str, str),)) == str
    assert get_repr_function(str, ((str, 'yay'),)) == 'yay'
    assert get_repr_function(str, ((int, 'yay'),)) == repr
    assert get_repr_function(3.14, ()) == repr
    assert get_repr_function(3.14, ((int, 'yay'),)) == repr
    assert get_repr_function(3.14, (((1, 2, 3.14), 'yay'),)) == 'yay'
    assert get_repr_function(1, (((1, 2, 3.14), 'yay'),)) == repr



# Generated at 2022-06-12 20:07:52.362103
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def write(self, s):
            pass
    assert issubclass(MyWritableStream, WritableStream)



# Generated at 2022-06-12 20:08:02.949446
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A:
        def write(self, s):
            return 'A.write(\'{}\')'.format(s)

    class B:
        pass

    class C:
        def write(self, s):
            return 'C.write(\'{}\')'.format(s)

    class D():
        def write(self, s):
            return 'D.write(\'{}\')'.format(s)

    class E(A, C):
        pass

    assert isinstance(A(), WritableStream)
    assert not isinstance(B(), WritableStream)
    assert isinstance(C(), WritableStream)
    assert isinstance(D(), WritableStream)
    assert isinstance(E(), WritableStream)

    assert 'A.write' in repr(WritableStream)
    assert 'B.write' not in repr

# Generated at 2022-06-12 20:08:11.102474
# Unit test for function get_repr_function
def test_get_repr_function():
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(B): pass
    class E(D): pass

    assert get_repr_function(A(), ()) is repr
    assert get_repr_function(A(), ((A, lambda x: 'a'))) == 'a'
    assert get_repr_function(A(), ((lambda x: True, lambda x: 'a'))) == 'a'
    assert get_repr_function(A(), ((lambda x: False, lambda x: 'a'))) is repr
    assert get_repr_function(
        A(), ((lambda x: False, lambda x: 'a'),(A, lambda x: 'a'))) == 'a'

# Generated at 2022-06-12 20:08:20.177790
# Unit test for function get_repr_function
def test_get_repr_function():
    def foo_repr(x):
        return 'foo'
    def bar_repr(x):
        return 'bar'
    class Foo(object): pass
    class Bar(object): pass

    assert get_repr_function(Foo(), ()) == repr
    assert get_repr_function(Bar(), ()) == repr
    assert get_repr_function(Foo(), [(Foo, foo_repr)]) == foo_repr
    assert get_repr_function(Bar(), [(Foo, foo_repr)]) == repr
    assert get_repr_function(Foo(), [(Foo, foo_repr), (Bar, bar_repr)]) == foo_repr
    assert get_repr_function(Bar(), [(Foo, foo_repr), (Bar, bar_repr)]) == bar_

# Generated at 2022-06-12 20:08:24.817485
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('1234567') == '1234567'
    assert get_shortish_repr('1234567', max_length=10) == '1234567'
    assert get_shortish_repr('1234567', max_length=9) == '...4567'
    assert get_shortish_repr('1234567', max_length=8) == '...567'
    assert get_shortish_repr('1234567', max_length=7) == '...67'
    assert get_shortish_repr('1234567', max_length=6) == '...7'
    assert get_shortish_repr('1234567', max_length=5) == '...'
    assert get_shortish_repr('1234567', max_length=4)

# Generated at 2022-06-12 20:08:29.319660
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MockStream(WritableStream):
        def __init__(self):
            self.contents = []
        def write(self, s):
            self.contents.append(s)
    s = MockStream()
    assert (len(s.contents) == 0)
    s.write('abc')
    assert (len(s.contents) == 1)
    s.write('def')
    assert (len(s.contents) == 2)