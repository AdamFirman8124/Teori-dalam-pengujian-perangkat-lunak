

# Generated at 2022-06-12 19:58:44.631300
# Unit test for function get_repr_function
def test_get_repr_function():
    class A(object): pass
    class B(object): pass
    class C(B): pass
    def repr_a(x):
        assert isinstance(x, A)
        return 'A'
    def repr_b(x):
        assert isinstance(x, B)
        return 'B'
    custom_repr = [(A, repr_a), (B, repr_b)]
    assert get_repr_function(A(), custom_repr) is repr_a
    assert get_repr_function(B(), custom_repr) is repr_b
    assert get_repr_function(C(), custom_repr) is repr_b
    assert get_repr_function(object(), custom_repr) is repr
    assert get_repr_function(None, custom_repr) is repr

# Generated at 2022-06-12 19:58:52.806795
# Unit test for function shitcode
def test_shitcode():
    assert shitcode('') == ''
    assert shitcode('abc') == 'abc'
    assert shitcode('\x00') == '?'
    assert shitcode('\x01') == '?'
    assert shitcode('\x02') == '?'
    assert shitcode('\x03') == '?'
    assert shitcode('\x04') == '?'
    assert shitcode('\x05') == '?'
    assert shitcode('\x06') == '?'
    assert shitcode('\x07') == '?'
    assert shitcode('\x08') == '?'
    assert shitcode('\x09') == '?'
    assert shitcode('\x0a') == '?'
    assert shitcode('\x0b') == '?'
    assert shitcode('\x0c') == '?'

# Generated at 2022-06-12 19:58:55.167800
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class X(WritableStream):
        def write(self, s):
            pass

    assert issubclass(X, WritableStream)

# Generated at 2022-06-12 19:59:03.730629
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('hello world') == "'hello world'"
    assert get_shortish_repr('hello world', max_length=10) == "'hello wo..."
    assert get_shortish_repr('hello world', max_length=10, normalize=True) == "'hello wo..."
    assert get_shortish_repr('hello world', max_length=5, normalize=True) == "'hel..."
    assert get_shortish_repr('hello world', max_length=1, normalize=True) == "'..."
    assert get_shortish_repr('hello\nworld') == "'hello\\nworld'"
    assert get_shortish_repr('hello\r\nworld') == "'hello\\nworld'"
    
    
    
if __name__ == '__main__':
    test_

# Generated at 2022-06-12 19:59:05.165667
# Unit test for function shitcode
def test_shitcode():
    assert shitcode(u'ab') == u'ab'
    assert shitcode(u'\xc9') == u'?'
    assert shitcode(u'ab\xc9') == u'ab?'



# Generated at 2022-06-12 19:59:12.840678
# Unit test for function get_repr_function
def test_get_repr_function():
    class A(object): pass
    class B(A): pass
    class C(A): pass

    assert get_repr_function(1, (
        (lambda x: x == 1, lambda x: x+1),
        (lambda x: x == 2, lambda x: x+2),
        (lambda x: True, lambda x: x),
    ))(1) == 2

    assert get_repr_function(2, (
        (lambda x: x == 1, lambda x: x+1),
        (lambda x: x == 2, lambda x: x+2),
        (lambda x: True, lambda x: x),
    ))(2) == 4


# Generated at 2022-06-12 19:59:24.804290
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(1) == repr(1)
    assert get_shortish_repr(1, max_length=2) == repr(1)
    assert get_shortish_repr(1, max_length=0) == repr(1)
    assert get_shortish_repr(1, max_length=1) == '1'
    assert get_shortish_repr(1, max_length=3) == '1'
    assert get_shortish_repr(1, max_length=4) == '1'
    assert get_shortish_repr(range(10), max_length=10) == 'range(0, 10)'
    assert get_shortish_repr(range(10), max_length=9) == 'range(0, ...'
    assert get_shortish

# Generated at 2022-06-12 19:59:28.156502
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class FakeFakeIOStream(WritableStream):
        def write(self, s):
            assert isinstance(s, str)

    FakeFakeIOStream().write('hi')



# Generated at 2022-06-12 19:59:35.255265
# Unit test for function get_repr_function
def test_get_repr_function():
    from types import GeneratorType, FunctionType
    custom_repr = [
        (GeneratorType, lambda x: 'generator'),
        (FunctionType, lambda x: 'function')
    ]

    def f(x): pass
    def g(): yield
    generator = g()

    assert get_repr_function(f, custom_repr) == str
    assert get_repr_function(g, custom_repr) == str

