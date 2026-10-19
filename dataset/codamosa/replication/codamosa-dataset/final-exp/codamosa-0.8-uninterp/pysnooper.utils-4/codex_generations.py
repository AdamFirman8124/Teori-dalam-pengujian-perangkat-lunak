

# Generated at 2022-06-12 19:58:51.159469
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, []) == repr
    assert get_repr_function(1, [(lambda x: True, str)]) == str
    assert get_repr_function(2, [(lambda x: True, str)]) == str
    assert get_repr_function(2, [(lambda x: False, str)]) == repr
    assert get_repr_function(1, [(lambda x: True, str),
                                 (lambda x: True, lambda x: 'A')]) == str
    assert get_repr_function(2, [(lambda x: False, str),
                                 (lambda x: True, lambda x: 'A')]) == \
                                                                    str

# Generated at 2022-06-12 19:58:53.985893
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Something(WritableStream):
        def write(self, s):
            return s

    assert isinstance(Something(), WritableStream)

    class Something(object):
        def write(self, s):
            return s

    assert not isinstance(Something(), WritableStream)

# Generated at 2022-06-12 19:58:56.686437
# Unit test for function shitcode
def test_shitcode():
    assert shitcode('') == ''
    assert shitcode('abc') == 'abc'
    assert shitcode('ab\x7f') == 'ab?'



# Generated at 2022-06-12 19:59:02.732170
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, []) is repr
    assert get_repr_function(1, [(int, str)]) is str

    assert get_repr_function(1, [lambda x: x > 0]) is repr
    assert get_repr_function(1, [(lambda x: x > 0, str)]) is str

    assert get_repr_function(1, [lambda x: x < 0]) is repr
    assert get_repr_function(1, [(lambda x: x < 0, str)]) is repr

# Generated at 2022-06-12 19:59:09.316442
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    # We do this here because "isinstance" checks for
    # subclasses, not exact types. And we only want to check
    # exact types.
    assert WritableStream.__subclasshook__(sys.stdout) is True
    assert WritableStream.__subclasshook__(object) is NotImplemented
    assert WritableStream.__subclasshook__(WritableStream) is NotImplemented


if __name__ == '__main__':
    test_WritableStream_write()

# Generated at 2022-06-12 19:59:10.996140
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class FileObject(WritableStream):
        def write(self, s): pass
    assert isinstance(FileObject(), WritableStream)



# Generated at 2022-06-12 19:59:13.244243
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class TestWritable(WritableStream):
        def write(self, s):
            assert len(s)
    TestWritable().write('abc')



# Generated at 2022-06-12 19:59:22.584457
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    from .output_stream import OutputStream
    from .output_redirector import OutputRedirector
    from python_toolbox import cute_iter_tools
    output_stream = OutputStream()
    output_redirector = OutputRedirector(output_stream)
    output_redirector.start()
    print('Hello world!')
    lines = tuple(cute_iter_tools.peekable(output_stream))
    assert lines[0].strip() == 'Hello world!'
    assert len(lines) == 1

    output_redirector.stop()



# Generated at 2022-06-12 19:59:30.913787
# Unit test for function get_repr_function
def test_get_repr_function():
    def my_repr(x):
        if isinstance(x, int):
            return 'int ' + hex(x)
        return repr(x)
    assert get_repr_function(5, custom_repr=[(int, my_repr)]) is my_repr
    assert get_repr_function(5, custom_repr=[(lambda x: x==5, my_repr)]) is my_repr
    assert get_repr_function(5, custom_repr=[(lambda x: x!=5, my_repr)]) is repr
    assert get_repr_function('', custom_repr=[(int, my_repr)]) is repr
    assert get_repr_function('', custom_repr=[(lambda x: x==5, my_repr)]) is repr
   

# Generated at 2022-06-12 19:59:39.926061
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(0, max_length=1) == '0'
    assert get_shortish_repr(1, max_length=1) == '1'
    assert get_shortish_repr(2, max_length=1) == '2'
    assert get_shortish_repr(123, max_length=1) == '1'
    assert get_shortish_repr(123, max_length=4) == '123'
    assert get_shortish_repr(123, max_length=5) == '123'
    assert get_shortish_repr(123456789, max_length=5) == '12...89'
    assert get_shortish_repr(123456789, max_length=6) == '12...89'
    assert get_short

# Generated at 2022-06-12 19:59:50.986680
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('hello world') == 'hello world'
    assert get_shortish_repr('hello world', max_length=5) == 'he...'
    assert get_shortish_repr('hello world', max_length=10) == 'hello worl'
    assert get_shortish_repr('hello world', max_length=11) == 'hello worl'
    assert get_shortish_repr('h' * 100, max_length=10) == '...'



