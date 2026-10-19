

# Generated at 2022-06-12 19:58:45.596194
# Unit test for function get_repr_function
def test_get_repr_function():

    class A(object): pass
    class B(A): pass
    class C(A): pass

    def repr_B(x): return 'B: ' + repr(x)
    def repr_C(x): return 'C: ' + repr(x)
    def repr_A(x): return 'A: ' + repr(x)

    customs = (
        (A, repr_A),
        (B, repr_B),
        (C, repr_C),
    )

    assert get_repr_function(A(), customs) is repr_A
    assert get_repr_function(B(), customs) is repr_B
    assert get_repr_function(C(), customs) is repr_C

    class D(C): pass

    assert get_repr_function(D(), customs) is repr_C


# Generated at 2022-06-12 19:58:49.473677
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class T(WritableStream):
        def __init__(self):
            self.k = []
        def write(self, s):
            self.k.append(s)
    t = T()
    t.write(1)
    t.write(2)
    assert t.k == [1, 2]


# Generated at 2022-06-12 19:58:55.455599
# Unit test for function get_repr_function
def test_get_repr_function():
    import six
    class A(object):
        pass
    class B(A):
        pass
    a = A()
    b = B()
    def repr_A(x):
        return 'repr_A ' + repr(x)
    def repr_B(x):
        return 'repr_B ' + repr(x)
    repr_a = get_repr_function(a, ((A, repr_A), (B, repr_B)))
    assert repr_a is repr_A
    repr_b = get_repr_function(b, ((A, repr_A), (B, repr_B)))
    assert repr_b is repr_B
    def repr_int(x):
        return 'repr_int ' + repr(x)

# Generated at 2022-06-12 19:59:03.852589
# Unit test for function get_shortish_repr

# Generated at 2022-06-12 19:59:05.297689
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class WritableStreamTest(WritableStream):
        def write(self, s):
            pass
    WritableStreamTest()
    print('test_WritableStream_write passed successfully')



# Generated at 2022-06-12 19:59:06.813834
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    sys.stdout.write('foo')
    assert isinstance(sys.stdout, WritableStream)
    assert issubclass(file, WritableStream)



# Generated at 2022-06-12 19:59:12.621636
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, []) is repr

    assert get_repr_function(1, [(lambda x: True, lambda x: 5)]) == 5
    assert get_repr_function(1, [(lambda x: False, lambda x: 5)]) is repr
    assert get_repr_function(1, [(lambda x: True, lambda x: 5),
                                 (lambda x: False, lambda x: 3)]) == 5
    assert get_repr_function(1, [(lambda x: False, lambda x: 5),
                                 (lambda x: True, lambda x: 3)]) == 3
    assert get_repr_function(1, [(lambda x: False, lambda x: 5),
                                 (lambda x: False, lambda x: 3)]) is repr


# Generated at 2022-06-12 19:59:24.638869
# Unit test for function get_repr_function
def test_get_repr_function():

    def f(x): return 'f(' + str(x) + ')'

    class A(object): pass
    class B(A): pass
    class C(object): pass

    assert get_repr_function(1, ()) == repr
    assert get_repr_function(1, ((1, f),)) == f
    assert get_repr_function(2, ((1, f),)) == repr
    assert get_repr_function(1.0, ((int, f),)) == f
    assert get_repr_function(1, ((int, f),)) == f
    assert get_repr_function(2, ((int, f),)) == f
    assert get_repr_function(1.5, ((int, f),)) == repr
    a = A()
    b = B()
    c = C()

# Generated at 2022-06-12 19:59:35.575244
# Unit test for function shitcode
def test_shitcode():
    assert shitcode('hello') == 'hello'
    assert shitcode(u'hello') == 'hello'
    assert shitcode(u'hellø') == 'hell?'
    assert shitcode(u'hellæ') == 'hell?'
    assert shitcode(u'\u05d5') == '?'

# Generated at 2022-06-12 19:59:43.566009
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def __init__(self, value_list=None):
            if value_list is None:
                value_list = []
            self.value_list = value_list
        def write(self, s):
            self.value_list.extend(s)

    assert issubclass(MyWritableStream, WritableStream)

    stream = MyWritableStream()
    assert stream.value_list == []
    stream.write(1)
    assert stream.value_list == [1]
    stream.write((2, 3))
    assert stream.value_list == [1, 2, 3]
    stream.write((4, 5))
    assert stream.value_list == [1, 2, 3, 4, 5]




