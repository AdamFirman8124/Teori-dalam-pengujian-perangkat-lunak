

# Generated at 2022-06-12 19:58:41.406067
# Unit test for function truncate
def test_truncate():
    assert truncate('abcde', 4) == '...e'
    assert truncate('abcd', 4) == 'a...'
    assert truncate('abc', 3) == 'abc'
    assert truncate('abc', None) == 'abc'

# Generated at 2022-06-12 19:58:43.971389
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MockStringIO(WritableStream):

        def __init__(self):
            self.data = ''

        def write(self, s):
            self.data += s

    s = 'hello there'
    mock_string_io = MockStringIO()
    mock_string_io.write(s)
    assert mock_string_io.data == s



# Generated at 2022-06-12 19:58:52.465724
# Unit test for function get_repr_function
def test_get_repr_function():


    def is_even(n):
        return n % 2 == 0

    def is_odd(n):
        return n % 2 == 1

    def even_repr(n):
        return 'even %s' % n

    def odd_repr(n):
        return 'odd %s' % n

    assert get_repr_function(5, [(is_even, even_repr), (is_odd, odd_repr)])(5) == 'odd 5'
    assert get_repr_function(6, [(is_even, even_repr), (is_odd, odd_repr)])(6) == 'even 6'
    assert get_repr_function(6, [(is_odd, odd_repr), (is_even, even_repr)])(6) == 'even 6'

   

# Generated at 2022-06-12 19:59:00.120433
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MockWritableStream(WritableStream):
        def __init__(self):
            self.my_list = []

        def write(self, x):
            self.my_list.append(x)

    writable_stream = MockWritableStream()

    writable_stream.write('meow')
    assert writable_stream.my_list == ['meow']
    
    writable_stream.write('woof')
    assert writable_stream.my_list == ['meow', 'woof']
    
    
    
    

# Generated at 2022-06-12 19:59:10.546606
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(1) == '1'
    assert get_shortish_repr(1, normalize=True) == '1'
    assert get_shortish_repr(1, max_length=5) == '1'
    assert get_shortish_repr(1, max_length=5, normalize=True) == '1'
    assert get_shortish_repr((1,2,3), max_length=5) == '(1, 2, 3)'
    assert get_shortish_repr((1,2,3), max_length=5, normalize=True) == '(1, 2, 3)'
    assert get_shortish_repr((1,2,3), max_length=20, normalize=True) == '(1, 2, 3)'
    assert get_shortish

# Generated at 2022-06-12 19:59:18.042208
# Unit test for function get_repr_function
def test_get_repr_function():
    class ThingA(object): pass
    class ThingB(object): pass

    custom_repr = ((lambda item: isinstance(item, ThingA),
                    lambda item: 'A'),)
    assert get_repr_function(ThingB(), custom_repr) is repr
    assert get_repr_function(ThingA(), custom_repr) is not repr
    assert get_repr_function(ThingA(), custom_repr)(ThingA()) == 'A'



# Generated at 2022-06-12 19:59:28.220565
# Unit test for function get_repr_function
def test_get_repr_function():
    class X(object):
        def __repr__(self):
            return 'yup'
    x = X()
    assert get_repr_function(x) is repr
    assert get_repr_function(x, custom_repr=[]) is repr
    assert get_repr_function(x, custom_repr=[(X, 'nope')]) == 'nope'
    assert get_repr_function(x, custom_repr=[(X, 'nope')],
                             normalize=True) == 'nope'
    assert get_repr_function(x, custom_repr=[(X, lambda x: 'nope')]) == 'nope'

# Generated at 2022-06-12 19:59:31.069609
# Unit test for function shitcode
def test_shitcode():
    assert shitcode(b'hell\x00o') == 'hell?o'
    assert shitcode('hell\x00o') == 'hell?o'



# Generated at 2022-06-12 19:59:34.406362
# Unit test for function get_repr_function
def test_get_repr_function():
    x = 5
    assert get_repr_function(x, ()) is repr
    def r(x):
        return 'r({})'.format(x)
    assert get_repr_function(x, ((int, r),)) is r



# Generated at 2022-06-12 19:59:42.562831
# Unit test for function truncate
def test_truncate():
    assert truncate('abcdefg', None) == 'abcdefg'
    assert truncate('abcdefg', 5) == 'abcde'
    assert truncate('abcdefg', 6) == 'abcdefg'
    assert truncate('abcdefg', 7) == 'abcdefg'
    assert truncate('abcdefg', 8) == 'abcdefg'
    assert truncate('abcdefg', 9) == 'abcdefg'
    assert truncate('abcdefg', 10) == 'abcdefg'
    assert truncate('abcdefg', 11) == 'abcdefg'
    assert truncate('abcdefg', 12) == 'abcdefg'


if __name__ == '__main__':
    from .testing import test_if
    test_if(__name__, sys.argv)

# Generated at 2022-06-12 19:59:52.869494
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A:
        def write(self, x):
            return 'A'

    class B(A):
        def write(self, x):
            return 'B'

    class C(B):
        pass


    assert issubclass(A, WritableStream)
    assert issubclass(B, WritableStream)
    assert issubclass(C, WritableStream)


    assert isinstance(A(), WritableStream)
    assert isinstance(B(), WritableStream)
    assert isinstance(C(), WritableStream)

    assert A().write(None) == 'A'
    assert B().write(None) == 'B'
    assert C().write(None) == 'B'

    with raises(TypeError):
        class D(A):
            pass
        D()


