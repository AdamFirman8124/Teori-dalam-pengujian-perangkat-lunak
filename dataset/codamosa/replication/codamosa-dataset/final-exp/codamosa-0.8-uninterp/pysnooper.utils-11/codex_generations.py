

# Generated at 2022-06-12 19:58:42.020126
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function('', []) is repr

    assert get_repr_function(1, []) is repr
    assert get_repr_function(1, [(lambda x: x%2 == 0, str)]) is repr
    assert get_repr_function(2, [(lambda x: x%2 == 0, str)]) is str

    assert get_repr_function(3, [(lambda x: x%2 == 0, str),
                                 (lambda x: x%3 == 0, int)]) is str
    assert get_repr_function(3, [(lambda x: x%3 == 0, int),
                                 (lambda x: x%2 == 0, str)]) is int

# Generated at 2022-06-12 19:58:46.164802
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class FakeFile(WritableStream):
        def __init__(self):
            pass
        def write(self, s):
            pass
    FakeFile()
    assert issubclass(FakeFile, WritableStream)
    assert not issubclass(WritableStream, FakeFile)

# Generated at 2022-06-12 19:58:53.656664
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def write(self, s):
            pass

    class MyOtherWritableStream(MyWritableStream):
        def write(self, s):
            pass

    MyWritableStream.__subclasshook__(MyWritableStream)
    MyWritableStream.__subclasshook__(MyOtherWritableStream)

    class MyMisspelledWritableStream(MyWritableStream):
        def writee(self, s):
            pass

    if MyWritableStream.__subclasshook__(MyMisspelledWritableStream) is not NotImplemented:
        raise Exception

    class MyWritableStream2(MyWritableStream):
        pass

    if MyWritableStream.__subclasshook__(MyWritableStream2) is not True:
        raise Exception


# Generated at 2022-06-12 19:58:58.707156
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class WritableStreamSubclass(WritableStream):
        def __init__(self):
            self.buff = []

        def write(self, s):
            self.buff.append(s)

    writable_stream = WritableStreamSubclass()
    assert writable_stream.write('meow') is None
    assert writable_stream.buff == ['meow']



# Generated at 2022-06-12 19:59:01.568793
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class BadlyBehavedWritableStream(WritableStream):
        def __init__(self):
            self.written_strings = []

        def write(self, s):
            self.written_strings.append(s)

    bbws = BadlyBehavedWritableStream()
    bbws.write('abc')
    bbws.write('def')
    assert bbws.written_strings == ['abc', 'def']

# Generated at 2022-06-12 19:59:05.153413
# Unit test for function get_repr_function
def test_get_repr_function():
    assert repr(get_repr_function(1, [])) == repr
    assert repr(get_repr_function(1, [(int, int.__repr__)])) == repr(
        int.__repr__
    )



# Generated at 2022-06-12 19:59:10.568931
# Unit test for function get_repr_function
def test_get_repr_function():

    class A(object): pass
    class B(A): pass
    class C(object): pass


# Generated at 2022-06-12 19:59:15.401980
# Unit test for function shitcode
def test_shitcode():
    assert shitcode(u'abc def') == u'abc def'
    assert shitcode(u'abc\u20acdef') == u'abc?def'
    assert shitcode(u'\u0fff') == u'?'
    assert shitcode(u'spam\x00eggs') == u'spam?eggs'



# Generated at 2022-06-12 19:59:26.182370
# Unit test for function get_repr_function
def test_get_repr_function():
    # Define classes and instances for testing
    class A:
        pass
    class B(A):
        pass
    class C(B):
        pass
    class D:
        pass

    a = A()
    b = B()
    c = C()
    d = D()

    # Define function and lambdas for testing
    def my_repr(x):
        return 'my_repr'

    lambda_1 = lambda x: 'lambda_1'
    lambda_2 = lambda x: 'lambda_2'
    lambda_3 = lambda x: 'lambda_3'

    # Define test lists