# Generated at 2022-06-12 19:59:39.094296
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class WritableStreamSubclass(WritableStream):
        def __init__(self):
            self.contents = ''
        def write(self, s):
            self.contents += s

    w = WritableStreamSubclass()
    w.write('hai')
    assert w.contents == 'hai'



# Generated at 2022-06-12 19:59:52.596769
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function('hello', custom_repr=((lambda x: True,
                                                    lambda x: 'world'),)) == (
        lambda x: 'world')
    assert get_repr_function('hello', custom_repr=((lambda x: False,
                                                    lambda x: 'world'),)) == repr
    assert get_repr_function(1, custom_repr=((lambda x: False,
                                              lambda x: 'world'),)) == repr
    assert get_repr_function(Exception,
                             custom_repr=((lambda x: False,
                                           lambda x: 'world'),)) == repr

# Generated at 2022-06-12 19:59:55.169551
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def write(self, s):
            pass
    assert issubclass(MyWritableStream, WritableStream)



# Generated at 2022-06-12 20:00:01.426674
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, []) is repr
    assert get_repr_function(1, [(lambda x: False, lambda: 2)]) is repr
    assert get_repr_function(1, [(lambda x: True, lambda: 2)])() == 2
    assert get_repr_function(1, [(lambda x: x == 1, lambda: 2)])() == 2
    assert get_repr_function(1, [(lambda x: x == 2, lambda: 2)]) is repr
    assert get_repr_function(1, [(int, lambda x: 1+2)])() == 3
    assert get_repr_function('', [(int, lambda x: 1+2)]) is repr



# Generated at 2022-06-12 20:00:06.767408
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class X:
        def __init__(self, string):
            self.string = string
        def write(self, s):
            self.string += s
    x = X('x')
    assert isinstance(x, WritableStream)
    x.write('y')
    assert x.string == 'xy'
    assert not isinstance(None, WritableStream)

test_WritableStream_write()

# Generated at 2022-06-12 20:00:12.091724
# Unit test for function shitcode
def test_shitcode():
    def test_item(original, expected):
        assert ''.join(
            (c if (0 < ord(c) < 256) else '?') for c in original
        ) == expected

    test_item(u'foo', u'foo')
    test_item(u'\u123cd', u'??cd')

# Generated at 2022-06-12 20:00:20.855722
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    class MyObject(object):
        __repr__ = lambda self: 'MyRepr'
        __str__ = lambda self: 'MyString'

    my_object = MyObject()
    assert get_shortish_repr(my_object) == 'MyRepr'
    assert get_shortish_repr(my_object, normalize=True) == 'MyRepr'
    assert get_shortish_repr(my_object, max_length=2) == 'My'
    assert get_shortish_repr(my_object, max_length=2, normalize=True) == 'My'

    assert get_shortish_repr(str, max_length=2) == 'st'
    assert get_shortish_repr(str, max_length=2, normalize=True) == 'st'

   

# Generated at 2022-06-12 20:00:25.723429
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class Example(WritableStream):
        def __init__(self):
            self.text_buffer = ''
        def write(self, text):
            self.text_buffer += text

    example = Example()
    example.write('text')
    assert example.text_buffer == 'text'


# Generated at 2022-06-12 20:00:26.682063
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    """t.b.c."""



# Generated at 2022-06-12 20:00:35.914781
# Unit test for function get_repr_function
def test_get_repr_function():
    class A(object):
        pass

    class B(A):
        pass

    assert get_repr_function(5, (
        (lambda x: isinstance(x, int), lambda x: 'INTEGER!')
    )) == str
    assert get_repr_function(5, (
        (lambda x: isinstance(x, int), lambda x: 'INTEGER!')
    ))('x') == 'x'
    assert get_repr_function(5, (
        (lambda x: isinstance(x, int), lambda x: 'INTEGER!'),
        (lambda x: isinstance(x, str), lambda x: 'STRING!')
    ))('x') == 'x'

# Generated at 2022-06-12 20:00:44.709189
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Thingy: pass
    assert not issubclass(Thingy, WritableStream)
    class Thingy(Thingy, WritableStream): pass
    assert issubclass(Thingy, WritableStream)
    class Thingy2(WritableStream): pass
    assert issubclass(Thingy2, WritableStream)
    class Thingy3(Thingy2): pass
    assert issubclass(Thingy3, WritableStream)
    class Thingy4(Thingy3): pass
    assert issubclass(Thingy4, WritableStream)