# Generated at 2022-06-12 20:00:00.827145
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(Exception(), ((1, repr),)) is repr
    assert get_repr_function(Exception(), ((Exception, str),)) is str
    assert get_repr_function(Exception(), ((Exception, None),)) is repr
    assert get_repr_function(Exception(), ((Exception, Exception),)) is repr
    assert get_repr_function(Exception(), ((Exception, ValueError),)) is repr
    assert get_repr_function(Exception(), ((ValueError, ValueError),)) is repr
    assert get_repr_function(Exception(), ((ValueError, Exception),)) is repr
    assert get_repr_function(Exception(), ((Exception, None), (ValueError, None),)) is repr
    assert get_repr_function(Exception(), ((ValueError, None), (Exception, None),)) is repr
    assert get

# Generated at 2022-06-12 20:00:10.382615
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(
        5,
        [(lambda x: type(x) == bool, lambda x: 'bool'),
         (lambda x: type(x) == int, lambda x: 'int'),
        ]
    )(5) == 'int'
    assert get_repr_function(
        False,
        [(lambda x: type(x) == bool, lambda x: 'bool'),
         (lambda x: type(x) == int, lambda x: 'int'),
        ]
    )(False) == 'bool'

# Generated at 2022-06-12 20:00:16.624067
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    class Foo(object):
        def __repr__(self):
            return "This is Foo's representation"

    foo = Foo()
    assert get_shortish_repr(foo) == "This is Foo's representation"
    assert get_shortish_repr('abc') == "abc"
    assert get_shortish_repr('abcdefghijklmnopqrstuvwxyz',
                             max_length=10) == '...stuvwxyz'



# Generated at 2022-06-12 20:00:21.685053
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    """
    Make sure that `WritableStream` gets us the correct behavior.

    This is a unit-test for the class `WritableStream`.
    """
    class A(WritableStream):
        def write(self, s):
            raise NotImplementedError
    assert isinstance(A(), WritableStream)

    class B(WritableStream):
        pass
    assert not isinstance(B(), WritableStream)

    class C(WritableStream):
        def write(self, s):
            pass
    assert isinstance(C(), WritableStream)





# Generated at 2022-06-12 20:00:32.183521
# Unit test for function get_repr_function
def test_get_repr_function():
    class A(object):
        pass
    class B(A):
        pass
    a = A()
    b = B()
    c = 1
    d = '2'

    assert get_repr_function(a, [(A, 'a_repr')]) == 'a_repr'
    assert get_repr_function(b, [(A, 'a_repr')]) == 'a_repr'
    assert get_repr_function(c, [(A, 'a_repr')]) is repr
    assert get_repr_function(d, [(A, 'a_repr')]) is repr

    custom_repr = (
        (A, 'a_repr'),
        (lambda x: True, 'true_repr'),
    )

# Generated at 2022-06-12 20:00:34.417321
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def write(self, s):
            pass

    assert issubclass(MyWritableStream, WritableStream)



# Generated at 2022-06-12 20:00:45.979825
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(10, custom_repr=[(int, 'int')]) == 'int'
    assert get_repr_function((1, 2, 3), custom_repr=[(tuple, 'tuple')]) == 'tuple'
    assert get_repr_function(10, custom_repr=[(tuple, 'tuple')]) == repr
    assert get_repr_function(10, custom_repr=[(tuple, 'tuple'),
                                              (int, 'int')]) == 'int'
    assert get_repr_function(10, custom_repr=[(tuple, 'tuple'),
                                              (lambda x: True, 'lambda')]) == \
           'lambda'

# Generated at 2022-06-12 20:00:49.855047
# Unit test for function shitcode
def test_shitcode():
    assert shitcode('abcd') == 'abcd'
    assert shitcode('Абцд') == '????'
    assert shitcode('\0\1\2\3') == '???'
    assert shitcode('\0\1\2\3Абцд') == '???????'

# Generated at 2022-06-12 20:01:00.809399
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Base(object):
        pass
    class A(WritableStream, Base):
        def write(self, s):
            pass
    class B(object):
        pass
    class C(WritableStream):
        def write(self, s):
            pass
    class D(WritableStream, object):
        def write(self, s):
            pass
    class E(WritableStream, object):
        pass
    class F(WritableStream):
        pass

    assert issubclass(A, WritableStream)
    assert issubclass(C, WritableStream)
    assert issubclass(D, WritableStream)
    assert not issubclass(B, WritableStream)
    assert not issubclass(Base, WritableStream)
    assert not issubclass(E, WritableStream)
    assert not issub

# Generated at 2022-06-12 20:01:10.354978
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    from .testing.common import (
        assert_equal, assert_true, assert_false, assert_raises
    )

    assert_equal(get_shortish_repr(None), 'None')

    assert_equal(get_shortish_repr(1), '1')
    assert_equal(get_shortish_repr('abcdef'), "'abcdef'")
    assert_equal(get_shortish_repr([1, 2, 3]), '[1, 2, 3]')
    assert_true('0x' not in get_shortish_repr([1, 2, 3]))
    assert_equal(get_shortish_repr(set(['a', 'b'])), "set(['a', 'b'])")