# Generated at 2022-06-12 20:00:00.398046
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    error_entries = (
        (KeyError, ValueError, TypeError, IndexError, AttributeError),
        (123, [1, 2, 3], {'a': 2}, {'b', 'c'}),
    )


# Generated at 2022-06-12 20:00:10.151266
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(123, ((lambda x: True, str),)) == str
    assert get_repr_function(123, ((lambda x: False, str),)) == repr

    assert get_repr_function(123, ((int, str),)) == str
    assert get_repr_function(123.0, ((int, str),)) == repr

    assert get_repr_function(123, ((1, str), (int, repr))) == repr
    assert get_repr_function(123, ((1, str), (int, repr), (lambda x: True,
                                                           str))) == str

    assert get_repr_function(123, ((1, str), (int, repr), (lambda x: False,
                                                           str))) == repr
    

# Generated at 2022-06-12 20:00:16.003832
# Unit test for function get_repr_function
def test_get_repr_function():
    class A: pass
    class B(A): pass
    assert get_repr_function(A(), []) == repr
    assert get_repr_function(B(), []) == repr

# Generated at 2022-06-12 20:00:22.577192
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A:
        def write(self, s):
            return (s+'A')[::-1]

    class B(A):
        pass

    class C:
        pass

    class PlainA:
        pass

    classes = (A, B, C, PlainA, sys.stdout)

    for C in classes:
        assert issubclass(C, WritableStream)

    for C in classes:
        instance = C()
        if issubclass(C, A):
            assert instance.write('s') == 'sA'
        else:
            assert exception_raised(TypeError, instance.write, 's')

# Generated at 2022-06-12 20:00:33.054559
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert (get_shortish_repr(None) == 'None')
    assert (get_shortish_repr(Ellipsis) == 'Ellipsis')
    assert (get_shortish_repr([]) == '[]')
    assert (get_shortish_repr([1, 2]) == '[1, 2]')
    assert (get_shortish_repr((1, 2)) == '(1, 2)')
    assert (get_shortish_repr([1, 2, 3, 4, 5], max_length=100)
            == '[1, 2, 3, 4, 5]')
    assert (get_shortish_repr([1, 2, 3, 4, 5], max_length=12)
            == '[1, 2, 3, 4, 5]')

# Generated at 2022-06-12 20:00:44.759587
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('abc') == "'abc'"
    assert get_shortish_repr('a' * 50) == "'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
                                         "aaaaaaa'"
    assert get_shortish_repr('a' * 50, max_length=20) == "'aaaaaaaa'..."
    assert get_shortish_repr('a' * 50, max_length=20, normalize=True) == "'aaaaa'"
    assert get_shortish_repr(Enum('X', 'Y Z')) == '<enum "Enum">.X'
    assert get_shortish_repr(Enum('X', 'Y Z'), max_length=12) == '<enum "...">'

# Generated at 2022-06-12 20:00:52.556929
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('abc') == 'abc'
    assert get_shortish_repr('abc' * 11) == 'abcabcabcabcabcabcabcabcabcabc...c'
    assert get_shortish_repr('abc' * 11, max_length=None) == 'abc' * 11
    assert get_shortish_repr(5) == '5'
    assert get_shortish_repr(5, normalize=True) == '5'
    assert get_shortish_repr(5, custom_repr=[(int, str), (float, repr)],
                             normalize=True) == '5'

# Generated at 2022-06-12 20:01:03.099274
# Unit test for function shitcode
def test_shitcode():
    for s in ("Foo", "M\u00fb", "M\u00ebn", "M\u00eb\u20acn", "M\u00ebno"):
        assert shitcode(s) == s

    assert shitcode("M\u00eb\u2301no") == "M\u00eb?no"
    assert shitcode('\x00\x01\x02\x03\x04') == '?????'
    assert shitcode('\x07') == '?'
    assert shitcode('\x08') == '?'
    assert shitcode('\x0e') == '?'
    assert shitcode('\x0f') == '?'
    assert shitcode('\x10') == '?'
    assert shitcode('\x11') == '?'

# Generated at 2022-06-12 20:01:07.419464
# Unit test for function shitcode
def test_shitcode():
    for string in ('hello', 'מהופך', 'אידיאלי'):
        assert string == shitcode(string)

    assert '????' == shitcode('א'*4)

    assert 'hello??????' == shitcode('hello' + 'א'*7)

    assert 'ם?ד?ו?ה?מ???' == shitcode('מהופך' + 'א'*6)



# Generated at 2022-06-12 20:01:21.342148
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    from .output_stream import OutputStream
    from .null_output_stream import NullOutputStream

    class Foo(WritableStream):
        pass

    class Bar(Foo):
        pass

    class WhoopsNope(Bar):

        def write(self, s):
            return

    class Okay(Bar):

        def write(self, s):
            return

    class AlsoOkay(Bar):
        pass

    class WhoopsTooMany(Bar):

        def write(self, s):
            return

        def __init__(self):
            self.write = None

    assert issubclass(OutputStream, WritableStream)
    assert issubclass(NullOutputStream, WritableStream)
    assert issubclass(Foo, WritableStream)
    assert issubclass(Bar, WritableStream)


