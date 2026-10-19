

# Generated at 2022-06-12 19:58:42.591895
# Unit test for function shitcode
def test_shitcode():
    assert shitcode('a') == 'a'
    assert shitcode('a\0\0') == 'a??'
    assert shitcode('a\0\0b') == 'a??b'
    assert shitcode('a\0\0b\0\xFF') == 'a??b???'
    assert shitcode('a\0\0b\0\xFF') == 'a??b???'
    assert shitcode(u'a\0\0b\0\xFF') == u'a??b???'
    assert shitcode('a☢') == 'a?'
    assert shitcode(u'a☢') == 'a?'
    #assert shitcode(u'a\u{2660}') == 'a??'



# Generated at 2022-06-12 19:58:50.179834
# Unit test for function shitcode
def test_shitcode():
    assert shitcode('רמר שחור') == '???? ???'
    assert shitcode('אושר יהדות') == '???? ?'
    assert shitcode('צחיחים') == '????'
    assert shitcode('צחוק') == '????'
    assert shitcode('צמוד') == '????'
    assert shitcode('f') == 'f'
    assert shitcode('צ י') == '?? ?'
    assert shitcode('צ') == '??'
    assert shitcode('צחח') == '????'



# Generated at 2022-06-12 19:58:53.311574
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class WritableStreamImpl(WritableStream):
        def write(self, s):
            sys.stdout.write(s)

    writable_stream = WritableStreamImpl()
    assert isinstance(writable_stream, WritableStream)
    writable_stream.write('hi')



# Generated at 2022-06-12 19:58:56.783154
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def write(self, s):
            pass

    assert issubclass(MyWritableStream, WritableStream)
    assert isinstance(MyWritableStream(), WritableStream)



# Generated at 2022-06-12 19:59:02.799102
# Unit test for function shitcode
def test_shitcode():
    test_dict = {'עברית': '?',
                 'Русский': '?',
                 'العربية': '?',
                 'ਪੰਜਾਬੀ': '?',
                 '🐱': '?',
                 'a': 'a',
                 '2': '2',
                 '❤': '?'}
    for key, value in test_dict.items():
        print(key)
        assert shitcode(key) == value



# Generated at 2022-06-12 19:59:11.912433
# Unit test for function get_repr_function
def test_get_repr_function():
    class Thing(object):
        def __init__(self, color, size):
            self.color = color
            self.size = size
        def __repr__(self):
            return 'Thing({}, {})'.format(self.color, self.size)
    thing = Thing('red', 'big')
    assert get_repr_function(thing, []) is repr
    assert get_repr_function(thing, [(Thing, lambda x: 'aha')]) == 'aha'
    assert get_repr_function(thing, [(str, lambda x: 'aha')]) is repr
    assert get_repr_function(thing, [(Thing, lambda thing: thing.color)]) == 'red'
    assert get_repr_function(thing, [(Thing, lambda thing: thing.size)]) == 'big'

# Generated at 2022-06-12 19:59:22.728929
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('', max_length=5) == ''
    assert get_shortish_repr('1234567', max_length=5) == '12...5'
    assert get_shortish_repr('1234567', max_length=7) == '1234567'
    assert get_shortish_repr(object()) == '<object object at ...>'
    assert get_shortish_repr(object(), max_length=2) == '<...>'
    from . import main_menu
    assert get_shortish_repr(main_menu) == '<module \'cute_mongo_shell.main_menu\' from ...>'



# Generated at 2022-06-12 19:59:26.596360
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Foo(object):
        def write(self, s):
            pass
    class Bar(object):
        pass
    assert issubclass(Foo, WritableStream)
    assert not issubclass(Bar, WritableStream)
    assert issubclass(sys.stdout.__class__, WritableStream)



# Generated at 2022-06-12 19:59:33.620339
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def __init__(self):
            self.chars = []
        def write(self, s):
            assert isinstance(s, str)
            self.chars.extend(s)
    stream = MyWritableStream()
    stream.write(u'abc')
    assert stream.chars == ['a', 'b', 'c']


if __name__ == '__main__':
    test_WritableStream_write()

# Generated at 2022-06-12 19:59:39.277428
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(23, [(lambda x: x < 0, str)]) == int
    assert get_repr_function(-23, [(lambda x: x < 0, str)]) == str
    assert get_repr_function(-23, [(int, str)]) == int
    assert get_repr_function(-23, [(int, str), (float, repr)]) == str
    assert get_repr_function(23.23, [(int, str), (float, repr)]) == repr