# Generated at 2022-06-12 20:01:16.900051
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class FakeWritableStream:
        def write(self, s):
            assert isinstance(s, str)
    assert isinstance(FakeWritableStream(), WritableStream)
    class NastyFakeWritableStream:
        def write(self, s):
            pass
        def foobar(self):
            pass
    assert not isinstance(NastyFakeWritableStream(), WritableStream)

# Generated at 2022-06-12 20:01:21.129804
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class FileLike(WritableStream):
        def __init__(self, file_obj):
            self.file_obj = file_obj

        def write(self, s):
            self.file_obj.write(s)

    file_like = FileLike(sys.stdout)
    file_like.write('hello world')

# Generated at 2022-06-12 20:01:24.555987
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class FakeWritableStream(WritableStream):
        def write(self, x):
            return x
    fake_writable_stream = FakeWritableStream()
    assert fake_writable_stream.write(3) == 3



# Generated at 2022-06-12 20:01:32.473152
# Unit test for function get_repr_function
def test_get_repr_function():
    x = (1, 2, 3)
    assert get_repr_function(x) == repr
    assert get_repr_function(x, custom_repr=(
        (lambda y: y == x, lambda y: 'satisfying!'),
    )) == (lambda y: 'satisfying!')
    assert get_repr_function(x, custom_repr=(
        ((lambda y: y == x), lambda y: 'satisfying!'),
    )) == (lambda y: 'satisfying!')
    assert get_repr_function(x, custom_repr=(
        (type(x), lambda y: 'satisfying!'),
    )) == (lambda y: 'satisfying!')



# Generated at 2022-06-12 20:01:35.565197
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    pyi_stdout = sys.stdout
    pyi_stderr = sys.stderr
    # no tests for user-defined methods in classes

# Generated at 2022-06-12 20:01:45.169981
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyStream(WritableStream):
        def write(self, s):
            pass

    stream = MyStream()
    assert isinstance(stream, WritableStream)

    class MyStream(WritableStream):
        def write(self):
            pass

    stream = MyStream()
    if sys.version_info[:2] >= (3, 5):
        assert not issubclass(MyStream, WritableStream)
    else:
        # Python 3.4 doesn't support single dispatch, so I didn't implement it
        # here.
        assert issubclass(MyStream, WritableStream)

    class MyStream(WritableStream):
        def write(self, s, t):
            pass

    stream = MyStream()

# Generated at 2022-06-12 20:01:47.367754
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Foo(WritableStream):
        def write(self, s):
            pass

    class Bar:
        pass

    assert issubclass(Foo, WritableStream)
    assert not issubclass(Bar, WritableStream)



# Generated at 2022-06-12 20:01:50.566928
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(WritableStream):
        def write(self, s):
            pass

    assert WritableStream.__subclasshook__(A) is True



# Generated at 2022-06-12 20:01:59.564003
# Unit test for function get_repr_function
def test_get_repr_function():
    def custom_repr_bool(x):
        return 'Yes!' if x else 'No!'
    def custom_repr_int(x):
        return 'No. {}'.format(x)
    custom_repr = (
        (lambda x: isinstance(x, bool), custom_repr_bool),
        (int, custom_repr_int),
    )
    repr_function = get_repr_function(True, custom_repr)
    assert repr_function(True) == 'Yes!'
    repr_function = get_repr_function(1, custom_repr)
    assert repr_function(1) == 'No. 1'
    repr_function = get_repr_function('hi', custom_repr)
    assert repr_function('hi') == "'hi'"



# Generated at 2022-06-12 20:02:11.394777
# Unit test for function get_repr_function
def test_get_repr_function():
    class A:
        pass
    class B(A):
        pass
    class C(B):
        pass

    a = A()
    b = B()
    c = C()

    f = lambda x: 'f ' + x
    g = lambda x: 'g ' + x

    assert get_repr_function(a, ((f, g), (B, lambda x: 'lambda'),
                                 (B, 'lambda'))) == f
    assert get_repr_function(b, ((f, g), (B, lambda x: 'lambda'),
                                 (B, 'lambda'))) == g

# Generated at 2022-06-12 20:02:15.577724
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def write(self, s):
            self.s = s
    my_writable_stream = MyWritableStream()
    my_writable_stream.write('hello world')
    assert my_writable_stream.s == 'hello world'

# Generated at 2022-06-12 20:02:19.658910
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Foo:
        def write(self, s):
            pass
    assert issubclass(Foo, WritableStream)
    f = Foo()
    f.write('')
    assert not issubclass(dict, WritableStream)
    assert not issubclass(list, WritableStream)




# Generated at 2022-06-12 20:02:29.658070
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    import sys
    import contextlib

    class CustomStream(io.TextIOBase):
        def write(self, s):
            return len(s)

    def test_write_method(s):
        assert isinstance(s, WritableStream)
        s.write('abc')
        return True

    assert test_write_method(sys.stdout)
    assert test_write_method(sys.stderr)
    assert test_write_method(CustomStream())

    @contextlib.contextmanager
    def temp_file():
        import tempfile
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            yield f.name