# Generated at 2022-06-12 19:59:36.781453
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    class A:
        def __repr__(self):
            return 'repr' * 1000000
    assert get_shortish_repr('asdfasdf') == 'asdfasdf'
    assert get_shortish_repr(A()) == 'reprreprr'
    assert get_shortish_repr('asdfasdf', max_length=4) == 'a...f'
    assert get_shortish_repr(u'asdfasdf', max_length=4) == 'a...f'
    assert get_shortish_repr('asdfasdf', max_length=5) == 'a...df'
    assert get_shortish_repr(u'asdfasdf', max_length=5) == 'a...df'

# Generated at 2022-06-12 19:59:50.612830
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(
        1, custom_repr=[]
    ) is repr

    assert get_repr_function(
        1, custom_repr=[(int, str)]
    ) is str

    assert get_repr_function(
        1, custom_repr=[(int, str), (lambda _: False, type)]
    ) is str

    assert get_repr_function(
        1, custom_repr=[(lambda _: False, type)]
    ) is repr

    assert get_repr_function(
        1.0, custom_repr=[(int, str)]
    ) is repr

    def foo():
        pass
    f = foo

# Generated at 2022-06-12 20:00:00.342501
# Unit test for function get_repr_function
def test_get_repr_function():
    class A(object): pass
    class B(A): pass
    class C(B): pass
    class D(C): pass
    class E(D): pass
    d = D()
    e = E()
    assert get_repr_function(1, ()) is repr
    assert get_repr_function(1, (((A, B), lambda x: 'hi'))) is repr
    assert get_repr_function(d, (((A, B), lambda x: 'hi'))) is repr
    assert get_repr_function(e, (((A, B), lambda x: 'hi'))) == 'hi'
    assert get_repr_function(d, (((D,), lambda x: 'hi'))) == 'hi'

# Generated at 2022-06-12 20:00:03.984580
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Writable:
        def write(self, s):
            pass

    class NotWritable:
        pass

    assert isinstance(Writable(), WritableStream)
    assert not isinstance(NotWritable(), WritableStream)



# Generated at 2022-06-12 20:00:10.344730
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Foo(WritableStream):
        def write(self, s):
            pass

    assert issubclass(Foo, WritableStream)
    assert isinstance(Foo(), WritableStream)

    class Bar(WritableStream):
        def write(self, s):
            pass

        def non_dunder(self):
            pass

    assert issubclass(Bar, WritableStream)
    assert isinstance(Bar(), WritableStream)

    class Baz(WritableStream):
        pass

    assert not issubclass(Baz, WritableStream)

# Generated at 2022-06-12 20:00:14.125479
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class AnyClass(WritableStream):
        def write(self, s):
            pass

    def write(s):
        pass

    assert WritableStream.register(AnyClass)
    assert not WritableStream.register(write)

# Generated at 2022-06-12 20:00:21.660482
# Unit test for function get_repr_function
def test_get_repr_function():

    def func1(x):
        return x.upper()

    def func2(x):
        return x.lower()

    custom_repr = [
        (lambda x: isinstance(x, str) or isinstance(x, str), func1),
        (lambda x: isinstance(x, object), func2),
    ]

    assert get_repr_function(1, custom_repr) == repr(1)
    assert get_repr_function('a', custom_repr) == func1('a')
    assert get_repr_function('a', custom_repr) == 'A'

    assert get_repr_function(1.2, custom_repr) == repr(1.2)
    assert get_repr_function(None, custom_repr) == repr(None)
    assert get_

# Generated at 2022-06-12 20:00:30.692441
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    try:
        import pytest
    except ImportError:
        pytest = None

    if pytest is None:
        raise Exception("Please install `pytest` to run tests.")

    # TODO: Test more thoroughly!
    import os.path
    import datetime
    x = [os.path.isdir, 5, os.path.join, {'x': 5}, datetime.datetime.now]
    for item in x:
        assert get_shortish_repr(item) == repr(item)
        assert get_shortish_repr(item, max_length=5) != repr(item)


