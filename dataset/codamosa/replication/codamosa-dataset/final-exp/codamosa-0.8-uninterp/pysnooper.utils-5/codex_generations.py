

# Generated at 2022-06-12 19:58:38.260429
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class WritableStreamTester(WritableStream):
        def __init__(self):
            self.str_ = ''

        def write(self, s):
            self.str_ += s

    wst = WritableStreamTester()
    wst.write('hello world')
    assert wst.str_ == 'hello world'



# Generated at 2022-06-12 19:58:44.129490
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('hi') == 'hi'
    assert get_shortish_repr('hi', max_length=2) == 'h...'
    assert get_shortish_repr('hi', max_length=1) == '...'
    assert get_shortish_repr('hi', max_length=3) == 'h...'
    assert get_shortish_repr('hi', max_length=3, normalize=True) == 'hi'
    assert get_shortish_repr('hi', max_length=5, normalize=True) == 'hi'
    assert get_shortish_repr('hi', max_length=4, normalize=True) == 'hi'
    assert get_shortish_repr('hi', max_length=3, normalize=True) == 'hi'

# Generated at 2022-06-12 19:58:47.113059
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyStream(WritableStream):
        def write(self, s):
            assert s == 'hi'
    my_stream = MyStream()
    my_stream.write('hi')



# Generated at 2022-06-12 19:58:51.782761
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class C:
        def __init__(self):
            self.so_far = ''
        def write(self, s):
            self.so_far += s
    assert issubclass(C, WritableStream)
    test_stream = C()
    test_stream.write('spam')
    assert test_stream.so_far == 'spam'





# Generated at 2022-06-12 19:58:54.021609
# Unit test for function shitcode
def test_shitcode():
    assert shitcode(u'abc') == u'abc'
    assert shitcode(u'abç') == u'ab?'
    assert type(shitcode(u'abç')) is unicode



# Generated at 2022-06-12 19:59:03.137521
# Unit test for function get_repr_function
def test_get_repr_function():
    example_object = object()
    assert get_repr_function(example_object) == repr
    assert get_repr_function(example_object, []) == repr
    assert get_repr_function(example_object, [
        (object, str),
    ]) == str
    assert get_repr_function(example_object, [
        (str, str),
        (type(None), str),
        (int, str),
    ]) == str
    assert get_repr_function(example_object, [
        (str, str),
        (type(None), str),
        (int, str),
    ]) == str

    def is_none(x): return x is None

# Generated at 2022-06-12 19:59:08.450443
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    from .contextlib_tools import managed_file
    with managed_file('') as file:
        class DummyWritable:
            def write(self, s):
                file.write(s)

        assert isinstance(DummyWritable(), WritableStream)

    class DummyWritable2:
        pass

    assert not isinstance(DummyWritable2(), WritableStream)






# Generated at 2022-06-12 19:59:12.889014
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    from .testing import run_assert_tests_with_array_reporter
    from .testing import assert_equal

    class MyStream(WritableStream):
        def __init__(self):
            self.text = ''

        def write(self, text):
            self.text += text

    stream = MyStream()
    stream.write('spam eggs')

    run_assert_tests_with_array_reporter(
        assert_equal,
        stream.text,
        'spam eggs'
    )

# Generated at 2022-06-12 19:59:24.843690
# Unit test for function shitcode
def test_shitcode():
    assert shitcode('abcdefghijklmnop') == 'abcdefghijklmnop'
    assert shitcode('abcd\xefghijklmnop') == 'abcd?ghijklmnop'
    assert shitcode('abcd\x7fghijklmnop') == 'abcd?ghijklmnop'
    assert shitcode('abcd\x80ghijklmnop') == 'abcd\x80ghijklmnop'
    assert shitcode('abcd\xffghijklmnop') == 'abcd\xffghijklmnop'
    assert shitcode(b'abcdefghijklmnop') == 'abcdefghijklmnop'
    assert shitcode(b'abcd\xefghijklmnop') == 'abcd?ghijklmnop'
    assert shitcode

# Generated at 2022-06-12 19:59:32.766115
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class DoesNotImplement(metaclass=ABC):
        __subclasshook__ = ABC.__subclasshook__

    class Implements(metaclass=ABC):
        __subclasshook__ = ABC.__subclasshook__
        @abc.abstractmethod
        def write(self):
            pass

    assert isinstance(DoesNotImplement, WritableStream) is False
    assert isinstance(Implements, WritableStream) is True
    assert isinstance(sys.__stdout__, WritableStream) is True



# Generated at 2022-06-12 19:59:44.601972
# Unit test for function get_repr_function
def test_get_repr_function():
    from .exceptions import (
        ReprFailure,
        NotReprizable,
        better_repr
    )
    class A(object):
        pass
    class B(object):
        pass
    f = lambda x: 'f'
    def g(x):
        return 'g'
    assert get_repr_function(1, [(2, 3)]) is repr

# Generated at 2022-06-12 19:59:48.736492
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io

    class Foo(WritableStream):
        def write(self, s):
            pass

    assert issubclass(io.StringIO, WritableStream)
    assert issubclass(io.BytesIO, WritableStream)