# Generated at 2022-06-12 20:00:58.655722
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(None) == repr
    assert get_repr_function(5) == repr
    assert get_repr_function('a') == repr
    assert get_repr_function(()) == repr
    assert get_repr_function(sys) == repr
    assert get_repr_function(
        5,
        custom_repr=[(lambda i: True, lambda i: 'hello')],
    ) == 'hello'
    assert get_repr_function(
        'a',
        custom_repr=[(lambda i: True, lambda i: 'hello')],
    ) == 'hello'
    assert get_repr_function(
        None,
        custom_repr=[(lambda i: True, lambda i: 'hello')],
    ) == 'hello'
    assert get_repr

# Generated at 2022-06-12 20:01:02.658535
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    b = bytearray(b'12345678')
    class X(WritableStream):

        def write(self, s):
            b[:] = s[:]

    x = X()
    x.write(b'ABCDEF')
    assert b == b'ABCDEF'





# Generated at 2022-06-12 20:01:10.449458
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def __init__(self):
            self.internal_string = ''
        def write(self, s):
            self.internal_string += s

    my_writable_stream = MyWritableStream()
    assert isinstance(my_writable_stream, WritableStream)
    assert my_writable_stream.internal_string == ''
    my_writable_stream.write('xo')
    assert my_writable_stream.internal_string == 'xo'
    my_writable_stream.write('xo')
    assert my_writable_stream.internal_string == 'xoxo'
    my_writable_stream.write('xo')
    assert my_writable_stream.internal_string == 'xoxoxo'



# Generated at 2022-06-12 20:01:14.691834
# Unit test for function shitcode
def test_shitcode():
    assert shitcode('abc') == 'abc'
    assert shitcode('a\x00b') == 'a?b'
    assert shitcode('a\x00b\x00c') == 'a?b?c'

# Generated at 2022-06-12 20:01:15.911335
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(WritableStream):
        def write(self, s):
            pass

    A()

# Generated at 2022-06-12 20:01:23.396134
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('12345678') == '12345678'
    assert get_shortish_repr('12345678', max_length=6) == '12...78'
    assert get_shortish_repr('12345678', max_length=6, normalize=True) == '12...78'
    assert get_shortish_repr('12345678', normalize=True) == '12345678'
    assert get_shortish_repr('12345678', max_length=11, normalize=True) == '12345678'

    assert get_shortish_repr((1, 2, 3, 4, 5, 6, 7, 8)) == '(1, 2, 3, 4, 5, 6, 7, 8)'

# Generated at 2022-06-12 20:01:27.104340
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def write(self, s):
            assert isinstance(s, str)

    MyWritableStream().write('foo')



if __name__ == '__main__':
    import pytest

    pytest.main()


# Generated at 2022-06-12 20:01:29.611060
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(WritableStream):
        def write(self, s):
            assert s == 'hello'

    a = A()
    a.write('hello')

# Generated at 2022-06-12 20:01:32.579583
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class MyWritableStream(WritableStream):
        def __init__(self):
            self.written = ''

        def write(self, s):
            self.written += s

    s = MyWritableStream()
    s.write('a')
    assert s.written == 'a'

# Generated at 2022-06-12 20:01:43.207876
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(1) == '1'
    assert get_shortish_repr(3, max_length=2) == '3'
    assert get_shortish_repr('123456789', max_length=10) == '123456789'
    assert get_shortish_repr('123456789', max_length=9) == '12345...9'
    assert get_shortish_repr('123456789', max_length=7) == '12...89'
    assert get_shortish_repr('123456789', max_length=3) == '12...'
    assert get_shortish_repr('123456789', max_length=2) == '1...'

# Generated at 2022-06-12 20:01:55.878608
# Unit test for function get_repr_function
def test_get_repr_function():

    def check(item, custom_repr, expected_repr):
        actual_repr = get_repr_function(item, custom_repr)
        assert actual_repr == expected_repr

    # Test for function:
    class O(object):
        def __repr__(self):
            return 'repr1'

    def f(x):
        return 'repr2'

    class A:
        pass

    class B(A):
        pass

    class C:
        pass

    class D(C):
        pass


# Generated at 2022-06-12 20:02:04.298273
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    from .stream import Stream
    from .pretty_printer import PrettyPrinter
    import io
    s = Stream()
    p = PrettyPrinter(output=s)
    p.print_('abc')
    assert s.read() == 'abc'
    try:
        unicode
    except NameError:
        pass
    else:
        s = Stream()
        p = PrettyPrinter(output=s)
        p.print_(u'abc')
        assert s.read() == u'abc'

    s = Stream()
    p = PrettyPrinter(output=s)
    p.print_(int(1))
    assert s.read() == '1'
    s.clear()
    p.print_(1)
    assert s.read() == '1'
    s.clear()