if __name__ == '__main__':
    test_get_shortish_repr()

# Generated at 2022-06-12 20:00:38.506452
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, []) is repr
    assert get_repr_function(1, [(lambda x: True, 'my_repr')]) == 'my_repr'
    assert get_repr_function(1, [(lambda x: False, 'my_repr')]) is repr
    assert get_repr_function('', [(lambda x: False, 'my_repr')]) is repr
    assert get_repr_function('', [(lambda x: True, 'my_repr')]) == 'my_repr'
    assert get_repr_function('', [(int, 'my_repr')]) is repr
    assert get_repr_function(1, [(int, 'my_repr')]) == 'my_repr'

# Generated at 2022-06-12 20:00:49.062629
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, ()) is repr
    assert get_repr_function(1., ()) is repr
    assert get_repr_function('1', ()) is repr
    assert get_repr_function('', ()) is repr
    assert get_repr_function(1, ((int, str), lambda x: 'foo')) is repr
    assert get_repr_function(1., ((int, str), lambda x: 'foo')) is repr
    assert get_repr_function('1', ((int, str), lambda x: 'foo')) is repr
    assert get_repr_function('', ((int, str), lambda x: 'foo')) is repr
    assert get_repr_function(1, ((int,), lambda x: 'foo')) is repr

# Generated at 2022-06-12 20:01:00.269447
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(3) == '3'
    assert get_shortish_repr(3.5) == '3.5'
    assert get_shortish_repr(3.9999999999999) == '3.9999999999999'
    assert get_shortish_repr('abc') == "'abc'"
    assert get_shortish_repr('a' * 200) == ('\'' + ('a' * 197) + '...\'')
    assert get_shortish_repr('a' * 200, max_length=30) == ('\'' + ('a' * 27) + '...')

    def identity(x):
        return x
    assert truncate(identity, None) is identity
    assert truncate('abc', None) == 'abc'

# Generated at 2022-06-12 20:01:07.452830
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, ((int, lambda x: 'integer'),)) == 'integer'
    assert get_repr_function(1.0, ((int, lambda x: 'integer'),)) == repr
    assert get_repr_function(1.0, ((str, lambda x: 'string'),)) == repr

# Generated at 2022-06-12 20:01:10.677692
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class ConcreteWritableStream(WritableStream):
        def write(self, s):
            pass

    ConcreteWritableStream()
    try:
        class Wrong:
            def write(self):
                pass
        Wrong()
    except TypeError:
        pass
    else:
        assert False, 'should have raised TypeError'




# Generated at 2022-06-12 20:01:21.580802
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    # Testing with functions that are known to fail
    # (https://github.com/aluriak/outcome/issues/6)
    # and file-like objects:

    class MyFile(object):
        def __init__(self):
            self.name = 'file'

    class MyNamespace(object):
        def __repr__(self):
            raise ValueError

        def __str__(self):
            return 'namespace'

    class MyNamedTuple(tuple):
        __repr__ = tuple.__repr__
        __str__ = tuple.__str__

        def __new__(cls, *args, **kwargs):
            return tuple.__new__(MyNamedTuple, *args, **kwargs)


# Generated at 2022-06-12 20:01:29.613111
# Unit test for function get_repr_function
def test_get_repr_function():
    def custom(*args): return 'got list'
    def always(*args): return 'always gets here'
    custom_repr = [
        (lambda x: isinstance(x, list), custom),
        (lambda x: True, always),
    ]
    assert get_repr_function([], custom_repr) == custom
    assert get_repr_function({}, custom_repr) == always
    assert get_repr_function(object(), custom_repr) == always


_ELLIPSIS = '{}...{}'
_L_ELLIPSIS = '{}...'
_R_ELLIPSIS = '...{}'