# Generated at 2022-06-12 19:59:52.324515
# Unit test for function get_repr_function
def test_get_repr_function():
    assert 'a' == get_shortish_repr('a', [])
    assert 'a' == get_shortish_repr('a', [(lambda s: True, str)])
    assert 'a' == get_shortish_repr('a', [(lambda s: True, lambda x: 'b')])
    assert 'b' == get_shortish_repr('a', [(lambda s: False, lambda x: 'b')])
    assert 'b' == get_shortish_repr('a', [(lambda s: True, lambda x: 'b'),
                                      (lambda s: True, lambda x: 'c')])
    assert 'a' == get_shortish_repr('a', [(lambda s: False, lambda x: 'b'),
                                      (lambda s: True, lambda x: 'c')])



# Generated at 2022-06-12 20:00:00.581521
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    def check(C):
        assert issubclass(C, WritableStream)
    check(WritableStream)
    class X(WritableStream):
        def write(self, s): pass
    check(X)
    class Y(X):
        def write(self, s): pass
    check(Y)
    class Z(Y, X):
        def write(self, s): pass
    check(Z)
    class W: pass
    assert not issubclass(W, WritableStream)
    class W(WritableStream): pass
    assert not issubclass(W, WritableStream)
    class W(WritableStream):
        def write(self, s): pass
        def writable(self): return True
    assert not issubclass(W, WritableStream)
    check(W)

# Generated at 2022-06-12 20:00:10.309360
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(1) == '1'
    assert get_shortish_repr(1, max_length=1) == '1'
    assert get_shortish_repr(1, max_length=2) == '1'
    assert get_shortish_repr(1, max_length=3) == '1'
    assert get_shortish_repr(1, max_length=4) == '1'
    assert get_shortish_repr(1, max_length=5) == '1'
    assert get_shortish_repr(1, max_length=6) == '1'

    assert get_shortish_repr(123, max_length=2) == '1...'

# Generated at 2022-06-12 20:00:16.262220
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    import unittest

    class MyClass(object):
        def __init__(self, x):
            self.x = x

        def __repr__(self):
            return '<MyClass with x={}>'.format(self.x)


    class MyOtherClass(object):
        def __repr__(self):
            raise Exception('bah')

    class Test(unittest.TestCase):
        def test(self):
            self.assertEqual(
                get_shortish_repr('meh'),
                "meh"
            )
            self.assertEqual(
                get_shortish_repr('meh', max_length=1),
                "meh"
            )

# Generated at 2022-06-12 20:00:19.051907
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    assert _check_methods(sys.stdout, 'write')



# Generated at 2022-06-12 20:00:30.351901
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    from .test_tools import assert_equal
    s = 'a' * 20
    assert_equal(get_shortish_repr(s, max_length=10), 'aaaaaaaaaa...aaaa')
    assert_equal(get_shortish_repr(s, max_length=11), 'aaaaaaaaaaa...aaaa')
    assert_equal(get_shortish_repr(s, max_length=30), repr(s))
    assert_equal(get_shortish_repr(s, max_length=None), repr(s))
    assert_equal(get_shortish_repr([1, 2, 3], max_length=10), '[1, 2, 3]')
    assert_equal(get_shortish_repr([1, 2, 3], max_length=1), '[...]')


# Generated at 2022-06-12 20:00:38.506778
# Unit test for function get_repr_function
def test_get_repr_function():
    def custom_repr_for_a(x):
        return 'A!'
    def custom_repr_for_b(x):
        return 'B!'
    def custom_repr_for_c(x):
        return 'C!'
    custom_repr = (('', custom_repr_for_a),
                   (lambda x: isinstance(x, str), custom_repr_for_b),
                   ((str, int), custom_repr_for_c),
                   (int, lambda x: 'int: {}'.format(x)))
    assert get_repr_function('', custom_repr)() == 'A!'
    assert get_repr_function('', custom_repr) == custom_repr_for_a

# Generated at 2022-06-12 20:00:45.929103
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class FakeWritableStream(WritableStream):
        def __init__(self):
            self.called = 0
            self.written_string = ''

        def write(self, s):
            self.called += 1
            self.written_string += s


    fws = FakeWritableStream()

    assert isinstance(fws, WritableStream)

    fws.write('A')
    fws.write('B')

    assert fws.called == 2
    assert fws.written_string == 'AB'



