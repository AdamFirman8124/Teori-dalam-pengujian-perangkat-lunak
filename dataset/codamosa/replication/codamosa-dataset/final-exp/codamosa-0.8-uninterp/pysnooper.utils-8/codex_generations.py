

# Generated at 2022-06-12 19:58:42.482939
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, ()) is repr
    assert get_repr_function(1, [(str, str)]) is str
    assert get_repr_function('1', [(str, str)]) is str
    assert get_repr_function('1', []) is repr
    assert get_repr_function('1', [(int, int)]) is repr
    assert get_repr_function(1, [(int, int)]) is int
    assert get_repr_function(1, [(int, int), (str, str)]) is int
    assert get_repr_function('1', [(int, int), (str, str)]) is str



# Generated at 2022-06-12 19:58:50.104321
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    def do_test():
        import io
        import sys

        def test_a(stream):
            assert isinstance(stream, WritableStream)
            stream.write('foo')

        def test_b(stream):
            assert not isinstance(stream, WritableStream)

        test_a(sys.stdout)
        test_a(io.BytesIO())
        test_b(None)
        test_b('spam')

    if sys.version_info.major == 3:
        import unittest
        unittest.main('myhdl_tools.utils.tests.test_WritableStream_write')

# Generated at 2022-06-12 19:58:56.614224
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('alpha') == "alpha"
    assert get_shortish_repr('alpha', max_length=3) == "..."
    assert get_shortish_repr('alpha', max_length=4) == "a..."
    assert get_shortish_repr('alpha', max_length=5) == "al..."
    assert get_shortish_repr('alpha', max_length=6) == "alph..."
    assert get_shortish_repr('alpha', max_length=7) == "alpha"
    assert get_shortish_repr('alpha', max_length=8) == "alpha"
    assert get_shortish_repr('alpha', max_length=9) == "alpha"


# Generated at 2022-06-12 19:59:00.621283
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Dummy(WritableStream):
        def __init__(self):
            self.value = ''
        def write(self, s):
            self.value += s

    dummy = Dummy()
    dummy.write('apple')
    assert dummy.value == 'apple'




# Generated at 2022-06-12 19:59:10.621723
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, custom_repr=((int, lambda x: str(x)*3),)) == \
                                                                   (lambda x: str(x)*3)
    assert get_repr_function(1, custom_repr=((lambda x: x > 0, lambda x: str(x)*3),)) == \
                                                                   (lambda x: str(x)*3)
    assert get_repr_function(1, custom_repr=((lambda x: x > 1, lambda x: str(x)*3),)) == repr

# Generated at 2022-06-12 19:59:13.914582
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A:
        def write(self):
            pass
    assert isinstance(A(), WritableStream)
    class B:
        pass
    assert not isinstance(B(), WritableStream)


if __name__ == '__main__':
    test_WritableStream_write()

# Generated at 2022-06-12 19:59:22.488346
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    r = get_shortish_repr(1)
    assert r == '1'
    r = get_shortish_repr('a nice and long string', max_length=10,
                                                     normalize=True)
    assert r == "'a nice a...ng'"
    r = get_shortish_repr('a nice and long string', max_length=10,
                                                     normalize=False)
    assert r == "'a nice a...g'"


### functions to test with doctest

# Generated at 2022-06-12 19:59:30.861481
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    import pytest

    class ReprFailer(object):
        def __repr__(self):
            raise Exception

    assert get_shortish_repr(ReprFailer()) == 'REPR FAILED'

    assert get_shortish_repr('1234567890') == '1234567890'
    assert get_shortish_repr('1234567890', max_length=10) == '1234567890'
    assert get_shortish_repr('1234567890', max_length=9) == '12345...90'
    assert get_shortish_repr('1234567890', max_length=8) == '12345...90'
    assert get_shortish_repr('1234567890', max_length=1) == '1...0'
    assert get_shortish_re

# Generated at 2022-06-12 19:59:35.954848
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('abcdefghijklmnopqrstuvwxyz', max_length=5) == 'abcde...xyz'
    assert get_shortish_repr(1, max_length=5, custom_repr=()) == '1'
    assert get_shortish_repr(1, max_length=None, custom_repr=()) == '1'

# Generated at 2022-06-12 19:59:40.345035
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class TestWritableStream(WritableStream):
        def __init__(self):
            self.result = ''

        def write(self, s):
            self.result += s
    t = TestWritableStream()
    assert t.write('hi') is None
    assert t.result == 'hi'
    t.write(' there')
    assert t.result == 'hi there'