# Generated at 2022-06-12 20:01:40.600537
# Unit test for function get_shortish_repr
def test_get_shortish_repr():

    assert get_shortish_repr(None, max_length=3) == 'None'
    assert get_shortish_repr(None, max_length=4) == 'None'
    assert get_shortish_repr(None, max_length=5) == 'None'

    assert get_shortish_repr(()) == "()"
    assert get_shortish_repr(()).__class__ is str

    assert get_shortish_repr((1, 2), max_length=5) == "(1, 2)"
    assert get_shortish_repr((1, 2), max_length=6) == "(1, 2)"
    assert get_shortish_repr((1, 2), max_length=7) == "(1, 2)"


# Generated at 2022-06-12 20:01:43.166480
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    x = [1, 2, 3, 4]
    assert get_shortish_repr(x) == normalize_repr(repr(x))

# Generated at 2022-06-12 20:01:50.163910
# Unit test for function get_repr_function
def test_get_repr_function():
    # 1) standard use case
    class A(object): pass
    class B(object): pass
    assert get_repr_function(A(), ((A, repr),)) == repr
    assert get_repr_function(A(), ((B, repr),)) == repr
    # 2) custom repr
    class A(object): pass
    class B(object): pass
    def custom_repr(x): pass
    assert get_repr_function(A(), ((A, custom_repr),)) == custom_repr
    assert get_repr_function(A(), ((B, custom_repr),)) == repr
    # 3) custom function using inheritance
    class A(object): pass
    class B(A): pass
    class C(object): pass

# Generated at 2022-06-12 20:01:55.224310
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class WritableStreamSimulation:
        attr = ('This is a WritableStreamSimulation, '
                'for testing the `write` method.')

        def __init__(self):
            self.written_string = ''

        def write(self, s):
            self.written_string += s

    assert isinstance(WritableStreamSimulation(), WritableStream)

# Generated at 2022-06-12 20:02:01.270174
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class MyWritableStream(WritableStream):

        def __init__(self):
            self._s = b''
            self.write_called = False

        def write(self, s):
            assert isinstance(s, bytes)
            self._s += s
            self.write_called = True

    assert issubclass(MyWritableStream, WritableStream)

    stream = MyWritableStream()
    stream.write(b'hello world!')

    assert stream._s == b'hello world!'
    assert stream.write_called


if __name__ == '__main__':
    for function in (test_WritableStream_write,):
        function()

# Generated at 2022-06-12 20:02:10.778693
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(object(), []) == repr
    assert get_repr_function(object(), [(object, 123)]) == 123
    assert get_repr_function(list(), [(tuple, 123)]) == repr
    assert get_repr_function(list(), [(list, 123)]) == 123
    assert get_repr_function(list(), [(list, 123), (tuple, 456)]) == 123
    assert get_repr_function(object(), [(object, 123), (list, 456)]) == 123
    assert get_repr_function(list(), [(lambda x: True, 123)]) == 123
    assert get_repr_function(list(), [(lambda x: False, 123)]) == repr



# Generated at 2022-06-12 20:02:29.669588
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    from collections import namedtuple
    from . import pycompat

    S = namedtuple('S', ['field'])
    x = S((1, 2, 3))

    repr_function = get_repr_function(
        x,
        custom_repr=(
            (lambda item: isinstance(item, S),
             lambda item: '{}: {}'.format(item.__class__.__name__,
                                          item.field)),
        )
    )
    assert repr_function(x) == 'S: (1, 2, 3)'

    with pycompat.suppress_unhandled_exception:
        assert truncate('abcdefghi', 10) == 'abcdefghi'
    assert truncate('abcdefghi', 9) == 'abcdef...'

# Generated at 2022-06-12 20:02:35.279537
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(3, []) == repr
    assert get_repr_function(3, [(int, str)]) == str
    assert get_repr_function(3, [(lambda x: x > 3, str)]) == repr
    assert get_repr_function(3, [(lambda x: x > 3, str), (int, str)]) == str



