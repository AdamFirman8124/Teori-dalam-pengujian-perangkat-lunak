

# Generated at 2022-06-12 19:58:39.101432
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class FakeStream(WritableStream):
        s = ''
        def write(self, s):
            self.s += s

    stream = FakeStream()

    stream.write('a')
    assert stream.s == 'a'
    stream.write('b')
    assert stream.s == 'ab'
    stream.write('c')
    assert stream.s == 'abc'
    stream.write('d')
    assert stream.s == 'abcd'



# Generated at 2022-06-12 19:58:42.998858
# Unit test for function get_repr_function
def test_get_repr_function():
    
    assert get_repr_function(1, ((lambda x: True, lambda x: 'x'))) == 'x'
    assert get_repr_function(1, ((lambda x: False, lambda x: 'x'))) == repr
    assert get_repr_function(1, ((int, lambda x: 'x'))) == 'x'
    assert get_repr_function(1, ((int, lambda x: 'x'), (int, lambda x: 2))) == 1


# Generated at 2022-06-12 19:58:46.468856
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(42, custom_repr=((int, str),)) == str
    assert get_repr_function(42.0, custom_repr=((int, str),)) == repr

test_get_repr_function()

# Generated at 2022-06-12 19:58:50.555087
# Unit test for function shitcode
def test_shitcode():
    assert shitcode('abcd') == 'abcd'
    assert shitcode('1234') == '1234'
    assert shitcode('\0') == '?'
    assert shitcode('\xff') == '?'
    assert shitcode('\x7f') == '?'
    assert shitcode('ab\xff\0cdef') == 'ab?\0cdef'



# Generated at 2022-06-12 19:58:54.873019
# Unit test for function get_repr_function
def test_get_repr_function():
    from .my_assert import assert_equal

    assert_equal(get_repr_function(1, [])(1), repr(1))

    assert_equal(get_repr_function(1, [(lambda x: (x == 1), lambda x: 'x')])(1),
                 'x')

    assert_equal(get_repr_function(1, [(bool, lambda x: 'x')])(1), 'x')

    assert_equal(get_repr_function(None, [(bool, lambda x: 'x')])(1), repr(1))



# Generated at 2022-06-12 19:58:58.218533
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class TestableWritableStream(WritableStream):
        pass
    TestableWritableStream.register(sys.stdout)
    assert TestableWritableStream.__subclasshook__(sys.stdout) is True



# Generated at 2022-06-12 19:59:00.620601
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    sio = io.StringIO()
    assert isinstance(sio, WritableStream)
    sio.write('')



# Generated at 2022-06-12 19:59:10.327695
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(b'12345678901234') == u'b\'12345678901234\''
    assert get_shortish_repr(b'12345678901234', max_length=13) == \
                                                u'b\'1234567890123\''
    assert get_shortish_repr(1234, max_length=3) == u'1234'
    assert get_shortish_repr('12345678901234', max_length=13) == \
                                                u'\'1234567890123\''
    assert get_shortish_repr('12345678901234', max_length=13, normalize=True) == \
                                               u'\'1234567890123\''

# Generated at 2022-06-12 19:59:21.411941
# Unit test for function get_shortish_repr
def test_get_shortish_repr():

    class Foo(object):
        def __init__(self):
            self.hue = 1


    class Bar(Foo):
        def __repr__(self):
            return 'huuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu'

    class FooBar(object):
        def __repr__(self):
            raise Exception()


    def test_all_types(repr_function, types, msg):
        for x in types:
            if x.__repr__ != repr_function:
                assert get_shortish_repr(x) == \
                       get_shortish_repr(x, custom_repr=((x, repr_function),)), \
                       (x, msg)

    class Hue(object):
        def __repr__(self):
            return 'hue'

# Generated at 2022-06-12 19:59:29.185031
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(WritableStream):
        def write(self, s):
            pass

    class B(A):
        pass

    assert issubclass(A, WritableStream)
    assert issubclass(B, WritableStream)

    class C(WritableStream):
        def flush(self):
            pass

    assert not issubclass(C, WritableStream)

    class D(WritableStream):
        pass

    assert not issubclass(D, WritableStream)

    class E(WritableStream):
        def write(self, s):
            pass
        def flush(self):
            pass

    assert issubclass(E, WritableStream)




# Generated at 2022-06-12 19:59:38.700815
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    global WritableStream

    class MyStream(WritableStream):
        def write(self, s):
            return

    def my_seld():
        global my_self
        my_self = MyStream()

    my_seld()
    my_self.write('ni')
    del my_self

    # TODO: Make sure that the object is not used after it's deleted



# Generated at 2022-06-12 19:59:43.388390
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Good(object, metaclass=ABCMeta):
        def write(self, s): pass

    class Bad(object, metaclass=ABCMeta):
        pass

    class ReallyBad(object, metaclass=ABCMeta):
        def write(self, s): pass
        write = None

    assert issubclass(Good, WritableStream)
    assert not issubclass(Bad, WritableStream)
    assert not issubclass(ReallyBad, WritableStream)