# Generated at 2022-06-12 20:00:48.361872
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class WritableStreamTester(WritableStream):
        def write(self, s): pass

    assert isinstance(WritableStreamTester(), WritableStream)



# Generated at 2022-06-12 20:00:52.625639
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, custom_repr=[(int, 'int')]) == 'int'
    assert get_repr_function((1, 2), custom_repr=[(tuple, 'tuple')]) == 'tuple'
    assert get_repr_function((1, 2), custom_repr=[(dict, 'dict')]) == repr
    assert get_repr_function((1, 2), custom_repr=[(dict, lambda _: 'dict')]) == 'dict'

# Generated at 2022-06-12 20:00:59.985798
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Thing(WritableStream):
        def write(self, s):
            return NotImplemented
    assert issubclass(Thing, WritableStream)
    assert not issubclass(int, WritableStream)

# Generated at 2022-06-12 20:01:05.147701
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(None, ()) is repr

    def cust_repr(x):
        return 'custom repr! on {}'.format(x)

    assert get_repr_function(None, ((lambda x: False, lambda x: 'bad'))) \
        is repr
    assert get_repr_function(None, ((lambda x: True, cust_repr))) is cust_repr
    assert get_repr_function(None, ((float, cust_repr))) is cust_repr



# Generated at 2022-06-12 20:01:15.868468
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    from .pycompat import StringIO

    class SomeWritableStream(WritableStream):
        def write(self, s):
            return 'XYZ{}'.format(s)

    class AnotherWritableStream(SomeWritableStream):
        def write(self, s):
            return '{}XYZ'.format(s)

    assert issubclass(StringIO, WritableStream)
    assert issubclass(SomeWritableStream, WritableStream)
    assert issubclass(AnotherWritableStream, WritableStream)

    stream = SomeWritableStream()
    assert stream.write('abc') == 'XYZabc'

    stream = AnotherWritableStream()
    assert stream.write('abc') == 'abcXYZ'

    class NotWritableStream(metaclass=ABC):
        pass

    assert NotWritableStream not in Writ

# Generated at 2022-06-12 20:01:23.379277
# Unit test for function get_repr_function
def test_get_repr_function():
    class A: pass
    class B(A): pass
    class C(A): pass
    a = A()
    b = B()
    c = C()

    # Simple test

# Generated at 2022-06-12 20:01:30.715026
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    print(get_shortish_repr(1))
    print(get_shortish_repr(2.7, max_length=2))
    print(get_shortish_repr(2.7, max_length=3))
    print(get_shortish_repr(2.7, max_length=4))
    print(get_shortish_repr(2.7, max_length=5))
    print(get_shortish_repr(2.7, max_length=6))
    print(get_shortish_repr(2.7, max_length=7))




# Generated at 2022-06-12 20:01:34.977131
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(2, []) == repr
    assert get_repr_function(2, [(int, str)]) == str
    assert get_repr_function(2.0, [(int, str)]) == repr
    assert get_repr_function(2, [(lambda x: x > 1, str)]) == repr
    assert get_repr_function(2, [(lambda x: x > 1, str), (int, str)]) == str



# Generated at 2022-06-12 20:01:44.751991
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(1) == '1'
    assert get_shortish_repr(1, custom_repr=((lambda x: True, lambda x: 'x'))) == 'x'
    assert get_shortish_repr(1, max_length=1) == '1'
    assert get_shortish_repr(1, max_length=2) == '1'
    assert get_shortish_repr(1, max_length=3) == '1'
    assert get_shortish_repr(111111, max_length=3) == '...'
    assert get_shortish_repr(111111, max_length=4) == '1...'
    assert get_shortish_repr(111111, max_length=5) == '11...'
    assert get_

# Generated at 2022-06-12 20:01:50.267313
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(5, []) is repr

    assert get_repr_function(5, [(int, lambda x: 'foo')]) == 'foo'
    assert get_repr_function(5.3, [(int, lambda x: 'foo')]) is repr

    assert get_repr_function(5, [(lambda x, y=5: x == y, lambda x: 'foo'),
                                 (lambda x, y=6: x == y, lambda x: 'bar')]) == 'foo'
    assert get_repr_function(6, [(lambda x, y=5: x == y, lambda x: 'foo'),
                                 (lambda x, y=6: x == y, lambda x: 'bar')]) == 'bar'