# Generated at 2022-06-12 20:02:38.767528
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class ScrappyWriter(WritableStream):
        pass

    class MyWriter(WritableStream):
        opened_files = []
        def __init__(self, *args, **kwargs):
            MyWriter.opened_files.append(self)
        def write(self, s):
            return 'S' * len(s)
        def my_method(self):
            return True

    assert MyWriter not in WritableStream.__subclasses__()
    assert MyWriter.__subclasshook__(MyWriter)
    assert MyWriter in WritableStream.__subclasses__()
    assert MyWriter.__subclasshook__(ScrappyWriter) is NotImplemented

    mw = MyWriter(1, 2, 3, x=1)
    assert mw.write('a') == 'S'

# Generated at 2022-06-12 20:02:41.920574
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class DummyA(WritableStream):
        def write(self, s):
            self.s = s

    class DummyB:
        pass

    assert isinstance(DummyA(), WritableStream)
    assert not isinstance(DummyB(), WritableStream)



# Generated at 2022-06-12 20:02:43.575434
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class F(WritableStream):
        def write(self, s):
            pass
    F()




# Generated at 2022-06-12 20:02:47.645438
# Unit test for function get_repr_function
def test_get_repr_function():
    from . import garbage_collecting_object
    n = garbage_collecting_object.GarbageCollectingObject()

    assert get_repr_function(n, []) == repr
    assert get_repr_function(n, [(lambda x: False, 'yo')]) == repr
    assert get_repr_function(n, [(lambda x: True, 'yo')]) == 'yo'

    assert get_repr_function(n, [
        (lambda x: True, 'yo'),
        (lambda x: False, 'yo'),
    ]) == 'yo'

    assert get_repr_function(n, [
        (lambda x: True, 'yo'),
        (lambda x: True, 'yo'),
    ]) == 'yo'


# Generated at 2022-06-12 20:02:50.248441
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class writer(object):
        def __init__(self):
            self.written = ''
        def write(self, s):
            self.written += s

    w = writer()
    w.write('foo')
    assert w.written == 'foo'

# Generated at 2022-06-12 20:02:55.453181
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class WritableStringStream(WritableStream):
        def __init__(self):
            self.written_string = ''

        def write(self, s):
            self.written_string += s

    writable_string_stream = WritableStringStream()
    writable_string_stream.write('foo')
    assert writable_string_stream.written_string == 'foo'

# Generated at 2022-06-12 20:03:01.820772
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(WritableStream):
        def write(self, s):
            pass
    class B(A):
        pass
    assert issubclass(A, WritableStream)
    assert issubclass(B, WritableStream)

# Generated at 2022-06-12 20:03:09.118565
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    def normalize_repr_test_object(self):
        return '<self>'
    class NormalizeReprTest(object):
        def __repr__(self):
            return normalize_repr_test_object(self)

    # Normalize repr for types inheriting from `object`
    assert get_shortish_repr(NormalizeReprTest(), normalize=True) == \
                                                                   '<self>'

    # Truncate non-normalized repr
    assert get_shortish_repr(NormalizeReprTest(), max_length=5,
                             normalize=False) == '<se...>'

    # Truncate normalized repr

# Generated at 2022-06-12 20:03:18.756662
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io

    class MyWritableStream(io.StringIO, WritableStream):
        pass

    class MyOtherWritableStream(io.TextIOBase, WritableStream):
        def __init__(self):
            self.written_data = ''

        def write(self, s):
            self.written_data += s

    assert issubclass(MyWritableStream, WritableStream)
    assert issubclass(MyOtherWritableStream, WritableStream)
    assert not issubclass(io.TextIOBase, WritableStream)

    writable_stream = MyWritableStream()
    writable_stream.write('spam')
    assert writable_stream.getvalue() == 'spam'

# Generated at 2022-06-12 20:03:25.598273
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    class MyWritableStream(WritableStream):
        def __init__(self):
            self.written_stuff = []
        def write(self, s):
            self.written_stuff.append(s)
    x = MyWritableStream()
    WritableStream.register(io.StringIO)
    assert issubclass(io.StringIO, WritableStream)  # io.StringIO should be
    # seen as a subclass of WritableStream.
    y = io.StringIO()
    assert isinstance(x, WritableStream)
    assert isinstance(y, WritableStream)
    x.write('hello, world!')
    y.write('hello, world!')
    assert x.written_stuff == ['hello, world!']
    assert y.getvalue() == 'hello, world!'

# Generated at 2022-06-12 20:03:30.824921
# Unit test for function get_repr_function
def test_get_repr_function():
    class Foo(object): pass
    class Bar(Foo): pass
    class Baz(object): pass

    custom_repr={int: lambda x: "not an integer"}

    assert get_repr_function(Foo(), custom_repr) is repr
    assert get_repr_function(Bar(), custom_repr) is repr
    assert get_repr_function(Baz(), custom_repr) is repr

    assert get_repr_function(1, custom_repr) is int
    assert get_repr_function(2, custom_repr) is int
    assert get_repr_function(3, custom_repr) is int
    assert get_repr_function(1.1, custom_repr) is repr
    assert get_repr_function(2.2, custom_repr) is repr