# Generated at 2022-06-12 19:59:52.620170
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function('x', ((str, str),)) is str
    assert get_repr_function(b'x', ((str, str),)) is not str
    assert get_repr_function(b'x', ((lambda x: isinstance(x, bytes),
                                     str))) is str
    assert get_repr_function(b'x', ((lambda x: isinstance(x, bytes),
                                     str),
                                    (lambda x: isinstance(x, int),
                                     str))) is str
    assert get_repr_function(b'x', ((lambda x: isinstance(x, int),
                                     str))) is not str
    assert get_repr_function(b'x', ()) is repr
    assert get_repr_function(1, ()) is repr
    assert get_repr_function

# Generated at 2022-06-12 19:59:55.555508
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1.0, [(float, 'hello')]) == 'hello'
    assert get_repr_function(1, [(float, 'hello')]) != 'hello'



# Generated at 2022-06-12 19:59:58.350712
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Empty: pass

    class A(Empty):
        def write(self, s):
            pass

    assert issubclass(A, WritableStream)

    class B(Empty): pass

    assert not issubclass(B, WritableStream)

# Generated at 2022-06-12 20:00:08.285462
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class WritableStreamImpl(WritableStream):
        def __init__(self, check_s_is_str=True):
            super(WritableStreamImpl, self).__init__()
            self.check_s_is_str = check_s_is_str

        def write(self, s):
            if self.check_s_is_str:
                assert isinstance(s, str), repr(s)
            else:
                assert isinstance(s, str), repr(s)

    assert isinstance(WritableStreamImpl(), WritableStream)
    assert isinstance(WritableStreamImpl(check_s_is_str=False), WritableStream)
    assert not isinstance(WritableStream.__subclasshook__, collections_abc.Callable)



# Generated at 2022-06-12 20:00:10.110727
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class SomeClass(object):
        def write(self, s):
            pass

    assert not isinstance(SomeClass(), WritableStream)

# Generated at 2022-06-12 20:00:12.934473
# Unit test for function shitcode
def test_shitcode():
    assert shitcode('Hello') == 'Hello'
    assert shitcode('Héllo') == 'H?llo'
    assert shitcode(u'H\u20acllo') == 'H?llo'




# Generated at 2022-06-12 20:00:20.155076
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('Hello world!', max_length=12) == 'Hello world!'
    assert get_shortish_repr('Hello world!', max_length=11) == 'Hello ...!'
    assert get_shortish_repr('Hello world!', max_length=8) == 'Hell...!'
    assert get_shortish_repr('Hello world!', max_length=5) == 'H...!'
    assert get_shortish_repr('Hello world!', max_length=4) == '...!'
    assert get_shortish_repr('Hello world!', max_length=3) == '...'



# Generated at 2022-06-12 20:00:22.611907
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class C:
        def write(self, s):
            pass
    assert issubclass(C, WritableStream)



# Generated at 2022-06-12 20:00:33.184652
# Unit test for function get_repr_function
def test_get_repr_function():

    def says_hi(x):
        return get_repr_function(x, (
            (lambda x: hasattr(x, 'hi'), lambda x: x.hi()),
            (lambda x: hasattr(x, 'bark'), repr),
        ))

    class X(object):
        def hi(self):
            return 'hi'
        def bark(self):
            pass

    assert says_hi(1)(1) == '1'
    assert says_hi(X())(X()) == 'hi'
    assert says_hi([1, 2, 3])([1, 2, 3]) == '[1, 2, 3]'

# Generated at 2022-06-12 20:00:35.555597
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(WritableStream):
        def write(self, s):
            assert isinstance(s, str)
            assert s == 'hello'

    A().write('hello')



# Generated at 2022-06-12 20:00:37.905784
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A:
        def write(self, s):
            pass
    class B:
        def foo(self):
            pass
    assert issubclass(A, WritableStream)
    assert not issubclass(B, WritableStream)



# Generated at 2022-06-12 20:00:46.776875
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class X(WritableStream):
        def write(self, s):
            assert isinstance(s, str)

    x = X()
    x.write('hi')

    try:
        class Y(WritableStream):
            def y(self):
                pass

        y = Y()
        y.write('hi')
        assert False
    except NotImplementedError:
        pass

    class Z(WritableStream):
        def write(self, s):
            assert isinstance(s, str)
        def __subclasshook__(self, _):
            return True

    z = Z()
    z.write('hi')

# Generated at 2022-06-12 20:00:53.301894
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(5, ((int, lambda x: 'x'))) == repr
    assert get_repr_function(5,
                            ((int, lambda x: 'x'),
                             (float, lambda x: 'y'))) == repr
    assert get_repr_function(5.5,
                            ((int, lambda x: 'x'),
                             (float, lambda x: 'y'))) == repr
    assert get_repr_function(5.5, ((float, lambda x: 'y'))) == repr
    assert get_repr_function(5, ((float, lambda x: 'y'))) == repr
    assert get_repr_function(5, ((int, lambda x: 'x'))) == repr

