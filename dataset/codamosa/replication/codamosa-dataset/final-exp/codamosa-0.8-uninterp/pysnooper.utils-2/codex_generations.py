

# Generated at 2022-06-12 19:58:45.083591
# Unit test for function get_repr_function
def test_get_repr_function():
    class A(object):
        pass
    class B(A):
        pass
    a = A()
    b = B()
    assert get_repr_function(a, custom_repr=((A, lambda x: 'A'),))(a) == 'A'
    assert get_repr_function(b, custom_repr=((A, lambda x: 'A'),))(b) == 'A'
    assert get_repr_function(a, custom_repr=((B, lambda x: 'B'),))(a) == 'A'
    assert get_repr_function(b, custom_repr=((B, lambda x: 'B'),))(b) == 'B'


# Generated at 2022-06-12 19:58:49.221957
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr([1, 2, 3]) == '[1, 2, 3]'
    assert get_shortish_repr([1, 2, 3], max_length=10) == '[1, 2, 3]'
    assert get_shortish_repr([1, 2, 3], max_length=5) == '[...]'
    assert get_shortish_repr([1, 2, 3], max_length=4) == '[1, 2]'
    assert get_shortish_repr([1, 2, 3], max_length=3) == '[1]'
    assert get_shortish_repr([1, 2, 3], max_length=2) == '[1]'
    assert get_shortish_repr([1, 2, 3], max_length=1) == '...'
    assert get_shortish

# Generated at 2022-06-12 19:58:55.344904
# Unit test for function get_repr_function
def test_get_repr_function():

    def test_equality(x, y):
        assert get_repr_function(x, custom_repr)(x) == y


    # Test that calling it with an `int` returns `repr(x)`
    for x in range(100):
        assert get_repr_function(x, custom_repr) is repr

    # Test that calling it with a `type` returns `repr(x)`
    for x in (int, type, object, str, bool):
        assert get_repr_function(x, custom_repr) is repr


    class X(object):
        pass
    x = X()

    # Test that calling it with an `X` returns `repr(x)`
    assert get_repr_function(x, custom_repr) is repr


    # Test that calling it

# Generated at 2022-06-12 19:58:59.811476
# Unit test for function shitcode
def test_shitcode():
    assert shitcode('hello') == 'hello'
    assert shitcode('hello\nwo\trld') == 'hello\nwo\trld'
    assert shitcode(u'Áÿü') == '???'
    if sys.version_info.major == 2:
        assert type(shitcode('hello')) is unicode

# Generated at 2022-06-12 19:59:04.178892
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class X:
        def write(self, s):
            pass

    assert issubclass(X, WritableStream)
    assert isinstance(X(), WritableStream)



# Generated at 2022-06-12 19:59:09.900820
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('hello', max_length=5) == 'hello'
    assert get_shortish_repr('hello', max_length=4) == 'hel'
    assert get_shortish_repr('hello', max_length=3) == 'he'
    assert get_shortish_repr('hello', max_length=2) == 'h'
    assert get_shortish_repr('hello', max_length=1) == ''
    assert get_shortish_repr('hello', max_length=0) == ''
    assert get_shortish_repr('hello', max_length=None) == 'hello'

    assert get_shortish_repr('helloworld', max_length=5) == 'h...d'

# Generated at 2022-06-12 19:59:11.988523
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    from .shugy import Empty
    from .shugy import EmptyDerived
    assert WritableStream.__subclasshook__(Empty) is NotImplemented
    assert WritableStream.__subclasshook__(EmptyDerived) is True



# Generated at 2022-06-12 19:59:17.908897
# Unit test for function shitcode
def test_shitcode():
    assert shitcode('a') == 'a'
    assert shitcode('a\x00') == 'a\x00'
    assert shitcode('a\x00b') == 'a\x00b'
    assert shitcode('a\x00b\xd5\xc3\xad') == 'a\x00b????'



# Generated at 2022-06-12 19:59:21.792578
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(WritableStream):
        def write(self, x):
            pass


    class B(A):
        pass


    assert isinstance(A(), WritableStream)
    assert isinstance(B(), WritableStream)