# Generated at 2022-06-12 19:59:56.695173
# Unit test for function get_repr_function
def test_get_repr_function():
    custom_repr = (
        (float, lambda x: 'X%rX' % x),
        (int, lambda x: 'Y%rY' % x),
    )
    assert get_repr_function(2, custom_repr) == 'Y%rY' % 2
    assert get_repr_function(2.5, custom_repr) == 'X%rX' % 2.5
    assert get_repr_function('hey', custom_repr) == repr('hey')

# Generated at 2022-06-12 20:00:03.941089
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(42, []) is repr
    assert get_repr_function(42, [(int, str)]) is str
    assert get_repr_function(42, [(lambda x: isinstance(x, int), str)]) is str
    assert get_repr_function(42, [(lambda x: isinstance(x, str), str),
                                  (lambda x: isinstance(x, int), str)]) is str



# Generated at 2022-06-12 20:00:09.013102
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class ConcreteWritableStream(WritableStream):
        def write(self, s):
            pass
    ConcreteWritableStream().write('s')
    class NotConcreteWritableStream(WritableStream):
        pass
    assert not issubclass(NotConcreteWritableStream, WritableStream)
    if sys.version_info[0] == 2:
        NotConcreteWritableStream()

# Generated at 2022-06-12 20:00:17.077666
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(5, ()) is repr
    assert get_repr_function(5, ((lambda x: True, lambda x: 'a'))) == 'a'
    assert get_repr_function(5, ((lambda x: False, lambda x: 'a'))) is repr
    assert get_repr_function(5, ((int, lambda x: 'a'))) == 'a'
    assert get_repr_function(5, ((int, lambda x: 'a'), (int, lambda x: 'b'))) == 'a'
    assert get_repr_function(5, ((str, lambda x: 'a'), (int, lambda x: 'b'))) == 'b'



# Generated at 2022-06-12 20:00:22.297580
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(int, ((int, repr))) is repr
    assert get_repr_function(1, ((int, repr))) is repr
    assert get_repr_function(int, ((str, str))) is repr
    assert get_repr_function(1, ((str, str))) is repr
    assert get_repr_function(int, ((str, str), (int, str))) is str
    assert get_repr_function(1, ((str, str), (int, str))) is str
    assert get_repr_function(1, ((str, str), (int, lambda x: 'x'))) == 'x'

# Generated at 2022-06-12 20:00:27.605872
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function('abc', (('abc', lambda _: 'asdf'),)) == 'asdf'
    assert get_repr_function('abc', (((0, 1), lambda _: 'asdf'),)) == repr
    assert get_repr_function(1, (((0, 1), lambda _: 'asdf'),)) == 'asdf'

# Generated at 2022-06-12 20:00:33.920609
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Obj:
        wrote = ''

        def write(self, s):
            self.wrote += s

    obj = Obj()
    assert isinstance(obj, WritableStream)
    assert issubclass(Obj, WritableStream)
    obj.write('hey')
    assert obj.wrote == 'hey'
    class BrokenObj:
        def write(self, s):
            pass

    assert not isinstance(BrokenObj(), WritableStream)
    assert not issubclass(BrokenObj, WritableStream)



# Generated at 2022-06-12 20:00:36.251425
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class FakeWritable(WritableStream):
        def write(self, s):
            assert isinstance(s, str)

    FakeWritable().write('s')



# Generated at 2022-06-12 20:00:41.076134
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    stream = io.StringIO()
    assert isinstance(stream, WritableStream)
    stream.write('yes')

# Generated at 2022-06-12 20:00:50.758395
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    class C(object):
        def __repr__(self):
            return 'hey'
    assert get_shortish_repr(1) == '1'
    assert get_shortish_repr(C()) == 'hey'
    assert get_shortish_repr(1, max_length=2) == '1'
    assert get_shortish_repr(1, max_length=0) == ''
    assert get_shortish_repr(1, max_length=1) == '1'
    assert get_shortish_repr(1, max_length=3) == '1'
    assert get_shortish_repr(1, max_length=4) == '1'
    assert get_shortish_repr(C(), max_length=2) == 'he...'
    assert get_short

# Generated at 2022-06-12 20:01:01.660492
# Unit test for function get_repr_function
def test_get_repr_function():

    class A(object): pass
    class B(object): pass
    class C(object): pass

    a = A()
    b = B()
    c = C()

    # First: Testing binary conditions

    repr_function = get_repr_function(
        a, (
            (bool, lambda x: 'A'+str(x)),
            (int, lambda x: 'B'+str(x)),
        )
    )
    assert repr_function(a) == 'A' + repr(True)

    repr_function = get_repr_function(
        20, (
            (bool, lambda x: 'A'+str(x)),
            (int, lambda x: 'B'+str(x)),
        )
    )
    assert repr_function(20) == 'B' + repr(20)

   