# Generated at 2022-06-12 20:00:56.347327
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(WritableStream):
        def write(self, s):
            print(s)
    class B(A):
        pass
    assert issubclass(A, WritableStream)
    assert issubclass(B, WritableStream)
    assert not issubclass(object, WritableStream)
    assert isinstance(A(), WritableStream)
    assert isinstance(B(), WritableStream)
    a = A()
    a.write('hi')
    b = B()
    b.write('ho')
    assert not isinstance(object(), WritableStream)


# ## Running doctests


# Generated at 2022-06-12 20:01:05.342421
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(None, ()) is repr
    assert get_repr_function(123, ()) is repr
    assert get_repr_function('abc', ()) is repr
    
    class A: pass
    class B(A): pass
    class C(A): pass
    assert get_repr_function(A(), ()) is repr
    assert get_repr_function(B(), ()) is repr
    assert get_repr_function(C(), ()) is repr

    class X: pass
    class Y(X): pass
    class Z(X): pass

    assert get_repr_function(X(), ((type(X), None),)) is None
    assert get_repr_function(Y(), ((type(X), None),)) is None
    assert get_repr_function(Z(), ((type(X), None),))

# Generated at 2022-06-12 20:01:13.470268
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Foo(WritableStream):
        def write(self, s): pass
    assert issubclass(Foo, WritableStream)
    class Bar(Foo):
        def foo(self): pass
    assert issubclass(Bar, WritableStream)
    class Baz(Foo):
        def write(self, s): pass
    assert issubclass(Baz, WritableStream)
    class Hello(object):
        def write(self, s): pass
    assert not issubclass(Hello, WritableStream)
    class Mars(Foo):
        pass
    assert issubclass(Mars, WritableStream)



# Generated at 2022-06-12 20:01:19.648048
# Unit test for function get_repr_function
def test_get_repr_function():

    # Built-in types
    from datetime import datetime
    from random import Random
    from decimal import Decimal
    from fractions import Fraction
    from collections import Counter

    now = datetime.now()
    random = Random(123)
    dec = Decimal('1.23')
    frac = Fraction(3, 5)
    counter = Counter([1, 2, 3])

    x = {1: 1, 2: 2, 3: 3}

    assert get_repr_function(now, ()) == repr
    assert get_repr_function(random, ()) == repr
    assert get_repr_function(dec, ()) == repr
    assert get_repr_function(frac, ()) == repr
    assert get_repr_function(counter, ()) == repr



# Generated at 2022-06-12 20:01:26.422945
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    if sys.platform == 'win32':
        # The next two lines are a workaround for a bug in Windows' `subprocess`
        # module. See https://github.com/garlicsim/garlicsim/issues/97
        import time
        time.sleep(0.1)

    import doctest
    doctest.testmod()


if __name__ == '__main__':
    test_get_shortish_repr()

# Generated at 2022-06-12 20:01:36.255007
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    def F(): pass
    def G(): pass
    class C: pass

    custom_repr = (('a', lambda x: "'my_string'"),
                   (F, lambda x: "F's repr"),
                   (G, lambda x: "G's repr"),
                   (C, lambda x: "C's repr"))

    assert get_shortish_repr(
        'a', custom_repr=custom_repr, max_length=None, normalize=False) == \
                                                                    "'my_string'"
    assert get_shortish_repr(
        'a', custom_repr=custom_repr, max_length=None, normalize=True) == \
                                                                    "'my_string'"

# Generated at 2022-06-12 20:01:45.682831
# Unit test for function get_repr_function
def test_get_repr_function():
    class A: pass
    class B(A): pass
    class C(B): pass
    class D(C): pass
    class E: pass

    a = A()
    b = B()
    c = C()
    d = D()
    e = E()

    custom_repr = (
        (A, lambda x: 'A'),
        (B, lambda x: 'B'),
        (lambda x: isinstance(x, (C, D)), lambda x: 'C or D'),
        (int, lambda x: 'int'),
    )


# Generated at 2022-06-12 20:01:50.958002
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class WritableStreamSubclass(WritableStream):
        def __init__(self):
            self.written = b''

        def write(self, s):
            self.written += s


    writable_stream = WritableStreamSubclass()
    writable_stream.write(b'Hello ')
    writable_stream.write(b'world!')
    assert writable_stream.written == b'Hello world!'

# Generated at 2022-06-12 20:01:59.752406
# Unit test for function get_repr_function
def test_get_repr_function():
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(B, C): pass
    class E(D): pass
    class F: pass
    class G(F): pass
    class H(F): pass
    class I(G, H): pass
    class J(D, I): pass

    assert get_repr_function(1, (type(1), lambda x: '`one`')) == '`one`'
    assert get_repr_function(None, (type(1), lambda x: '`one`')) == repr

    assert get_repr_function(B(), ((A,), lambda x: '`class A`')) == '`class A`'

# Generated at 2022-06-12 20:02:01.759089
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def write(self, s):
            pass
    assert issubclass(MyWritableStream, WritableStream)



# Generated at 2022-06-12 20:02:11.117581
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(5, ()) is repr
    assert get_repr_function(5, ((lambda x: True, str),)) is str
    assert get_repr_function(5, ((lambda x: False, str),)) is repr
    assert get_repr_function(5, ((lambda x: True, str), (lambda x: False,
                                                          str))) is str
    assert get_repr_function(5, ((lambda x: False, str), (lambda x: True,
                                                          str))) is str
    assert get_repr_function(5, ((int, str), (lambda x: True, str))) is str
    assert get_repr_function(5, ((lambda x: True, str), (int, str))) is str