# Generated at 2022-06-12 19:59:50.230215
# Unit test for function shitcode
def test_shitcode():
    assert shitcode(u'a') == u'a'
    assert shitcode(u'ã') == u'?'
    assert shitcode('猫') == '?'
    assert shitcode(u'a'.encode('utf-8')) == u'a'
    assert shitcode(u'ã'.encode('utf-8')) == u'?'
    assert shitcode('猫'.encode('utf-8')) == '?'



# Generated at 2022-06-12 20:00:00.314749
# Unit test for function shitcode

# Generated at 2022-06-12 20:00:03.984531
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    """
    This tests `write()` on the `WritableStream` ABC.
    """
    class WhateverStream(WritableStream):
        def write(self, s):
            pass
    assert issubclass(WhateverStream, WritableStream)

# Generated at 2022-06-12 20:00:11.882001
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(3, custom_repr=[(int, str)]) == str
    assert get_repr_function(3, custom_repr=[(str, int)]) == repr
    assert get_repr_function(3,
                             custom_repr=[(int, str), (str, int)]) == str
    assert get_repr_function(3,
                             custom_repr=[(int, str), (int, int)]) == str
    assert get_repr_function('a', custom_repr=[(int, str)]) == repr
    assert get_repr_function('a',
                             custom_repr=[(lambda x: x.startswith('a'), str)]) == str

# Generated at 2022-06-12 20:00:20.770678
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    class A(object):
        def __repr__(self):
            return 'this is a very long repr that should get shortened'

    class B(A):
        pass

    a = A()
    b = B()

    assert get_shortish_repr(a, max_length=50) == 'this is a very long repr that should get shortene...'
    assert get_shortish_repr(a, max_length=0) == '...'
    assert get_shortish_repr(a, (A, lambda x: x is a), max_length=50) == 'this is a very long repr that should get shortened'
    assert get_shortish_repr(a, (A, lambda x: x is b), max_length=50) == 'this is a very long repr that should get shortene...'

# Generated at 2022-06-12 20:00:31.121239
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(3, custom_repr=[(lambda x: x == 4, lambda x: '4')]) \
                                               == repr
    assert get_repr_function(3, custom_repr=[(3, lambda x: '3')]) == '3'
    assert get_repr_function(3, custom_repr=[(float, lambda x: '3')]) == '3'
    assert get_repr_function(3, custom_repr=[(int, lambda x: '3')]) == '3'
    assert get_repr_function(3, custom_repr=[(int, lambda x: '3'),
                                             (float, lambda x: '3.0')]) == '3'


# Generated at 2022-06-12 20:00:38.979713
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(3) == '3'
    assert get_shortish_repr(4.5) == '4.5'
    assert get_shortish_repr(True) == 'True'
    assert get_shortish_repr('hello') == "u'hello'"
    assert get_shortish_repr([3]) == '[3]'
    assert get_shortish_repr(xrange(3)) == 'xrange(3)'

# Generated at 2022-06-12 20:00:49.370821
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('hello') == "'hello'"
    assert get_shortish_repr('hello', max_length=2) == "'h'"
    assert get_shortish_repr('hello', max_length=5) == "'h...'"
    assert get_shortish_repr('hello', max_length=6) == "'hello'"
    assert get_shortish_repr('hello', max_length=100) == "'hello'"

    assert get_shortish_repr(4) == '4'
    assert get_shortish_repr(4, max_length=1) == '4'
    assert get_shortish_repr(4, max_length=0) == '4'

    assert get_shortish_repr(None) == 'None'
    assert get_shortish_repr

# Generated at 2022-06-12 20:01:00.452341
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    from .spammy_import import import_and_get_the_spam

    spam = import_and_get_the_spam()
    assert get_shortish_repr(spam) == 'The spam'
    assert get_shortish_repr(spam[0]) == "'The'"
    assert get_shortish_repr(spam[0], max_length=3) == '...'

    class TheSpam: pass
    the_spam = TheSpam()
    assert get_shortish_repr(the_spam, custom_repr=((TheSpam, id),)) == \
                                                                    hex(id(the_spam))

    assert get_shortish_repr((1, 2, 3)) == '(1, 2, 3)'

# Generated at 2022-06-12 20:01:07.510779
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(5, ()) is repr
    assert get_repr_function(5, [(None, repr)]) is repr
    assert get_repr_function(5, [(None, id)]) is id
    assert get_repr_function(5, [(type(5), id)]) is id
    assert get_repr_function(5, [(type(2), id)]) is repr
    assert get_repr_function(5, [
        (lambda x: x < 10, id),
        (lambda x: True, 'Hello')
    ]) is id
    assert get_repr_function(5, [
        (lambda x: x > 10, id),
        (lambda x: True, 'Hello')
    ]) == 'Hello'