# Generated at 2022-06-12 20:01:59.363264
# Unit test for function get_repr_function
def test_get_repr_function():
    from .typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from typing import Tuple, TypeVar

    T = TypeVar('T')

    def get_repr_function_test(custom_repr, item, expected_function):
        actual_function = get_repr_function(item, custom_repr)
        assert actual_function is expected_function

    custom_repr = ((str, str), (int, int))

    get_repr_function_test(
        custom_repr, '123',
        str
    )
    get_repr_function_test(
        custom_repr, 456,
        int
    )
    get_repr_function_test(
        custom_repr, {},
        repr
    )


# Generated at 2022-06-12 20:02:03.108108
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(object):
        pass
    class B(object):
        def write(self):
            pass
    class C(object):
        def write(self, s):
            pass
    assert not issubclass(A, WritableStream)
    assert not issubclass(B, WritableStream)
    assert issubclass(C, WritableStream)



# Generated at 2022-06-12 20:02:16.811009
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(1) == '1'
    assert get_shortish_repr(1, max_length=2) == '1'
    assert get_shortish_repr(1, max_length=1) == '1'

    assert (get_shortish_repr(3.14159265359, max_length=10) ==
                                                          '3.14159...9265359')
    assert (get_shortish_repr(3.14159265359, max_length=20) ==
                                                          '3.14159265359')
    assert (get_shortish_repr(3.14159265359, max_length=20, normalize=True) ==
                                                              '3.14159265359')

# Generated at 2022-06-12 20:02:19.296082
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A:
        def write(self, s):
            pass
    assert issubclass(A, WritableStream)



# Generated at 2022-06-12 20:02:21.417712
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    pass


if __name__ == '__main__':
    test_WritableStream_write()

# Generated at 2022-06-12 20:02:27.991630
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Foo(WritableStream):
        pass

    assert WritableStream.__subclasshook__(Foo) is NotImplemented

    class Foo(WritableStream):
        def write(self, s):
            pass

    assert WritableStream.__subclasshook__(Foo) is True

    class Foo(WritableStream):
        def write(self, s, another_argument=None):
            pass

    assert WritableStream.__subclasshook__(Foo) is True



# Generated at 2022-06-12 20:02:35.696888
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class FakeWritableStream(WritableStream):
        def __init__(self):
            self.contents = ''

        def write(self, s):
            self.contents += s

    class FakeNonWritableStream:
        def write(self, s):
            pass

    fws = FakeWritableStream()
    assert isinstance(fws, WritableStream)

    fws.write('spam')

    assert fws.contents == 'spam'

    assert not isinstance(FakeNonWritableStream(), WritableStream)

# Generated at 2022-06-12 20:02:45.440844
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr("I'm a string") == "I'm a string"
    assert get_shortish_repr("I'm a string", max_length=20) == "I'm a string"
    assert get_shortish_repr("I'm a string", max_length=20, normalize=True) == "I'm a string"
    assert get_shortish_repr("I'm a string", max_length=10) == "I'm a..."
    assert get_shortish_repr("I'm a string", max_length=10, normalize=True) == "I'm a..."
    assert get_shortish_repr("I'm a string", max_length=9) == "I'm a..."

# Generated at 2022-06-12 20:02:50.961490
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(123) == '123'
    import math
    assert get_shortish_repr(math.sqrt) == '<built-in function sqrt>'
    assert get_shortish_repr(range(9), max_length=6) == 'range'
    assert get_shortish_repr(b'123', max_length=6) == "b'123'"
    assert get_shortish_repr(u'123', max_length=6) == "'123'"
    assert get_shortish_repr(u'123', max_length=None) == "'123'"

# Generated at 2022-06-12 20:02:54.354949
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Tests(object):
        def __init__(self, *a, **kw):
            pass

        def a(self):
            pass

        def write(self, arg):
            pass

    assert issubclass(Tests, WritableStream)



# Generated at 2022-06-12 20:03:03.620140
# Unit test for function get_repr_function
def test_get_repr_function():

    class SomeClass(object):
        pass

    class SomeOtherClass(object):
        pass

    class SomeSubclass(SomeClass):
        pass

    class SomeOtherSubclass(SomeClass):
        pass

    some_list = [1, 2, 'a', 'b', SomeClass()]

# Generated at 2022-06-12 20:03:16.059570
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    from .fuckup import Fuckup, FuckupHandler
    from .stdout_redirector import StdoutCapture

    def short_repr(x):
        return '%s, %s' % (type(x).__name__, x.__class__.__name__)


# Generated at 2022-06-12 20:03:27.997762
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(WritableStream):
        def write(self, s): pass
    assert issubclass(A, WritableStream)
    a = A()
    assert isinstance(a, WritableStream)