# Generated at 2022-06-12 19:59:53.134474
# Unit test for function get_repr_function
def test_get_repr_function():
    class Foo(object): pass
    class Bar(object): pass
    class Baz(object): pass

    f = Foo()
    b = Bar()
    z = Baz()

    # First let's check the default case:
    assert get_repr_function(f) is repr
    assert get_repr_function(b) is repr
    assert get_repr_function(z) is repr

    # Now let's check the specification case:
    def a_func(x):
        if isinstance(x, Foo):
            return 'foo'
        if isinstance(x, Bar):
            return 'bar'
        if isinstance(x, Baz):
            return 'baz'
        assert False

    assert get_repr_function(f, custom_repr=((a_func, 'x'))) is a_func
   

# Generated at 2022-06-12 19:59:57.693667
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    from .type_tools import get_shortish_repr, CustomReprType, CustomReprObject
    import doctest
    assert doctest.testmod(get_shortish_repr).failed == 0

    assert get_shortish_repr(CustomReprType()) == '42'
    assert get_shortish_repr(CustomReprObject()) == '42'



# Generated at 2022-06-12 20:00:07.958392
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    from python_toolbox import cute_testing
    from python_toolbox.logic_tools import get_argument_callable
    for stream in (sys.stdout, sys.stderr):
        def write(_s):
            stream.write(_s)
        write = get_argument_callable(write)
        assert isinstance(write, WritableStream)
        with cute_testing.RaiseAssertor(AttributeError):
            class NoWriteable:
                pass
            isinstance(NoWriteable(), WritableStream)
        isinstance(write, WritableStream)
        with cute_testing.RaiseAssertor(AttributeError):
            class NoWriteable:
                def write(self, _s):
                    pass
            NoWriteable.write = get_argument_callable(NoWriteable.write)

# Generated at 2022-06-12 20:00:14.839845
# Unit test for function get_repr_function
def test_get_repr_function():
    def myrepr_int(x):
        return 'integer: ' + repr(x)
    def myrepr_float(x):
        return 'float: ' + repr(x)

    custom_repr = ((int, myrepr_int), (float, myrepr_float))

    assert get_repr_function(1, custom_repr) is myrepr_int
    assert get_repr_function(1.0, custom_repr) is myrepr_float

    def myrepr_dict(x):
        return 'dict: ' + repr(x)

    assert get_repr_function({}, custom_repr) is repr

    custom_repr = ((dict, myrepr_dict),) + custom_repr

    assert get_repr_function({}, custom_repr) is my

# Generated at 2022-06-12 20:00:19.937272
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(WritableStream):
        def write(self, s):
            pass
    assert issubclass(A, WritableStream)
    assert issubclass(A(), WritableStream)



# Generated at 2022-06-12 20:00:24.900423
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Superclass(object):
        def write(self, s):
            pass

    class Subclass(Superclass):
        def write(self, s):
            pass

    assert isinstance(Superclass(), WritableStream)
    assert isinstance(Subclass(), WritableStream)



# Generated at 2022-06-12 20:00:31.590716
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class WritableStream(metaclass=ABCMeta):
        @abstractmethod
        def write(self, string):
            pass
    class MyStream(WritableStream):
        def __init__(self):
            self.buffer = ''
        def write(self, string):
            self.buffer += string
    my_stream = MyStream()
    assert isinstance(my_stream, WritableStream)
    assert my_stream.buffer == ''
    my_stream.write('abc')
    assert my_stream.buffer == 'abc'

# Generated at 2022-06-12 20:00:39.079741
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class FileLike(WritableStream):
        def __init__(self, *args, **kwargs):
            pass
        def write(self, s):
            pass

    import tempfile
    temp_file = tempfile.TemporaryFile()

    class MyFileLike(FileLike):
        def __init__(self, filename):
            super(MyFileLike, self).__init__()
            self.filename = filename
        def write(self, s):
            with open(self.filename, 'w') as f:
                f.write(s)

    my_file_like = MyFileLike('~/my_file_like.txt')
    assert isinstance(my_file_like, WritableStream)

    import io
    assert isinstance(io.StringIO(), WritableStream)


# Generated at 2022-06-12 20:00:43.209997
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    global sys
    sys.stderr = NonImplementingWritableStream()
    try:
        import doctest
        doctest.testfile('tests/test_WritableStream.rst')
    finally:
        sys.stderr = sys.__stderr__

# Generated at 2022-06-12 20:00:51.831926
# Unit test for function get_repr_function
def test_get_repr_function():

    def get_repr_function(item, custom_repr):
        for condition, action in custom_repr:
            if isinstance(condition, type):
                condition = lambda x, y=condition: isinstance(x, y)
            if condition(item):
                return action
        return repr