# Generated at 2022-06-12 20:01:06.558826
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def __init__(self, result):
            self.result = result
        def write(self, s):
            self.result.append(s)
    s = []
    w = MyWritableStream(s)
    w.write('hey there')
    w.write('how are you?')
    assert s == ['hey there', 'how are you?']

# Generated at 2022-06-12 20:01:10.845852
# Unit test for function shitcode
def test_shitcode():
    assert shitcode('אאאאאאאאאאאאאאא') == '?????????'
    assert shitcode('') == ''
    assert shitcode(u'\u1234') == '?'
    assert shitcode('-') == '-'
    assert shitcode(u'\U00012345') == '?'




# Generated at 2022-06-12 20:01:20.086855
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(None) is repr
    assert get_repr_function(5) is repr

    def int_repr(self): return 'an int'

    assert get_repr_function(5, [(int, int_repr)]) is int_repr

    def condition(x): return isinstance(x, int) and x > 3
    assert get_repr_function(5, [(condition, int_repr)]) is repr

    assert get_repr_function(4, [(condition, int_repr)]) is int_repr



# Generated at 2022-06-12 20:01:28.854977
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Y:
        pass

    class X:
        def write(self, s):
            pass

    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B, C):
        def write(self, s):
            pass

    class E(D):
        pass

    assert WritableStream.__subclasshook__(Y) is NotImplemented
    assert WritableStream.__subclasshook__(X) is True
    assert WritableStream.__subclasshook__(D) is True
    assert WritableStream.__subclasshook__(E) is True


# Generated at 2022-06-12 20:01:39.539517
# Unit test for function get_repr_function
def test_get_repr_function():
    assert (get_repr_function('', custom_repr=[]) == repr)

# Generated at 2022-06-12 20:01:43.617728
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(3, ((int, str),)) == str
    assert get_repr_function(3.0, ((int, str),)) == repr
    assert get_repr_function(3.0, ((int, str), (str, repr))) == repr



# Generated at 2022-06-12 20:01:50.430481
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(object):
        def write(self, foo):
            pass

    assert issubclass(A, WritableStream)

    class B(object):
        pass

    assert not issubclass(B, WritableStream)

    class C(object):
        def write(self, foo):
            pass

        def write2(self, foo):
            pass

    assert issubclass(C, WritableStream)

    class D(C):
        def write(self, foo):
            pass

    assert issubclass(D, WritableStream)

    class E(C):
        def write(self, foo):
            pass
        del write2

    assert issubclass(E, WritableStream)

    class F(E):
        def write(self, foo):
            pass
        del write2

    assert issubclass

# Generated at 2022-06-12 20:02:01.190181
# Unit test for function get_repr_function
def test_get_repr_function():
    assert normalize_repr('<Hebrew> at 0x10242F8F0>') == '<Hebrew>'

    assert get_shortish_repr(1.0, max_length=15) == '1.0'
    assert get_shortish_repr(set(['hey']), max_length=15) == "{'hey'}"
    assert get_shortish_repr(set(['hey']), max_length=10) == "{'h...'"
    assert get_shortish_repr(set(['hey']), max_length=5) == "{'...'"

    assert get_shortish_repr(1.0, max_length=15, normalize=True) == '1.0'

# Generated at 2022-06-12 20:02:11.300267
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class WritableStream(object):
        pass
    class Test1(WritableStream):
        def write(self, s):
            pass
    assert issubclass(Test1, WritableStream)
    class Test2(WritableStream):
        pass
    assert not issubclass(Test2, WritableStream)
    class Test3(WritableStream):
        def write(self, s):
            pass
        def write2(self, s):
            pass
    assert issubclass(Test3, WritableStream)
    class Test4(WritableStream):
        def write(self, s):
            pass
        write2 = None
    assert issubclass(Test4, WritableStream)
    class Test5(WritableStream):
        def write(self, s):
            pass
        write = None
    assert not issub

# Generated at 2022-06-12 20:02:14.459708
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class X(WritableStream):
        def write(self, s):
            pass

    x = X()

    assert isinstance(x, WritableStream)

# Generated at 2022-06-12 20:02:17.028068
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class FileLike(WritableStream):
        def write(self, s):
            pass

    class AlsoFileLike(FileLike):
        pass

    assert issubclass(AlsoFileLike, WritableStream)

# Generated at 2022-06-12 20:02:19.449445
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(WritableStream):
        def write(self, s):
            pass

    assert isinstance(A, WritableStream)
    assert issubclass(A, WritableStream)
    assert isinstance(A(), WritableStream)



# Generated at 2022-06-12 20:02:25.525979
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('my string which is too long!') == 'my string...long!'
    assert get_shortish_repr('my string which is too long!', max_length=1) == 'm...!'
    assert get_shortish_repr('my string which is too long!', max_length=2) == 'my...!'
    assert get_shortish_repr('my string which is too long!', max_length=3) == 'my ...!'
    assert get_shortish_repr('my string which is too long!', max_length=4) == 'my s...!'
    assert get_shortish_repr('my string which is too long!', max_length=5) == 'my s...!'