# Generated at 2022-06-12 20:03:35.510098
# Unit test for function get_shortish_repr
def test_get_shortish_repr():

    assert get_shortish_repr('abcde', max_length=3) == 'abc...'
    assert get_shortish_repr('abcde', max_length=4) == 'abcd...'
    assert get_shortish_repr('abcde', max_length=5) == 'abcde'
    assert get_shortish_repr('abcde', max_length=6) == 'abcde'

    assert get_shortish_repr(None, max_length=5) == 'None'

    assert get_shortish_repr(object(), max_length=5) == 'objec...'

    assert get_shortish_repr((1, 2), max_length=5) == '(1, 2)'


# Generated at 2022-06-12 20:03:37.313996
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    get_shortish_repr(lambda x: x, [(lambda x: x, 'works')])



# Generated at 2022-06-12 20:03:47.628465
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(1) == '1', repr(get_shortish_repr(1))
    assert get_shortish_repr(1, max_length=1) == '1', \
                                                   repr(get_shortish_repr(1))
    assert get_shortish_repr(1, max_length=2) == '1', \
                                                   repr(get_shortish_repr(1))
    assert get_shortish_repr(1, max_length=4) == '1', \
                                                   repr(get_shortish_repr(1))
    assert get_shortish_repr(1, max_length=0) == '...', \
                                                   repr(get_shortish_repr(1))

# Generated at 2022-06-12 20:03:55.911564
# Unit test for function get_shortish_repr
def test_get_shortish_repr():

    # Testing size limitation
    assert get_shortish_repr('1234567890', max_length=9) == \
                                                            '12345...'
    assert get_shortish_repr('1234567890', max_length=10) == \
                                                            '1234567890'
    assert get_shortish_repr('1234567890', max_length=11) == \
                                                            '1234567890'

    # Testing broken repr
    class Broken(object):
        def __repr__(self):
            raise Exception()
    broken = Broken()
    assert get_shortish_repr(broken) == 'REPR FAILED'

# Generated at 2022-06-12 20:03:57.308430
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def write(self, s):
            pass
    assert issubclass(MyWritableStream, WritableStream)



# Generated at 2022-06-12 20:04:00.301315
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyFile(WritableStream):
        def write(self, s):
            pass
    file_object = MyFile()
    assert isinstance(file_object, WritableStream)


if __name__ == '__main__':
    test_WritableStream_write()

# Generated at 2022-06-12 20:04:03.332843
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyStream(WritableStream):
        def __init__(self):
            self.s = ''
        def write(self, s):
            self.s += s
        
    s = MyStream()
            
    s.write('hello ')
    s.write('world!')
    
    assert s.s == 'hello world!'


# Generated at 2022-06-12 20:04:08.360315
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    """Testing the get_shortish_repr function"""
    assert get_shortish_repr(list, max_length=11) == 'list'
    assert get_shortish_repr(list, max_length=10) == 'list'
    assert get_shortish_repr(list, max_length=9) == 'l...t'
    assert get_shortish_repr(list, max_length=8) == '...t'
    assert get_shortish_repr(list, max_length=7) == '...t'
    assert get_shortish_repr(list, max_length=6) == '...t'
    assert get_shortish_repr(list, max_length=5) == '...t'
    assert get_shortish_repr(list, max_length=4)

# Generated at 2022-06-12 20:04:13.645337
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    from .doctest import capture_stdout_stderr
    with capture_stdout_stderr() as (stdout, stderr):
        print('hello')
        assert isinstance(stdout, WritableStream)
        assert not isinstance(stderr, WritableStream)


if __name__ == '__main__':
    test_WritableStream_write()

# Generated at 2022-06-12 20:04:21.953754
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class TestClass:
        def write(self, s):
            pass
    assert isinstance(TestClass(), WritableStream)



# Generated at 2022-06-12 20:04:24.304661
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class BogusWritableStream(WritableStream):
        write_called = False
        def write(self, s):
            self.write_called = True
    bogus_writable_stream = BogusWritableStream()
    assert bogus_writable_stream.write_called is False
    bogus_writable_stream.write('')
    assert bogus_writable_stream.write_called is True



# Generated at 2022-06-12 20:04:30.625334
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function('', []) is repr

    assert get_repr_function(1, [(lambda x: True, lambda x: 2)]) == 2

    assert get_repr_function(1, [
        (lambda x: False, lambda x: 2),
        (lambda x: True, lambda x: 3)
    ]) == 3

    assert get_repr_function(1, [
        (lambda x: False, lambda x: 2),
        (lambda x: False, lambda x: 3)
    ]) == 2