# Generated at 2022-06-12 20:01:22.187564
# Unit test for function get_repr_function
def test_get_repr_function():
    assert normalize_repr('foo at 0x1234') == 'foo'
    assert normalize_repr('foo at 0x12345') == 'foo'
    assert normalize_repr('foo at 0x123456') == 'foo'
    assert normalize_repr('foo at 0x1234567') == 'foo'
    assert normalize_repr('foo at 0x12345678') == 'foo'
    assert normalize_repr('foo at 0x123456789') == 'foo'
    assert normalize_repr('foo at 0x123456789A') == 'foo'
    assert normalize_repr('foo at 0x123456789AB') == 'foo'
    assert normalize_repr('foo at 0x123456789ABC') == 'foo'
    assert normalize_re

# Generated at 2022-06-12 20:01:24.809045
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class TestWritableStream(WritableStream):
        def write(self, s):
            pass

    TestWritableStream().write('hello')



# Generated at 2022-06-12 20:01:27.709889
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(WritableStream):
        def write(self, s):
            pass

    assert issubclass(A, WritableStream)

    a = A()
    a.write('meow')

# Generated at 2022-06-12 20:01:32.291900
# Unit test for function shitcode
def test_shitcode():
    assert shitcode(u'רום') == u'\ufffd\ufffd'
    assert shitcode(u'רום\xa0+\ufffd') == u'\ufffd\ufffd +\ufffd'
    assert shitcode(u'abcdf') == u'abcdf'
    assert shitcode(u'abc\x81df') == u'abc?df'



# Generated at 2022-06-12 20:01:43.038350
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    class A: pass
    class B: pass
    class C: pass

    a = A()
    b = B()

    assert get_shortish_repr(a) == normalize_repr(repr(a))
    assert get_shortish_repr(b) == normalize_repr(repr(b))

    custom_repr = (
        (lambda x: x is a, lambda x: 'the A'),
        (A, lambda x: 'an A'),
        (lambda x: isinstance(x, collections_abc.Iterable),
         lambda x: 'something iterable'),
        (lambda x: isinstance(x, str),
         lambda x: 'a string'),
        (None, lambda x: 'something else')
    )

# Generated at 2022-06-12 20:01:50.086973
# Unit test for function shitcode
def test_shitcode():
    assert shitcode(r"C:\Users\Gabi\Documents\My Games\Space Grunts\data\maps\space_station.tga") == r"C:\Users\Gabi\Documents\My Games\Space Grunts\data\maps\space_station.tga"
    assert shitcode(r"C:\Users\Gabi\Documents\My Games\Space Grunts\data\maps\space_station_\tga") == r"C:\Users\Gabi\Documents\My Games\Space Grunts\data\maps\space_station_?tga"

# Generated at 2022-06-12 20:01:59.231716
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('hello') == "'hello'"
    assert get_shortish_repr(1) == '1'
    assert get_shortish_repr((1, 2, 3)) == '(1, 2, 3)'
    assert get_shortish_repr([1, 2, 3]) == '[1, 2, 3]'

# Generated at 2022-06-12 20:02:04.352768
# Unit test for method write of class WritableStream
def test_WritableStream_write():


    class WritableStreamTest(WritableStream):
        def __init__(self):
            self.written_lines = []

        def write(self, s):
            self.written_lines.append(s)

    stream = WritableStreamTest()
    stream.write('foo\n')
    stream.write('bar\n')
    assert stream.written_lines == ['foo\n', 'bar\n']

    class NotAStream:
        pass

    assert not isinstance(NotAStream(), WritableStream)

# Generated at 2022-06-12 20:02:07.991962
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    from .smart_io import get_smart_stream
    smart_stream = get_smart_stream()
    smart_stream.write('foo')
    assert smart_stream.result == 'foo'
    smart_stream.write('bar')
    assert smart_stream.result == 'foobar'





# Generated at 2022-06-12 20:02:13.123665
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(1) == '1'
    assert get_shortish_repr('abc', max_length=3) == 'abc'
    assert get_shortish_repr('abc', max_length=2) == 'ab...'
    assert get_shortish_repr('abc', max_length=1) == 'a...'


# Unit tests for function ensure_tuple

# Generated at 2022-06-12 20:02:21.009346
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class MockWritableStream(WritableStream):

        def write(self, s):
            pass

    assert issubclass(MockWritableStream, WritableStream)