# Generated at 2022-06-12 20:02:14.777416
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class FileLikeObject(WritableStream):

        def __init__(self):
            self.written = ''

        def write(self, s):
            self.written += s

    f = FileLikeObject()
    f.write('Hello')
    assert f.written == 'Hello'



# Generated at 2022-06-12 20:02:20.668827
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class TestWritableStream(WritableStream):
        def write(self, s):
            pass
    assert issubclass(TestWritableStream, WritableStream)

    class TestWritableStream:
        def write(self, s):
            pass
    assert not issubclass(TestWritableStream, WritableStream)

    class TestWritableStream(WritableStream):
        def write(self, s):
            pass
    assert issubclass(TestWritableStream, WritableStream)

    class TestWritableStream(WritableStream):
        pass
    assert not issubclass(TestWritableStream, WritableStream)

# Generated at 2022-06-12 20:02:25.346841
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Plain(WritableStream):
        def write(self, s):
            pass

    class Prefix(WritableStream):
        def write(self, s):
            pass

    assert isinstance(Plain(), WritableStream)
    assert isinstance(Prefix(), WritableStream)




# Generated at 2022-06-12 20:02:31.054244
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    # WritableStream.write(self, string) accepts a `string` and writes it with
    # `self.write(string)`.
    class MockWritableStream(WritableStream):
        def __init__(self, *args):
            self.written_items = []
        def write(self, s):
            self.written_items.append(s)
    mws = MockWritableStream()
    ws = WritableStream()
    ws.write(mws, 'dog')
    assert mws.written_items == ['dog']



# Generated at 2022-06-12 20:02:41.688424
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(123, []) is repr
    assert get_repr_function(321, [(int, str)]) is str
    assert get_repr_function('hello', [(str, bool)]) is bool
    assert get_repr_function(object(), [(object, bool)]) is bool
    assert get_repr_function('hello', [(lambda x: True, bool)]) is bool
    assert get_repr_function('hello', [(lambda x: False, bool)]) is repr
    assert get_repr_function('hello', [(1, bool)]) is repr



# Generated at 2022-06-12 20:02:46.594048
# Unit test for function get_repr_function
def test_get_repr_function():

    # Test `custom_repr` being a class
    assert get_repr_function('a', (str, str, )) == str

    # Test `custom_repr` being a function
    assert get_repr_function('a', ((str, ), str, )) == str

    # Test `custom_repr` being a lambda
    assert get_repr_function('a', ((lambda x: x == 'a', ), str, )) == str



# Generated at 2022-06-12 20:02:53.165230
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, ()) is repr
    assert get_repr_function(1, (int, repr)) is repr
    assert get_repr_function(1, (int, str)) is str
    assert get_repr_function(1, ((lambda s: s == 1, str))) is str
    assert get_repr_function(1, ((lambda s: s == 2, str))) is repr




# Generated at 2022-06-12 20:03:02.435813
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class X(WritableStream):
        def write(self, s):
            return s
    assert isinstance(X, type)
    assert issubclass(X, WritableStream)
    assert isinstance(X(), WritableStream)
    x = X()
    assert x.write('hi') == 'hi'
    assert x.write(b'hi') == b'hi'

    class Y(object):
        def write(self, s):
            return s
    assert not isinstance(Y, type)
    assert not issubclass(Y, WritableStream)
    y = Y()
    assert not isinstance(y, WritableStream)

    class Z(WritableStream):
        pass
    assert isinstance(Z, type)
    assert issubclass(Z, WritableStream)

# Generated at 2022-06-12 20:03:03.925804
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Dummy(WritableStream):
        def write(s):
            pass
    Dummy()





# Generated at 2022-06-12 20:03:08.475847
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    assert issubclass(sys.stdout.__class__, WritableStream)
    assert not issubclass(42, WritableStream)
    assert not issubclass(type(None), WritableStream)
    class Foo(object):
        pass
    assert not issubclass(Foo, WritableStream)
    assert _check_methods(sys.stdout.__class__, 'write') == True
    assert _check_methods(Foo, 'write') == NotImplemented



# Generated at 2022-06-12 20:03:12.175457
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import StringIO
    assert WritableStream.register(StringIO.StringIO)
    assert WritableStream.register(sys.stdout)
    assert not WritableStream.register(set)



# Generated at 2022-06-12 20:03:18.080505
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStreamSubclass(WritableStream):
        def __init__(self):
            self.items = []

        def write(self, s):
            self.items.append(s)

    assert issubclass(MyWritableStreamSubclass, WritableStream)

    my_writable_stream_subclass = MyWritableStreamSubclass()
    my_writable_stream_subclass.write(1)

    assert my_writable_stream_subclass.items == [1]