# Generated at 2022-06-12 20:02:12.056636
# Unit test for function get_repr_function
def test_get_repr_function():

    class Apple: pass
    class Pear: pass

    def my_repr(x):
        return 'my repr of {}'.format(x)

    def other_repr(x):
        return 'other repr of {}'.format(x)

    custom_repr = [
        (lambda x: isinstance(x, Apple), my_repr),
        (Pear, other_repr)
    ]

    class Banana: pass

    apple = Apple()
    pear = Pear()
    banana = Banana()

    assert get_repr_function(apple, custom_repr) is my_repr
    assert get_repr_function(pear, custom_repr) is other_repr
    assert get_repr_function(banana, custom_repr) is repr



# Generated at 2022-06-12 20:02:18.800896
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, ()) == repr
    assert get_repr_function(1, custom_repr=((int, str),)) == str
    assert get_repr_function(1.0, custom_repr=((int, str),)) == repr
    assert get_repr_function(lambda x: x, custom_repr=((int, str),)) == repr
    assert get_repr_function(lambda x: x,
                             custom_repr=((lambda x: True, str),)) == str
    assert get_repr_function(lambda x: x,
                             custom_repr=((lambda x: False, str),)) == repr



# Generated at 2022-06-12 20:02:22.222065
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(3, ((int, lambda x: x * 3),)) == 3 * 3
    assert get_repr_function(3.0, ((int, lambda x: x * 3),)) == 3.0

# Generated at 2022-06-12 20:02:31.253427
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    class C:
        def __repr__(self):
            return 'C'
    assert get_shortish_repr('abc') == repr('abc')
    assert get_shortish_repr(b'abc') == repr('abc')
    assert get_shortish_repr(5) == repr(5)
    assert get_shortish_repr(C()) == repr('C')
    custom_repr = ((int, lambda n: 'n'),)
    assert get_shortish_repr(5, custom_repr=custom_repr) == 'n'
    assert get_shortish_repr('abc', max_length=3) == 'abc'
    assert get_shortish_repr('abcde', max_length=3) == 'ab...e'

# Generated at 2022-06-12 20:02:41.688390
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    class X(object):
        def __repr__(self):
            return 'this should be a short repr'
    assert get_shortish_repr(X()) == 'this should be a short repr'
    assert get_shortish_repr(X(), custom_repr=((X, lambda x: 'Y'),)) == 'Y'
    assert get_shortish_repr(X(), max_length=7) == 'this sh...'
    assert get_shortish_repr(X(), max_length=12) == 'this shou...'
    assert get_shortish_repr(X(), max_length=13) == 'this should...'
    assert get_shortish_repr(X(), max_length=14) == 'this should ...'

# Generated at 2022-06-12 20:02:48.641995
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    def assert_equal(item, result):
        assert get_shortish_repr(item) == result

    class A:
        def __repr__(self):
            return 'repr of A'

        def custom_repr(self):
            return 'custom repr of A'

    class B:
        def __repr__(self):
            return 'repr of B'

        def custom_repr(self):
            return 'custom repr of B'

    assert_equal('hello', "'hello'")
    assert_equal(123, '123')

# Generated at 2022-06-12 20:02:57.709856
# Unit test for function get_repr_function
def test_get_repr_function():
    class A:
        pass
    class B:
        pass
    class C:
        pass

    def repr_func_a(x):
        return 'i am using repr_func_a'
    def repr_func_b(x):
        return 'i am using repr_func_b'
    def repr_func_c(x):
        return 'i am using repr_func_c'

    custom_repr = (
        (lambda x: isinstance(x, A), repr_func_a),
        (lambda x: isinstance(x, B), repr_func_b),
        (C, repr_func_c),
    )
    assert get_repr_function(A(), custom_repr) is repr_func_a
    assert get_repr_function(B(), custom_repr) is repr_func

# Generated at 2022-06-12 20:03:01.093618
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class C:
        pass
    assert not issubclass(C, WritableStream)
    class C:
        def write(self, s):
            pass
    assert issubclass(C, WritableStream)

# Generated at 2022-06-12 20:03:14.439697
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(0, [(int, str)]) is str
    assert get_repr_function(0.0, [(int, str)]) is repr
    assert get_repr_function(0.0, [(int, str), (float, str)]) is str
    assert get_repr_function(0.0, [(None, str), (float, str)]) is str
    assert get_repr_function(0.0, [(float, str), (None, str)]) is str
    assert get_repr_function(0.0, [(float, str), (0.0, str)]) is str