# Generated at 2022-06-12 20:02:30.379402
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class X(WritableStream):
        __slots__ = 's'
        def __init__(self):
            self.s = ''
        def write(self, s):
            self.s += s
    x = X()
    x.write('hello')
    assert x.s == 'hello'
    x.write(' ')
    assert x.s == 'hello '
    x.write('there')
    assert x.s == 'hello there'



# Generated at 2022-06-12 20:02:40.682049
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, custom_repr=()) == repr
    assert get_repr_function(1, custom_repr=[]) == repr
    assert get_repr_function(1, custom_repr=((int, lambda x: '1'), (int, 1))) == repr
    assert get_repr_function(1, custom_repr=((int, lambda x: '1'), (int, 1))) == repr
    assert get_repr_function(1, custom_repr=((int, lambda x: 'e'),)) == 'e'
    assert get_repr_function([], custom_repr=((int, lambda x: 'e'),
                                              (list, lambda x: 'lis'))) == 'lis'

# Generated at 2022-06-12 20:02:45.402021
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, (int, str)) is int.__repr__
    assert get_repr_function(1, (str, int)) is int.__repr__
    assert get_repr_function(1, (str,)) is repr
    assert get_repr_function(1, ((int, str),)) is int.__repr__




# Generated at 2022-06-12 20:02:49.822709
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class Writable(metaclass=ABCMeta):
        @abc.abstractmethod
        def write(self, s):
            raise NotImplementedError

        def flush(self):
            pass


    class RealWritable(Writable):
        def write(self, s):
            print(s)



    assert(issubclass(Writable, WritableStream))
    assert(issubclass(RealWritable, WritableStream))



# Generated at 2022-06-12 20:02:56.804936
# Unit test for function shitcode
def test_shitcode():
    orig_sys_stdout = sys.stdout
    try:
        sys.stdout = open(__file__.replace('.pyc', '.py'), 'rb')
        try:
            shitcode(sys.stdout.read())
        finally:
            sys.stdout.close()
    finally:
        sys.stdout = orig_sys_stdout



# Generated at 2022-06-12 20:03:05.884764
# Unit test for function get_repr_function
def test_get_repr_function():
    from .exceptions import TestException
    custom_repr = (
        (lambda x: isinstance(x, int), lambda x: 'int: %d' % x),
        (type, lambda x: 'class: %r' % x),
    )

    def test_custom_repr(item_repr, expected_repr):
        item = eval(item_repr)
        item_repr = get_shortish_repr(item, custom_repr)
        assert item_repr == expected_repr, test_custom_repr

    test_custom_repr("TestException('foo')",
                     'class: <exception test_python_toolbox.TestException>')
    test_custom_repr('TestException',
                     'class: <exception test_python_toolbox.TestException>')


# Generated at 2022-06-12 20:03:15.701165
# Unit test for function get_repr_function
def test_get_repr_function():
    l = [1]
    assert get_repr_function(l, []) is repr

    def get_repr(l, max_length=20):
        return get_repr_function(
            l,
            [(tuple, lambda x, y=max_length: truncate(repr(x), y)),
             (list, lambda x, y=max_length: truncate(repr(x), y))]
        )

    assert get_repr(l) is repr
    assert get_repr(tuple(l)) is truncate
    assert get_repr(tuple(l)) is truncate





# Generated at 2022-06-12 20:03:20.914854
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    a_list = list(range(20))
    a_list[5] = 'middle'
    assert get_shortish_repr(
        a_list,
        custom_repr=(
            (lambda x: x[5] == 'middle', lambda x: 'hello'),
        ),
        max_length=50,
        normalize=True
    ) == 'hello'
    assert get_shortish_repr(
        a_list,
        custom_repr=(
            (lambda x: x[5] == 'middle', lambda x: 'hello'),
        ),
        max_length=50,
        normalize=False
    ) == "'hello'"

# Generated at 2022-06-12 20:03:30.621346
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('') == "''"
    assert get_shortish_repr('') == "''"
    assert get_shortish_repr('hello') == "'hello'"
    assert get_shortish_repr('hello', max_length=4) == "'hel...'"
    assert get_shortish_repr('hello', max_length=2) == "'he...'"
    assert get_shortish_repr('he\nllo', max_length=4) == "'hel...'"
    assert get_shortish_repr('he\nllo', max_length=None) \
                                            in ("'he\\nllo'", 'he\\nllo')

    class A:
        def __repr__(self):
            return 'A'

# Generated at 2022-06-12 20:03:33.064602
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyIOWrapper(WritableStream):

        def __init__(self):
            self.value = ''


        def write(self, s):
            super(MyIOWrapper, self).write(s)
            self.value += s


    m = MyIOWrapper()
    m.write('!' * 10)
    assert m.value == '!' * 10




# Generated at 2022-06-12 20:03:35.341317
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class C(WritableStream):
        def write(self, s):
            pass
    c = C()
    c.write('hi')



# Generated at 2022-06-12 20:03:39.880360
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    """Ensure that `test.test_import.test_wrapper.test_WritableStream.test_WritableStream_write` passes"""
    class Foo:
        def write(self, s):
            pass
    assert isinstance(Foo(), WritableStream)