# Generated at 2022-06-12 20:01:01.328937
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(int, custom_repr=((int, lambda x: 'int'))) == \
                                                                      (lambda x: 'int')

    assert get_repr_function(3, custom_repr=((int, lambda x: 'int'))) == \
                                                                      (lambda x: 'int')

    assert get_repr_function(3, custom_repr=((str, lambda x: 'str'))) == \
                                                                      repr

# Generated at 2022-06-12 20:01:09.613486
# Unit test for function get_repr_function
def test_get_repr_function():
    class Class1(object): pass
    class Class2(Class1): pass
    class Class3(object): pass
    class Class4(Class3): pass
    def repr_func_1(x):
        return 'repr_func_1'
    def repr_func_2(x):
        return 'repr_func_2'
    def repr_func_3(x):
        return 'repr_func_3'
    def repr_func_4(x):
        return 'repr_func_4'
    custom_repr = (
        (Class1, repr_func_1),
        (Class2, repr_func_2),
        (lambda x: isinstance(x, Class3), repr_func_3),
        (Class4, repr_func_4),
    )
    assert get_repr

# Generated at 2022-06-12 20:01:21.261135
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, []) == repr
    assert get_repr_function(2.5, []) == repr
    assert get_repr_function('a', []) == repr
    assert get_repr_function('a', [(lambda x: True, str)]) == str
    assert get_repr_function('a', [(lambda x: False, str)]) == repr
    assert get_repr_function('a', [(lambda x: False, str),
                                   (lambda x: True, str)]) == str
    assert get_repr_function('a', [(str, str)]) == str
    assert get_repr_function('a', [(float, str)]) == repr
    assert get_repr_function(2.5, [(float, str)]) == str
    assert get_repr_

# Generated at 2022-06-12 20:01:28.214393
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(object):
        def write(self, s):
            pass
    assert issubclass(A, WritableStream)

    class B(object):

        @classmethod
        def method(cls):
            pass


    class C(object):
        def write(self, s):
            pass

        @classmethod
        def method(cls):
            pass

    assert not issubclass(B, WritableStream)
    assert not issubclass(C, WritableStream)


_dict_with = object()


# Generated at 2022-06-12 20:01:34.688827
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('') == "''"
    assert get_shortish_repr('1') == "'1'"


if sys.version_info[0] == 3:
    # IronPython 2.7 returns a byte string for `repr(unicode(chr(0xFFFD)))`
    # when it should return a unicode string. We'll try to fix that.
    def unicode_repr(x):
        r = repr(x)
        if isinstance(r, bytes):
            return r.decode('utf-8')
        else:
            return r
else:
    unicode_repr = repr


# Generated at 2022-06-12 20:01:40.340749
# Unit test for function shitcode
def test_shitcode():
    assert shitcode('hello') == 'hello'
    assert shitcode('\0hello\0') == '\0hello\0'
    assert shitcode('\0\255hellö\0') == '\0\255hell?\0'
    assert shitcode('\0\255hellö\0'.decode('utf-8')) == '\0\255hell?\0'




# Generated at 2022-06-12 20:01:44.212801
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class FakeWritableStream(WritableStream):
        def __init__(self):
            self.s = ''
        def write(self, s):
            self.s += s
    FWS = FakeWritableStream()
    FWS.write('hello')
    assert FWS.s == 'hello'

# Generated at 2022-06-12 20:01:47.507001
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyClass(WritableStream):
        def write(self, s):
            pass
    assert issubclass(MyClass, WritableStream)
    assert issubclass(sys.__stdout__.__class__, WritableStream)

    class MyClass2:
        pass
    assert not issubclass(MyClass2, WritableStream)

# Generated at 2022-06-12 20:01:50.358139
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def __init__(self):
            self.write_was_called = False
        def write(self, s):
            assert not self.write_was_called
            self.write_was_called = True
    assert issubclass(MyWritableStream, WritableStream)



# Generated at 2022-06-12 20:01:59.399059
# Unit test for function get_repr_function
def test_get_repr_function():
    class A(object):
        pass
    class B(A):
        pass
    class C(object):
        pass
    class D(object):
        pass

    s = 's'
    assert get_repr_function(s, []) is repr

    def custom_repr(x):
        return 'custom_repr'
    assert get_repr_function(s, [(str, custom_repr)]) is custom_repr
    assert get_repr_function(A(), [(str, custom_repr)]) is repr
    assert get_repr_function(B(), [(str, custom_repr)]) is repr
    assert get_repr_function(C(), [(str, custom_repr)]) is repr
    assert get_repr_function(D(), [(str, custom_repr)]) is repr