# Generated at 2022-06-12 19:59:30.496694
# Unit test for function get_repr_function
def test_get_repr_function():

    class Widget(object):
        pass

    class WidgetChild(Widget):
        pass

    class WidgetGranChild(WidgetChild):
        pass

    class WidgetGreatGrandChild(WidgetGranChild):
        pass

    def f(x):
        return 'xxx'

    assert get_repr_function(Widget(), []) is repr
    assert get_repr_function(WidgetChild(), []) is repr
    assert get_repr_function(WidgetGranChild(), []) is repr
    assert get_repr_function(WidgetGreatGrandChild(), []) is repr

    assert get_repr_function(Widget(), [(Widget, f)]) is repr
    assert get_repr_function(WidgetChild(), [(Widget, f)]) is f

# Generated at 2022-06-12 19:59:37.188367
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(object):
        pass
    class B(object):
        def write(self):
            pass
    class D(A):
        pass
    class C(B):
        def write(self):
            pass
    assert issubclass(sys.stdin, WritableStream)
    assert issubclass(A, WritableStream)
    assert issubclass(B, WritableStream)
    assert issubclass(C, WritableStream)
    assert issubclass(D, WritableStream)

# Generated at 2022-06-12 19:59:39.961826
# Unit test for function shitcode
def test_shitcode():
    assert shitcode('a') == 'a'
    assert shitcode(u'\u1234') == '?'
    assert shitcode('\xfe') == '?'
    assert shitcode(u'\U00012345') == '?'



# Generated at 2022-06-12 19:59:43.941385
# Unit test for function get_repr_function
def test_get_repr_function():
    class A(object):
        pass

    class B(object):
        def __repr__(self):
            return 'custom repr'

    a = A()
    b = B()

    assert 'custom repr' == get_repr_function(b, [])()

    assert 'custom repr' == get_repr_function(b, [(B, lambda i: 'custom repr')])()



# Generated at 2022-06-12 19:59:47.351125
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class X(WritableStream):
        def write(self, s):
            pass
    assert X.__subclasshook__(X) is True

# Generated at 2022-06-12 19:59:57.843556
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    from .test_python_toolbox import TestCase

    def repr_for_ints(item):
        if isinstance(item, int):
            return '{}i'.format(item)

    class TestGetShortishRepr(TestCase):
        def test_short_repr(self):
            r = get_shortish_repr('foo', max_length=20)
            self.assertEqual(r, "'foo'")

            r = get_shortish_repr(123, custom_repr=[(int, repr_for_ints)],
                                  max_length=20)
            self.assertEqual(r, '123i')

        def test_long_repr(self):
            r = get_shortish_repr('foo bar baz', max_length=10)

# Generated at 2022-06-12 20:00:02.882852
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def __init__(self):
            self._written = ''
        def write(self, s):
            self._written += s
    my_writable_stream = MyWritableStream()
    my_writable_stream.write('abc')
    assert my_writable_stream._written == 'abc'



# Generated at 2022-06-12 20:00:09.352587
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class WritableStreamMock(WritableStream):
        def __init__(self):
            self.written = []
            self.writes = 0
        def write(self, s):
            self.written.append(s)
            self.writes += 1

    mock = WritableStreamMock()
    mock.write('1')
    assert mock.written == ['1'], mock.written
    mock.write('2')
    assert mock.written == ['1', '2'], mock.written
    assert mock.writes == 2
    assert issubclass(WritableStreamMock, WritableStream)



# Generated at 2022-06-12 20:00:15.258603
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def __init__(self, target_list):
            self.target_list = target_list
            self.contents = []
        def write(self, s):
            self.target_list.append(s)
    target = []
    stream = MyWritableStream(target)
    stream.write('hi')
    assert target == ['hi']


if __name__ == '__main__':
    test_WritableStream_write()

# Generated at 2022-06-12 20:00:23.215765
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(3) == '3'
    assert not get_shortish_repr('hello') == 'hello'
    assert get_shortish_repr('hello', max_length=5) == 'hello'
    assert get_shortish_repr('hello', max_length=4) == 'hel...'
    assert get_shortish_repr('a' * 100, max_length=10) == 'aaaaaaa...aa'
    assert get_shortish_repr(u'\U0001F4A9' * 100, 100) == u'\U0001F4A9' * 33 + u'...'
    assert get_shortish_repr(u'\U0001F4A9' * 100, 33) == u'\U0001F4A9' * 10 + u'...'