# Generated at 2022-06-12 20:03:42.753538
# Unit test for function shitcode
def test_shitcode():
    assert shitcode(u'בדיקה') == '???'
    assert shitcode(u'שלום.') == '????.'



# Generated at 2022-06-12 20:03:49.635014
# Unit test for function get_repr_function
def test_get_repr_function():
    class A: pass
    class B: pass
    class C: pass
    assert get_repr_function(A(), []) is repr
    assert get_repr_function(B(), []) is repr
    a = A()
    assert get_repr_function(a, [(lambda x: True, str)]) is str
    assert get_repr_function(a, [(lambda x: False, str)]) is repr
    assert get_repr_function(a, [
        (lambda x: False, str),
        (lambda x: True, str),
    ]) is str
    assert get_repr_function(a, [
        (lambda x: False, str),
        (A, str),
    ]) is str



# Generated at 2022-06-12 20:04:00.401713
# Unit test for function get_repr_function
def test_get_repr_function():
    from .python_toolbox import typing_tools
    class X(object):
        def __init__(self, x):
            self.x = x
        def __repr__(self):
            return 'X({!r})'.format(self.x)

    class A(object):
        pass
    class B(A):
        pass
    class C(A):
        pass

    b = B()
    c = C()
    x = X(10)

    assert get_repr_function(x, ()) == repr
    assert get_repr_function(c, ()) == repr
    assert get_repr_function(c, ((typing_tools.anything, str),)) == str

    assert get_repr_function(b, ((typing_tools.anything, str),)) == repr
    assert get_repr

# Generated at 2022-06-12 20:04:09.052608
# Unit test for function get_repr_function
def test_get_repr_function():

    def string_repr(x, max_length=70):
        return truncate(str(x), max_length)
    
    CUSTOM_REPR = (
        (lambda x: isinstance(x, list), lambda x: 'list'),
        (lambda x: isinstance(x, dict), lambda x: 'dict'),
        (lambda x: isinstance(x, set), lambda x: 'set'),
        (lambda x: isinstance(x, int), lambda x: 'int'),
        (lambda x: isinstance(x, str), string_repr),
        (str, string_repr),
        (tuple, string_repr),
    )
    

# Generated at 2022-06-12 20:04:19.397954
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(5, ((lambda x: True, lambda x: 'five'),)) == 'five'
    assert get_repr_function(5, ((lambda x: False, lambda x: 'five'),)) == repr
    assert get_repr_function(5, ((lambda x: False, lambda x: 'five'),
                                 (int, lambda x: 'five'))) == 'five'
    assert get_repr_function(5, ((lambda x: 'foo' in x, lambda x: 'five'),
                                 (int, lambda x: 'five'))) == 'five'
    assert get_repr_function('abc', ((lambda x: 'foo' in x, lambda x: 'five'),
                                     (int, lambda x: 'five'))) == repr



# Generated at 2022-06-12 20:04:28.121433
# Unit test for function get_repr_function
def test_get_repr_function():

    assert (repr('') ==
            repr(get_repr_function('', (
                (lambda s: True, lambda s: s.center(3, ' '))
            ))))

    assert (repr('') ==
            repr(get_repr_function('', (
                (lambda s: False, lambda s: s.center(3, ' '))
            ))))

    assert (repr('') ==
            repr(get_repr_function('', (
                (lambda s: True, lambda s: '123'),
                (lambda s: False, lambda s: s.center(3, ' '))
            ))))


# Generated at 2022-06-12 20:04:33.995324
# Unit test for function get_shortish_repr
def test_get_shortish_repr():

    class MyObject:
        def __repr__(self):
            return "MyObject"
    assert get_shortish_repr(MyObject(), max_length=9) == 'MyObject'
    assert get_shortish_repr(MyObject(), max_length=8) == 'MyObjec...'
    assert get_shortish_repr(MyObject(), max_length=7) == 'MyObj...'
    assert get_shortish_repr(MyObject(), max_length=6) == 'MyOb...'
    assert get_shortish_repr(MyObject(), max_length=5) == 'MyO...'
    assert get_shortish_repr(MyObject(), max_length=4) == 'My...'

# Generated at 2022-06-12 20:04:35.542367
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function('a', [(lambda x: True, str)]) == str

# Generated at 2022-06-12 20:04:46.060943
# Unit test for function get_repr_function
def test_get_repr_function():
    re_1 = re.compile(r'^123')
    re_2 = re.compile(r'^12')
    re_3 = re.compile(r'^1')
    re_4 = re.compile(r'^0')
    re_5 = re.compile(r'^')
    re_6 = re.compile(r'^\d+')

# Generated at 2022-06-12 20:04:54.545203
# Unit test for function shitcode
def test_shitcode():
    assert shitcode('הַכּוֹתֶל בִּימִין וְהַכּוֹתֶל בְּשֵׂמֹאל יִהְיֶה זֶרַע') == \
                                                                 '???...???...'
    assert shitcode('简体中文') == '????'
    assert shitcode('简体中文', encoding='gbk') == '简体中文'
    assert shitcode('简体中文', encoding='gb2312') == '简体中文'