# Generated at 2022-06-12 20:02:30.252411
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(42) == '42'
    assert get_shortish_repr(42, max_length=1) == '4'
    assert get_shortish_repr('hello') == 'hello'
    assert get_shortish_repr('hello', max_length=3) == 'hel'
    assert get_shortish_repr({1, 2, 3}, max_length=8) == '{1, 2, 3}'
    assert get_shortish_repr('hello\nworld\nfoo bar') == 'hello world foo bar'
    assert get_shortish_repr('hello', max_length=3) == 'hel'
    assert get_shortish_repr('hello'*100, max_length=50) == 'hellohellohellohellohellohellohel'
    assert get_

# Generated at 2022-06-12 20:02:36.563491
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class TracingWritableStream(WritableStream):
        def __init__(self):
            self.traces = []
            self.write_called = False
        def write(self, s):
            self.traces.append(s)
            self.write_called = True
    tws = TracingWritableStream()
    assert isinstance(tws, WritableStream)
    tws.write('abc')
    assert tws.traces == ['abc']
    assert tws.write_called

# Generated at 2022-06-12 20:02:43.534451
# Unit test for function get_repr_function
def test_get_repr_function():
    custom_repr = (
        (
            lambda x: isinstance(x, int) and x % 2 == 0,
            lambda x: 'even'
        ),
        (
            lambda x: isinstance(x, float),
            lambda x: 'float'
        )
    )


# Generated at 2022-06-12 20:02:47.613778
# Unit test for function get_repr_function
def test_get_repr_function():
    import datetime as _datetime
    D = _datetime.date
    T = _datetime.time
    DT = _datetime.datetime
    custom_repr = (
        (D, lambda x: 'date({})'.format(x.year)),
        (T, lambda x: 'time({})'.format(x.hour)),
        (DT, lambda x: 'datetime({})'.format(x.year)),
        (lambda x: x < 10, lambda x: 'smaller than ten ({})'.format(x)),
        (lambda x: (x.startswith('a') or x.startswith('b')),
         lambda x: 'starts with a or b: {}'.format(x))
    )
    d = D(2017, 4, 1)
    t = T(15, 18, 9)


# Generated at 2022-06-12 20:02:54.497228
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(5, ((int, lambda x: 'I am an int!'),)) == \
                                                               'I am an int!'
    assert get_repr_function(5.4, ((int, lambda x: 'I am an int!'),)) != \
                                                               'I am an int!'
    assert get_repr_function('me', ((int, lambda x: 'I am an int!'),)) \
                                                                  != 'I am an int!'



# Generated at 2022-06-12 20:03:03.733813
# Unit test for function get_repr_function
def test_get_repr_function():
    class X(object): pass
    x = X()
    assert get_repr_function(x, [
        (lambda z: z == x, lambda z: 'XYZ'),
        (X, lambda z: 'ABC'),
    ]) == 'XYZ'
    y = X()
    assert get_repr_function(y, [
        (lambda z: z == x, lambda z: 'XYZ'),
        (X, lambda z: 'ABC'),
    ]) == 'ABC'
    assert get_repr_function(y, [
        (lambda z: z == x, lambda z: 'XYZ'),
        (lambda z: z == y, lambda z: 'MNO'),
    ]) == 'MNO'

# Generated at 2022-06-12 20:03:08.220636
# Unit test for function shitcode
def test_shitcode():
    chars = [chr(n) for n in range(256)]
    shitcoded_chars = shitcode(''.join(chars))
    assert shitcoded_chars == ''.join(chars) + '?' * 7

# Generated at 2022-06-12 20:03:10.769074
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    assert issubclass(sys.stdout, WritableStream)
    assert issubclass(object, WritableStream) is False

# Generated at 2022-06-12 20:03:14.352896
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    try:
        sys.stdout.write('hello')
    except:
        assert not isinstance(sys.stdout, WritableStream)
    else:
        assert isinstance(sys.stdout, WritableStream)

# Generated at 2022-06-12 20:03:25.545114
# Unit test for function get_repr_function
def test_get_repr_function():

    def custom_1(x):
        return 'custom_1'

    def custom_2(x):
        return 'custom_2'

    custom_repr = [
        (lambda x: True, custom_1),
        (lambda x: True, custom_2),
        (lambda x: True, custom_1)
    ]

    assert get_repr_function(None, custom_repr) is custom_2
    assert get_repr_function(1, custom_repr) is custom_2
    assert get_repr_function('abc', custom_repr) is custom_2
    assert get_repr_function(1.5, custom_repr) is custom_2

    custom_repr.pop(0)
    assert get_repr_function(None, custom_repr) is custom_2