# Generated at 2022-06-12 20:03:25.050080
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(0) == '0'
    assert get_shortish_repr(1) == '1'
    assert get_shortish_repr(2) == '2'
    assert get_shortish_repr(3) == '3'
    assert get_shortish_repr(4) == '4'
    assert get_shortish_repr(5) == '5'
    assert get_shortish_repr(6) == '6'
    assert get_shortish_repr(7) == '7'
    assert get_shortish_repr(8) == '8'
    assert get_shortish_repr(9) == '9'
    assert get_shortish_repr(10) == '10'
    assert get_shortish_repr(11)

# Generated at 2022-06-12 20:03:33.026133
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    WritableStream.register(StringIO)
    WritableStream.register(type(sys.stdout))

    class Foo(object):
        def write(self, s):
            pass

    class Bar(Foo):
        pass

    class Baz(Bar):
        def write(self, s):
            pass

    assert isinstance(Baz(), WritableStream)
    assert not isinstance(Bar(), WritableStream)
    assert isinstance(Foo(), WritableStream)

    assert isinstance(sys.stderr, WritableStream)
    assert isinstance(StringIO(), WritableStream)


if __name__ == '__main__':
    test_WritableStream_write()
    print("All tests passed.")

# Generated at 2022-06-12 20:03:37.229065
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class X:
        def write(self, s):
            pass
    X() # Doesn't throw



# Generated at 2022-06-12 20:03:47.554087
# Unit test for function get_repr_function
def test_get_repr_function():
    class Item(object):
        pass

    item = Item()
    assert get_repr_function(item, ()) is repr

    class MoreSpecificItem(Item):
        pass

    more_specific_item = MoreSpecificItem()
    assert get_repr_function(more_specific_item, ()) is repr

    child_item_repr = lambda x: 'child item repr' if isinstance(x, ChildItem) else None
    assert get_repr_function(more_specific_item, (
        (child_item_repr, lambda x: 'child item repr'),
    )) is repr

    class ChildItem(Item):
        pass

    child_item = ChildItem()

# Generated at 2022-06-12 20:03:53.503422
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class WritableStream_Test(WritableStream):
        def __init__(self):
            self.write_log = []

        def write(self, s):
            assert isinstance(s, str)
            self.write_log.append(s)

    ws = WritableStream_Test()
    ws.write('spam')
    ws.write('eggs')
    assert ws.write_log == ['spam', 'eggs']

# Generated at 2022-06-12 20:03:56.665642
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import types
    class MyFileType(types.FileType):
        def write(self, s):
            pass

    my_file = MyFileType(0, 'w')
    assert isinstance(my_file, WritableStream)
    my_file.write('hello')



# Generated at 2022-06-12 20:03:58.784517
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    r = get_shortish_repr([1, 2, 3, 4, 5], max_length=16)
    assert r == '[1, 2, 3, 4,...'

# Generated at 2022-06-12 20:04:03.467419
# Unit test for function get_repr_function
def test_get_repr_function():
    def my_repr(x): # `x` is a Person instance
        return x.name
    mary = Person(name='Mary', age=30)
    assert get_repr_function(mary, custom_repr=((Person, my_repr),)) == my_repr
    assert get_repr_function(mary, custom_repr=()) == repr

# Generated at 2022-06-12 20:04:04.720166
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function('foo', [(lambda x: True, lambda x: x + 'bar')]) == 'foobar'



# Generated at 2022-06-12 20:04:07.799446
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class MyWritable(WritableStream):
        def __init__(self):
            self.buffer = ''

        def write(self, s):
            self.buffer += s


    my_writable = MyWritable()
    assert isinstance(my_writable, WritableStream)
    words = ['help', 'me', 'please']
    for word in words:
        my_writable.write(word)
    assert my_writable.buffer == ''.join(words)

# Generated at 2022-06-12 20:04:18.013669
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Blah: pass
    assert WritableStream.__subclasshook__(Blah) is NotImplemented
    class Blah:
        def write(self, s): pass
    assert WritableStream.__subclasshook__(Blah) is True
    class Blah:
        def write(self, s): pass
        def doesntmatter(self): pass
    assert WritableStream.__subclasshook__(Blah) is True
    class Blah(WritableStream): pass
    assert WritableStream.__subclasshook__(Blah) is True
    class Blah(WritableStream):
        def write(self, s): pass
    assert WritableStream.__subclasshook__(Blah) is True
    class Blah(WritableStream):
        def write(self, s): pass

# Generated at 2022-06-12 20:04:24.555256
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyStream(WritableStream):

        def __init__(self):
            self.stored_string = ''

        def write(self, s):
            self.stored_string += s

    my_stream = MyStream()
    my_stream.write('hello')
    assert my_stream.stored_string == 'hello'
    my_stream.write(' there')
    assert my_stream.stored_string == 'hello there'
    print('test_WritableStream_write passed!')

# Generated at 2022-06-12 20:04:39.622545
# Unit test for function get_repr_function
def test_get_repr_function():

    # Let's try some features one at a time

    assert get_repr_function(3, ()) == repr
    assert get_repr_function(3.2, ()) == repr
    assert get_repr_function('s', ()) == repr

    custom_repr = ((int, lambda i: 'int({})'.format(i)),)
    assert get_repr_function(3, custom_repr) == (lambda i: 'int({})'.format(i))
    assert get_repr_function(3.2, custom_repr) == repr
    assert get_repr_function('s', custom_repr) == repr

    assert get_repr_function(Range, custom_repr) == repr