# Generated at 2022-06-12 20:02:07.457493
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function((1,), ()) == repr
    assert get_repr_function((1,), ((type, str), str)) == str
    assert get_repr_function(1, ((type, str), str)) == repr
    assert get_repr_function((1,), ((lambda x: x == (1,), str), )) == str



# Generated at 2022-06-12 20:02:15.802143
# Unit test for function get_repr_function
def test_get_repr_function():
    assert eval(get_repr_function(1, [])(1)) == 1
    assert eval(get_repr_function('a', [])('a')) == 'a'
    assert eval(get_repr_function(1, [(int, str)])(1)) == '1'
    assert eval(get_repr_function('a', [(int, str)])('a')) == 'a'
    assert eval(get_repr_function(
        1, [(lambda x: x == 1, str), (int, type)]
    )(1)) == "<type 'int'>"
    assert eval(get_repr_function(
        'a', [(lambda x: x == 1, str), (int, type)]
    )('a')) == "'a'"



# Generated at 2022-06-12 20:02:22.673445
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    result = get_shortish_repr(set([1]), max_length=None)
    assert result == "<class 'set'>"
    result = get_shortish_repr([1, 2, 3], max_length=None)
    assert result == "[1, 2, 3]"
    result = get_shortish_repr({1: 2, 3: 4}, max_length=None)
    assert result == "{1: 2, 3: 4}"
    result = get_shortish_repr(set([1]), max_length=9)
    assert result == "<class 's...'>"
    result = get_shortish_repr([1, 2, 3], max_length=9)
    assert result == "[1, 2, ...]"

# Generated at 2022-06-12 20:02:28.112375
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def __init__(self) -> None:
            self.text_written = ''

        def write(self, s):
            self.text_written += s

    my_writable_stream = MyWritableStream()
    my_writable_stream.write('hello')
    assert my_writable_stream.text_written == 'hello'


# Generated at 2022-06-12 20:02:31.386204
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, custom_repr=(
        (lambda x: isinstance(x, int), str),
    )) is str



# Generated at 2022-06-12 20:02:41.550656
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(WritableStream):
        def write(self, s):
            pass

    class B(WritableStream):
        def write(self, s):
            pass

    class C(B):
        pass

    class D(WritableStream):
        pass

    assert WritableStream.__subclasshook__(A) is True
    assert issubclass(A, WritableStream)
    assert WritableStream.__subclasshook__(B) is True
    assert issubclass(B, WritableStream)
    assert WritableStream.__subclasshook__(C) is True
    assert issubclass(C, WritableStream)
    assert WritableStream.__subclasshook__(D) is NotImplemented
    assert not issubclass(D, WritableStream)



# Generated at 2022-06-12 20:02:48.954955
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(object):
        def write(self, s):
            pass
    obj = MyWritableStream()
    assert isinstance(obj, WritableStream)
    class MyWritableStream(object):
        def write(self, s):
            pass
        def write_line(self, s):
            pass
    obj = MyWritableStream()
    assert isinstance(obj, WritableStream)
    class MyWritableStream(object):
        def write_line(self, s):
            pass
    obj = MyWritableStream()
    assert not isinstance(obj, WritableStream)

# Generated at 2022-06-12 20:02:54.585019
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def __init__(self):
            self.output_string = ''

        def write(self, s):
            assert isinstance(s, string_types)
            self.output_string += s

    writable_stream = MyWritableStream()
    writable_stream.write('hello, world!')
    assert writable_stream.output_string == 'hello, world!'



# Generated at 2022-06-12 20:02:56.021692
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    # TODO: Write unit test for function `get_shortish_repr`
    pass



# Generated at 2022-06-12 20:03:05.190070
# Unit test for function get_repr_function
def test_get_repr_function():
    from .tools import assert_equal, assert_raises

    def _repr(x):
        return 'repr is {}'.format(x)
    def _repr2(x):
        return 'repr2 is {}'.format(x)
    def _repr3(x):
        return 'repr3 is {}'.format(x)

    assert get_repr_function(1, []) is repr

    assert_equal(get_repr_function(1, [(isinstance, _repr)])(1), 'repr is 1')
    assert_equal(get_repr_function('a', [(isinstance, _repr)])('a'), 'repr is a')