# Generated at 2022-06-12 20:03:40.703701
# Unit test for function get_repr_function
def test_get_repr_function():
    class A:
        pass
    class B(A):
        def __repr__(self):
            return '__repr__ of B'
    class C:
        def __repr__(self):
            return '__repr__ of C'
    class D(B):
        pass
    class E(C):
        pass

    assert get_repr_function(A(), ()) == repr
    assert get_repr_function(B(), ()) == B.__repr__
    assert get_repr_function(C(), ()) == C.__repr__
    assert get_repr_function(D(), ()) == B.__repr__
    assert get_repr_function(E(), ()) == C.__repr__


# Generated at 2022-06-12 20:03:49.088813
# Unit test for function get_shortish_repr
def test_get_shortish_repr():

    from .test_tools import assert_equal

    class MyObject(object):

        def __init__(self, x):
            self.x = x

        def __repr__(self):
            return 'repr: %s' % self.x

    class MyOtherObject(object):

        def __init__(self, x):
            self.x = x

    class MyException(Exception):
        pass


    def my_repr_function(my_object):
        my_object.repr_was_called = True
        return 'this is my repr'


    assert_equal(get_shortish_repr(''), "''")
    assert_equal(get_shortish_repr(1), '1')

# Generated at 2022-06-12 20:03:54.873756
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, custom_repr=[]) is repr
    assert get_repr_function(1, custom_repr=[(int, str)]) is str
    assert get_repr_function(1, custom_repr=[(int, id)]) is id
    assert get_repr_function(1, custom_repr=[(lambda x: x==1, str),
                                             (int, id)]) is str



# Generated at 2022-06-12 20:04:01.862063
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    class Thingy(object):
        def __init__(self, name):
            self.name = name

        def __repr__(self):
            return self.name

    thingy1 = Thingy('fred')
    assert get_shortish_repr(thingy1, max_length=4) == 'fre...'
    assert get_shortish_repr(thingy1, max_length=5) == 'fred?'

    thingy2 = Thingy('barney')
    assert get_shortish_repr(thingy2) == 'barney'

    thingy3 = Thingy('gumbo')
    assert get_shortish_repr(thingy3, max_length=2) == 'g...'



# Generated at 2022-06-12 20:04:09.941958
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(0, ()) == repr

    custom_repr = (
        (lambda x: isinstance(x, int), lambda x: 'int:' + str(x)),
        (lambda x: isinstance(x, str), lambda x: 'string:' + x),
    )

    assert get_repr_function(0, custom_repr) == custom_repr[0][1]
    assert get_repr_function('', custom_repr) == custom_repr[1][1]
    assert get_repr_function([], custom_repr) == repr
    assert get_repr_function(None, custom_repr) == repr

    assert get_repr_function(0, custom_repr) == 'int:0'

# Generated at 2022-06-12 20:04:15.342187
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Stream(WritableStream):
        def write(self, s):
            return s
    assert Stream().write('Hello, world!') == 'Hello, world!'



# Generated at 2022-06-12 20:04:17.779890
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A:
        def write(self, s):
            return 'a' in s.lower()

    assert issubclass(A, WritableStream)

    assert A().write('abc')

    class B:
        pass

    assert not issubclass(B, WritableStream)

    assert not A().write('def')



# Generated at 2022-06-12 20:04:21.852909
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(WritableStream): pass
    assert WritableStream.__subclasshook__(A) is NotImplemented

    class B(object):
        def write(self, x): pass

    assert  WritableStream.__subclasshook__(B) is True



# Generated at 2022-06-12 20:04:29.620421
# Unit test for function get_repr_function
def test_get_repr_function():

    custom_repr = [
        (int, lambda i: 'int: {}'.format(i)),
        (dict, lambda d: 'dict: {}'.format(d)),
        (lambda x: True, lambda x: 'x: {}'.format(x)),
    ]

    def assert_get_repr_function(item, expected_repr):
        repr_function = get_repr_function(item, custom_repr)
        assert repr_function(item) == expected_repr

    assert_get_repr_function(0, 'int: 0')
    assert_get_repr_function(1, 'int: 1')
    assert_get_repr_function(1.0, 'x: 1.0')
    assert_get_repr_function({}, 'dict: {}')
    assert_get_re

# Generated at 2022-06-12 20:04:40.967254
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(1) == '1'
    assert get_shortish_repr(1, max_length=2) == '1'
    assert get_shortish_repr(1, max_length=1) == '1'
    assert get_shortish_repr([], max_length=2) == '[]'
    assert get_shortish_repr([1], max_length=2) == '[1]'
    assert get_shortish_repr([1], max_length=1) == '[1]'
    assert get_shortish_repr([1], max_length=0) == '[1]'
    assert get_shortish_repr([1, 2], max_length=2) == '[1, 2]'

# Generated at 2022-06-12 20:04:50.802340
# Unit test for function get_shortish_repr
def test_get_shortish_repr():

    assert get_shortish_repr(1) == '1'
    assert get_shortish_repr('Hello world') == "'Hello world'"

    assert get_shortish_repr('Hello world!', max_length=5) == "'Hel...'"

    long_string = 'abcd' * 1000 + '?!'
    assert get_shortish_repr(long_string) == long_string
    assert get_shortish_repr(long_string,
                             max_length=12) == 'abcdabcdab...'

    class Thingy(object):
        def __repr__(self):
            return 'thingy'

    class OtherThingy(object):
        def __repr__(self):
            return 'otherthingy'
            raise Exception