# Generated at 2022-06-12 20:00:26.697813
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('abcde', max_length=6) == 'abcde'
    assert get_shortish_repr('abcde', max_length=5) == 'abcde'
    assert get_shortish_repr('abcde', max_length=4) == 'a...e'
    assert get_shortish_repr('abcde', max_length=3) == 'a...'
    assert get_shortish_repr('abcde', max_length=2) == 'a.'
    assert get_shortish_repr('abcde', max_length=1) == '.'
    assert get_shortish_repr('abcde', max_length=0) == ''

# Generated at 2022-06-12 20:00:34.023222
# Unit test for function get_repr_function
def test_get_repr_function():
    class MyNumber(object):
        def __init__(self, value):
            self.value = value

    class MyOtherNumber(MyNumber):
        pass

    class AnotherNumber(object):
        def __init__(self, value):
            self.value = value

    for item in [MyNumber(5), MyOtherNumber(10), AnotherNumber(1)]:
        assert get_repr_function(
            item, [(MyNumber, lambda i: 'hello ' + str(i.value))]
        )(item) == 'hello ' + str(item.value)

    for item in [MyOtherNumber(5), AnotherNumber(10)]:
        assert get_repr_function(
            item, [(MyNumber, lambda i: 'hello ' + str(i.value))]
        )(item) == repr(item)

   

# Generated at 2022-06-12 20:00:40.276749
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(1) == '1'
    assert get_shortish_repr(1.1) == '1.1'
    assert get_shortish_repr("something longer") == "something longer"
    assert get_shortish_repr("something longer", max_length=10) == "something..."
    assert get_shortish_repr("something longer", max_length=20) == "something longer"
    assert get_shortish_repr("something longer", max_length=20, normalize=True) == "something longer"
    assert get_shortish_repr("<module 'some.module' from 'module path.pyc'>", max_length=300) == "<module 'some.module' from 'module path.pyc'>"

# Generated at 2022-06-12 20:00:46.439522
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Class:
        pass
    assert issubclass(Class, WritableStream) is NotImplemented
    class Class:
        def write(self, s):
            return None
    assert issubclass(Class, WritableStream) is True
    class Class:
        def write(self, s):
            return None
        def do_something_else(self):
            return None
    assert issubclass(Class, WritableStream) is True



# Generated at 2022-06-12 20:00:47.431292
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class FooWritableStream(WritableStream):
        ...

# Generated at 2022-06-12 20:00:54.542843
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def __init__(self):
            self.written_strings = []
        def write(self, s):
            self.written_strings.append(s)
    x = MyWritableStream()
    x.write('hey')
    assert x.written_strings == ['hey']
    with pytest.raises(TypeError):
        class NonWritableStream(object):
            pass
        issubclass(NonWritableStream, WritableStream)



# Generated at 2022-06-12 20:00:57.759804
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(WritableStream):
        def write(self, s):
            pass
    assert isinstance(A(), WritableStream)
    assert isinstance(A(), ABC)

# Generated at 2022-06-12 20:01:02.305661
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    """Test that un-implemented stream write raises a NotImplementedError."""
    with pytest.raises(NotImplementedError) as excinfo:
        WritableStream().write("test_string")
    assert excinfo.value.args == ("Can't write to stream because it doesn't "
                                  "implement `write`.",)



# Generated at 2022-06-12 20:01:04.577751
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    s = io.StringIO()
    s.write('foo')
    assert isinstance(s, WritableStream)
    assert s.getvalue() == 'foo'

# Generated at 2022-06-12 20:01:07.303536
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class Foo(WritableStream):
        def __init__(self):
            self.written_items = []

        def write(self, s):
            self.written_items.append(s)

    foo = Foo()
    foo.write('foo')
    assert foo.written_items == ['foo']

# Generated at 2022-06-12 20:01:16.055734
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('banana') == "'banana'"
    assert get_shortish_repr('banana', max_length=2) == "'ba'"
    assert get_shortish_repr(
        'banana', max_length=2, normalize=True) == "'ba'"
    assert get_shortish_repr('banana', max_length=2) == "'ba'"
    assert get_shortish_repr(1, custom_repr=((int, lambda i: 'int'))) == 'int'