# Generated at 2022-06-12 20:04:46.985004
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyStringIO(WritableStream):
        def __init__(self):
            self.text = ''

        def write(self, s):
            self.text += s

    my_string_io = MyStringIO()
    assert isinstance(my_string_io, WritableStream)
    assert my_string_io.text == ''

    my_string_io.write('hi')

    assert my_string_io.text == 'hi'

    my_string_io.write(' ')
    my_string_io.write('there')

    assert my_string_io.text == 'hi there'



# Generated at 2022-06-12 20:04:50.845867
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class T(list):
        def write(self, s):
            return self.append(s)
    assert issubclass(T, WritableStream)
    assert T()
    assert T().write(3)
    assert T().write(3) == [3]



# Generated at 2022-06-12 20:04:56.245602
# Unit test for function get_repr_function
def test_get_repr_function():
    class A(object):
        pass
    class B(A):
        pass
    class C(A):
        pass
    b = B()
    assert get_repr_function(b, ((A, lambda x: 'A!'),)) == 'A!'
    assert get_repr_function(b, ((C, lambda x: 'C!'),)) != 'C!'
    assert get_repr_function(b, ((A, lambda x: 'A!'),
                                 (C, lambda x: 'C!'))) == 'A!'

# Generated at 2022-06-12 20:05:00.791688
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(WritableStream):
        def __init__(self, output_list):
            self.output_list = output_list
        def write(self, x):
            self.output_list.append(x)
    a = A([])
    assert isinstance(a, WritableStream)
    a.write('hi')
    assert a.output_list == ['hi']
    a.write('there')
    assert a.output_list == ['hi', 'there']
    a.write('%s/%s' % (a.output_list[0], a.output_list[1]))
    assert a.output_list == ['hi', 'there', 'hi/there']



# Generated at 2022-06-12 20:05:03.423758
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(WritableStream):
        def write(self, s):
            pass
    assert isinstance(A(), WritableStream)



# Generated at 2022-06-12 20:05:05.204975
# Unit test for method write of class WritableStream

# Generated at 2022-06-12 20:05:08.462599
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    class A(WritableStream):
        def write(self, s):
            pass
    assert issubclass(A, WritableStream)
    assert not issubclass(io.StringIO, WritableStream)

# Generated at 2022-06-12 20:05:18.160280
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, (
        (int, lambda x: 'int %s' % x),
        (float, lambda x: 'float %s' % x),
        (type(None), lambda x: 'None')
    )) == repr
    assert get_repr_function(1.5, (
        (int, lambda x: 'int %s' % x),
        (float, lambda x: 'float %s' % x),
        (type(None), lambda x: 'None')
    )) == repr
    assert get_repr_function(None, (
        (int, lambda x: 'int %s' % x),
        (float, lambda x: 'float %s' % x),
        (type(None), lambda x: 'None')
    )) == repr



# Generated at 2022-06-12 20:05:23.888437
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def __init__(self):
            self.last_written = None
        def write(self, s):
            self.last_written = s

    x = MyWritableStream()
    x.write('abc')
    assert x.last_written == 'abc'

# Generated at 2022-06-12 20:05:32.537834
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class FakeFileObject(object):
        def __init__(self):
            self.data = ''
        def write(self, data):
            self.data += data
    ffo = FakeFileObject()
    assert isinstance(ffo, WritableStream)
    assert ffo.__class__.__mro__ == (FakeFileObject, object)
    ffo.write('a')
    ffo.write('\n')
    ffo.write('b')
    assert ffo.data == 'a\nb'



# Generated at 2022-06-12 20:05:38.711723
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyDummyStream(object):
        def write(self, s):
            pass

    assert issubclass(MyDummyStream, WritableStream)

_WritableStream_write_test_done = False

if not _WritableStream_write_test_done:
    test_WritableStream_write()
    _WritableStream_write_test_done = True



# Generated at 2022-06-12 20:05:42.681946
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class WritableStream1(WritableStream):
        def write(self, s):
            pass

    assert issubclass(WritableStream1, WritableStream)

    class WritableStream2(WritableStream):
        pass

    assert not issubclass(WritableStream2, WritableStream)


test_WritableStream_write()

# Generated at 2022-06-12 20:05:49.800515
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(WritableStream):
        def write(self, s):
            pass
    assert issubclass(A, WritableStream)
    class B(A):
        pass
    assert issubclass(B, WritableStream)
    class C(A):
        pass
    assert issubclass(C, WritableStream)
    class D(A):
        write = None
    assert not issubclass(D, WritableStream)