# Generated at 2022-06-12 20:04:52.751587
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def write(self, s):
            return s

    assert MyWritableStream()



# Generated at 2022-06-12 20:04:57.978865
# Unit test for function get_repr_function
def test_get_repr_function():
    class A: pass
    class B(A): pass
    class C(A): pass
    b = B()
    c = C()
    assert get_repr_function(b, [(A, str)])(b) == 'B object'
    assert get_repr_function(c, [(A, str)])(c) == 'C object'
    assert get_repr_function(b, [(B, str), (A, 'default')])(b) == 'B object'
    assert get_repr_function(c, [(B, str), (A, 'default')])(c) == 'default'

# Generated at 2022-06-12 20:05:07.808801
# Unit test for function get_repr_function
def test_get_repr_function():
    from .cute_iter_tools import my_repr

    custom_repr = (
        (int, str),
        (lambda x: x == 2, lambda x: 'two'),
        (lambda x: x == 3, lambda x: 'three'),
    )

    assert get_repr_function(1, custom_repr) is str
    assert get_repr_function(2, custom_repr) is custom_repr[1][1]
    assert get_repr_function(3, custom_repr) is custom_repr[2][1]
    assert get_repr_function(4, custom_repr) is repr

    assert get_repr_function(1, custom_repr, my_repr) is my_repr



# Generated at 2022-06-12 20:05:17.724522
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(None, ()) == repr
    assert get_repr_function(0, ()) == repr
    assert get_repr_function(0.0, ()) == repr
    assert get_repr_function('', ()) == repr
    assert get_repr_function([], ()) == repr
    assert get_repr_function(tuple(), ()) == repr
    assert get_repr_function(dict(), ()) == repr
    assert get_repr_function(set(), ()) == repr

    def some_function(x):
        return 42

    assert get_repr_function(some_function, ()) == repr

    def some_function1(x):
        return 42

    def custom_repr_function(x):
        return 'foo'


# Generated at 2022-06-12 20:05:25.888332
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def __init__(self):
            self.written_lines = []
        def write(self, s):
            self.written_lines.append(s)

    ws = MyWritableStream()
    ws.write('foo')
    assert ws.written_lines == ['foo']

# Generated at 2022-06-12 20:05:30.222192
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MockFile(WritableStream):
        def __init__(self):
            self.written_to = False

        def write(self, s):
            self.written_to = True

    mock_file = MockFile()
    mock_file.write('foo')
    assert mock_file.written_to

# Generated at 2022-06-12 20:05:41.085422
# Unit test for function get_repr_function
def test_get_repr_function():
    # (item, custom_repr, expected_output)
    tests = [
        (1, (), repr),
        (2j, (), repr),
        (1, ((int, str), lambda x: '-1'), str),
        (1j, ((int, str), lambda x: '-1'), repr),
        (1j, ((int, str), lambda x: '-1'), lambda x: 'great success',
         lambda x: 'great success'),
    ]
    for (item, custom_repr, expected_output) in tests:
        output = get_repr_function(item, custom_repr)
        assert output == expected_output, (item, custom_repr, output,
                                               expected_output)

# Generated at 2022-06-12 20:05:47.449586
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    from .exception_handling import ExceptionRecord, ExceptionLog
    from .colored import colored
    from .output_streams import ColoredOutputStream
    exception_log = ExceptionLog()
    exception_log.exception_records = [
        ExceptionRecord(
            exception=ValueError('Hello world!'),
            stack=('test_exception_log_writer.py', 4, 'test_not_a_number',
                                                                         None))
    ]
    exception_log.exception_records.append(
        ExceptionRecord(
            exception=ValueError('Hello world, again!'),
            stack=('test_exception_log_writer.py', 4, 'test_not_a_number',
                                                                         None))
    )

    def write(s):
        assert isinstance(s, string_types)
       

# Generated at 2022-06-12 20:05:56.405054
# Unit test for function get_repr_function
def test_get_repr_function():
    def func(x):
        return 'func'

    class C:
        pass

    class D(C):
        pass

    class E(object):
        pass

    assert get_repr_function(1, ()) == repr
    assert get_repr_function(1, ((lambda x: False, 'fail'),)) == repr

    assert get_repr_function(1, ((1, func),)) == func
    assert get_repr_function(1, ((int, func),)) == func
    assert get_repr_function('1', ((int, func),)) == repr

    assert get_repr_function(C(), ((C, func),)) == func
    assert get_repr_function(D(), ((C, func),)) == func
    assert get_repr_function(D(), ((D, func),)) == func

# Generated at 2022-06-12 20:06:00.919330
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(object):
        def write(self, s):
            pass

    class B(WritableStream):
        def write(self, s):
            pass

    a = A()
    b = B()
    assert isinstance(a, WritableStream)
    assert isinstance(b, WritableStream)



# Generated at 2022-06-12 20:06:10.037621
# Unit test for function get_shortish_repr
def test_get_shortish_repr():

    # Let's not go crazy here
    r = get_shortish_repr(range(10**10), max_length=1000)
    assert r.endswith('...)]')
    assert len(r) >= 1000

    r = get_shortish_repr(range(10**10), max_length=1000, normalize=True)
    assert r.endswith('...]')
    assert len(r) >= 1000

    class Thing(object):
        def __repr__(self):
            return 'my_repr'

    r = get_shortish_repr(Thing(), max_length=1000)
    assert r == 'my_repr'

    r = get_shortish_repr(Thing(), max_length=1000, normalize=True)
    assert r == 'my_repr'

   