# Generated at 2022-06-12 20:03:24.242151
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('hello') == "'hello'"
    assert get_shortish_repr(5) == '5'
    assert get_shortish_repr(5.2) == '5.2'
    assert get_shortish_repr(5.2+3j) == '5.2+3j'
    assert get_shortish_repr([1, 2, 3]) == '[1, 2, 3]'
    assert get_shortish_repr(('hello', 5)) == "('hello', 5)"
    assert get_shortish_repr({'a': 5, 'b': 7}) == "{'b': 7, 'a': 5}"

# Generated at 2022-06-12 20:03:33.259149
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function('a', custom_repr=(
        (str, lambda x: '<str>'),
        (int, lambda x: '<int>'),
    )) == repr

# Generated at 2022-06-12 20:03:37.399997
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def write(self, s): pass

    assert issubclass(MyWritableStream, WritableStream)
    my_writable_stream = MyWritableStream()
    assert isinstance(my_writable_stream, WritableStream)
    assert isinstance(my_writable_stream, MyWritableStream)

# Generated at 2022-06-12 20:03:47.695166
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    from .test_python_toolbox import ensure_except
    custom_repr=(
        (lambda x: isinstance(x, set), lambda x: str(x)),
        (set, lambda x: str(x)),
        (int, lambda x: str(x)),
        (lambda x: isinstance(x, str), lambda x: x + ' bar'),
    )
    assert get_shortish_repr(1, custom_repr) == '1'
    assert get_shortish_repr(1, custom_repr, 10) == '1'
    assert get_shortish_repr(1, custom_repr, 5) == '1...'
    assert get_shortish_repr({1, 2}, custom_repr) == "{1, 2}"

# Generated at 2022-06-12 20:03:57.136217
# Unit test for function get_repr_function
def test_get_repr_function():
    from .testing import frozen_dict
    from .testing import assert_equal
    from .testing import assert_not_equal

    custom_repr = (
        (lambda x: x == 'bla', lambda x: 'bla!'),
        (lambda x: x == 'bla2', lambda x: 'bla2!'),
        (lambda x: x == 'bla3', lambda x: 'bla3!'),
        (lambda x: x == 'bla4', lambda x: 'bla4!'),
        (lambda x: x == 'bla5', lambda x: 'bla5!'),
    )

    assert_equal(get_repr_function('bla', custom_repr), lambda x: 'bla!')

# Generated at 2022-06-12 20:04:00.161565
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, (('a', 'b'))) == repr
    assert get_repr_function('a', (('a', 'b'))) == 'b'


# Todo: Test shitcode, truncate, and ensure_tuple

# Generated at 2022-06-12 20:04:02.777396
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MySubclass(WritableStream):
        def write(self, s):
            pass

    assert issubclass(MySubclass, WritableStream)



# Generated at 2022-06-12 20:04:06.297159
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    # Implementation for class MockBytesIOWriter
    class MockBytesIOWriter(WritableStream):
        def __init__(self):
            self.written_text = ''
        def write(self, s):
            self.written_text += s

    mock_bytes_io_writer = MockBytesIOWriter()
    mock_bytes_io_writer.write('Hello world')
    mock_bytes_io_writer.write('!')
    assert mock_bytes_io_writer.written_text == 'Hello world!'

# Generated at 2022-06-12 20:04:17.124708
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(3, [(int, 'b')]) == 'b'
    assert get_repr_function(3.5, [(int, 'b')]) != 'b'
    assert get_repr_function(3.5, [(int, 'b')]) == repr
    assert get_repr_function(3, [(lambda x: x > 3, 'b')]) != 'b'
    assert get_repr_function(4, [(lambda x: x > 3, 'b')]) == 'b'
    assert get_repr_function(3.5, [(lambda x: x > 3, 'b')]) == repr
    assert get_repr_function(3.5, [(lambda x: x > 3, 'b'), (float, 'a')]) == 'a'
    assert get_repr_function

# Generated at 2022-06-12 20:04:24.654659
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def write(self, s):
            pass
    assert issubclass(MyWritableStream, WritableStream)


# Unit tests for method __subclasshook__ of class WritableStream

# Generated at 2022-06-12 20:04:33.146673
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(set([1, 2, 3])) == "set([1, 2, 3])"
    assert get_shortish_repr([1, 2, 3]) == "[1, 2, 3]"
    assert get_shortish_repr((1, 2, 3)) == "(1, 2, 3)"
    assert get_shortish_repr({1, 2, 3}) == "{1, 2, 3}"
    assert get_shortish_repr(set([1, 2, 3]), max_length=9) == "set([1,...)"
    assert get_shortish_repr(set([1, 2, 3]), max_length=10) == "set([1, 2,...)"