# Generated at 2022-06-12 20:01:27.054777
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def __init__(self):
            self.data = b''

        def write(self, s):
            self.data += s
    writable_stream = MyWritableStream()
    writable_stream.write(b'hello')
    writable_stream.write(b' ')
    writable_stream.write(b'world')
    assert writable_stream.data == b'hello world'

# Generated at 2022-06-12 20:01:34.949089
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    from python_toolbox import cute_testing
    custom_repr = ((lambda x: x > 3, lambda x: 'blah'),)
    assert get_shortish_repr(1, custom_repr=custom_repr,
                             max_length=20, normalize=True) == \
           '1'
    assert get_shortish_repr(21, custom_repr=custom_repr,
                             max_length=20, normalize=True) == \
           '21'
    assert get_shortish_repr(4, custom_repr=custom_repr,
                             max_length=20, normalize=True) == \
           'blah'

# Generated at 2022-06-12 20:01:38.442930
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('a' * 100, max_length=100) == 'a' * 100
    assert get_shortish_repr('a' * 100, max_length=50) == 'a' * 47 + '...'

# Generated at 2022-06-12 20:01:42.282975
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    """
    Tests that the method `write` of class `WritableStream` is recognized.
    """
    class MyWritableStream(WritableStream):

        def write(self, s):
            pass

    assert issubclass(MyWritableStream, WritableStream)



# Generated at 2022-06-12 20:01:49.499006
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    class GoodRepr:
        def __repr__(self):
            return 'shit'
    assert get_shortish_repr(GoodRepr()) == 'shit'

    class BadRepr:
        def __repr__(self):
            1 / 0
    assert get_shortish_repr(BadRepr()) == 'REPR FAILED'

    class TooLongRepr:
        def __repr__(self):
            return ''.join(str(i) for i in range(1000))
    assert get_shortish_repr(TooLongRepr(), max_length=100) == '0...999'

    def my_repr(x):
        return 'foo'

# Generated at 2022-06-12 20:01:58.947590
# Unit test for function get_shortish_repr
def test_get_shortish_repr():

    assert get_shortish_repr('abcde') == 'abcde'
    assert get_shortish_repr(b'abcde') == 'abcde'
    assert get_shortish_repr('abcde', max_length=3) == 'abc'
    assert get_shortish_repr('abcde', max_length=4) == 'abcd'
    assert get_shortish_repr('abcde', max_length=5) == 'abcde'
    assert get_shortish_repr('abcde', max_length=4, normalize=True) == 'abc...'

    class Foo(object):
        def __repr__(self):
            return 'Foo'
        class Bar(object):
            def __repr__(self):
                return 'Foo.Bar'

    foo = Foo()

# Generated at 2022-06-12 20:02:08.759216
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('a', max_length=None) == 'a'
    assert get_shortish_repr('a', max_length=1) == 'a'
    assert get_shortish_repr('a', max_length=2) == 'a'
    assert get_shortish_repr('abcd', max_length=2) == 'ab...'
    assert get_shortish_repr('abcd', max_length=3) == 'abc...'
    assert get_shortish_repr('a', max_length=5) == 'a'
    assert get_shortish_repr('abc', max_length=2) == 'ab...'
    assert get_shortish_repr('abc', max_length=5) == 'abc'


# Generated at 2022-06-12 20:02:11.839818
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    from abc import ABCMeta

    class _Writable(metaclass=ABCMeta):
        def write(self, s):
            pass

    assert issubclass(_Writable, WritableStream)



# Generated at 2022-06-12 20:02:14.547772
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(10, [(lambda x: True, lambda x: x * 2)])(10) == 20
    assert get_repr_function(10, [])(10) == '10'



# Generated at 2022-06-12 20:02:27.913430
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(1) == '1'

    assert get_shortish_repr(1, max_length=10) == '1'

    assert get_shortish_repr(
        1, max_length=7, normalize=True
    ) == '1'

    assert get_shortish_repr([1, 2, 3], max_length=12) == '[1, 2, 3]'

    assert get_shortish_repr(
        [1, 2, 3], max_length=10
    ) == '[1, 2...]'

    assert get_shortish_repr(
        [1, 2, 3], max_length=10, normalize=True
    ) == '[1, 2...]'