# Generated at 2022-06-12 20:06:17.524767
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class X:
        def write(self, s):
            return s

    assert isinstance(X, WritableStream)

    class Y:
        def write(self, s):
            return s
        def write_something_else(self, s):
            return s

    assert isinstance(Y, WritableStream)

    class Z:
        def write(self, s):
            return s
        def something_else(self, s):
            return s

    assert not isinstance(Z, WritableStream)

    class A:
        def xyz(self, s):
            return s
        def write(self, s):
            return s

    assert isinstance(A, WritableStream)

    class B:
        def xyz(self, s):
            return s
        def write(self, s):
            return s


# Generated at 2022-06-12 20:06:22.413604
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class WritableStreamGood(WritableStream):
        def write(self, s):
            print(s)

    class WritableStreamBad1(WritableStream):
        def close(self):
            pass

    class WritableStreamBad2(WritableStream):
        pass

    assert WritableStreamGood.__subclasshook__(WritableStreamGood)
    assert not WritableStreamGood.__subclasshook__(WritableStreamBad1)
    assert not WritableStreamGood.__subclasshook__(WritableStreamBad2)

# Generated at 2022-06-12 20:06:23.913120
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A:
        def write(self, s):
            pass
    assert isinstance(A(), WritableStream)

# Generated at 2022-06-12 20:06:33.622329
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    class MyClass(object):
        def __repr__(self):
            return '<MyClass %x>' % id(self)
    my_object = MyClass()
    assert get_shortish_repr(my_object, max_length=20) == '<MyClass 000000>'
    assert get_shortish_repr(None, max_length=20) == 'None'
    assert get_shortish_repr(True, max_length=20) == 'True'
    assert get_shortish_repr(23, max_length=20) == '23'
    assert get_shortish_repr(23, max_length=2) == '23'
    assert get_shortish_repr(23, max_length=1) == '...'

# Generated at 2022-06-12 20:06:41.859286
# Unit test for function get_repr_function
def test_get_repr_function():
    class A(object): pass
    class B(A): pass
    
    def A_repr(x):
        return 'A_repr'
    def B_repr(x):
        return 'B_repr'
    
    a = A()
    b = B()
    
    assert get_repr_function(a, custom_repr=((A, A_repr), (B, B_repr))) is A_repr
    assert get_repr_function(b, custom_repr=((A, A_repr), (B, B_repr))) is B_repr



# Generated at 2022-06-12 20:06:46.785524
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class TestWritableStream(WritableStream):
        def __init__(self):
            self.string = ''

        def write(self, s):
            self.string += s

    test_writable_stream = TestWritableStream()
    test_writable_stream.write('qwerty')
    assert test_writable_stream.string == 'qwerty'

# Generated at 2022-06-12 20:06:54.683154
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(3.5, custom_repr=()) == repr

# Generated at 2022-06-12 20:07:04.997754
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, [])(1) == '1'
    assert get_repr_function(1, [(1, lambda: 'hi')])(1) == 'hi'
    assert get_repr_function(1, [(1, lambda: 'hi')])(2) == '2'
    assert get_repr_function(1, [(1, lambda: 'hi'), (2, lambda: 'oh')])(2) == 'oh'
    assert get_repr_function(1, [(1, lambda: 'hi')])('hi') == 'hi'
    assert get_repr_function(1, [('hi', lambda: 'yay')])('hi') == 'yay'

# Generated at 2022-06-12 20:07:06.463790
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Foo:
        def write(self, s):
            pass
    assert issubclass(Foo, WritableStream)

# Generated at 2022-06-12 20:07:11.132908
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Foo(WritableStream):
        def __init__(self):
            self.contents = ''
        def write(self, s):
            self.contents += s
    foo = Foo()
    foo.write('hello ')
    foo.write('world!')
    assert foo.contents == 'hello world!'



# Generated at 2022-06-12 20:07:13.413362
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def write(self, s):
            pass

    assert issubclass(MyWritableStream, WritableStream)



# Generated at 2022-06-12 20:07:20.150869
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, [(int, lambda x: 'integer!'),
                                 (str, lambda x: 'string!')]) == str
    assert get_repr_function('a', [(int, lambda x: 'integer!'),
                                   (str, lambda x: 'string!')]) == repr
    assert get_repr_function([1, 2, 3], [(list, lambda x: 'list!')]) == repr
    assert get_repr_function({1, 2, 3}, [(list, lambda x: 'list!')]) == repr
    assert get_repr_function({1, 2, 3}, [(set, lambda x: 'set!')]) == str
    assert get_repr_function({1, 2, 3}, [(frozenset, lambda x: 'set!')]) == str



# Generated at 2022-06-12 20:07:24.048292
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    from contextlib import redirect_stdout
    from io import StringIO
    with StringIO() as string_io:
        with redirect_stdout(string_io):
            print('hello world')
        string_io.write('hello world')