# Generated at 2022-06-12 20:05:57.529162
# Unit test for function get_repr_function
def test_get_repr_function():
    d = dict(a=4, b=5)

    assert get_repr_function(d, []) == repr
    assert get_repr_function(d, [(str, str)]) == str
    assert get_repr_function(d, [(str, str), (dict, dict)]) == dict
    assert get_repr_function(d, [(dict, dict), (str, str)]) == dict
    assert get_repr_function(d, [(re.compile('[ad]'), str)]) == dict
    assert get_repr_function(d, [(re.compile('[bc]'), str)]) == repr
    assert get_repr_function(d, [(re.compile('[bc]'), str), (dict, dict)]) \
                                                                   == dict
    assert get_repr_

# Generated at 2022-06-12 20:05:59.170408
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class CrazyWriter(WritableStream):
        def write(self, s):
            assert isinstance(s, str)

# Generated at 2022-06-12 20:06:08.841144
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    """Unit test for method write of class WritableStream."""

    # Testing simple printing
    class SimpleStream(WritableStream):
        def __init__(self):
            self.text = ''

        def write(self, s):
            self.text += s

    simple_stream = SimpleStream()
    simple_stream.write('abcd')
    assert simple_stream.text == 'abcd'

    # Testing file writing
    class FileStream(WritableStream):
        def __init__(self):
            self.f = open('testing_file', 'w')

        def write(self, s):
            self.f.write(s)

    file_stream = FileStream()
    file_stream.write('efgh')
    file_stream.f.close()
    testing_file = open('testing_file', 'r')

# Generated at 2022-06-12 20:06:12.428819
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def __init__(self):
            self.output = ''

        def write(self, s):
            self.output += s

    stream = MyWritableStream()
    stream.write('hi\n')
    stream.write('there\n')
    assert stream.output == 'hi\nthere\n'

# Generated at 2022-06-12 20:06:15.796517
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyFileLikeObject(WritableStream):
        def write(self, s):
            print('got a string!')
    assert isinstance(MyFileLikeObject(), WritableStream)

# Generated at 2022-06-12 20:06:18.730254
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Foo:
        def write(self, foo):
            return foo
    class Bar:
        pass
    assert isinstance(Foo(), WritableStream)
    assert not isinstance(Bar(), WritableStream)


# Generated at 2022-06-12 20:06:32.519625
# Unit test for method write of class WritableStream

# Generated at 2022-06-12 20:06:42.921010
# Unit test for function get_repr_function
def test_get_repr_function():

    class A(object):
        pass

    class B(A):
        pass

    class C(object):
        pass

    assert get_repr_function(A(), [(A, lambda: 'a')])() == 'a'
    assert get_repr_function(B(), [(B, lambda: 'b')])() == 'b'
    assert get_repr_function(B(), [(A, lambda: 'a')])() == 'a'
    assert get_repr_function(A(), [(int, lambda: 'int')])() == 'int'
    assert get_repr_function(A(), [(int, lambda: 'int'), (A, lambda: 'a')])() == 'a'


# Generated at 2022-06-12 20:06:45.963032
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class TestClass(object):
        def write(self, s):
            pass

    assert issubclass(TestClass, WritableStream)
    assert WritableStream.register(TestClass) is TestClass



# Generated at 2022-06-12 20:06:54.146510
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class DummyStream(WritableStream):
        def __init__(self):
            self.output = ''
            self.write_called = False
        def write(self, s):
            self.output += s
            self.write_called = True
    dummy_stream = DummyStream()
    assert issubclass(DummyStream, WritableStream)
    dummy_stream.write('hi')
    assert dummy_stream.write_called
    assert dummy_stream.output == 'hi'
    assert not isinstance(dummy_stream, WritableStream)
    assert dummy_stream.write('hi') is None
    class DummyStreamNoWriteMethod(WritableStream):
        def __init__(self):
            self.output = ''
            self.write_called = False
    dummy_stream_no_write_method = Dummy

# Generated at 2022-06-12 20:06:56.195159
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class DummyWritableStream(WritableStream):
        def write(self, s):
            pass

    assert isinstance(DummyWritableStream(), WritableStream)




# Generated at 2022-06-12 20:06:58.404878
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyStream(WritableStream):
        def write(self, s):
            pass

    assert issubclass(MyStream, WritableStream)



# Generated at 2022-06-12 20:07:08.855466
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    from .fake_streams import FakeStream
    import os
    import sys
    import contextlib

    class WritableStreamExample(WritableStream):
        def write(self, s):
            assert isinstance(s, bytes)

    def write(stream, s):
        stream.write(s)
    
    with FakeStream() as fake:
        with WritableStreamExample() as writable_stream_example:
            write(fake, b'foo')
            write(writable_stream_example, b'foo')
            write(sys.stdout, b'foo')
            write(sys.stderr, b'foo')
            with contextlib.closing(open(__file__, 'rb')) as writable_file:
                write(writable_file, b'foo')

# Generated at 2022-06-12 20:07:11.858598
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class WritableStreamSubclass(WritableStream):
        def write(self, s):
            print(s)

    x = WritableStreamSubclass()
    x.write('abc')