# Generated at 2022-06-12 20:04:43.821691
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('') == u'""'
    assert get_shortish_repr('a') == u'"a"'
    assert get_shortish_repr('b') == u'"b"'
    assert get_shortish_repr('ba') == u'"ba"'
    assert get_shortish_repr('c') == u'"c"'
    assert get_shortish_repr('ca') == u'"ca"'
    assert get_shortish_repr('cat') == u'"cat"'
    assert get_shortish_repr('cat', max_length=3) == u'"..."'
    assert get_shortish_repr('cat', max_length=2) == u'"c..."'
    assert get_shortish_repr('cat', max_length=1) == u'"...'


# Generated at 2022-06-12 20:04:53.326409
# Unit test for function get_shortish_repr
def test_get_shortish_repr():

    class Thing(object):
        def __init__(self, name):
            self.name = name
        def __repr__(self):
            return 'Thing({})'.format(self.name)

    class SpecialThing(Thing):
        pass

    assert get_shortish_repr('abc', normalize=False) == 'abc'
    assert get_shortish_repr('abc', normalize=True) == 'abc'

    assert get_shortish_repr('abc', max_length=10, normalize=False) == 'abc'
    assert get_shortish_repr('abc', max_length=10, normalize=True) == 'abc'

    assert get_shortish_repr('abc', max_length=5, normalize=False) == 'abc'
    assert get_shortish_re

# Generated at 2022-06-12 20:04:58.231708
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class WritableStreamSubclass(WritableStream):
        def write(self, s):
            pass

    test_stream = WritableStreamSubclass()
    assert isinstance(test_stream, WritableStream)
    assert isinstance(test_stream, WritableStreamSubclass)


test_WritableStream_write()



# Generated at 2022-06-12 20:05:07.179995
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(b'hello world') == 'b\'hello world\''
    assert get_shortish_repr(1) == '1'
    assert get_shortish_repr(1.0) == '1.0'
    long_string = '*' * 100
    assert (get_shortish_repr(long_string, max_length=15) ==
            '***********...***********')
    assert (get_shortish_repr(long_string, max_length=20) ==
            '***********...***********')
    assert (get_shortish_repr(long_string, max_length=21) ==
            '***********************')

# Generated at 2022-06-12 20:05:17.391722
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('abc') == "'abc'"
    assert get_shortish_repr('abc', max_length=1) == "'a'"
    assert get_shortish_repr(3) == '3'
    assert get_shortish_repr(3, max_length=2) == '3'
    assert get_shortish_repr(3, max_length=1) == '3'

# Generated at 2022-06-12 20:05:29.481877
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, [(int, repr)]) == repr
    assert get_repr_function(1.0, [(int, repr)]) == repr
    assert get_repr_function('1', [(int, repr)]) == repr
    assert get_repr_function(1.0, [(int, None)]) == repr
    assert get_repr_function('1', [(int, None)]) == repr
    assert get_repr_function(1, [(lambda x: True, None)]) == None
    assert get_repr_function(1, [(lambda x: False, None)]) == repr
    assert get_repr_function(1, [(lambda x: False, None),
                                 (lambda x: True, object)]) == object





# Generated at 2022-06-12 20:05:40.149279
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    import sys
    import contextlib
    class WritableStreamSubclass(WritableStream):
        def write(self, s):
            pass
    assert issubclass(WritableStreamSubclass, WritableStream)

    class NotWritableStreamSubclass(object):
        def write(self, s):
            pass
    assert not issubclass(NotWritableStreamSubclass, WritableStream)

    assert issubclass(type(""), WritableStream)

    assert issubclass(io.StringIO, WritableStream)
    assert issubclass(type(sys.stdout), WritableStream)

    with open('temp.txt', 'w'):
        assert issubclass(type(open('temp.txt')), WritableStream)



# Generated at 2022-06-12 20:05:45.548334
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr([{1: 2, 5: 6}, (5, 7)], normalize=True) \
           == "[{...}, (...)]"
    assert get_shortish_repr(((1, 2, 3), (4, 5, 6))) == "((1, 2, 3), (4, 5, 6))"
    assert get_shortish_repr(((1, 2, 3), (4, 5, 6)), max_length=20) \
           == "((1, 2, 3), (4, ...))"