# Generated at 2022-06-12 20:05:05.732801
# Unit test for function get_shortish_repr
def test_get_shortish_repr():

    assert get_shortish_repr(None) == 'None'
    assert get_shortish_repr('abc') == 'abc'
    assert get_shortish_repr('a\nb') == 'a\nb'
    assert get_shortish_repr('a\nb', max_length=2) == 'a...'
    assert get_shortish_repr([], max_length=2, normalize=True) == '[]'
    assert get_shortish_repr([1, 2], max_length=2, normalize=True) == '[1...'
    assert (
        get_shortish_repr(u'abc\rdef\nghi', max_length=8, normalize=True) ==
        'abcdef\n...'
    )

# Generated at 2022-06-12 20:05:16.069966
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import sys
    from .pycompat import PY2

    assert issubclass(sys.stdout, WritableStream)

    class MyWritableStream(WritableStream):

        def __init__(self):
            self.last_thing_written = None

        def write(self, thing):
            self.last_thing_written = thing

    my_writable_stream = MyWritableStream()
    my_writable_stream.write('hi')
    assert my_writable_stream.last_thing_written == 'hi'

    my_writable_stream = MyWritableStream()
    my_writable_stream.write(u'hi')
    assert my_writable_stream.last_thing_written == u'hi'

    # Test number 2 is only relevant to Python 2
    my_writable_stream = My

# Generated at 2022-06-12 20:05:30.584092
# Unit test for function get_repr_function
def test_get_repr_function():
    class X(object):
        def __repr__(self):
            return 'repr from X object'

    x = X()
    assert get_repr_function(x, [])() == 'repr from X object'
    assert get_repr_function(x, [
        (lambda x: isinstance(x, X), lambda x: 'repr from X class')
    ])() == 'repr from X class'

    assert get_repr_function(2, [
        (lambda x: isinstance(x, X), lambda x: 'repr from X class'),
    ])() == repr(2)

    a = (1, 2, 3)

# Generated at 2022-06-12 20:05:42.119593
# Unit test for function shitcode
def test_shitcode():
    assert shitcode('שלום עולם') == 'שלום עולם'
    assert shitcode('\xa4\xa5') == '??'
    assert shitcode('') == ''
    assert shitcode('a') == 'a'
    assert shitcode(ensure_binary_string('\xa4\xa5')) == '??'


if sys.version_info[0] == 2:
    def ensure_binary_string(string):
        if isinstance(string, unicode):
            return string.encode('utf-8')
        else:
            return string
else:
    def ensure_binary_string(string):
        if isinstance(string, bytes):
            return string
        else:
            return string.encode('utf-8')

# Generated at 2022-06-12 20:05:53.077818
# Unit test for function shitcode
def test_shitcode():
    assert shitcode(b'\xde\xad\xbe\xef') == '????'
    assert shitcode(b'\xde\xab\xbe\xef') == '???'
    assert shitcode(b'\xde\xad\xbe\x00') == '???'
    assert shitcode(b'\xde\xad\xbe\xff') == '???'
    assert shitcode(b'\xde\xad\x00\xef') == '???'
    assert shitcode(b'\xde\xad\xff\xef') == '???'
    assert shitcode(b'\xde\x00\xbe\xef') == '?'
    assert shitcode(b'\xde\xff\xbe\xef') == '?'
    assert shitcode

# Generated at 2022-06-12 20:05:57.601106
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(5, []) == repr

    assert get_repr_function(5, [(int, lambda x: 'int')]) == \
                                                        (lambda x: 'int')

    assert get_repr_function(5, [(lambda x: x > 4, lambda x: 'big')]) == \
                                                        (lambda x: 'big')



# Generated at 2022-06-12 20:06:07.491635
# Unit test for function get_repr_function
def test_get_repr_function():
    class A: pass
    class B: pass
    class C: pass
    class AA(A): pass
    class AB(A): pass
    a = A()
    b = B()
    c = C()
    aa = AA()
    ab = AB()

    def first_repr(x):
        return 'FIRST REPR'
    def second_repr(x):
        return 'SECOND REPR'

    assert get_repr_function(a, (
        (lambda x: x is a, first_repr),
        (lambda x: isinstance(x, A), second_repr),
        (lambda x: False, lambda x: 'error'),
    ))(a) == first_repr(a)

# Generated at 2022-06-12 20:06:12.872981
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    long_string = 'a' * 500
    assert get_shortish_repr(long_string) == long_string
    assert get_shortish_repr(long_string, max_length=400) == 'a' * 400
    from . import misc_tools
    assert (get_shortish_repr(
        misc_tools.GoodCustomRepr, normalize=True
    ) == '<misc_tools.GoodCustomRepr instance>')

# Generated at 2022-06-12 20:06:14.601343
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyStream(WritableStream):
        def write(self, s):
            assert isinstance(s, str)
            assert s == 'hello'
    MyStream().write('hello')