# Generated at 2022-06-12 20:07:28.210922
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Foo(WritableStream):
        def write(self, s):
            return len(s)
    foo = Foo()
    assert foo.write('') == 0

# Generated at 2022-06-12 20:07:29.408656
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import sys
    sys.stdout = WritableStream()
    sys.stdout.write('hi')

# Generated at 2022-06-12 20:07:39.242563
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    repr_function = get_repr_function(None, [])
    assert repr_function == repr
    item = sys.modules[__name__]
    shortish_repr = get_shortish_repr(item)
    assert shortish_repr.startswith('<module ')
    assert shortish_repr.endswith(' at...')
    assert len(shortish_repr) <= 40
    item = open(__file__)
    shortish_repr = get_shortish_repr(item)
    assert shortish_repr.startswith('<open file ')
    assert shortish_repr.endswith(' at...>')
    assert len(shortish_repr) <= 40
    item = 'hi'

# Generated at 2022-06-12 20:07:41.015557
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class WritableStreamTest(WritableStream):
        def write(self, s):
            pass

    WritableStreamTest()



# Generated at 2022-06-12 20:07:43.908530
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class StdoutStream(object): pass # TODO: delete this line and implement
    # method `write` of `StdoutStream` to make mypy happy.
    assert isinstance(WritableStream.__subclasshook__(StdoutStream), bool)



# Generated at 2022-06-12 20:07:49.004874
# Unit test for function get_repr_function
def test_get_repr_function():
    class A(object):
        pass
    class B(object):
        pass
    class C(A):
        pass
    a = A()
    b = B()
    c = C()
    assert get_repr_function(a, ((B, lambda *args: 'B'), (A, lambda *args: 'A'))) == 'A'
    assert get_repr_function(b, ((B, lambda *args: 'B'), (A, lambda *args: 'A'))) == 'B'
    assert get_repr_function(c, ((B, lambda *args: 'B'), (A, lambda *args: 'A'))) == 'A'




# Generated at 2022-06-12 20:07:56.789393
# Unit test for function get_repr_function
def test_get_repr_function():
    class A: pass
    class B(A): pass
    class C(B): pass
    class D(C): pass

# Generated at 2022-06-12 20:08:03.582233
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import six
    class _TestWritableStream(WritableStream):
        def __init__(self):
            self.written = None
        def write(self, s):
            self.written = s

    x = _TestWritableStream()
    assert isinstance(x, WritableStream)
    assert WritableStream in [base.__name__ for base in _TestWritableStream.__bases__]
    assert WritableStream in [base.__name__ for base in _TestWritableStream.__mro__]
    x.write('hi')
    assert x.written == 'hi'



# Generated at 2022-06-12 20:08:11.623838
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('hello') == "'hello'"
    assert get_shortish_repr(1) == '1'
    assert len(get_shortish_repr([1, 'hello', [3, 4]])) < 25
    assert get_shortish_repr(b'hello') == "b'hello'"
    assert get_shortish_repr(1) == '1'
    assert len(get_shortish_repr([1, 'hello', [3, 4]])) < 25
    assert get_shortish_repr(1, max_length=5) == '1'
    assert get_shortish_repr('hello world', max_length=5) == "'h...'"
    assert get_shortish_repr('hello world', max_length=11) == "'hello wor...'"
   

# Generated at 2022-06-12 20:08:15.375520
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class BogusWritableStream:
        pass

    class MyWritableStream(WritableStream):
        def write(self, s):
            pass

    assert issubclass(MyWritableStream, WritableStream)
    assert not issubclass(BogusWritableStream, WritableStream)

# Generated at 2022-06-12 20:08:20.765576
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class TestWritableStream(WritableStream):
        def write(self, s):
            return s
    assert isinstance(TestWritableStream(), WritableStream)
    TestWritableStream().write('blah')



# Generated at 2022-06-12 20:08:24.620885
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def __init__(myself):
            myself.written_stuff = ''
        def write(myself, s):
            myself.written_stuff += s

    mws = MyWritableStream()
    mws.write('spam')
    assert mws.written_stuff == 'spam'

# Generated at 2022-06-12 20:08:29.739516
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function('hi', custom_repr=((str, 'a'), (list, 'b'))) == repr
    assert get_repr_function('hi', custom_repr=((str, 'a'),))('hi') == 'a'
    assert get_repr_function('hi', custom_repr=((int, 'a'),))('hi') == repr
    assert get_repr_function('hi', custom_repr=((int, 'a'),))(1) == 'a'



# Generated at 2022-06-12 20:08:31.110387
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Woof(WritableStream):
        def write(self, s):
            pass
    assert issubclass(Woof, WritableStream)



# Generated at 2022-06-12 20:08:41.446068
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('abc') == "'abc'"
    assert get_shortish_repr('abc', max_length=3) == "'a...'"
    assert get_shortish_repr(['abc'], max_length=9) == "['abc']"
    assert get_shortish_repr(['abcd'], max_length=9) == "['a...']"
    assert get_shortish_repr(('ab', 'cd'), max_length=9) == "('ab', 'cd')"
    assert get_shortish_repr(('ab', 'cdef'), max_length=9) == "('ab', '...')"
    assert get_shortish_repr({'abc': 123}, max_length=9) == "{'abc...': 123}"
    assert get_shortish_