# Generated at 2022-06-12 20:02:45.126450
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(4, [(int, lambda n: 'number ' + str(n))]) == \
                                                         'number 4'
    assert get_repr_function(2j, [(complex, lambda n: 'complex ' + str(n))]) == \
                                                          'complex 2j'
    class C: pass
    assert get_repr_function(C(), [(object, lambda n: 'object ' + str(n))]) == \
                                                            "object <__main__.C object at 0x{:x}>".format(
                                                                               id(C())
                                                                             )
    def error_repr_function(item):
        raise ValueError('TEST')
    assert get_repr_function(4, [(int, error_repr_function)]) == repr

# Generated at 2022-06-12 20:02:49.793828
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Subclass(WritableStream):
        def write(self, s): # Valid
            pass
    assert isinstance(Subclass(), WritableStream)

    class Subclass(WritableStream):
        def write(self, s, x): # Invalid
            pass
    assert not isinstance(Subclass(), WritableStream)

    class Subclass(WritableStream):
        pass
    assert not isinstance(Subclass(), WritableStream)
    return



# Generated at 2022-06-12 20:02:58.380800
# Unit test for function get_repr_function
def test_get_repr_function():
    class Item(object):
        pass
    item = Item()

    assert get_repr_function(item) is repr
    assert get_repr_function(item, ((int, id),)) is id
    assert (get_repr_function(item, ((int, id), (object, str))) is
                                                            str)
    assert (get_repr_function(item, ((object, str), (int, id))) is
                                                            str)
    assert (get_repr_function(item, ((object, str), (Item, id))) is
                                                            id)
    assert (get_repr_function(item, ((Item, id), (object, str))) is
                                                            id)

    # Test truncating:
    s = 'abcdef'

# Generated at 2022-06-12 20:03:03.965713
# Unit test for function get_repr_function
def test_get_repr_function():
    class Foo(object): pass
    class Bar(object): pass
    foo = Foo()
    bar = Bar()
    assert get_repr_function(foo, []) == repr
    assert get_repr_function(bar, []) == repr
    assert get_repr_function(foo, [(Foo, None)]) == None
    assert get_repr_function(bar, [(Bar, None)]) == None
    assert get_repr_function(foo, [(Foo, 'a')]) == 'a'
    assert get_repr_function(bar, [(Bar, 'a')]) == 'a'
    assert get_repr_function(foo, [(Foo, 'a'), (Foo, 'b')]) == 'b'

# Generated at 2022-06-12 20:03:09.464231
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert normalize_repr('hello') == 'hello'
    assert normalize_repr('hello at 0x1234') == 'hello'
    assert normalize_repr('hello at 0x12345678901234567890') == 'hello'
    assert normalize_repr('hello at 0x123456789012345678901') == 'hello at 0x123456789012345678901'
    assert normalize_repr('hello at 0x1234567890ABCDEF') == 'hello'
    assert normalize_repr('hello at 0x1234567890abcdef') == 'hello'
    assert normalize_repr('hello at 0x1234567890') == 'hello'

# Generated at 2022-06-12 20:03:13.386064
# Unit test for function get_repr_function
def test_get_repr_function():
    basket = ['apple', 'orange', 'pear', 'banana', 'strawberry', 'rasberry']
    c_repr = [(lambda x: x.startswith('r'),
               lambda x: 'R-' + x.upper()),
              (lambda x: x in ('apple', 'banana'),
               lambda x: '<' + x + '>'),
              (True, normalize_repr),
              ]
    for fruit in basket:
        assert get_repr_function(fruit, c_repr)(fruit) == get_shortish_repr(
                                                   fruit, c_repr, normalize=True)

# Generated at 2022-06-12 20:03:23.165052
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class TestCase(object):
        def test(self):
            assert issubclass(TestCase, WritableStream)

        def _test(self):
            assert issubclass(TestCase, WritableStream)

    TestCase().test()

    class TestCase(object):
        def test(self):
            pass

        def _test(self):
            assert issubclass(TestCase, WritableStream)

    TestCase().test()

    class TestCase(object):
        def test(self):
            pass

        def _test(self):
            pass

    TestCase().test()

    class TestCase(object):
        pass

    TestCase().test()

    class TestCase(WritableStream):
        def test(self):
            assert issubclass(TestCase, WritableStream)