# Generated at 2022-06-12 20:02:37.983133
# Unit test for function get_repr_function
def test_get_repr_function():
    class A(object):
        pass
    class B(object):
        pass
    class C(object):
        pass
    assert get_repr_function(A()) == repr
    assert get_repr_function(B()) == repr
    assert get_repr_function(C()) == repr
    assert get_repr_function(A(), ((type(A()), str),)) == str
    assert get_repr_function(B(), ((type(A()), str),)) == repr
    assert get_repr_function(C(), ((type(A()), str),)) == repr
    assert get_repr_function(A(), ((A, str),)) == str
    assert get_repr_function(B(), ((A, str),)) == repr

# Generated at 2022-06-12 20:02:46.441556
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    import random
    import string
    import textwrap
    import sys

    # This function generates one random string of random length
    random_string = lambda: u''.join(
        (
            random.choice(string.ascii_letters)
            for i in range(random.randint(0, 100))
        )
    )


# Generated at 2022-06-12 20:02:53.000453
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    """Unit test for function ``get_shortish_repr``."""
    assert get_shortish_repr('a') == "'a'"
    assert get_shortish_repr('a' * 50) == "'" + ('a' * 50) + "'"
    assert get_shortish_repr('a' * 51) == "'" + ('a' * 24) + "...'" + ('a' * 23) + "'"



# Generated at 2022-06-12 20:03:02.359605
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(str(123), ()) is repr
    assert get_repr_function(str(123), ((type(str(123)), lambda x: 999))) \
                                                                     == 999
    assert get_repr_function(str(123), ((lambda x: False, lambda x: 999))) \
                                                                      is repr
    assert get_repr_function(str(123), ((lambda x: True, lambda x: 999))) \
                                                                       == 999
    class X: pass
    x = X()
    assert get_repr_function(x, ((X, lambda x: 999))) == 999
    assert get_repr_function(x, ((X, lambda x: 999), (str, lambda x: 888))) \
                                                                        == 999

# Generated at 2022-06-12 20:03:08.644025
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    r = get_shortish_repr(1, custom_repr=((int, lambda i: '*%s*' % i),))
    assert r == '*1*'
    r = get_shortish_repr(1.0, custom_repr=((int, lambda i: '*%s*' % i),))
    assert r == '1.0'
    r = get_shortish_repr(1.0, max_length=3)
    assert r == '1.'
    r = get_shortish_repr('1' * 300, max_length=8)
    assert r == '1'*5 + '...' + '1'*3
    r = get_shortish_repr('1' * 10, max_length=8)
    assert r == '1'*10
   

# Generated at 2022-06-12 20:03:12.255802
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class X:
        def __init__(self):
            self.called = False

        def write(self, s):
            self.called = True

    assert issubclass(X, WritableStream)



# Generated at 2022-06-12 20:03:13.365194
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    from .pycompat import StringIO
    sio = StringIO()
    assert isinstance(sio, WritableStream)

# Generated at 2022-06-12 20:03:17.225332
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class WriteCalled(Exception): pass
    class Foo(WritableStream):
        def write(self, s):
            raise WriteCalled
    assert isinstance(Foo(), WritableStream)
    assert not isinstance(object(), WritableStream)

    foo = Foo()
    with pytest.raises(WriteCalled):
        foo.write('hey')

# Generated at 2022-06-12 20:03:19.098151
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, [(int, str)]) == str
    assert get_repr_function('s', [(int, str)]) == repr



# Generated at 2022-06-12 20:03:26.564643
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    from .std_streams import stdout
    assert isinstance(stdout, WritableStream)



# Generated at 2022-06-12 20:03:29.360755
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    temp_file = open('temp_file.txt', 'w')
    assert isinstance(temp_file, WritableStream)
    temp_file.write('123')
    temp_file.close()



# Generated at 2022-06-12 20:03:31.969931
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(1.0) == '1.0'
    assert get_shortish_repr(1.0, max_length=1) == '1.'



# Generated at 2022-06-12 20:03:36.645477
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    try:
        from pathlib import Path
    except ImportError: # pragma: no cover
        from pathlib2 import Path

    with open(Path(__file__).parent / 'test_WritableStream_write.txt', 'w') \
                                                                     as f:
        writable_stream = WritableStream()
        writable_stream.write = f.write

        writable_stream.write('hello world!')


    with open(Path(__file__).parent / 'test_WritableStream_write.txt', 'r') \
                                                                     as f:
        assert f.read() == 'hello world!'

# Generated at 2022-06-12 20:03:38.019597
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    assert _check_methods(sys.stdout, 'write')

# Generated at 2022-06-12 20:03:41.140933
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    class C:
        pass

    assert get_shortish_repr(C) == '<class __main__.C>'



# Generated at 2022-06-12 20:03:49.338018
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    import pytest
    a = object()
    shr = get_shortish_repr(a, max_length=1000)
    assert issubclass(type(shr), str)
    assert ' at 0x' in shr
    assert shr == repr(a)
    shr = get_shortish_repr(a, max_length=2)
    assert issubclass(type(shr), str)
    assert ' at 0x' in shr
    assert len(shr) == 2

    class BadReprObject(object):
        def __repr__(self):
            raise Exception('blaha')

    a = BadReprObject()

    shr = get_shortish_repr(a, max_length=1000)
    assert issubclass(type(shr), str)
    assert shr == 'REPR FAILED'
    shr