# Generated at 2022-06-12 20:03:28.408472
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class MyWritableStream(WritableStream):
        def write(self, s):
            pass

        def asd(self):
            pass

    assert issubclass(MyWritableStream, WritableStream)



# Generated at 2022-06-12 20:03:35.722167
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(WritableStream): pass
    assert A.__subclasshook__(A) is NotImplemented
    class B(A):
        def write(self, s): pass
    assert B.__subclasshook__(B) is True
    class C(B): pass
    assert C.__subclasshook__(C) is True
    class D(A): pass
    assert D.__subclasshook__(D) is NotImplemented
    class E(A):
        def write(self, s): pass
    assert E.__subclasshook__(E) is True
    class F(A):
        def write(self, s): pass
        @classmethod
        def __subclasshook__(cls, C):
            return True
    assert F.__subclasshook__(F) is True



# Generated at 2022-06-12 20:03:46.313985
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, custom_repr=[
        (lambda x: x < 3, lambda x: str(x)),
        (lambda x: x < 5, lambda x: str(x) + '-'),
    ]) == str
    assert get_repr_function(1, custom_repr=[
        (lambda x: x < 3, lambda x: str(x)),
        (lambda x: x < 2, lambda x: str(x) + '-'),
    ]) == (lambda x: str(x) + '-')
    assert get_repr_function(1, custom_repr=[
        (lambda x: x < 1, lambda x: str(x)),
        (lambda x: x < 2, lambda x: str(x) + '-'),
    ]) == repr
    assert get_repr_function

# Generated at 2022-06-12 20:03:51.498032
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class X(WritableStream):
        def write(self, s):
            pass

    x = X()
    traceable_write = x.write

    assert callable(traceable_write)
    assert traceable_write.__self__ is x



# Generated at 2022-06-12 20:03:57.903441
# Unit test for function get_repr_function
def test_get_repr_function():

    assert get_repr_function(0, ()) == repr

    assert get_repr_function(0, ((lambda x: x == 0, ''))) == str

    assert get_repr_function(1, ((lambda x: x == 0, ''))) == repr

    assert get_repr_function(
        '1',
        custom_repr=((lambda x: x == '1', ''),)
    ) == str

    assert get_repr_function(
        '2',
        custom_repr=((lambda x: x == '1', ''),)
    ) == repr



# Generated at 2022-06-12 20:03:59.543263
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def write(self, s):
            pass
    class MyNonWritableStream(WritableStream):
        pass

# Generated at 2022-06-12 20:04:01.260542
# Unit test for function get_repr_function
def test_get_repr_function():
    import mock
    get_repr_function('a', [(lambda x: True, lambda _: '1')])

# Generated at 2022-06-12 20:04:09.685972
# Unit test for function get_repr_function
def test_get_repr_function():

    # Custom repr function that always returns the same string
    def custom_repr(x):
        return '<custom_repr>'

    # Custom repr function that returns a tuple of its arguments
    def custom_repr_with_args(x, y):
        return (x, y)

    # Custom repr function that determines whether the arg is an instance of
    # the custom_type class and then decides the return value
    class custom_type(object):
        pass

    def custom_repr_by_type(x, custom_type=custom_type):
        if isinstance(x, custom_type):
            return '<custom_repr_by_type>'
        else:
            return '<not_custom_repr_by_type>'

    # Custom repr function that determines whether the arg is of the type
    # custom

# Generated at 2022-06-12 20:04:15.604946
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(2, ((int, shitcode),)) == shitcode
    assert get_repr_function(2.0, ((int, shitcode),)) != shitcode
    assert get_repr_function(2.0, ((int, shitcode),)) == repr
    assert get_repr_function(2.0, ((float, shitcode),)) == shitcode

# Generated at 2022-06-12 20:04:28.932231
# Unit test for function get_repr_function
def test_get_repr_function():
    class C(object): pass
    get_repr_function(C(), []) == repr # default, class C is not in any condition
    get_repr_function(C(), [(lambda x:True, lambda x: 'result')]) == 'result' # condition (lambda x:True) is always True
    get_repr_function(C(), [(isinstance, lambda x: 'result')]) == 'result' # condition isinstance is True, therefore function get_repr_function returns 'result'
    get_repr_function(C(), [(lambda x:False, lambda x: 'result')]) == repr # condition (lambda x:False) is always False
    get_repr_function(C(), [(isinstance, lambda x: 'result'), (lambda x:True, lambda x: 'result')]) == 'result' # condition (lambda x:True)