# Generated at 2022-06-12 20:06:05.433428
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class C(object):
        pass
    class D(C, WritableStream):
        def write(self, s):
            pass
    assert issubclass(D, WritableStream)

    class E(object):
        def write(self, s):
            pass
    assert issubclass(E, WritableStream)

    class F(object):
        pass
    assert not issubclass(F, WritableStream)



# Generated at 2022-06-12 20:06:10.949088
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert (get_shortish_repr(123, max_length=10) == '123')
    assert (get_shortish_repr('abcd efgh ijkl', max_length=10) == 'abcd efgh...')
    assert (get_shortish_repr('abcd efgh ijkl', max_length=None) == 'abcd efgh ijkl')
    assert (get_shortish_repr('abcd efgh ijkl', max_length=0) == '')



# Generated at 2022-06-12 20:06:18.388465
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class OldSkool:
        def write(self, s):
            pass

    assert issubclass(OldSkool, WritableStream)
    assert isinstance(OldSkool(), WritableStream)
    assert isinstance(sys.stderr, WritableStream)

    class NoWrite:
        pass

    assert not issubclass(NoWrite, WritableStream)
    assert not isinstance(NoWrite(), WritableStream)

    class WithWritable:
        write = 'lalalala'

    assert not issubclass(WithWritable, WritableStream)
    assert not isinstance(WithWritable(), WritableStream)

    class WithNope:
        write = None

    assert not issubclass(WithNope, WritableStream)
    assert not isinstance(WithNope(), WritableStream)


# Generated at 2022-06-12 20:06:26.156985
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, custom_repr=()) is repr

    assert get_repr_function(
        1,
        custom_repr=[(lambda x: x == 1, lambda x: 'one'),
                     (lambda x: x == 2, lambda x: 'two')]
    ) is repr

    assert get_repr_function(
        1,
        custom_repr=[(lambda x: x == 2, lambda x: 'two'),
                     (lambda x: x == 1, lambda x: 'one')]
    ) == 'one'

    assert get_repr_function(
        3,
        custom_repr=[(int, lambda x: 'an integer: %s' % x),
                     (lambda x: x == 2, lambda x: 'two')]
    ) == 'an integer: 3'

# Generated at 2022-06-12 20:06:30.165827
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    from io import BytesIO
    from io import StringIO
    assert issubclass(BytesIO, WritableStream)
    assert issubclass(StringIO, WritableStream)
    class X:
        def write(self, s):
            self.s = s
    assert issubclass(X, WritableStream)
    with pytest.raises(TypeError):
        class Y:
            pass
        issubclass(Y, WritableStream)



# Generated at 2022-06-12 20:06:33.859544
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    from .temp_file_tools import make_temp_file

    def write(s):
        temp_file.write(s)
        temp_file.write(s.encode('utf-8'))

    with make_temp_file() as temp_file:
        WritableStream.register(type('WritableStreamSubclass',
                                     (object,),
                                     {'write': write}))
        assert issubclass(WritableStreamSubclass, WritableStream)



# Generated at 2022-06-12 20:06:41.779968
# Unit test for function get_repr_function
def test_get_repr_function():
    custom_repr = ((int, str), (id, 'id(' + str(id(0)) + ')'.upper()))
    assert get_repr_function(0, custom_repr) == str
    assert get_repr_function(1, custom_repr) == repr
    assert get_repr_function((), custom_repr) == repr
    assert get_repr_function(0, ()) == repr

    assert get_repr_function(0, custom_repr) == str
    assert get_repr_function(1, custom_repr) == repr



# Generated at 2022-06-12 20:06:46.469656
# Unit test for function get_repr_function
def test_get_repr_function():
    if sys.version_info >= (3, 0):
        rev = reversed
    else:
        def rev(it):
            r = list(it)
            r.reverse()
            return iter(r)

    assert get_repr_function(
        [],
        custom_repr=(
            (list, str),
            (tuple, str),
            (type(None), str),
            (str, int),
            (str, str),
            (str, lambda l: 'b' + ''.join(rev(l)) + 'a'),
        )
    )('shit') == 'a'.join(reversed('shit'))

# Generated at 2022-06-12 20:06:48.526304
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class X:
        def write(self, s):
            print('hi')

    assert issubclass(X, WritableStream)

# Generated at 2022-06-12 20:06:52.132653
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class FakeFile(WritableStream):
        def __init__(self):
            self.lines = []

        def write(self, s):
            self.lines.append(s)

    fake_file = FakeFile()
    fake_file.write('hello')
    assert fake_file.lines == ['hello']