# Generated at 2022-06-12 20:03:19.263851
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('abc') == "'abc'"
    assert get_shortish_repr(123) == '123'
    assert get_shortish_repr(123, max_length=6) == '123'
    assert get_shortish_repr(123, max_length=5) == '123'
    assert get_shortish_repr(123, max_length=4) == '123'
    assert get_shortish_repr(123, max_length=3) == '123'
    assert get_shortish_repr(123, max_length=2) == '1...'
    assert get_shortish_repr(123, max_length=1) == '...'
    assert get_shortish_repr(123, max_length=0) == '...'
    assert get

# Generated at 2022-06-12 20:03:25.403533
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class MyWritableStream(WritableStream):
        def write(self, s):
            pass

    assert issubclass(MyWritableStream, WritableStream)

    class MyWritableStreamWithBrokenWrite(WritableStream):
        def not_write(self, s):
            pass

    assert not issubclass(MyWritableStreamWithBrokenWrite, WritableStream)



# Generated at 2022-06-12 20:03:27.953632
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def write(self, s):
            return s
    assert isinstance(MyWritableStream(), WritableStream)

# Generated at 2022-06-12 20:03:35.485441
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class GoodWritableStream(WritableStream):
        def write(self, s):
            assert isinstance(s, basestring)
            return len(s)
    assert issubclass(GoodWritableStream, WritableStream)

    class BadWritableStream1(WritableStream):
        def write(self, s):
            return len(s)
    assert not issubclass(BadWritableStream1, WritableStream)

    class BadWritableStream2(WritableStream):
        def write(self, s, length):
            return len(s)
    assert not issubclass(BadWritableStream2, WritableStream)

    class BadWritableStream3(WritableStream):
        def write(self, s):
            return 2.5
    assert not issubclass(BadWritableStream3, WritableStream)

   

# Generated at 2022-06-12 20:03:37.617157
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyFile(WritableStream):
        def write(self, s):
            pass
    assert issubclass(MyFile, WritableStream)

# Generated at 2022-06-12 20:03:47.795422
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    import sys
    import time
    import random


    class FakeTime(object):
        n = 0
        @staticmethod
        def sleep(t):
            FakeTime.n += t

    class FakeRandom(object):
        numbers = range(100)
        @staticmethod
        def random():
            return FakeRandom.numbers.pop(0) / 100.


    def fake_time_sleep(t):
        FakeTime.sleep(t)

    def fake_random_random():
        return FakeRandom.random()


    sys.modules['time'] = FakeTime
    sys.modules['random'] = FakeRandom

    sys.modules['time'].sleep = fake_time_sleep
    sys.modules['random'].random = fake_random_random


    n = 0


# Generated at 2022-06-12 20:03:52.432189
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class MyWritableStream(WritableStream):
        pass

    MyWritableStream.register(file)

    assert issubclass(file, MyWritableStream)
    assert issubclass(MyWritableStream, MyWritableStream)

    assert not issubclass(int, MyWritableStream)

# Generated at 2022-06-12 20:04:00.475923
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class TestWritableStream(WritableStream):
        def write(self, s):
            if not isinstance(s, string_types):
                raise TypeError('string_types')
            if isinstance(s, bytes):
                raise TypeError('bytes')

    assert issubclass(TestWritableStream, WritableStream)

    stream = TestWritableStream()
    stream.write('1')

    try:
        stream.write(1)
        raise AssertionError('`stream.write(1)` did not raise TypeError.')
    except TypeError:
        pass

    try:
        stream.write(b'2')
        raise AssertionError('`stream.write(b"2")` did not raise TypeError.')
    except TypeError:
        pass


# Generated at 2022-06-12 20:04:08.270292
# Unit test for function get_repr_function
def test_get_repr_function():
    class A: pass
    class B: pass
    class C: pass
    class D: pass
    class E(D): pass
    class F(E): pass
    
    custom_repr = [
        (A, str),
        (C, str),
        (D, str),
        (str, str),
    ]
    
    assert get_repr_function(A(), custom_repr) is str
    assert get_repr_function(B(), custom_repr) is repr
    assert get_repr_function(C(), custom_repr) is str
    assert get_repr_function(D(), custom_repr) is str

# Generated at 2022-06-12 20:04:18.606665
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    custom_repr = (None, lambda x: '???')

    assert get_shortish_repr(5) == '5'
    assert get_shortish_repr('yossi') == "'yossi'"

    assert get_shortish_repr(NotImplementedError(), custom_repr=custom_repr) == \
                                                                         '???'
    assert get_shortish_repr('yossi', custom_repr=custom_repr) == \
                                                                     '???'
    assert get_shortish_repr(NotImplementedError(), max_length=10,
                             custom_repr=custom_repr) == '???'