# Generated at 2022-06-12 20:04:36.626765
# Unit test for function get_repr_function
def test_get_repr_function():
    def y(): pass

    def f(x): return lambda y=x: y

    class C:
        pass

    class C2:
        pass

    assert get_repr_function(f(1), [(int, lambda n: n + 3)])(3) == '6'

    assert get_repr_function(f(1), [(int, lambda n: n + 4)])(3) == '4'

    assert get_repr_function(f(1), [(C2, 42)])(3) == '3'

    assert shitcode(get_repr_function(bytearray(b'\x81'),
                                      [(C, lambda x: x.__class__.__name__)])(3)) \
                                                                                == \
                                                                                    'bytearray'

    assert get

# Generated at 2022-06-12 20:04:41.041497
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Stream(WritableStream):
        def __init__(self):
            self.s = ''
        def write(self, s):
            self.s += s

    stream = Stream()
    stream.write('meow')
    assert stream.s == 'meow'


# Generated at 2022-06-12 20:04:50.889593
# Unit test for function get_shortish_repr
def test_get_shortish_repr():

    assert get_shortish_repr(4, max_length=None) == '4'
    assert get_shortish_repr(4, max_length=2) == '4'
    assert get_shortish_repr(4, max_length=1) == '4'
    assert get_shortish_repr(4, max_length=0) == ''

    assert get_shortish_repr(4, (
        (type(4), lambda n: str(n ** 3)),
    ), max_length=None) == '64'
    assert get_shortish_repr(4, (
        (type(4), lambda n: str(n ** 3)),
    ), max_length=5) == '64'

# Generated at 2022-06-12 20:04:58.111075
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    # `WritableStream` is an abstract base class.
    
    class Example(WritableStream):
        def __init__(self):
            self.written = ''
        def write(self, s):
            self.written += s
            return len(s)
    
    # `WritableStream` demands a `write` method.
    
    class ExampleMissingWrite(WritableStream):
        pass
    
    assert issubclass(Example, WritableStream)
    assert not issubclass(ExampleMissingWrite, WritableStream)
    
    # A `write` method that doesn't return an integer raises an exception.
    
    class ExampleWrongWrite(WritableStream):
        def write(self, s):
            return 'not integer'
    
    assert not issubclass(ExampleWrongWrite, WritableStream)
    



# Generated at 2022-06-12 20:05:03.048450
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A:
        pass

    assert issubclass(A, WritableStream)

    a = A()

    def boom():
        issubclass(A, WritableStream)

    assert _check_methods(a, 'write')



# Generated at 2022-06-12 20:05:06.766846
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class AStream(WritableStream):
        def write(self, s):
            print(s)
    assert issubclass(AStream, WritableStream)
    AStream().write('hello')

    class BStream(AStream): pass
    assert issubclass(BStream, WritableStream)
    BStream().write('hello')



# Generated at 2022-06-12 20:05:10.018010
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Foo:
        def write(self, s):
            return
    assert isinstance(Foo(), WritableStream)
    assert issubclass(Foo, WritableStream)