# Generated at 2022-06-12 20:01:30.026142
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Class0(WritableStream):
        def write(self, s):
            pass

    assert Class0.__subclasshook__(Class0) is True

    class Class1:
        pass
    assert Class1.__subclasshook__(Class1) is NotImplemented

    class Class2(WritableStream):
        pass
    assert Class2.__subclasshook__(Class2) is NotImplemented

    class Class3(WritableStream):
        def write(self, s):
            pass
        def fuck(self):
            pass
    assert Class3.__subclasshook__(Class3) is True
    class Class4(Class3):
        pass
    assert Class4.__subclasshook__(Class4) is True
    class Class5(Class3):
        def write(self, s):
            pass

# Generated at 2022-06-12 20:01:33.394168
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def write(self, s):
            return s.upper()
    assert issubclass(MyWritableStream, WritableStream)



# Generated at 2022-06-12 20:01:37.713673
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Foobar:
        def write(self):
            pass

    assert WritableStream.__subclasshook__(Foobar) is True

    class Foobar:
        pass

    assert WritableStream.__subclasshook__(Foobar) is NotImplemented

# Generated at 2022-06-12 20:01:41.503468
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class StreamWritable(object):
        def write(self, s): pass
    assert issubclass(StreamWritable, WritableStream)
    class StreamNotWritable(object): pass
    assert not issubclass(StreamNotWritable, WritableStream)


# Generated at 2022-06-12 20:01:43.575108
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class TestClass(WritableStream):
        def write(self, s):
            pass
    assert issubclass(TestClass, WritableStream)

# Generated at 2022-06-12 20:01:47.937029
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import sys
    from .pycompat import StringIO

    class Foo(WritableStream):
        def write(self, s): pass

    assert sys.stdout in issubclass(sys.stdout, WritableStream)
    assert sys.stdout in isinstance(sys.stdout, WritableStream)

    assert StringIO() in issubclass(StringIO, WritableStream)
    assert StringIO() in isinstance(StringIO(), WritableStream)

    assert Foo() in issubclass(Foo, WritableStream)
    assert Foo() in isinstance(Foo(), WritableStream)

# Generated at 2022-06-12 20:01:55.291873
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    from .stringio import StringIO
    from .stdout_redirector import StdoutRedirector
    from .stderr_redirector import StderrRedirector

    assert issubclass(StringIO, WritableStream)
    assert issubclass(StdoutRedirector, WritableStream)
    assert issubclass(StderrRedirector, WritableStream)
    assert not issubclass(int, WritableStream)
    assert not issubclass(list, WritableStream)

# Generated at 2022-06-12 20:02:01.537537
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, ()) is repr
    assert get_repr_function(1, ((int, str), (lambda x: True, id))) is id
    assert get_repr_function(1.1, ((int, str), (lambda x: True, id))) is repr
    assert get_repr_function(1, ((int,), (lambda x: True, id))) is id
    assert get_repr_function(1.1, ((int,), (lambda x: True, id))) is repr



# Generated at 2022-06-12 20:02:07.038888
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyStringIO(WritableStream):
        def __init__(self):
            self.lines = []

        def write(self, line):
            self.lines.append(line)

    my_string_io = MyStringIO()
    my_string_io.write('foo')
    assert my_string_io.lines == ['foo']

# Generated at 2022-06-12 20:02:15.749078
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('hello') == "'hello'"
    assert get_shortish_repr('hello', custom_repr=((lambda x: True, 'X'))) == \
                                                                            'X'
    assert get_shortish_repr('hello', custom_repr=((lambda x: False, 'X'))) \
                                                                          == \
                                                                          "'hello'"
    assert get_shortish_repr('hello', max_length=3) == "'he...'"
    assert get_shortish_repr(u'hello', max_length=3) == "u'he...'"
    assert get_shortish_repr('hello', max_length=2) == "'h...'"

# Generated at 2022-06-12 20:02:24.278795
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, [(int, lambda x: 'int')]) == 'int'
    assert get_repr_function('a', [(int, lambda x: 'int')]) == repr