# Generated at 2022-06-12 20:03:58.202866
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Written:
        pass
    class CustomWritableStream(WritableStream):
        def __init__(self):
            self.written = []
        def write(self, s):
            self.written.append(s)

    custom_writable_stream = CustomWritableStream()
    assert issubclass(CustomWritableStream, WritableStream)

    custom_writable_stream.write('spam')
    assert custom_writable_stream.written[0] == 'spam'
    custom_writable_stream.write('eggs')
    assert custom_writable_stream.written[1] == 'eggs'
    custom_writable_stream.write('ham')
    assert custom_writable_stream.written[2] == 'ham'
    custom_writable_stream.write('bacon')
    assert custom

# Generated at 2022-06-12 20:04:06.778356
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Operator:
        def __init__(self, operator):
            self.operator = operator
        def __or__(self, other):
            return other.operator(self.operator)
        def __ror__(self, other):
            return self.operator(other)
        def __call__(self, other):
            return other

    class A(WritableStream):
        def write(self, s):
            pass

    assert issubclass(A, WritableStream)

    class B:
        def write(self, s):
            pass

    assert not issubclass(B, WritableStream)

    class C:
        def write(self, s):
            pass

        def __repr__(self):
            return 'hello'


# Generated at 2022-06-12 20:04:17.698131
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(123) == '123'
    assert get_shortish_repr(123, max_length=2) == '12'
    assert get_shortish_repr('abcdefghijklmnop') == 'abcdefghijklmnop'
    assert get_shortish_repr('abcdefghijklmnop', max_length=12) == \
                                                             'abcdefghijkl...'
    assert get_shortish_repr('abcdefghijklmnop', max_length=13) == \
                                                             'abcdefghijkl...'
    assert get_shortish_repr('abcdefghijklmnop', max_length=14) == \
                                                             'abcdefghijklmnop'



# Generated at 2022-06-12 20:04:39.623169
# Unit test for function get_repr_function
def test_get_repr_function():

    class A(object): pass
    class B(A): pass
    class C(A): pass

    a_instance = A()
    b_instance = B()
    c_instance = C()

    def repr_a(x): return "a repr"
    def repr_b(x): return "b repr"
    def repr_c(x): return "c repr"
    def repr_a_instance(x): return "a_instance repr"
    def repr_b_instance(x): return "b_instance repr"
    def repr_unrelated_number(x): return "unrelated number repr"

    assert get_repr_function(a_instance, []) is repr
    assert get_repr_function(b_instance, []) is repr
    assert get_repr_function(c_instance, []) is repr


# Generated at 2022-06-12 20:04:43.227144
# Unit test for function get_repr_function
def test_get_repr_function():
    class Foo(object): pass
    class Bar(object): pass
    assert get_repr_function(Foo(), [
        (Foo, repr)
    ]) is repr
    assert get_repr_function(Bar(), [
        (Foo, repr)
    ]) is repr

# Generated at 2022-06-12 20:04:45.089186
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Example:
        def write(self, s):
            return

    assert issubclass(Example, WritableStream)

# Generated at 2022-06-12 20:04:49.469322
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyClass(WritableStream):
        def __init__(self, string=''):
            self.string = string

        def write(self, s):
            self.string += s

    my_class = MyClass()
    my_class.write('hi')
    assert my_class.string == 'hi'



# Generated at 2022-06-12 20:04:53.560266
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyOwnWritableStream(WritableStream):
        def write(self, s):
            assert isinstance(s, string_types)

    class MyOwnUnWritableStream(WritableStream):
        pass

    assert issubclass(MyOwnWritableStream, WritableStream)
    assert not issubclass(MyOwnUnWritableStream, WritableStream)

# Generated at 2022-06-12 20:05:04.388586
# Unit test for function get_repr_function
def test_get_repr_function():

    assert get_repr_function(1, ()) == repr
    assert get_repr_function(1, ((int, str),)) == str
    assert get_repr_function(1, ((lambda x: (x == 3), str),)) == str
    assert get_repr_function(1, ((lambda x: (x == 3), str),
                                 (lambda x: (x == 1), str),
                                 (lambda x: (x == 2), str),)) == str

    assert get_repr_function(1, ((None,),)) == repr
    assert get_repr_function(None, ((None,),)) is None
    assert get_repr_function(None, ((None, 1),)) == 1



# Generated at 2022-06-12 20:05:09.031192
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class WritableStub(WritableStream):
        def write(self, s):
            pass

    assert not isinstance(WritableStub, WritableStream)
    WritableStub.register(WritableStream)
    assert isinstance(WritableStub, WritableStream)