# Generated at 2022-06-12 20:04:40.081755
# Unit test for function get_repr_function
def test_get_repr_function():
    import re
    custom_repr = [
        (lambda x: isinstance(x, int),
         lambda x: '%d!' % x),
        (lambda x: isinstance(x, re._pattern_type),
         lambda x: x.pattern),
    ]

    def foo(match):
        return match.group(1) * int(match.group(2))
    custom_repr.append((re.compile(r'a{(.*),(.*?)}').search, foo))

    assert get_repr_function(42, custom_repr)(42) == '42!'
    assert get_repr_function(re.compile('foo'), custom_repr)(re.compile('foo')) \
        == 'foo'

# Generated at 2022-06-12 20:04:42.895856
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MockWritableStream(WritableStream):
        def write(self, s):
            assert isinstance(s, str)
    stream = MockWritableStream()
    stream.write('Hola')



# Generated at 2022-06-12 20:04:46.578472
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class LineWriter(object):
        def __init__(self):
            self.lines = []

        def write(self, s):
            self.lines.append(s)

    line_writer = LineWriter()

    assert issubclass(LineWriter, WritableStream)

# Generated at 2022-06-12 20:04:55.529700
# Unit test for function get_repr_function
def test_get_repr_function():
    try:
        import yaml
    except ImportError:
        return
    import collections
    import inspect
    d = collections.defaultdict(lambda: 'default value')
    assert get_shortish_repr(
        d,
        custom_repr=(
            (lambda x: isinstance(x, collections_abc.Mapping),
             lambda x: 'mapping {!r}'.format(yaml.dump(x))),
            (collections.defaultdict, lambda x: 'special'),
        ),
    ) == "'special'"
    assert ((get_repr_function(collections.defaultdict, ()).__module__,
            inspect.getsource(get_repr_function(collections.defaultdict, ())))
            == (__name__, 'repr(x)'))

# Generated at 2022-06-12 20:05:06.518941
# Unit test for function get_repr_function
def test_get_repr_function():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(B, C): pass
    class E(object): pass
    a = A()
    b = B()
    c = C()
    d = D()
    e = E()

    assert get_repr_function(a, custom_repr=((D, lambda x: 'd'),))(a) == 'd'
    assert get_repr_function(a, custom_repr=((D, lambda x: 'd'),))(b) == 'd'
    assert get_repr_function(a, custom_repr=((D, lambda x: 'd'),))(c) == 'd'

# Generated at 2022-06-12 20:05:11.624966
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Foo(WritableStream):
        pass

    foo = Foo()

    try:
        foo.write(5)
    except TypeError:
        assert True
    else:
        assert False

    try:
        return foo.write(b'abcdef') is None
    except NotImplementedError:
        assert True
    else:
        assert False




# Generated at 2022-06-12 20:05:15.651961
# Unit test for function get_repr_function
def test_get_repr_function():
    class A(object): pass
    class B(A): pass
    class C(B): pass
    class D(A): pass
    a = A()
    b = B()
    c = C()
    d = D()
    assert get_repr_function(a, [(A, lambda a: 'yay')])(a) == 'yay'
    assert get_repr_function(b, [(A, lambda a: 'yay')])(b) == 'yay'
    assert get_repr_function(c, [(A, lambda a: 'yay')])(c) == 'yay'
    assert get_repr_function(d, [(B, lambda a: 'yay')])(d) is None

# Generated at 2022-06-12 20:05:22.403335
# Unit test for function get_repr_function
def test_get_repr_function():
    def get_repr_function_test(item, custom_repr=(), expected_result=repr):
        assert get_repr_function(item, custom_repr) is expected_result

    get_repr_function_test(1, [])
    get_repr_function_test('', [])
    get_repr_function_test(1, [(lambda x: True, lambda x: '')])
    get_repr_function_test(1, [(lambda x: False, lambda x: '')])
    get_repr_function_test(1, [(lambda x: True, lambda x: ''),
                               (lambda x: True, lambda x: '')])

# Generated at 2022-06-12 20:05:32.025397
# Unit test for function get_repr_function
def test_get_repr_function():
    from .python_toolbox import frozendict, frozenset
    custom_repr = (
        (frozendict, lambda item: '%r' % item.data),
        (lambda x: hasattr(x, '__name__'), lambda item: item.__name__),
        (str, lambda item: '%r' % item),
        (re.compile, lambda item: item.pattern),
    )
    print(get_repr_function([1, 2, 3], custom_repr))
    d = frozendict({1: 2, 3: 4})
    print(get_repr_function(d, custom_repr))
    print(get_repr_function(frozenset([1, 2, 3]), custom_repr))