# Generated at 2022-06-12 20:02:32.292430
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert truncate('1234567890', 5) == '1...0'

    assert get_shortish_repr(1) == '1'
    assert get_shortish_repr(1, custom_repr=[(int, lambda x: 'int')]) == 'int'
    assert get_shortish_repr(1, max_length=1) == '1'
    assert get_shortish_repr(1, max_length=2) == '1'
    assert get_shortish_repr(1, max_length=3) == '1'
    assert get_shortish_repr(1, max_length=4) == '1'
    assert get_shortish_repr(1, max_length=5) == '1'

# Generated at 2022-06-12 20:02:34.494232
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, custom_repr=((float, lambda x: str(x)),)) == str



# Generated at 2022-06-12 20:02:41.315856
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def __init__(self):
            self.my_call_count = 0
        def write(self, s):
            self.my_call_count += 1

    good_class = MyWritableStream
    assert issubclass(good_class, WritableStream)
    good_instance = good_class()
    assert isinstance(good_instance, WritableStream)
    assert good_instance.write('bla bla') is None
    assert good_instance.my_call_count == 1

    class NonWritableStream(WritableStream):
        pass

    bad_class = NonWritableStream
    assert not issubclass(bad_class, WritableStream)

    class NonWritableStream:
        pass
    assert not issubclass(NonWritableStream, WritableStream)

# Generated at 2022-06-12 20:02:44.166047
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class X:
        def write(self, s):
            print(s)
    assert isinstance(X(), WritableStream)
    x = X()
    x.write('hello')



# Generated at 2022-06-12 20:02:51.185048
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(4) == '4'
    assert get_shortish_repr(4, max_length=2) == '4'
    assert get_shortish_repr(4, max_length=1) == '4'
    assert get_shortish_repr(4, max_length=0) == ''
    assert get_shortish_repr(4, max_length=3) == '4'
    assert get_shortish_repr(4, max_length=4) == '4'
    assert get_shortish_repr('foobar', max_length=0) == ''
    assert get_shortish_repr('foobar', max_length=4) == 'foob'

# Generated at 2022-06-12 20:02:54.272988
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function('1', custom_repr=((str, lambda s: 'zz'),)) == 'zz'
    assert get_repr_function(int, custom_repr=((str, lambda s: 'zz'),)) == \
                                                                       repr



# Generated at 2022-06-12 20:02:57.794609
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    """Unit test for method write of class WritableStream"""
    class FakeWritableStream(WritableStream):
        def __init__(self, *args, **kwargs):
            pass
    my_fake_writable_stream = FakeWritableStream()
    my_fake_writable_stream.write('hi')

# Generated at 2022-06-12 20:03:04.154564
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(1) == '1'
    assert get_shortish_repr('a', max_length=4) == 'a'
    assert get_shortish_repr(1, max_length=4) == '1'
    assert get_shortish_repr('abcde', max_length=4) == 'ab...e'
    assert get_shortish_repr('abcdefgh', max_length=4) == 'ab...gh'




# Generated at 2022-06-12 20:03:10.205105
# Unit test for function get_repr_function
def test_get_repr_function():
    custom_repr = ((int, 'int!'),
                   (lambda x: isinstance(x, tuple), 'tuple!'),
                   (lambda x: isinstance(x, list), 'list!'))
    assert get_repr_function(1, custom_repr) is str
    assert get_repr_function(int, custom_repr) is str
    assert get_repr_function(1.0, custom_repr) is repr
    assert get_repr_function(1, custom_repr) == 'int!'
    assert get_repr_function((1, 2), custom_repr) == 'tuple!'
    assert get_repr_function([1, 2], custom_repr) == 'list!'

# Generated at 2022-06-12 20:03:30.579884
# Unit test for function get_repr_function
def test_get_repr_function():
    import types

    assert get_repr_function(5, []) == repr
    assert get_repr_function(5, [(lambda x: True, lambda x: '5')]) == '5'
    assert get_repr_function(5, [(lambda x: False, lambda x: '5')]) == repr
    assert get_repr_function('a', [(str, lambda x: '"a"')]) == '"a"'
    assert get_repr_function(u'a', [(str, lambda x: '"a"')]) == repr
    assert get_repr_function(5, [(types.StringTypes, lambda x: '"5"')]) == '5'
    assert get_repr_function(5, [(types.IntType, lambda x: '5')]) == '5'
    assert get_repr