# Generated at 2022-06-12 20:04:33.735606
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('abc') == "'abc'"
    assert get_shortish_repr('abc' * 1000) == "'abc' * 1000"
    assert get_shortish_repr(True) == 'True'
    assert get_shortish_repr(b'abc') == "b'abc'"
    assert get_shortish_repr(b'abc' * 1000) == "b'abc' * 1000"
    assert get_shortish_repr(object()) == 'object()'
    assert get_shortish_repr(object()) == 'object()'
    if sys.version_info[0] == 2:
        assert get_shortish_repr(unicode('hi')) == 'u"hi"'

# Generated at 2022-06-12 20:04:44.601991
# Unit test for function get_repr_function
def test_get_repr_function():
    from . import NONE
    from .dummy_types import Dummy
    from .constants import ZERO
    from .dinglebat import Dinglebat
    from python_toolbox import cute_testing
    x = Dummy()
    assert get_repr_function(x, ((Dummy, lambda _: 'hi'),))() == 'hi'
    assert get_repr_function(ZERO, ((Dummy, lambda _: 'hi'),))() == '0'
    assert get_repr_function(NONE, ((Dummy, lambda _: 'hi'),))() == 'None'
    assert get_repr_function(Dinglebat, ((Dummy, lambda _: 'hi'),))() == \
                                                   'Dinglebat(dingle=None)'

# Generated at 2022-06-12 20:04:48.170984
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Foo(WritableStream):
        def write(self, s):
            pass

    foo = Foo()
    with pytest.raises(NotImplementedError):
        def bar(): pass
        bar.write = None
        issubclass(bar, WritableStream)

# Generated at 2022-06-12 20:04:54.944666
# Unit test for function shitcode
def test_shitcode():
    tests = [
        (u'abc', 'abc'),
        (u'abc\x01\x02def', 'abc?def'),
        (u'abc\u2222\u2323def', 'abc?def'),
        (u'\x00', '?'),
        (u'\x0f', '?'),
        (u'\x10', '?'),
        (u'\xfd', '?'),
        (u'\xfe', '?'),
        (u'\xff', '?'),
    ]

    for before, after in tests:
        assert shitcode(before) == after

# Generated at 2022-06-12 20:04:56.992468
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class MyWritableStream(WritableStream):

        def write(self, s):
            pass

    assert isinstance(MyWritableStream(), WritableStream)

# Generated at 2022-06-12 20:05:07.474332
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(3, ()) is repr
    assert get_repr_function('abc', ()) is repr
    assert get_repr_function([], ()) is repr

    assert get_repr_function(3, ((int, str), repr)) is repr
    assert get_repr_function('abc', ((int, str), repr)) is repr
    assert get_repr_function([3, 4], ((int, str), repr)) is str


# Generated at 2022-06-12 20:05:17.575268
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    import collections
    import unittest

    class TestCase(unittest.TestCase):
        pass

    for item, expected in (
        (None, 'None'),
        (3, '3'),
        (3.0, '3.0'),
        (3 + 4j, '(3+4j)'),
        ([1, 2, 3], '[1, 2, 3]'),
        ((1, 2, 3), '(1, 2, 3)'),
        ({1, 2, 3}, '{1, 2, 3}'),
        ({1: 2, 3: 4}, '{1: 2, 3: 4}')
    ):
        with TestCase.subTest(item=item, expected=expected):
            result = get_shortish_repr(item)
            TestCase.assertEqual(result, expected)
   

# Generated at 2022-06-12 20:05:22.336517
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyFile(WritableStream):
        def write(self, s):
            pass
    assert issubclass(MyFile, WritableStream)
    MyFile().write('')
    try:
        class MyFile2(WritableStream):
            pass
    except TypeError:
        pass
    else:
        raise AssertionError
    class MyFile3(WritableStream):
        def write(self, s):
            pass
        def rude_write(self, s):
            pass
    MyFile3().write('')
    assert issubclass(MyFile3, WritableStream)

# Generated at 2022-06-12 20:05:29.070993
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    from .pycompat import StringIO
    with StringIO() as s:
        try:
            assert issubclass(StringIO, WritableStream)
        except Exception:
            raise AssertionError('StringIO is not registered as '
                                 'a sublcass of WritableStream')
        else:
            s.write('hello')
            assert s.getvalue() == 'hello'