# Generated at 2022-06-12 20:05:42.903294
# Unit test for function get_shortish_repr
def test_get_shortish_repr():

    assert(get_shortish_repr('Testing', max_length=20) == 'Testing')
    assert(get_shortish_repr('Testing', max_length=4) == 'Tes...')
    assert(get_shortish_repr('Testing', max_length=5) == 'Testi...')
    assert(get_shortish_repr('Testing', max_length=6) == 'Testin...')
    assert(get_shortish_repr('Testing', max_length=7) == 'Testing')

    assert(get_shortish_repr('Testing', max_length=None) == 'Testing')
    assert(get_shortish_repr('Testing', max_length=-3) == 'Testing')


# Generated at 2022-06-12 20:06:07.604781
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class TestABC(WritableStream):
        def write(self, x):
            print('x')
    assert issubclass(TestABC, WritableStream)
    assert issubclass(TestABC, WritableStream)
    assert not issubclass(float, WritableStream)


# Generated at 2022-06-12 20:06:15.903106
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    reprs = (
        (0,),
        (0, 1),
        (object,),
        ([],),
        ((0,),),
        ([1, (2, 3), 'asdwqrwqrqwrqsdfq', ['asdqwerqwersdf']],),
        ({0, 1, 'asdwqrwqrqwrqsdfq', ['asdqwerqwersdf']},),
        ({'a': 1, 'b': 'asdwqrwqrqwrqsdfq', 'c': ['asdqwerqwersdf']},),
        ([i for i in range(100)],)
    )


# Generated at 2022-06-12 20:06:17.920295
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, ((lambda x: True, str),)) == str



# Generated at 2022-06-12 20:06:24.792993
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class MockWritableStream(WritableStream):
        def __init__(self):
            self.written = None

        def write(self, x):
            self.written = x

    mock_writable_stream = MockWritableStream()
    mock_writable_stream.write(3)

    time_now = time()
    time_now = time()
    time_now = time()
    time_now = time()
    time_now = time()
    time_now = time()
    time_now = time()
    time_now = time()
    time_now = time()
    time_now = time()

    assert mock_writable_stream.written == 3



# Generated at 2022-06-12 20:06:28.796415
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class WritableStreamSubclass(WritableStream):
        def __init__(self):
            self.write_buffer = []
        def write(self, s):
            self.write_buffer.append(s)

    stream = WritableStreamSubclass()
    assert not isinstance(stream, WritableStream)
    stream.write('a')
    assert stream.write_buffer == ['a']

# Generated at 2022-06-12 20:06:40.101508
# Unit test for function get_repr_function
def test_get_repr_function():
    list_ = []
    float_ = 3.1415
    string = 'hello world'
    tuple_ = (0, 1, 2)

    assert get_repr_function(list_, (
        (list, 'list'),
    )) == 'list'

    assert get_repr_function(float_, (
        (list, 'list'),
    )) == repr

    assert get_repr_function(float_, (
        (float_, 'float'),
    )) == 'float'

    assert get_repr_function(float_, (
        (lambda x: isinstance(x, float) and x == 3.1415, 'float'),
    )) == 'float'


# Generated at 2022-06-12 20:06:49.548756
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(1) == '1'
    assert get_shortish_repr(1, max_length=1) == '1'
    assert get_shortish_repr(1, max_length=2) == '1'
    assert get_shortish_repr((1,), max_length=2) == '(1)'
    assert get_shortish_repr((1,), max_length=3) == '(1)'
    assert get_shortish_repr((1,), max_length=4) == '(1)'
    assert get_shortish_repr((1,), max_length=5) == '(1)'
    assert get_shortish_repr((1,), max_length=6) == '(1)'

# Generated at 2022-06-12 20:06:52.456176
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    for write in (lambda s: sys.stdout.write(s), print, lambda s: s):
        assert isinstance(write, WritableStream)
    assert not isinstance(lambda s: None, WritableStream)
    assert not isinstance(object(), WritableStream)



# Generated at 2022-06-12 20:07:01.430809
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function('', ()) is repr
    assert get_repr_function('', ((int, lambda x: 'int'),)) is repr
    assert get_repr_function(1, ((int, lambda x: 'int'),)) is repr
    assert get_repr_function(1, (1, lambda x: 'int'),) is repr
    assert get_repr_function(1, ((int, lambda x: 'int'),
                                 (1, lambda x: '1'),
                                 (2, lambda x: '2'))) is repr
    assert get_repr_function(1, ((int, lambda x: 'int'),
                                 (1, lambda x: '1'),
                                 (2, lambda x: '2'))) is repr