# Generated at 2022-06-12 20:03:32.374551
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(15, []) == repr
    assert get_repr_function(15, [(lambda x: x < 0, lambda x: 'too small')]) \
        == repr
    assert get_repr_function(-15, [(lambda x: x < 0, lambda x: 'too small')]) \
        == (lambda x: 'too small')
    assert get_repr_function(
        -15,
        [(lambda x: x < 0, lambda x: 'too small'),
         (lambda x: x > 100, lambda x: 'too big')]
    ) == (lambda x: 'too small')

# Generated at 2022-06-12 20:03:52.548802
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, [(lambda x: True, str)]) == str
    assert get_repr_function(1.0, [(lambda x: True, str)]) == repr



# Generated at 2022-06-12 20:03:55.463423
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import sys
    stream = WritableStream()
    stream.write('some\n')
    stream.write(u'stuff\n')
    stream.write(b'b\xc3\xa5f\n')




# Generated at 2022-06-12 20:04:01.030765
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        pass
    assert not issubclass(MyWritableStream, WritableStream)

    class MyWritableStream2(WritableStream):
        def write(self, s):
            pass
    assert issubclass(MyWritableStream2, WritableStream)

    class MyWritableStream3(WritableStream):
        def __init__(self):
            self.write
    assert issubclass(MyWritableStream3, WritableStream)

    class MyWritableStream3(WritableStream):
        def write(self, s):
            pass
        def write2(self, s):
            pass
    assert issubclass(MyWritableStream3, WritableStream)

# Generated at 2022-06-12 20:04:02.664173
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Foo(WritableStream):
        def write(self, s):
            return s


    foo = Foo()
    assert foo.write('hi') == 'hi'

# Generated at 2022-06-12 20:04:07.972860
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyMockObject:

        def __init__(self):
            self.write_arguments = []

        def write(self, s):
            self.write_arguments.append(s)

    my_mock_object = MyMockObject()

    assert isinstance(my_mock_object, WritableStream)

    my_mock_object.write('Hello, world!')

    assert my_mock_object.write_arguments == ['Hello, world!']




# Generated at 2022-06-12 20:04:12.023049
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class DummyWritableStream(WritableStream):
        def write(self, s):
            return None

    assert (isinstance(DummyWritableStream(), WritableStream))
    assert (not isinstance(DummyWritableStream, WritableStream))

# Generated at 2022-06-12 20:04:18.429752
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class File(WritableStream):
        def write(self, s):
            pass

    def f():
        pass

    class Iterator(WritableStream):
        def __init__(self):
            self.buffer = ''

        def write(self, s):
            self.buffer += s

        def __iter__(self):
            yield self.buffer

    for stream in [sys.stdout, sys.stderr, File(), Iterator()]:
        assert isinstance(stream, WritableStream)

# Generated at 2022-06-12 20:04:20.733928
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Foo(WritableStream):
        def write(self, s):
            pass

    assert isinstance(Foo(), WritableStream)

# Generated at 2022-06-12 20:04:29.086845
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    def round_trip(x, custom_repr=(), max_length=None, normalize=False):
        return eval(get_shortish_repr(
            x, custom_repr=custom_repr,
            max_length=max_length,
            normalize=normalize
        ))
    assert round_trip(1) == 1
    assert round_trip('abc') == 'abc'
    assert round_trip((1, 2, 3)) == (1, 2, 3)
    assert round_trip({1: 2}) == {1: 2}

    class A(object):
        def __init__(self, x):
            self.x = x
        def __repr__(self):
            return '<A %s>' % self.x
    assert round_trip(A(1)) == A(1)

# Generated at 2022-06-12 20:04:34.837415
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    print(
        get_shortish_repr(
            ['a', 'b', 'c', 'd'],
            custom_repr=((list, lambda x: repr(x[:2])),),
            max_length=12,
            normalize=True
        )
    )
    print(
        get_shortish_repr(
            ['a', 'b', 'c', 'd'],
            custom_repr=((list, lambda x: repr(x[:2])),),
            max_length=12,
            normalize=False
        )
    )