# Generated at 2022-06-12 20:07:19.265321
# Unit test for function get_repr_function
def test_get_repr_function():

    def get_repr_function_wrapper(item, custom_repr):
        return get_repr_function(item, custom_repr)

    assert (get_repr_function_wrapper(
        2,
        ((int, 'int'),)
    ) == 'int')

    assert (get_repr_function_wrapper(
        2,
        ((float, 'float'), (int, 'int'))
    ) == 'int')

    assert (get_repr_function_wrapper(
        2.5,
        ((float, 'float'), (int, 'int'))
    ) == 'float')

    assert (get_repr_function_wrapper(
        2.5,
        ((int, 'int'), (float, 'float'))
    ) == 'float')


# Generated at 2022-06-12 20:07:23.736218
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MockStringIO(object):
        def write(self, string):
            self.string = string

    a = MockStringIO()
    a.write('meow')
    assert a.string == 'meow'



# Generated at 2022-06-12 20:07:40.682992
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    # We want to give `abc.ABC` a set of methods and then check if
    # `WritableStream` is a subclass of that ABC. If it isn't, it means that
    # `WritableStream`s are not correct. (Probably because its `__subclasshook__`
    # is not working.)

    class DummyWritableStream:
        def write(self, s):
            pass

    class DummyUnwritableStream:
        pass

    assert isinstance(DummyWritableStream(), WritableStream)
    assert WritableStream.__subclasshook__(DummyWritableStream) is True

    assert not isinstance(DummyUnwritableStream(), WritableStream)
    assert WritableStream.__subclasshook__(DummyUnwritableStream) is NotImplemented

# Generated at 2022-06-12 20:07:45.476672
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(2, ()) is repr
    assert get_repr_function(2, ((lambda x: True, str),)) is str
    assert get_repr_function(2, ((lambda x: False, str),)) is repr
    assert get_repr_function(2.5, ((lambda x: True, int),)) is int
    assert get_repr_function(2.5, ((lambda x: False, int),)) is repr



# Generated at 2022-06-12 20:07:50.998535
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Foo(WritableStream):
        pass
    try:
        assert issubclass(Foo, WritableStream)
    except Exception:
        # py.test
        pass
    try:
        assert Foo.__subclasshook__(Foo) is True
    except Exception:
        # py.test
        pass

# Generated at 2022-06-12 20:07:56.788593
# Unit test for function get_repr_function
def test_get_repr_function():
    def f1(x):
        return x

    def f2(x):
        return x

    assert get_repr_function(1, ((int, f1), (str, f2))) is f1
    assert get_repr_function('', ((int, f1), (str, f2))) is f2
    assert get_repr_function(1, ((str, f2),)) is repr
    assert get_repr_function(1, ((lambda x: False, f1), (str, f2))) is repr
    assert get_repr_function(1, ((lambda x: True, f1), (str, f2))) is f1




# Generated at 2022-06-12 20:08:00.292483
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    from .streams import Stream
    from .files import SerializedFile

    file = SerializedFile()
    stream = Stream(file, 'utf8', False, False)
    stream.write('hello')
    assert file.get_string() == 'hello'


# Generated at 2022-06-12 20:08:06.333447
# Unit test for function get_repr_function
def test_get_repr_function():
    class A(object): pass
    class B(A): pass

    assert get_repr_function(A(), []) is repr
    assert get_repr_function(A(), [(A, int)]) is int

    assert get_repr_function(B(), []) is repr
    assert get_repr_function(B(), [(B, int)]) is int
    assert get_repr_function(B(), [(A, int)]) is int
    assert get_repr_function(B(), [(object, int)]) is int

# Generated at 2022-06-12 20:08:09.811927
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class WritableStream(ABC):
        @abc.abstractmethod
        def write(self, s):
            pass

    class MyWritableStream(WritableStream):

        def write(self, s):
            pass

    assert issubclass(MyWritableStream, WritableStream)
    assert not issubclass(object, WritableStream)

# Generated at 2022-06-12 20:08:16.483797
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, (int, lambda n: n + 1),
                             (float, lambda n: n + 1.5))(1) == '2'
    assert get_repr_function(set(['a']), (int, lambda n: n + 1),
                             (float, lambda n: n + 1.5)) == set
    assert get_repr_function(1, (int, lambda n: n + 1),
                             (float, lambda n: n + 1.5))('1') == "'1'"

# Generated at 2022-06-12 20:08:21.946737
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream:
        def write(self, s):
            pass
    assert issubclass(MyWritableStream, WritableStream)
    for bad_write_method in (
        '', # not callable
        lambda x: None, # not returning None
        lambda x: x, # not returning None
        lambda x: None, lambda x: x, # not returning None
    ):
        MyWritableStream.write = bad_write_method
        assert not issubclass(MyWritableStream, WritableStream)




# Generated at 2022-06-12 20:08:27.496825
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(0, ()) == repr
    assert get_repr_function(1.5, ()) == repr
    assert get_repr_function(True, ()) == repr
    assert get_repr_function("", ()) == repr
    assert get_repr_function("hello", ()) == repr
    assert get_repr_function(u"hello", ()) == repr
    assert get_repr_function(u"\u2603", ()) == repr
    assert get_repr_function((), ()) == repr
    assert get_repr_function([], ()) == repr
    assert get_repr_function([1], ()) == repr
    assert get_repr_function((1, 2), ()) == repr
    assert get_repr_function({}, ()) == repr