# Generated at 2022-06-12 20:06:23.713447
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(range(100)) == '(0, 1, 2, 3, 4, 5, ..., 94, 95, 96, 97, 98, 99)'
    assert get_shortish_repr('abcdefghijklmnopqrstuvwxyz') == 'abcdefghijklmnopqrstuvwxyz'
    assert get_shortish_repr('abcdefghijklmnopqrstuvwxyz', max_length=26) == 'abcdefghijklmnopqrstuvwxyz'
    assert get_shortish_repr('abcdefghijklmnopqrstuvwxyz', max_length=25) == 'abcdefghijklmnopqrstuvw...'

# Generated at 2022-06-12 20:06:30.361936
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class GoodWritable(WritableStream):
        def write(self, s):
            print(s)

    assert issubclass(GoodWritable, WritableStream)

    class BadWritable1(WritableStream):
        pass

    assert not issubclass(BadWritable1, WritableStream)

    class BadWritable2(WritableStream):
        def write(self, s):
            print(s)

        def write2(self, s):
            print(s)

    assert not issubclass(BadWritable2, WritableStream)

    class BadWritable3(WritableStream):
        def write(self, s):
            print(s)

    BadWritable3.write = None
    assert not issubclass(BadWritable3, WritableStream)



# Generated at 2022-06-12 20:06:41.937731
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class MyWritableStream(WritableStream):

        def __init__(self):
            self.output = ''

        def write(self, s):
            assert isinstance(s, str)
            self.output += s

    my_writable_stream = MyWritableStream()
    my_writable_stream.write('hi')
    assert my_writable_stream.output == 'hi'

    assert isinstance(my_writable_stream, WritableStream)
    assert issubclass(MyWritableStream, WritableStream)

    assert isinstance(sys.stdout, WritableStream)
    assert issubclass(type(sys.stdout), WritableStream)

    class MyNonWritableStream(WritableStream):
        pass

    assert not isinstance(MyNonWritableStream(), WritableStream)
    assert not iss

# Generated at 2022-06-12 20:06:53.627030
# Unit test for function get_repr_function
def test_get_repr_function():
    assert not issubclass(dict, tuple)
    class Tuplifier(type(lambda: 0)):
        def __repr__(self):
            return 'TUPLE OF {}'.format(super(Tuplifier, self).__repr__())

    custom_repr = ((lambda x: isinstance(x, tuple), Tuplifier),)
    assert get_repr_function(tuple(), custom_repr)(tuple()) == 'TUPLE OF ()'
    assert get_shortish_repr(tuple(), custom_repr=custom_repr) \
                                                                == 'TUPLE OF ()'

    assert get_repr_function(dict(), custom_repr=(lambda x: isinstance(x, tuple),
                                                  lambda x: 'tuple')) == repr
    assert get_shortish_

# Generated at 2022-06-12 20:07:03.378645
# Unit test for function get_shortish_repr
def test_get_shortish_repr():

    assert get_shortish_repr('hello world', max_length=4) == 'hel...'
    assert get_shortish_repr('hello world', max_length=5) == 'hello...'
    assert get_shortish_repr('hello world', max_length=6) == 'hello...'
    assert get_shortish_repr('hello world', max_length=7) == 'hello w...'
    assert get_shortish_repr('hello world', max_length=8) == 'hello wo...'
    assert get_shortish_repr('hello world', max_length=9) == 'hello wor...'
    assert get_shortish_repr('hello world', max_length=10) == 'hello worl...'
    assert get_shortish_repr('hello world', max_length=11)

# Generated at 2022-06-12 20:07:13.205091
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(12345, max_length=12) == '12345'
    assert get_shortish_repr('bacon', max_length=12) == 'bacon'
    assert get_shortish_repr('a'*100, max_length=4) == 'a...a'
    assert get_shortish_repr('a'*123, max_length=11) == 'a...a (123)'
    assert get_shortish_repr('a'*123, max_length=11, normalize=True) == \
                                                                     'a...a'
    assert get_shortish_repr('a'*123, max_length=11, normalize=True) == \
                                                                     'a...a'

# Generated at 2022-06-12 20:07:20.063634
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    custom_repr = (
        (lambda x: isinstance(x, str), lambda x: 'the string {!r}'.format(x)),
        (lambda x: isinstance(x, set), lambda x: 'the set {!r}'.format(x)),
    )
    assert (get_shortish_repr(123, custom_repr) ==
            get_shortish_repr(123, custom_repr, 10) ==
            get_shortish_repr(123, custom_repr, 1) ==
            '123')
    assert (get_shortish_repr('hi', custom_repr) ==
            get_shortish_repr('hi', custom_repr, 1) ==
            'the...')

# Generated at 2022-06-12 20:07:26.228407
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class OneWrite(WritableStream):
        def write(self, s):
            return 1
    assert isinstance(OneWrite(), WritableStream)

    class ZeroWrite(WritableStream):
        def write(self, s):
            return 0
    assert not isinstance(ZeroWrite(), WritableStream)

    class BrokenWrite(WritableStream):
        pass
    assert not isinstance(BrokenWrite(), WritableStream)