# Generated at 2022-06-12 20:05:14.369758
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(None, ()) == repr

# Generated at 2022-06-12 20:05:16.240953
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert (get_shortish_repr(1, max_length=10, normalize=True) == '1')

# Generated at 2022-06-12 20:05:18.589991
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class MyWritableStream(WritableStream):
        def write(self, s):
            return s

    assert issubclass(MyWritableStream, WritableStream)



# Generated at 2022-06-12 20:05:30.477476
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('1234567890', max_length=100) == '1234567890'
    assert get_shortish_repr('1234567890', max_length=9) == '1234567...'
    assert get_shortish_repr('1234567890', max_length=8) == '1234567...'
    assert get_shortish_repr('1234567890', max_length=7) == '12345...'
    assert get_shortish_repr('1234567890', max_length=6) == '12345...'
    assert get_shortish_repr('1234567890', max_length=5) == '12...'
    assert get_shortish_repr('1234567890', max_length=4) == '12...'

# Generated at 2022-06-12 20:05:42.039443
# Unit test for function get_repr_function
def test_get_repr_function():
    class Foo(object): pass

    def custom_repr(x):
        return 'custom %s' % (x, )

    custom_repr_tuple = (custom_repr, )

    foo = Foo()
    assert get_repr_function(foo, custom_repr_tuple) is repr
    assert get_repr_function(foo, ((Foo, custom_repr), )) is custom_repr
    assert get_repr_function(foo, ((int, custom_repr), )) is repr

    custom_repr_tuple = (
        (Foo, custom_repr),
    )

    assert get_repr_function(foo, custom_repr_tuple) is custom_repr
    assert get_repr_function(2, custom_repr_tuple) is repr

   

# Generated at 2022-06-12 20:05:52.948955
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream): pass
    assert issubclass(MyWritableStream, WritableStream)
    assert not issubclass(WritableStream, MyWritableStream)
    assert MyWritableStream.__subclasshook__ == WritableStream.__subclasshook__

    class MyWritableStream(object): pass
    assert not issubclass(MyWritableStream, WritableStream)

    class MyWritableStream(WritableStream):
        def write(self, s): pass
    assert issubclass(MyWritableStream, WritableStream)

    class MyWritableStream(WritableStream):
        def write(self, s): return None
    assert issubclass(MyWritableStream, WritableStream)

    class MyWritableStream(WritableStream):
        def write(self, s): return NotImplemented

# Generated at 2022-06-12 20:05:55.373131
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class X: pass
    assert not issubclass(X, WritableStream)

    class Y(X):
        def write(self, s):
            pass

    assert issubclass(Y, WritableStream)

# Generated at 2022-06-12 20:05:59.890509
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A:
        def write(self, s):
            assert (
                isinstance(s, string_types) or
                isinstance(s, bytes)
            )

    assert issubclass(A, WritableStream)
    a = A()
    a.write(u'bla')
    a.write(b'bla')


try:
    import StringIO
    class StringIOStream(WritableStream):
        def __init__(self):
            self.stringio = StringIO.StringIO()

        def write(self, s):
            self.stringio.write(s)

        def __str__(self):
            return 'StringIOStream({!r})'.format(self.stringio.getvalue())
except ImportError:
    pass




# Generated at 2022-06-12 20:06:09.472047
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(123456789, max_length=7) == '1234567...'
    assert get_shortish_repr({'a': 123456789}, max_length=7) == "{'a': ...}"
    assert get_shortish_repr(123456789, max_length=None) == '123456789'
    assert get_shortish_repr({'a': 123456789}, max_length=None) == "{'a': 123456789}"
    assert get_shortish_repr(123456789, max_length=10) == '123456789'
    assert get_shortish_repr({'a': 123456789}, max_length=10) == '{...}'