# Generated at 2022-06-12 20:05:41.363808
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyFile(object):
        def write(self, s): pass
    MyFile.__bases__ += (WritableStream,)
    return MyFile()

assert isinstance(test_WritableStream_write(), WritableStream)

# Generated at 2022-06-12 20:05:43.393093
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class WritableFile(WritableStream):
        def write(self, s):
            print(s)

    WritableFile().write('hello')



# Generated at 2022-06-12 20:05:48.742673
# Unit test for function get_repr_function
def test_get_repr_function():
    class Foo(object):
        def __repr__(self):
            return 'repr'
    class Bar(object):
        def __str__(self):
            return 'str'
    f = Foo()
    b = Bar()
    assert get_repr_function(f, (
            (lambda item: hasattr(item, '__repr__'), repr),
            (lambda item: hasattr(item, '__str__'), str)
    )) is repr
    assert get_repr_function(b, (
            (lambda item: hasattr(item, '__repr__'), repr),
            (lambda item: hasattr(item, '__str__'), str)
    )) is str

# Generated at 2022-06-12 20:05:51.922176
# Unit test for function shitcode

# Generated at 2022-06-12 20:05:54.207536
# Unit test for function shitcode
def test_shitcode():
    assert shitcode('he\u2713') == 'he?'
    assert shitcode(u'\u2713'*1000) == '?'*1000



# Generated at 2022-06-12 20:05:55.586710
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def write(self, s):
            pass
    ws = MyWritableStream()
    assert isinstance(ws, WritableStream)

# Generated at 2022-06-12 20:06:00.223876
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(None) == 'None'
    assert get_shortish_repr(0) == '0'
    assert get_shortish_repr('') == '\'\''
    assert get_shortish_repr(u'') == 'u\'\''
    assert get_shortish_repr('a', max_length=4) == '\'a\''
    assert get_shortish_repr('a', max_length=3) == '\'a\''
    assert get_shortish_repr('a', max_length=2) == '\'a\''
    assert get_shortish_repr('a', max_length=1) == '\'a\''
    assert get_shortish_repr('a', max_length=0) == '\'a\''

# Generated at 2022-06-12 20:06:09.722769
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    class Kuku:
        def __init__(self, name):
            self.name = name

        def __repr__(self):
            return '{}({})'.format(self.__class__.__name__, self.name)

    def no_repr(x):
        """For testing stuff that does not have a `__repr__`"""
        return 'no repr'

    def no_repr_with_args(x, y):
        return "no repr with args!"

    class Kuku2:
        def __repr__(self):
            return 'Kuku2()'

    assert get_shortish_repr(Kuku('kuku')) == 'Kuku(kuku)'

# Generated at 2022-06-12 20:06:17.271036
# Unit test for function get_repr_function
def test_get_repr_function():
    # `repr_of` is a dummy function that checks that it's receiving the correct
    # args.
    def repr_of(item, custom_repr):
        if item == 'foo':
            if custom_repr is None:
                return 1
            else:
                return 2
        else:
            if custom_repr is None:
                return 3
            else:
                return 4

    assert get_repr_function('foo', ()) == repr
    assert get_repr_function('foo', custom_repr=[
        (lambda item: item == 'foo', repr_of)
    ]) == repr_of

    assert get_repr_function(object(), ()) == repr
    assert get_repr_function(object(), custom_repr=[
        (lambda item: False, repr_of)
    ]) == repr



# Generated at 2022-06-12 20:06:25.029056
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    class Class(object):
        def __repr__(self):
            return 'this is an object of Class'
    class Class2(object):
        def __repr__(self):
            return 'this is an object of Class2'
    assert get_shortish_repr('abc') == "'abc'"
    assert get_shortish_repr('abc', max_length=2) == "'ab'"
    assert get_shortish_repr('abc', max_length=5) == "'abc'"
    assert get_shortish_repr('abc', max_length=6) == "'abc'"
    assert get_shortish_repr(Class()) == 'this is an object of Class'

# Generated at 2022-06-12 20:06:49.102014
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A:
        pass

    class B:
        def write(self):
            pass
    class C:
        def write(self, s):
            pass

    assert WritableStream.__subclasshook__(A) == NotImplemented
    assert WritableStream.__subclasshook__(B) == NotImplemented
    assert WritableStream.__subclasshook__(C) == True

# Generated at 2022-06-12 20:06:51.623407
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(Z(42), []) is repr
    assert get_repr_function(Z(42), [(Z, lambda x: 'Z(%s)' % x.a)]) == 'Z(42)'
    assert get_repr_function(1, [(Z, lambda x: 'Z(%s)' % x.a)]) is repr