# Generated at 2022-06-12 20:07:32.517427
# Unit test for function get_repr_function
def test_get_repr_function():
    class A(object):
        pass
    class B(A):
        pass

    # A function matching the item
    assert get_repr_function(1, custom_repr=[(lambda x: True, lambda x: 'b')]) == 'b'
    # A function not matching the item
    assert get_repr_function(1, custom_repr=[(lambda x: False, lambda x: 'b')]) != 'b'
    # A function matching a given type
    assert get_repr_function(B(), custom_repr=[(B, lambda x: 'b')]) == 'b'
    assert get_repr_function(A(), custom_repr=[(B, lambda x: 'b')]) != 'b'
    # Several functions

# Generated at 2022-06-12 20:07:39.947434
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    import sys
    assert issubclass(io.StringIO, WritableStream)
    assert issubclass(sys.stdout, WritableStream)
    assert not issubclass(int, WritableStream)
    assert not issubclass(dict, WritableStream)
    assert not issubclass(type, WritableStream)
    assert not issubclass(io.StringIO.__new__, WritableStream)
    class C(object):
        def write(self, x):
            return 'hi'
    assert issubclass(C, WritableStream)
    class D(object):
        pass
    assert not issubclass(D, WritableStream)

# Generated at 2022-06-12 20:07:47.417490
# Unit test for function get_repr_function
def test_get_repr_function():
    fixture_1 = (
        # (condition, action)
        (lambda x: x, lambda x: 'first'),
        (lambda x: x, lambda x: 'second')
    )
    assert get_repr_function(1, fixture_1) == fixture_1[0][1]
    assert get_repr_function(2, fixture_1) == fixture_1[1][1]
    assert get_repr_function(3, fixture_1) == repr

    fixture_2 = (
        (1, lambda x: 'first'),
        (2, lambda x: 'second'),
        (3, lambda x: 'third')
    )
    assert get_repr_function(1, fixture_2) == fixture_2[0][1]
    assert get_repr_function(2, fixture_2) == fixture

# Generated at 2022-06-12 20:07:55.090273
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function('abc', []) is repr
    assert get_repr_function(13, [
        (lambda x: isinstance(x, str), lambda x: 'string: ' + x),
        (lambda x: isinstance(x, int), lambda x: 'integer: ' + str(x)),
    ]) == 'integer: 13'
    assert get_repr_function('abc', [
        (lambda x: isinstance(x, str), lambda x: 'string: ' + x),
        (lambda x: isinstance(x, int), lambda x: 'integer: ' + str(x)),
    ]) == 'string: abc'

# Generated at 2022-06-12 20:08:03.987631
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    def one():
        class Foo(object):
            @property
            def custom_repr(self):
                return 'bar'
        foo = Foo()
        assert get_shortish_repr(foo) == 'bar'


    def two():
        def get_repr(message):
            def repr_function(x):
                return message
            return repr_function

        foo = 'foo'
        assert get_shortish_repr(foo, custom_repr=((str, get_repr('bar')),)) == \
                                                                            'bar'

        assert get_shortish_repr(foo, custom_repr=((str, get_repr('bar')),
                                                   (object, get_repr('baz')))) \
                                                                           == 'bar'

    one()
   

# Generated at 2022-06-12 20:08:12.059686
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class WritableStreamTest(WritableStream):
        def write(self, s):
            pass
    WritableStreamTest.register(file)
    assert issubclass(file, WritableStream)
    assert WritableStreamTest in WritableStream.__subclasses__()

    class NotWritableStreamTest:
        def write(self, s):
            pass
    assert not issubclass(NotWritableStreamTest, WritableStream)



# Generated at 2022-06-12 20:08:20.840195
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(1) == '1'
    assert get_shortish_repr(1, max_length=2) == '1'
    assert get_shortish_repr(1, max_length=1) == '1'
    assert get_shortish_repr(1, max_length=1) == '1'
    assert get_shortish_repr(1, max_length=0) == ''
    assert get_shortish_repr('a' * 100, max_length=101) == 'a' * 100
    assert get_shortish_repr('a' * 101, max_length=101) == 'a' * 101
    assert get_shortish_repr('a' * 100, max_length=100) == 'a' * 100
    assert get_shortish_re

# Generated at 2022-06-12 20:08:28.869209
# Unit test for function get_shortish_repr
def test_get_shortish_repr():

    def assert_shortish_repr_of(item, result):
        assert get_shortish_repr(item) == result

    class Foo:
        def __repr__(self):
            return u'Foo object'

    class Bar:
        def __repr__(self):
            return u'Bar object'

    class Baz:
        def __repr__(self):
            return b'Baz object'

    assert_shortish_repr_of(123, '123')
    assert_shortish_repr_of(123.456, '123.456')
    assert_shortish_repr_of(Foo(), 'Foo object')
    assert_shortish_repr_of(Bar(), 'Bar object')
    assert_shortish_repr_of(Baz(), 'Baz object')