# Generated at 2022-06-12 20:05:12.783613
# Unit test for function get_repr_function
def test_get_repr_function():
    class A(Exception):
        pass
    class B(Exception):
        pass
    class C(A, B):
        pass
    class D(Exception):
        pass

    for f in [eval(repr(A)), eval(repr(B)), eval(repr(C))]:
        repr_function = get_repr_function(f(''), [(A, A.__repr__)])
        assert repr_function is A.__repr__
    repr_function = get_repr_function(D(''), [(A, A.__repr__)])
    assert repr_function is repr



# Generated at 2022-06-12 20:05:15.361813
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Q(WritableStream):
        def write(self, s):
            print(s)
    q = Q()
    q.write('hi')




# Generated at 2022-06-12 20:05:21.562166
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    from collections import defaultdict
    class Stream(WritableStream):
        def __init__(self):
            self.sent_strings = defaultdict(str)
        def write(self, s, stream_name=None):
            self.sent_strings[stream_name] += s
    stream = Stream()
    stream.write('Hello, world!\n')
    stream.write('Hello, world!\n', 0)
    stream.write('Hello, world!\n', 1)
    assert stream.sent_strings[None] == stream.sent_strings[0] == \
                                                               'Hello, world!\n'
    assert stream.sent_strings[1] == 'Hello, world!\n'



# Generated at 2022-06-12 20:05:29.881123
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def write(self, s):
            self.s = s

    stream = MyWritableStream()
    stream.write('meow')
    assert stream.s == 'meow'



# Generated at 2022-06-12 20:05:36.942611
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    from .pycompat import StringIO
    from .file_system_tools import hash_text_file


    stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        WritableStream.register(type(sys.stdout))
        assert isinstance(sys.stdout, WritableStream)
    finally:
        sys.stdout = stdout



# Generated at 2022-06-12 20:05:42.645880
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class X(WritableStream):
        def write(self, s):
            pass
    assert issubclass(X, WritableStream)

    class Y:
        pass
    assert not issubclass(Y, WritableStream)

    class Z:
        def write(self, s):
            pass
    assert not issubclass(Z, WritableStream)

    class W:
        pass
    W.write = lambda self, s: None
    assert not issubclass(W, WritableStream)

# Generated at 2022-06-12 20:05:50.821307
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class C:
        def write(self, s):
            self.data = s

    assert isinstance(C(), WritableStream)

    class D: pass
    class E:
        def writing(self, s):
            self.data = s

    assert not isinstance(D(), WritableStream)
    assert not isinstance(E(), WritableStream)

    class F:
        def write(self, s):
            pass

        def __del__(self):
            raise IOError
    assert not isinstance(F(), WritableStream)

# Generated at 2022-06-12 20:05:59.508444
# Unit test for function get_repr_function
def test_get_repr_function():
    class X:
        def __repr__(self):
            return 'X'
    class Y:
        def __repr__(self):
            return 'Y'
    custom_repr = (
        (X, lambda x: 'custom repr for X'),
        (lambda x: isinstance(x, (int, float)),
         lambda x: 'custom repr'),
    )
    assert get_repr_function(__import__('pytest'), custom_repr) is repr
    assert get_repr_function(X(), custom_repr) is (lambda x: 'custom repr for X')
    assert get_repr_function('hello', custom_repr) is repr
    assert get_repr_function(Y(), custom_repr) is repr

# Generated at 2022-06-12 20:06:02.131670
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class FakeFile(object):
        def write(self, s):
            pass
    FakeFile().write('foo')
    FakeFile().write(u'foo')



# Generated at 2022-06-12 20:06:10.495959
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    from .my_io import StringIO
    class MyWritableStream(WritableStream):
        def __init__(self):
            self.written_text = ''
        def write(self, s):
            self.written_text += s

    x = MyWritableStream()
    assert isinstance(x, WritableStream)
    x.write('hello')
    assert x.written_text == 'hello'
    x.write(' world!')
    assert x.written_text == 'hello world!'
    try:
        class MyWritableStream(WritableStream):
            def __init__(self):
                self.written_text = ''

        assert False
    except TypeError:
        pass # As expected



# Generated at 2022-06-12 20:06:14.412289
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class FakeStream(WritableStream):
        def __init__(self):
            self.written_string = ''

        def write(self, s):
            self.written_string += s

    fake_stream = FakeStream()
    assert isinstance(fake_stream, WritableStream)
    fake_stream.write('ram')
    assert fake_stream.written_string == 'ram'

# Generated at 2022-06-12 20:06:18.284113
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def write(self, s):
            pass

    assert issubclass(MyWritableStream, WritableStream)
    assert isinstance(MyWritableStream(), WritableStream)