# Generated at 2022-06-12 20:07:00.481807
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(WritableStream): pass
    assert issubclass(A, WritableStream)
    assert WritableStream.__subclasshook__(A) is True
    class WritableString(str, WritableStream):
        def write(self, s):
            self += s
    assert issubclass(WritableString, WritableStream)
    assert WritableStream.__subclasshook__(WritableString) is True

    # Passing test
    s = WritableString()
    assert isinstance(s, WritableStream)

    # Failing test
    class B(WritableStream): pass
    assert not issubclass(B, WritableStream)
    assert WritableStream.__subclasshook__(B) is NotImplemented

# Generated at 2022-06-12 20:07:08.895578
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A:
        def write(self, s):
            pass

    assert issubclass(A, WritableStream)

    class B:
        pass

    assert not issubclass(B, WritableStream)

    class C:
        def write(self):
            pass

    assert not issubclass(C, WritableStream)

    class D:
        @staticmethod
        def write(s):
            pass

    assert not issubclass(D, WritableStream)

    class E:
        @property
        def write(self):
            pass

    assert not issubclass(E, WritableStream)

# Generated at 2022-06-12 20:07:17.580024
# Unit test for function get_repr_function
def test_get_repr_function():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    assert get_repr_function(A(), []) == repr
    assert get_repr_function(A(), [(list, lambda x: 'list')]) == repr
    assert get_repr_function(A(), [(list, lambda x: 'list'),
                                   (A, lambda x: 'A')]) == repr
    assert get_repr_function(A(), [(list, lambda x: 'list'),
                                   (A, lambda x: 'A'),
                                   (B, lambda x: 'B')]) == repr
    assert get_repr_function(B(), [(list, lambda x: 'list'),
                                   (A, lambda x: 'A'),
                                   (B, lambda x: 'B')]) == 'B'
   

# Generated at 2022-06-12 20:07:28.713773
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    b = (1, 2, 3, 4)
    assert get_shortish_repr(b, max_length=2) == '1...'
    assert get_shortish_repr(b, max_length=3) == '(1...'
    assert get_shortish_repr(b, max_length=4) == '(1,...'
    assert get_shortish_repr(b, max_length=5) == '(1,2...'
    assert get_shortish_repr(b, max_length=6) == '(1,2,...'
    assert get_shortish_repr(b, max_length=7) == '(1,2,3...'
    assert get_shortish_repr(b, max_length=8) == '(1,2,3,...'
    assert get_shortish

# Generated at 2022-06-12 20:07:39.168253
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(None, ()).__name__ == 'repr'
    assert get_repr_function(None, ((), lambda s: 'foo')) == 'foo'
    assert get_repr_function(None, ((lambda x: True, lambda s: 'foo'))) == 'foo'
    assert get_repr_function(None, ((lambda x: False, lambda s: 'foo'))) == 'repr'
    assert get_repr_function(None, ((lambda x: False, lambda s: 'foo'),
                                    (lambda x: True, id))) == id
    assert get_repr_function(None, ((lambda x: False, lambda s: 'foo'),
                                    (lambda x: False, id))) == 'repr'

# Generated at 2022-06-12 20:07:41.500746
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function('c', ((str, repr), (int, repr))) == repr
    assert get_repr_function(5, ((str, repr), (int, repr))) == repr

# Generated at 2022-06-12 20:07:52.286746
# Unit test for function get_repr_function
def test_get_repr_function():
    class C1: pass
    class C2: pass
    c1 = C1()
    c2 = C2()
    assert get_repr_function(c1, ((lambda x: x is C1, lambda x: 'a'),))(c1) == 'a'
    assert get_repr_function(c1, ((lambda x: x is C2, lambda x: 'b'),))(c1) != 'b'
    assert get_repr_function(c2, ((lambda x: x is C2, lambda x: 'b'),))(c2) == 'b'

    assert get_repr_function(c1, ((C1, lambda x: 'a'),))(c1) == 'a'

# Generated at 2022-06-12 20:08:02.770211
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('hello') == "'hello'"
    assert get_shortish_repr(
        'hello',
        max_length=None,
    ) == "'hello'"
    assert get_shortish_repr(
        'hello',
        max_length=1,
    ) == "'h'"
    assert get_shortish_repr(
        'hello',
        max_length=6,
    ) == "'hello'"
    assert get_shortish_repr(
        'hello',
        max_length=7,
    ) == "'hello'"
    assert get_shortish_repr(
        'hello',
        max_length=8,
    ) == "'hello'"