# Generated at 2022-06-12 20:07:19.875548
# Unit test for function get_repr_function
def test_get_repr_function():
    from .abc import ABC
    from .enum import enum
    from .ordered_dict import OrderedDict

    class Foo(object): pass
    class Bar(object): pass
    class FooBar(Foo, Bar): pass
    class Baz(object): pass

    x = Foo()
    y = Bar()
    z = Baz()
    xyz = FooBar()
    o = object()

    def foo_repr(x):
        return 'foo!'

    def baz_repr(x):
        return 'baz!'

    assert get_repr_function(x, ((Foo, foo_repr), (Baz, baz_repr))) == foo_repr
    assert get_repr_function(y, ((Foo, foo_repr), (Baz, baz_repr))) == repr

# Generated at 2022-06-12 20:07:24.789404
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        pass

    class MyFakeWritableStream:
        pass

    assert issubclass(MyWritableStream, WritableStream)
    assert not issubclass(MyFakeWritableStream, WritableStream)
    assert issubclass(MyWritableStream, WritableStream)

    # todo



# Generated at 2022-06-12 20:07:31.058124
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def __init__(self):
            self._buffer = b''
        def write(self, s):
            self._buffer += s

    w = MyWritableStream()
    w.write(b'hello')
    assert w._buffer == b'hello'
    w.write(b' abcd')
    assert w._buffer == b'hello abcd'
    w.write(b'\x01\x02\x03')
    assert w._buffer == b'hello abcd\x01\x02\x03'
    assert issubclass(MyWritableStream, WritableStream)
    assert isinstance(w, WritableStream)
    print('Passed.')



# Generated at 2022-06-12 20:07:40.273015
# Unit test for function get_repr_function
def test_get_repr_function():

    assert get_repr_function(1, custom_repr=((int, lambda x: x + 1),)) == \
                                                             get_repr_function
    assert get_repr_function(1, custom_repr=((int,
                                              lambda x: x + 1),
                                             (float,
                                              lambda x: x + 1),)) == \
                                                             get_repr_function
    assert get_repr_function(1.0, custom_repr=((int, lambda x: x + 1),
                                               (float, lambda x: x + 1),)) == \
                                                             get_repr_function

# Generated at 2022-06-12 20:07:50.687828
# Unit test for function shitcode
def test_shitcode():
    assert shitcode('\x01\x02\x03') == '\x01\x02\x03'
    assert shitcode('\x01\x02\xff') == '\x01\x02?'
    assert shitcode('\x01\x02\xffff') == '\x01\x02??'
    assert shitcode('\x01\x02\u0fff') == '\x01\x02?'
    assert shitcode('abc\!') == 'abc!'
    assert shitcode('\u00eb') == '?'
    assert shitcode('\u00eb\x01\n') == '?\x01\n'
    assert shitcode('\u00eb\x01\n\u00da') == '?\x01\n?'

# Generated at 2022-06-12 20:07:52.553645
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Foo(WritableStream):
        def write(self, s):
            pass
    assert issubclass(Foo, WritableStream)

# Generated at 2022-06-12 20:07:58.681630
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function("hello", ((str, str), (int, int))) == str
    assert get_repr_function(1, ((str, str), (int, int))) == int
    assert get_repr_function("nope", ((str, str), (int, int))) == repr
    assert get_repr_function(1, ((str, str), (int, float))) == int



# Generated at 2022-06-12 20:08:02.424015
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(WritableStream):
        def __init__(self):
            self.output = ''
        def write(self, s):
            self.output += s

    stream = MyWritableStream()
    stream.write('hello')
    assert stream.output == 'hello'



# Generated at 2022-06-12 20:08:10.673484
# Unit test for function get_repr_function
def test_get_repr_function():
    import pytest
    assert get_repr_function(123, ()) == repr
    assert get_repr_function(123, (('a', 'b'))) == repr
    assert get_repr_function(123, ((lambda x: x == 123, 'hello'))) == 'hello'
    assert get_repr_function(123, ((lambda x: x == 12, 'hello'))) == repr
    assert get_repr_function('a', ((str, 'hello'))) == 'hello'
    assert get_repr_function('a', ((str, 'hello'), (str, 'bye'))) == 'hello'
    assert get_repr_function('b', ((str, 'hello'), (str, 'bye'))) == 'bye'

# Generated at 2022-06-12 20:08:14.882143
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    from .console_io import ConsoleWriter, FileWriter
    from .capturing import CapturingStreamWriter

    for writer_cls in (CapturingStreamWriter, ConsoleWriter, FileWriter):
        writer = writer_cls()
        assert isinstance(writer, WritableStream)
        writer.write('spam')