# Generated at 2022-06-12 20:06:20.206465
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class x(WritableStream):
        def write(self, s):
            pass
    WritableStream.register(x)
    assert isinstance(x(), WritableStream)

# Generated at 2022-06-12 20:06:28.629182
# Unit test for function get_repr_function
def test_get_repr_function():
    # Default repr:
    assert get_repr_function('hello', tuple()) == repr
    # Custom repr:
    assert get_repr_function('hello', ((
        lambda s: isinstance(s, str),
        lambda s: s.upper(),
    ),)) == str.upper



# Generated at 2022-06-12 20:06:31.193861
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(WritableStream):
        pass
    A.register(file)
    assert inspect.isclass(WritableStream)
    assert WritableStream.__subclasshook__(A) is True
    assert WritableStream.__subclasshook__(object) is NotImplemented

# Generated at 2022-06-12 20:06:40.470420
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyStream(WritableStream):
        def __init__(self):
            self.get_buffer = None
            self.write = self.write_simple

        def write_simple(self, s):
            self.get_buffer = s

        def write_bytes(self, b):
            self.get_buffer = b

    assert MyStream().get_buffer is None
    s = 'this is a test'
    MyStream().write(s)
    assert MyStream().get_buffer == s
    b = s.encode()
    MyStream().write_bytes(b)
    assert MyStream().get_buffer == b

# Generated at 2022-06-12 20:06:49.908818
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function('foo', []) is repr
    assert get_repr_function(b'foo', []) is repr
    assert get_repr_function(1, [(str, str)]) is str
    assert get_repr_function(1, [(str, None)]) is repr
    assert get_repr_function(str, [(str, str)]) is str
    assert get_repr_function(str, [(str, None)]) is repr
    assert get_repr_function(b'foo', [(str, str)]) is repr
    assert get_repr_function(b'foo', [(str, None)]) is repr
    assert get_repr_function(b'foo', [(lambda x: isinstance(x, str), str)]) is repr

# Generated at 2022-06-12 20:06:56.706284
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert(get_shortish_repr('abcdefghijklmnopqrstuvwxyz') == 'abcdefghijklmnopq...')
    assert(get_shortish_repr('abcdefghijklmnopqrstuvwxyz', max_length=None) ==
           'abcdefghijklmnopqrstuvwxyz')
    assert(get_shortish_repr('abcdefghijklmnopqrstuvwxyz', max_length=10) ==
           'abcdefghij...')
    assert(get_shortish_repr('abc', max_length=10) == 'abc')
    assert(get_shortish_repr(['a', 'b'], max_length=10) == "['a', 'b']")

# Generated at 2022-06-12 20:07:04.295162
# Unit test for function get_repr_function
def test_get_repr_function():
    from . import python_toolbox

    assert get_repr_function(5, ((int, str),)) == str

    class A(object): pass
    class B(object): pass

    assert get_repr_function(5, ((A, str),)) == repr
    assert get_repr_function(A(), ((A, str),)) == str

    class C(object):
        def __repr__(self):
            raise ValueError

    assert get_repr_function(C(), ((python_toolbox.misc.PseudoException,
                                    str),)) == str



# Generated at 2022-06-12 20:07:14.127864
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(5, ()) is repr
    assert get_repr_function('abc', ()) is repr
    assert get_repr_function(5, ((int, str), lambda x: 'XXX')) == 'XXX'
    assert get_repr_function([1,2], ((int, str), lambda x: 'XXX')) is repr
    assert get_repr_function([1,2], ((list, str), lambda x: 'XXX')) == 'XXX'
    assert get_repr_function([1,2], ((str, lambda x: 'XXX'),)) is repr
    assert get_repr_function('abc', ((str, lambda x: 'XXX'),)) == 'XXX'

# Generated at 2022-06-12 20:07:20.476950
# Unit test for function get_repr_function
def test_get_repr_function():
    from .contextlib_tools import ContextManagers

    class Thingie(object):
        def __init__(self, x):
            self.x = x

        def __repr__(self):
            if self.x is None:
                raise Exception('oops')
            return '<Thingie x={!r}>'.format(self.x)

    def thingie_repr(thingie):
        return 'Thingie! x={!r}'.format(thingie.x)

    thingy_repr = lambda thing: 'thingy!'

    custom_repr = (
        (lambda thingie: thingie.x is None, 'NONE'),
        (Thingie, thingie_repr),
        (object, thingy_repr)
    )


# Generated at 2022-06-12 20:07:26.411824
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(3, ((int, str), (float, lambda x: 'Three'))) \
        == repr
    assert get_repr_function('hi', ((int, str), (float, lambda x: 'Three'))) \
        == str