# Generated at 2022-06-12 20:03:34.905376
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    from .general_utils import get_shortish_repr
    assert get_shortish_repr(()).replace(" ", "") == "()"
    assert get_shortish_repr({}).replace(" ", "") == "{}"
    assert get_shortish_repr("").replace(" ", "") == '""'
    assert get_shortish_repr("a" * 100).replace(" ", "") == '"{}"'.format("a" * 100)
    assert get_shortish_repr("a" * 101).replace(" ", "") == '"{}"'.format(("a" * 49) + "..." + ("a" * 49))
    assert get_shortish_repr("a" * 100, max_length=100).replace(" ", "") == '"{}"'.format("a" * 100)
   

# Generated at 2022-06-12 20:03:45.658152
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(5, []) is repr
    assert get_repr_function(5, [(lambda x: True, str)]) is str
    assert get_repr_function(5, [(lambda x: True, str), (lambda x: False, str)]) \
                                                                           is str
    assert get_repr_function(5, [(lambda x: False, str), (lambda x: True, str)]) \
                                                                           is str
    assert get_repr_function(5, [(lambda x: False, str)]) is repr
    assert get_repr_function(5, [(lambda x: None, str)]) is repr
    assert get_repr_function(5, [(None, str)]) is repr

# Generated at 2022-06-12 20:03:47.683845
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class DummyStream(WritableStream):
        def write(self, s):
            pass

    return DummyStream().write('')

# Generated at 2022-06-12 20:03:52.000747
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def write(self, s):
            pass
    class MyNotWritableStream:
        pass
    assert isinstance(MyWritableStream(), WritableStream)
    assert not isinstance(MyNotWritableStream(), WritableStream)

# Generated at 2022-06-12 20:04:00.095635
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('abc', max_length=1) == 'a'
    assert get_shortish_repr('abc', max_length=2) == 'ab'
    assert get_shortish_repr('abc', max_length=3) == 'abc'
    assert get_shortish_repr('abc', max_length=4) == 'abc'
    assert get_shortish_repr('abc', max_length=5) == 'abc'
    assert get_shortish_repr('abc', max_length=6) == 'abc'
    assert get_shortish_repr('abc', max_length=7) == 'abc'
    assert get_shortish_repr('abc', max_length=8) == 'abc'


# Generated at 2022-06-12 20:04:03.665875
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Test: pass

    assert WritableStream.__subclasshook__(Test) is NotImplemented

    class Test(WritableStream):
        def write(self, s):
            pass

    assert WritableStream.__subclasshook__(Test) is True



# Generated at 2022-06-12 20:04:06.778822
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class MyFile(WritableStream):
        def write(self, s):
            pass

    my_file = MyFile()

    assert isinstance(my_file, WritableStream)
    assert WritableStream.__subclasshook__(MyFile)




# Generated at 2022-06-12 20:04:17.698334
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert (normalize_repr('abcde at 0xabcd') == 'abcde')
    assert (normalize_repr('abcde') == 'abcde')
    assert (normalize_repr('abcde at 0xabcd at 0x0123') == 'abcde')
    assert ('abcde' == get_shortish_repr('abcde', max_length=5))
    assert ('ab...e' == get_shortish_repr('abcde', max_length=6))
    assert ('abcde' == get_shortish_repr('abcde', max_length=7))
    assert ('abcdefghij' == get_shortish_repr('abcdefghij', max_length=7))

# Generated at 2022-06-12 20:04:24.590338
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(()) == get_repr_function([]) == get_repr_function({}) == get_repr_function('') != \
                                                                                                            get_repr_function(3)

# Generated at 2022-06-12 20:04:54.801672
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    import pytest
    shortish_repr_function = get_shortish_repr

    assert shortish_repr_function(5) == '5'
    assert shortish_repr_function(5, max_length=2) == '5'
    assert shortish_repr_function(5, max_length=1) == '5'

    assert shortish_repr_function(5, max_length=0) == '5'
    assert shortish_repr_function(5, max_length=-1) == '5'

    with pytest.raises(AssertionError):
        assert shortish_repr_function(5, max_length='a')

    with pytest.raises(AssertionError):
        assert shortish_repr_function(5, max_length=object())


   