# Generated at 2022-06-12 20:06:13.425642
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    from .string_stream import StringStream
    from .string_io import StringIO
    from .file_stream import FileStream
    from .raw_file_stream import RawFileStream
    for StreamType in (StringStream, StringIO, FileStream, RawFileStream):
        stream = StreamType()
        stream.write('abc')
        assert stream.read() == 'abc'



# Generated at 2022-06-12 20:07:25.084452
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class WritableStreamSubclass(WritableStream):
        def write(self, s):
            pass

    writable_stream_subclass = WritableStreamSubclass()
    assert isinstance(writable_stream_subclass, WritableStream)



# Generated at 2022-06-12 20:07:27.587639
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(None, ((type(None), lambda x: 'fish'),)) == 'fish'
    assert callable(get_repr_function(None, ((None, lambda x: 'fish'),)))



# Generated at 2022-06-12 20:07:33.487009
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    a = [1, 2, 3, 4]
    try:
        a[5]
    except:
        _, exc_value, _ = sys.exc_info()

    assert get_shortish_repr(a) == '[1, 2, 3, 4]'
    assert get_shortish_repr([1, 2, 3, 4],
                             max_length=10) == '[1, 2, ...]'
    assert get_shortish_repr(a, custom_repr=[(list, lambda x: 'fuuu')]) == 'fuuu'
    assert get_shortish_repr(a, custom_repr=[(list, 'fuuu')]) == 'fuuu'
    assert get_shortish_repr(None) == 'None'

# Generated at 2022-06-12 20:07:35.519341
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class a(WritableStream):
        def write(self, x):
            return x
    assert isinstance(a(), WritableStream)

# Generated at 2022-06-12 20:07:43.737157
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    # `get_shortish_repr` should use `repr` by default
    assert get_shortish_repr(1) == repr(1)  # noqa
    assert get_shortish_repr(1.5) == repr(1.5)  # noqa
    assert get_shortish_repr('hello') == repr('hello')  # noqa
    # `get_shortish_repr` should limit the returned representation to the
    # specified length
    assert len(get_shortish_repr('hello', max_length=4)) == 4  # noqa
    # `get_shortish_repr` should support a `custom_repr` argument
    assert get_shortish_repr(1, custom_repr=((int, str),)) == '1'  # noqa
    assert get_

# Generated at 2022-06-12 20:07:46.438402
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class TestClass(WritableStream):
        def write(self, s):
            print('write got called with parameter {}'.format(s))

    TestClass().write('hello world')

# Generated at 2022-06-12 20:07:48.872729
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def __init__(self):
            self.written_text = ''
        def write(self, s):
            self.written_text += s
    stream = MyWritableStream()
    stream.write('hello')
    assert stream.written_text == 'hello'




# Generated at 2022-06-12 20:07:56.687519
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    import sys
    import os
    from .pycompat import StringIO
    
    assert isinstance(sys.stdout, WritableStream)
    assert isinstance(sys.stderr, WritableStream)
    assert isinstance(StringIO(), WritableStream)
    assert isinstance(StringIO(), io.StringIO)
    if sys.version_info.major == 2:
        import tkMessageBox
        assert isinstance(tkMessageBox, WritableStream)
    else:
        import tkinter
        import tkinter.messagebox
        assert isinstance(tkinter.messagebox, WritableStream)
    try:
        open(os.devnull, 'w')
    except OSError:
        pass

# Generated at 2022-06-12 20:08:01.850842
# Unit test for function get_repr_function
def test_get_repr_function():
    assert(get_repr_function(1) == repr)
    assert(get_repr_function('hello') == repr)
    assert(get_repr_function('hello', [(lambda x: False, lambda x: x)]) ==
           repr)
    assert(get_repr_function(
        'hello', [(lambda x: True, lambda x: x * 2)]
    ) == (lambda x: x * 2))



# Generated at 2022-06-12 20:08:03.985593
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def write(self, s):
            pass
    assert issubclass(MyWritableStream, WritableStream)