# Generated at 2022-06-12 20:07:11.129489
# Unit test for function get_repr_function
def test_get_repr_function():
    from .testing_tools import assert_equal
    custom_repr = [
        (lambda x: isinstance(x, dict), lambda x: 'dictionary: {}'.format(x)),
        (lambda x: isinstance(x, (list, tuple)), lambda x: 'list: {}'.format(x)),
    ]
    assert_equal(get_repr_function({1: 2}, custom_repr), lambda x: 'dictionary: {}'.format(x))
    assert_equal(get_repr_function([1, 2], custom_repr), lambda x: 'list: {}'.format(x))
    assert_equal(get_repr_function(3, custom_repr), repr)



# Generated at 2022-06-12 20:07:53.862283
# Unit test for function get_repr_function
def test_get_repr_function():
    a = 'a'
    assert get_repr_function(a) is repr
    assert get_repr_function(a, [(lambda x: False, "I'm a teapot")]) is repr
    assert get_repr_function(a, [(str, str)]) is str



# Generated at 2022-06-12 20:08:03.433149
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(u'This is a long unicode string', max_length=20) \
                                            == u'This is a long...string'
    assert get_shortish_repr(b'This is a long strng', max_length=20) \
                                            == 'This is a lo...ng strng'
    assert get_shortish_repr([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], max_length=20) \
                                            == '[1, 2, 3, 4, ..., 8, 9, 0]'

# Generated at 2022-06-12 20:08:11.305821
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class NotWritableStream(object): pass
    class WritableStreamImplementingWrite(object):
        def write(self, s): pass
    class WritableStreamNotImplementingWrite(object):
        write = None
    class WritableStreamImplementingWriteAndSomethingElse(object):
        def write(self, s): pass
        def something_else(self): pass

    assert issubclass(NotWritableStream, WritableStream) is False
    assert issubclass(WritableStreamImplementingWrite, WritableStream) is True
    assert issubclass(WritableStreamNotImplementingWrite, WritableStream) is False
    assert issubclass(WritableStreamImplementingWriteAndSomethingElse,
                      WritableStream) is True

# Generated at 2022-06-12 20:08:20.029552
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(WritableStream): # noqa
        pass
    assert not issubclass(A, WritableStream)
    class B(WritableStream): # noqa
        def write(self, s):
            pass
    assert issubclass(B, WritableStream)
    class C(WritableStream): # noqa
        def write(self, s):
            return self.write(s)
    assert not issubclass(C, WritableStream)
    class D(WritableStream): # noqa
        def write(s):
            pass
    assert not issubclass(D, WritableStream)
    class E(WritableStream): # noqa
        def bla(self):
            pass
    assert not issubclass(E, WritableStream)



# Generated at 2022-06-12 20:08:26.214573
# Unit test for function get_repr_function
def test_get_repr_function():

    class A(object): pass
    class B(A): pass
    class C(B): pass
    class D(C): pass
    class E(D): pass

    def f(x): return ('f', x)
    def g(x): return ('g', x)

    custom_repr = [(A, f), (D, g)]

    a = A()
    b = B()
    c = C()
    d = D()
    e = E()

    assert get_repr_function(a, custom_repr) is repr
    assert get_repr_function(b, custom_repr) is repr
    assert get_repr_function(c, custom_repr) is repr
    assert get_repr_function(d, custom_repr) is g

# Generated at 2022-06-12 20:08:29.096668
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    class X:
        def write(self, s):
            pass
    assert isinstance(X(), WritableStream)
    assert not isinstance(sys.stdout, WritableStream)
    assert isinstance(io.StringIO(), WritableStream)




# Generated at 2022-06-12 20:08:34.004232
# Unit test for function get_repr_function
def test_get_repr_function():
    from .asserts import assert_equal
    assert_equal(get_repr_function(1, ((int, lambda x: '1')))(1), '1')
    assert_equal(get_repr_function(1, ((int, lambda x: '1'),) +
                                           ((str, lambda x: '2')))(1), '1')
    assert_equal(get_repr_function(1, ((float, lambda x: '2'),) +
                                           ((int, lambda x: '1')))(1), '1')
    assert_equal(get_repr_function(1, ((float, lambda x: '2'),) +
                                           ((int, lambda x: '1')))(1.0),
                                                                        '2')