# Generated at 2022-06-12 20:05:05.889028
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    def write_function(s):
        print(s)

    # test_WritableStream_write
    assert isinstance(write_function, WritableStream)
    # test_WritableStream_write

    class A(WritableStream):
        def write(self, s):
            return write_function(s)

    # test_WritableStream_write
    assert isinstance(A(), WritableStream)
    # test_WritableStream_write

    class B(WritableStream):
        def write(self, s):
            return write_function(s)

    # test_WritableStream_write
    assert isinstance(B(), WritableStream)
    # test_WritableStream_write

    class C(B):
        pass

    # test_WritableStream_write
    assert isinstance(C(), WritableStream)


# Generated at 2022-06-12 20:05:10.017533
# Unit test for function get_repr_function
def test_get_repr_function():
    class Item(object):
        pass
    custom_repr = [(lambda x: x.number > 3, lambda x: 'blah')]
    repr_function = get_repr_function(Item(), custom_repr)
    assert repr_function(Item()) == repr(Item())

# Generated at 2022-06-12 20:05:13.271854
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class T(WritableStream):
        def write(self, s):
            self.s = s

    t = T()
    t.write('spam')
    assert t.s == 'spam'



# Generated at 2022-06-12 20:05:18.681868
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    import io
    import typing

    class MyWritableStream(WritableStream):
        pass

    MyWritableStream.register(typing.IOBase)

    f = io.StringIO()
    assert isinstance(f, WritableStream)

    class MyWritableString(str):
        def write(self, s):
            super(MyWritableString, self).__init__(s)


    f = MyWritableString()
    assert isinstance(f, WritableStream)

# Generated at 2022-06-12 20:05:30.581930
# Unit test for function get_repr_function
def test_get_repr_function():
    class A: pass
    class B(A): pass
    class C(B): pass
    class D: pass

# Generated at 2022-06-12 20:05:34.662915
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Foo:
        def write(self, s):
            pass

    assert isinstance(Foo(), WritableStream)



# Generated at 2022-06-12 20:05:43.751526
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function([], []) == repr
    assert get_repr_function([], [(list, lambda x: 'a list')]) == \
                                                           (lambda x: 'a list')
    assert get_repr_function(6, [(list, lambda x: 'a list')]) == repr
    assert get_repr_function(6, [(int, lambda x: 'an int')]) == \
                                                           (lambda x: 'an int')
    assert get_repr_function(6, [(float, lambda x: 'a float')]) == repr
    assert get_repr_function(6, [(lambda x: x > 5, lambda x: 'a big int')]) == \
                                               (lambda x: 'a big int')

# Generated at 2022-06-12 20:05:52.548167
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io

    class GoodClass:
        def write(self, s): pass

    class BadClass1: pass

    class BadClass2:
        def write(self): pass

    class GoodSubclass(GoodClass): pass

    assert issubclass(GoodClass, WritableStream)
    assert issubclass(GoodSubclass, WritableStream)
    assert not issubclass(BadClass1, WritableStream)
    assert not issubclass(BadClass2, WritableStream)
    assert issubclass(io.TextIOBase, WritableStream)
    assert issubclass(io.StringIO, WritableStream)
    assert issubclass(io.BytesIO, WritableStream)



# Generated at 2022-06-12 20:05:55.920544
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(WritableStream):
        def write(self, x):
            self.x = x
    a = A()
    a.write(3)
    assert a.x == 3
    a.write('aaa')
    assert a.x == 'aaa'
test_WritableStream_write()

# Generated at 2022-06-12 20:06:43.578600
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    from .stringstream import StringStream
    from .encodingstream import EncodingStream

    class No(object):
        pass

    no = No()
    no.write = None
    assert not isinstance(no, WritableStream)

    a = StringStream()
    assert isinstance(a, WritableStream)

    b = EncodingStream(StringStream(), encoding='ascii')
    assert isinstance(b, WritableStream)