# Generated at 2022-06-12 20:05:27.365669
# Unit test for function get_repr_function
def test_get_repr_function():
    lower = lambda x: x.lower()
    upper = lambda x: x.upper()
    z_repr = get_repr_function('z', (
        (lambda x: x in 'abcdefghijklmnopqrstuvwxyz', lower),
        (lambda x: x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', upper),
    ))
    assert z_repr('z') == 'z'
    assert z_repr('Z') == 'Z'



# Generated at 2022-06-12 20:05:30.510861
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream:
        def write(self, s):
            pass
    assert issubclass(MyWritableStream, WritableStream)
    assert not issubclass(WritableStream, MyWritableStream)

# Generated at 2022-06-12 20:05:37.894160
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class WritableStreamExceptWrite:
        def write(self, s):
            raise Exception

    print('This should not raise:')
    WritableStream.register(WritableStreamExceptWrite)
    assert issubclass(WritableStreamExceptWrite, WritableStream)
    writable_stream_except_write = WritableStreamExceptWrite()
    writable_stream_except_write.write('foo')


# Generated at 2022-06-12 20:05:45.657426
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def __init__(self):
            self.write_called_with_args = []
        def write(self, s):
            self.write_called_with_args.append(s)
    my_writable_stream = MyWritableStream()
    assert issubclass(MyWritableStream, WritableStream)
    assert isinstance(my_writable_stream, WritableStream)
    my_writable_stream.write('hi')
    assert my_writable_stream.write_called_with_args == ['hi']
    class MyNonWritableStream: pass
    assert not issubclass(MyNonWritableStream, WritableStream)
    assert not isinstance(MyNonWritableStream(), WritableStream)
    class MyWritableStream2(MyWritableStream): pass

# Generated at 2022-06-12 20:05:48.777762
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    try:
        sys.stdout.write('a')
        sys.stdout.write(b'b')
    except:
        assert False, "sys.stdout is not a WritableStream."

# Generated at 2022-06-12 20:05:56.962612
# Unit test for function get_repr_function
def test_get_repr_function():

    class FooClass(object):
        pass

    # Simply test that get_repr_function works.
    assert get_repr_function(1, (int, str)) == repr
    assert get_repr_function(1, (int, str)) != repr
    assert get_repr_function(1, (str, int)) == repr
    assert get_repr_function(1, (str, int)) != repr
    assert get_repr_function(1, (int, lambda x: True)) == repr
    assert get_repr_function(1, (int, lambda x: False)) != repr
    assert get_repr_function(1, (int, lambda x: True)) != repr
    assert get_repr_function(1, (int, lambda x: False)) == repr

# Generated at 2022-06-12 20:06:00.082771
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyOwnWritableStream(WritableStream):
        def write(self, s):
            pass

    assert callable(MyOwnWritableStream.write)
    assert issubclass(MyOwnWritableStream, WritableStream)

# Generated at 2022-06-12 20:06:02.660031
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class X(WritableStream):
        def write(self, s):
            return s == 'hi'
    assert issubclass(X, WritableStream)



# Generated at 2022-06-12 20:06:11.512985
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MockWritableStream(WritableStream):
        def __init__(self):
            self._write_calls = []

        def write(self, s):
            self._write_calls.append(s)

    mock = MockWritableStream()
    assert mock.write('a') is None
    assert mock.write('b') is None
    assert mock._write_calls == ['a', 'b']

    class MockWritableStreamWithFormatting:
        def __init__(self):
            self._write_calls = []

        def write(self, s):
            self._write_calls.append(s)

        def __format__(self, format_spec):
            return 'woof!'

    mock = MockWritableStreamWithFormatting()
    assert mock.write('a') is None

# Generated at 2022-06-12 20:06:14.918669
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(WritableStream):
        def write(self, s):
            pass

    class B(A):
        pass

    class C(A):
        def write(self, s):
            pass

    assert issubclass(A, WritableStream)
    assert issubclass(B, WritableStream)
    assert issubclass(C, WritableStream)

# Generated at 2022-06-12 20:06:38.545864
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Foo:
        def write(self):
            pass

    assert not isinstance(Foo(), WritableStream)

    class Bar:
        def write(self, s):
            pass

    assert isinstance(Bar(), WritableStream)



# Generated at 2022-06-12 20:06:41.818413
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MockingObject(object):
        def __init__(self):
            self.writes = []

        def write(self, s):
            self.writes.append(s)

    assert isinstance(MockingObject(), WritableStream)



# Generated at 2022-06-12 20:06:47.391578
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    # subprocess.Popen.stdin is of type `WritableStream`
    # with the `write` method
    assert hasattr(sys.stdout, 'write')
    assert hasattr(sys.stderr, 'write')
    assert hasattr(sys.stdin, 'write')
    assert not hasattr(sys.stdin.buffer, 'write')
    assert hasattr(sys.stdin.buffer, 'write')

# Generated at 2022-06-12 20:06:51.314616
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyFile(object):
        def __init__(self):
            self.s = ''
        def write(self, s):
            self.s += s
    myfile = MyFile()
    myfile.write('1')
    myfile.write(2)
    assert myfile.s == u'12'



# Generated at 2022-06-12 20:06:55.744701
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyFile(WritableStream):
        def __init__(self):
            self.content = ''
        def write(self, s):
            self.content += s
    my_file = MyFile()
    my_file.write('Hello!')
    assert my_file.content == 'Hello!'



# Generated at 2022-06-12 20:07:01.273740
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('abcdef') == 'abcdef'
    assert get_shortish_repr('abcdef', 4) == 'abc...'
    assert get_shortish_repr(1234, 4) == '12...'
    assert get_shortish_repr(1234.567, 4) == '12...'
    assert get_shortish_repr(u'ab\xc3\xadcdef', 4) == u'ab...?...'
    assert get_shortish_repr(u'ab\xc3\xadcdef', 4, normalize=True) == u'ab...?...'
    assert get_shortish_repr(lambda x: x, 4) == '<funct...'

# Generated at 2022-06-12 20:07:10.525290
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream1(WritableStream):
        def write(self, s):
            pass

    class MyWritableStream2(WritableStream):
        def __init__(self):
            self.x = 2

    # assert_is_subclass(MyWritableStream1, WritableStream)
    assert not (MyWritableStream1.__subclasshook__(MyWritableStream1))
    assert not (MyWritableStream1.__subclasshook__(MyWritableStream2))

    assert not (WritableStream.__subclasshook__(MyWritableStream1))
    assert not (WritableStream.__subclasshook__(MyWritableStream2))

# Generated at 2022-06-12 20:07:18.361840
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Good(WritableStream):
        def write(self, s):
            pass
    assert isinstance(Good(), WritableStream)

    class NoWrite(WritableStream):
        pass
    assert not isinstance(NoWrite(), WritableStream)

    class NoMethod(WritableStream):
        def write(self, s, x):
            pass
    assert not isinstance(NoMethod(), WritableStream)

    class Multi(WritableStream):
        def write(self, s):
            pass
        def writeagain(self, s):
            pass
    assert isinstance(Multi(), WritableStream)

    class WrongMethod(WritableStream):
        def somethingelse(self, s):
            pass
    assert not isinstance(WrongMethod(), WritableStream)





# Generated at 2022-06-12 20:07:25.381263
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class X(object):
        def write(self, s):
            pass

    assert issubclass(X, WritableStream)

    class Y(object):
        def write(self, s):
            pass

        def a(self):
            pass

    assert issubclass(Y, WritableStream)

    class Z(object):
        def a(self):
            pass

    assert not issubclass(Z, WritableStream)

# Generated at 2022-06-12 20:07:28.838053
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Mock:
        def write(self, s):
            self.written_stuff = s
    mock = Mock()
    WritableStream.register(Mock)
    assert isinstance(mock, WritableStream)
    assert not isinstance(sys.stdout, WritableStream)

    mock.write('hi!')
    assert mock.written_stuff == 'hi!'

# Generated at 2022-06-12 20:08:15.666440
# Unit test for function get_repr_function
def test_get_repr_function():
    class A: pass
    class B: pass
    class C: pass
    class D: pass
    class E: pass
    a = A()
    b = B()
    c = C()
    d = D()
    e = E()
    assert get_repr_function(a, [(A, 'foo'), (B, 'bar')]) == 'foo'
    assert get_repr_function(b, [(A, 'foo'), (B, 'bar')]) == 'bar'
    assert get_repr_function(c, [(A, 'foo'), (B, 'bar')]) == repr
    assert get_repr_function(d, [(lambda x: isinstance(x, C), 'foo'),
                                 (lambda x: isinstance(x, D), 'bar')]) == 'foo'
    assert get_repr

# Generated at 2022-06-12 20:08:17.462650
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(WritableStream):
        pass
    try:
        a = A()
        assert False
    except TypeError:
        pass

# Generated at 2022-06-12 20:08:22.675239
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(None, ((None, lambda _: '<None>'))) == \
                                                                   '<None>'
    assert get_repr_function(lambda _: _, ((None, lambda _: '<None>'))) == \
                                                                 repr
    assert get_repr_function(1, ((int, lambda _: '<int>'))) == '<int>'
    assert get_repr_function(1.1, ((int, lambda _: '<int>'))) == repr





# Generated at 2022-06-12 20:08:30.645065
# Unit test for function get_repr_function
def test_get_repr_function():
    class X(object): pass
    class Y(X): pass
    class Z(object): pass

    repr_functions = [
        (lambda x: True, lambda x: 'All items'),
        (lambda x: isinstance(x, X), lambda x: 'X or its subclasses'),
        (X, lambda x: 'X itself'),
        (lambda x: isinstance(x, Z), lambda x: 'Z'),
    ]

    assert get_repr_function(None, repr_functions) == repr
    assert get_repr_function(1, repr_functions) == repr
    assert get_repr_function('hi', repr_functions) == repr
    assert get_repr_function(X(), repr_functions) == 'X itself'
    assert get_repr_function(Y(), repr_functions)