# Generated at 2022-06-12 20:07:30.951756
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    from .test_tools import assert_reprs_equal
    assert_reprs_equal(get_shortish_repr(1, max_length=1), '1')
    assert_reprs_equal(get_shortish_repr(1, max_length=2), '1')
    assert_reprs_equal(get_shortish_repr(1, max_length=3), '1')
    assert_reprs_equal(get_shortish_repr(1, max_length=4), '1')
    assert_reprs_equal(get_shortish_repr(1, max_length=5), '1')

    assert_reprs_equal(get_shortish_repr(1234567, max_length=5), '...567')
    assert_reprs

# Generated at 2022-06-12 20:07:38.399009
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class DummyStream(WritableStream):
        def write(self, s): return s

    stream = DummyStream()
    assert stream.write('Hello') == 'Hello'




# Generated at 2022-06-12 20:07:46.156323
# Unit test for function get_repr_function
def test_get_repr_function():
    def f(x):
        return x

    a = (1, 2)
    b = 'b'
    assert get_repr_function(1, (lambda x: True, f))(1) == f(1)
    assert get_repr_function(a, ((lambda x: isinstance(x, int), f),))(a) == \
                                                                          str(a)
    assert get_repr_function(a, ((type(a), f),))(a) == f(a)
    assert get_repr_function(a, ((lambda x: isinstance(x, int), f),
                                 (type(a), f)))(a) == f(a)

# Generated at 2022-06-12 20:07:54.312004
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, ((int, lambda x: str(2 * x)),)) == (
        lambda x: str(2 * x))
    assert get_repr_function(1, ((2, lambda x: str(2 * x)),)) == (
        lambda x: str(2 * x))
    assert get_repr_function(1, ((lambda x: x == 1, lambda x: str(2 * x)),)) == (
        lambda x: str(2 * x))
    assert get_repr_function(1, ((int, str),)) == str



# Generated at 2022-06-12 20:07:57.308754
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class WritableStream(object):
        def write(self, s):
            return s
    assert WritableStream.__subclasshook__(WritableStream)



# Generated at 2022-06-12 20:07:58.892488
# Unit test for function get_repr_function
def test_get_repr_function():
    get_repr_function(None, ((lambda x: x is None, lambda x: 'None')))



# Generated at 2022-06-12 20:08:07.518109
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1.0, custom_repr=(
        (lambda x: isinstance(x, (float, int)),
            lambda x: '{} float'.format(x)
        ),
        (lambda x: x == 'a',
            lambda x: '{} special'.format(x)
        ),
    )) == '1.0 float'

    assert get_repr_function('a', custom_repr=(
        (lambda x: isinstance(x, (float, int)),
            lambda x: '{} float'.format(x)
        ),
        (lambda x: x == 'a',
            lambda x: '{} special'.format(x)
        ),
    )) == 'a special'


# Generated at 2022-06-12 20:08:16.330102
# Unit test for function get_repr_function
def test_get_repr_function():
    class A(object):
        def __init__(self):
            self.a = 1 + 1
            self.b = 2 * 2
            self.c = 3 / 3
        def __repr__(self):
            return 'A(a=%s, b=%s, c=%s)' % (self.a, self.b, self.c)
    a = A()

    assert get_repr_function(a, ([str], lambda x: 'str')) == 'str'
    assert get_repr_function(a, ([str], lambda x: 'str'), [int], lambda x: 'int') == 'int'
    assert get_repr_function(a, ([str], lambda x: 'str'), [int], lambda x: 'int',
                             [int], lambda x: 'int') == 'int'

# Generated at 2022-06-12 20:08:23.797649
# Unit test for function get_repr_function
def test_get_repr_function():
    def repr_function_1(x):
        return 'repr_function_1({})'.format(x)
    def repr_function_2(x):
        return 'repr_function_2({})'.format(x)
    def repr_function_3(x):
        return 'repr_function_3({})'.format(x)
    assert get_repr_function(5, ((lambda x: x > 10, repr_function_1),
                                 (lambda x: x < 10, repr_function_2),
                                 (lambda x: x == 10, repr_function_3))) == \
                                                                     repr

# Generated at 2022-06-12 20:08:29.514696
# Unit test for function get_repr_function
def test_get_repr_function():
    assert 0 == get_repr_function(0, ())(0)
    assert 0 == get_repr_function(0, ((float, str),))(0)
    assert '0' == get_repr_function(0, ((int, str),))(0)

    class A: pass
    a = A()

    assert a == get_repr_function(a, ())(a)
    assert 0 == get_repr_function(a, ((A, int),))(a)
    assert '0' == get_repr_function(a, ((A, str),))(a)



# Generated at 2022-06-12 20:08:31.805280
# Unit test for function get_repr_function
def test_get_repr_function():
    assert (get_repr_function(5, ((int, lambda x: 'hey'))) ==
            get_repr_function(5, ((int, 'hey')))) == 'hey'

    assert get_repr_function(5, ((str, 'hey'))) is repr