# Generated at 2022-06-12 20:06:47.106795
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Foo(WritableStream):
        def write(self, s):
            pass

    class Bar: pass

    assert issubclass(Foo, WritableStream)
    assert not issubclass(Bar, WritableStream)



# Generated at 2022-06-12 20:06:54.919930
# Unit test for function get_repr_function
def test_get_repr_function():
    assert normalize_repr('Hello at 0xabcd') == 'Hello'
    assert normalize_repr('Hello at 0xabcd at 0x1234') == 'Hello'
    assert normalize_repr('Hello at 0xabcd at 0x1234 at 0x5678') == 'Hello'
    assert normalize_repr('Hello at 0xabcd at 0x1234 at 0x5678 at 0x9876') == 'Hello'
    assert normalize_repr('Hello at 0xabcdef') == 'Hello'
    assert normalize_repr('Hello at 0xabcd at 0x1234 at 0x5678 at 0x9876 at 0xba9s') == 'Hello'

# Generated at 2022-06-12 20:06:59.835994
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MockWritableStream(WritableStream):
        def __init__(self, *args, **kwargs):
            pass
        def write(self, s):
            return self
        def close(self):
            return self
    mock_writable_stream = MockWritableStream()
    assert isinstance(mock_writable_stream, WritableStream)
    mock_writable_stream.write('hey')



# Generated at 2022-06-12 20:07:10.405012
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(1) == '1'
    assert get_shortish_repr(1, max_length=1) == '1'
    assert get_shortish_repr(1, max_length=2) == '1'
    assert get_shortish_repr(1, max_length=3) == '1'
    assert get_shortish_repr(1, max_length=4) == '1'
    assert get_shortish_repr(1, max_length=5) == '1'
    assert get_shortish_repr(1, max_length=6) == '1'

    assert get_shortish_repr(123456789, max_length=1) == '...'

# Generated at 2022-06-12 20:07:18.583120
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('') == "''"
    assert get_shortish_repr('', normalize=True) == "''"
    assert get_shortish_repr('\n') == "''"
    assert get_shortish_repr('\n', normalize=True) == "''"
    assert get_shortish_repr('\r') == "''"
    assert get_shortish_repr('\r', normalize=True) == "''"
    assert get_shortish_repr('\r\n') == "''"
    assert get_shortish_repr('\r\n', normalize=True) == "''"
    assert get_shortish_repr('a' * 100000) == repr('')

# Generated at 2022-06-12 20:07:28.781846
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    # regular repr
    assert get_shortish_repr(1) == '1'
    # repr that fails
    assert get_shortish_repr(1/0) == 'REPR FAILED'
    # regular repr with truncation
    assert get_shortish_repr(1234567890, max_length=7) == '1234567...'
    # regular repr with truncation, 2
    assert get_shortish_repr(1234567890, max_length=8) == '123456...'
    # regular repr with truncation, 3
    assert get_shortish_repr(1234567890, max_length=9) == '1234567...'
    # regular repr with truncation, 4
    assert get_shortish_repr(1234567890) == '1234567890'
   

# Generated at 2022-06-12 20:07:39.169633
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(object, max_length=9) == "object"
    assert get_shortish_repr(object, max_length=10) == "object"
    assert get_shortish_repr(object, max_length=11) == "object"
    assert get_shortish_repr(object, max_length=8) == "object"
    assert get_shortish_repr(object, max_length=7) == "objec..."
    assert get_shortish_repr(object, max_length=6) == "obj..."
    assert get_shortish_repr(object, max_length=5) == "ob..."
    assert get_shortish_repr(object, max_length=4) == "o..."

# Generated at 2022-06-12 20:07:40.170967
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    assert issubclass(type(sys.__stdout__), WritableStream)

# Generated at 2022-06-12 20:07:47.524808
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('hi', max_length=5) == 'hi'
    assert get_shortish_repr('hi', max_length=2) == 'hi'
    assert get_shortish_repr('hi', max_length=1) == 'h...'
    assert get_shortish_repr('hi', max_length=0) == '...'
    assert get_shortish_repr('hi', max_length=-1) == '...'
    assert get_shortish_repr('hi', max_length=None) == 'hi'
    assert get_shortish_repr('hi', max_length=True) == 'hi'
    assert get_shortish_repr('hi', max_length=False) == 'hi'