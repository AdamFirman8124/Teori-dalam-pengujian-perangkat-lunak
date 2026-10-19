

# Generated at 2022-06-12 19:58:46.070568
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream:
        def write(self, s): pass
    assert issubclass(MyWritableStream, WritableStream)
    assert not issubclass(MyWritableStream, WritableStream)

# Generated at 2022-06-12 19:58:50.522860
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, []) == repr
    assert get_repr_function('hi', []) == repr
    assert get_repr_function(1, [(str, lambda x: 'a_string')]) == repr
    assert get_repr_function('hi', [(str, lambda x: 'a_string')]) == (
        lambda x: 'a_string')



# Generated at 2022-06-12 19:58:55.942156
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(int, ((lambda x: x != 1, lambda x: x))) == int
    assert get_repr_function(1, ((lambda x: x != 1, lambda x: x))) == 1
    assert get_repr_function(1, ((lambda x: x != 1, 12))) == 12
    assert get_repr_function(1, ((lambda x: True, 12))) == 12
    assert get_repr_function(1, ((lambda x: False, 12))) == repr
    assert get_repr_function(1, ((lambda x: False, 12), (lambda x: True, 13))) \
                                                                          == 13
    assert get_repr_function(1, ((2, 3), (lambda x: True, 13))) == 13

# Generated at 2022-06-12 19:59:01.951467
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class MyWritableStream(WritableStream):

        def __init__(self):
            self.memory = ''

        def write(self, s):
            self.memory += s

    stream = MyWritableStream()
    assert isinstance(stream, WritableStream) is True
    stream.write('hello')
    assert stream.memory == 'hello'
    stream.write(' ')
    assert stream.memory == 'hello '
    stream.write('world')
    assert stream.memory == 'hello world'



# Generated at 2022-06-12 19:59:11.881146
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(lambda x: x) == '<function <lambda> at 0x...>'
    assert get_shortish_repr(lambda x: x, (lambda x: True, lambda x: '123')) == '123'
    assert get_shortish_repr(lambda x: x, (lambda x: False, lambda x: '123')) == '<function <lambda> at 0x...>'
    assert get_shortish_repr(lambda x: x, max_length=10) == '<function <lambda> at 0x...>'
    assert get_shortish_repr(lambda x: x, max_length=8) == '<functi...>'
    assert get_shortish_repr(lambda x: x, max_length=4) == '<fu...>'


# Generated at 2022-06-12 19:59:21.493455
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr({1, 2, 3}, max_length=3) == '{1,...}'
    assert get_shortish_repr((1, 2, 3), max_length=100) == '(1, 2, 3)'

# Generated at 2022-06-12 19:59:25.426154
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(None, ()) is repr
    assert get_repr_function(0, ()) is repr
    assert get_repr_function(None, ((type(None), str),)) is str
    assert get_repr_function(0, ((type(None), str),)) is repr



# Generated at 2022-06-12 19:59:35.574849
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function('foo', custom_repr=((str, str),)) is str
    assert get_repr_function('foo', custom_repr=((int, str),)) is repr
    assert get_repr_function('foo', custom_repr=((lambda x: 1, str),)) is repr
    assert get_repr_function('foo', custom_repr=(('a', str),
                                                 (int, str),)) is str
    assert get_repr_function('foo', custom_repr=((lambda x: 1, str),
                                                 (int, str),)) is str
    assert get_repr_function('foo', custom_repr=((lambda x: False, str),)) \
                                                                     is repr

# Generated at 2022-06-12 19:59:43.565383
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(None, ()) == repr
    assert get_repr_function(1, ()) == repr
    assert get_repr_function('', ()) == repr

    assert get_repr_function(None, ((lambda x: x is None, str))) == str
    assert get_repr_function(1, ((lambda x: x is None, str))) == repr
    assert get_repr_function('', ((lambda x: x is None, str))) == repr

    assert get_repr_function(None, ((type(None), str))) == str
    assert get_repr_function(1, ((type(None), str))) == repr
    assert get_repr_function('', ((type(None), str))) == repr


# Generated at 2022-06-12 19:59:49.958416
# Unit test for function get_repr_function
def test_get_repr_function():
    def _test(item, expected_repr_function,
              custom_repr=((int, str), (lambda x: x > 0, repr))):
        repr_function = get_repr_function(item, custom_repr)
        assert repr_function is expected_repr_function
    _test(0, str)
    _test(1, repr)
    _test(-1, None)

# Generated at 2022-06-12 20:00:01.154763
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function([1, 2, 3], custom_repr=(
            (lambda x: isinstance(x, list), lambda x: '[1, 2, 3]'),
    )) == '[1, 2, 3]'

# Generated at 2022-06-12 20:00:08.410305
# Unit test for function shitcode
def test_shitcode():
    assert shitcode('abcde12345') == 'abcde12345'
    assert shitcode('aЬцФгшхийклмнопq') == 'a?ц?г????клмнопq'
    assert shitcode('hello world!') == 'hello world!'
    assert shitcode(r'C:\Program Files\Microsoft Corporation\Microsoft Office\Office14') == 'C:\\Program Files\\Microsoft Corporation\\Microsoft Office\\Office14'
    assert shitcode('\r\n') == '\r\n'



# Generated at 2022-06-12 20:00:13.618976
# Unit test for function get_repr_function
def test_get_repr_function():
    from .string_concatenation import StringConcatenation

    assert get_repr_function(StringConcatenation(),
                             custom_repr=((StringConcatenation, str),)) == str


__all__ = [
    'WritableStream',
    'file_reading_errors',
    'shitcode',
    'get_repr_function',
    'normalize_repr',
    'get_shortish_repr',
    'truncate',
    'ensure_tuple',
    'test_get_repr_function',
]

# Generated at 2022-06-12 20:00:15.668612
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class T(WritableStream):
        def __init__(self):
            self.text = ''
        def write(self, s):
            self.text += s

    t = T()
    t.write('spam')
    assert t.text == 'spam'

# Generated at 2022-06-12 20:00:18.767473
# Unit test for function shitcode
def test_shitcode():
    assert shitcode('a') == 'a'
    assert shitcode('a' * 256) == 'a' * 256
    assert shitcode(bytearray.fromhex('ce')) == '?'
    assert shitcode(u'a\U0001f604') == 'a'

# Generated at 2022-06-12 20:00:30.310548
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr("foo", max_length=33) == "foo"
    assert get_shortish_repr("foobar", max_length=3) == "foo..."
    assert get_shortish_repr("foobar", max_length=4) == "foo..."
    assert get_shortish_repr("foobar", max_length=None) == "foobar"
    assert get_shortish_repr("foobar", max_length=6) == "foobar"
    assert get_shortish_repr("foobar", max_length=7) == "foobar"
    assert get_shortish_repr("foobar", max_length=8) == "foobar"
    assert get_shortish_repr("foobar", max_length=9) == "foobar"
    assert get

# Generated at 2022-06-12 20:00:38.476119
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(3) == '3'
    assert get_shortish_repr(3, max_length=None) == '3'
    assert get_shortish_repr(3, max_length=1) == '3'
    assert get_shortish_repr(3, max_length=3) == '3'
    assert get_shortish_repr(3, max_length=2) == '3'
    assert get_shortish_repr(3, max_length=1) == '3'
    assert get_shortish_repr(3, max_length=0) == '...'
    assert get_shortish_repr([1, 2, 3]) == '[1, 2, 3]'

# Generated at 2022-06-12 20:00:49.061194
# Unit test for function get_repr_function
def test_get_repr_function():
    from . import sequencing

    def foo(x):
        return 'foo'

    def bar(x, y):
        return 'bar'

    custom_repr = [
        (lambda x: True, foo),
        (lambda x: False, bar),
        (lambda x, y=sequencing.Sequence: isinstance(x, y), lambda x: 'baz'),
    ]

    assert get_repr_function(None, custom_repr) is foo
    assert get_repr_function(None, custom_repr) is foo
    assert get_repr_function(sequencing.Sequence(), custom_repr) is foo
    assert get_repr_function((), custom_repr) is foo

# Generated at 2022-06-12 20:01:00.268741
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    from .test_tools import assert_equal

    class A(object):
        pass

    a = A()
    assert_equal(get_shortish_repr(a), repr(a))

    class B(object):
        def __repr__(self):
            return 'a B'

    b = B()
    assert_equal(get_shortish_repr(b), 'a B')

    custom_repr = (
        (lambda x: x is b, lambda x: 'b! ' + repr(x)),
        (A, lambda x: 'A'),
        (B, lambda x: 'B'),
    )

    assert_equal(get_shortish_repr(a, custom_repr), 'A')

# Generated at 2022-06-12 20:01:08.384656
# Unit test for function get_repr_function
def test_get_repr_function():
    custom_repr = (
        (lambda item: hasattr(item, 'foo'), lambda item: str(item.foo)),
        ((0, 1, 2, 3), lambda item: '0-3'),
    )
    assert get_repr_function(5, custom_repr) is repr
    assert get_repr_function(0, custom_repr) is repr
    assert get_repr_function(1, custom_repr) is repr
    assert get_repr_function(2, custom_repr) is repr
    assert get_repr_function(3, custom_repr) is repr
    assert get_repr_function((0, 1, 2, 3), custom_repr) is repr

# test_get_repr_function()



# Generated at 2022-06-12 20:01:21.545184
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    from .repr_example import thing
    from .repr_example_2 import thing2
    custom_repr = (
        (lambda x: isinstance(x, thing), lambda x: 'thing: {}'.format(x.name)),
        (lambda x: isinstance(x, thing2), lambda x: 'thing2: {}'.format(x.name)),
    )
    assert get_shortish_repr(thing('a'), custom_repr=custom_repr) == \
                                                                     'thing: a'
    assert get_shortish_repr(thing2('b'), custom_repr=custom_repr) == \
                                                                    'thing2: b'

# Generated at 2022-06-12 20:01:31.173081
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    import pytest

    assert (
        get_shortish_repr({1, 2, 3, 4, 5}, max_length=None) ==
        '{1, 2, 3, 4, 5}'
    )
    assert (
        get_shortish_repr({1, 2, 3, 4, 5}, max_length=9) ==
        '{1, 2, 3,...}'
    )
    assert (
        get_shortish_repr({1, 2, 3, 4, 5}, max_length=10) ==
        '{1, 2, 3,...}'
    )
    assert (
        get_shortish_repr({1, 2, 3, 4, 5}, max_length=11) ==
        '{1, 2, 3,...}'
    )

# Generated at 2022-06-12 20:01:37.657217
# Unit test for function get_repr_function
def test_get_repr_function():
    class Foo: pass
    class Bar(Foo): pass
    class Baz: pass
    custom_repr = (
        (Foo, lambda x: 'foo'),
        (Bar, lambda x: 'bar'),
    )

# Generated at 2022-06-12 20:01:45.500435
# Unit test for function get_repr_function
def test_get_repr_function():
    class MyClass(object): pass
    my_object = MyClass()
    assert get_repr_function(my_object, []) is repr
    assert get_repr_function(my_object, [(lambda x: False, 1)]) is repr
    assert get_repr_function(my_object, [(lambda x: True, 1)]) == 1
    assert get_repr_function(my_object, [(MyClass, 2)]) == 2
    assert get_repr_function(my_object, [(MyClass, 2), (object, 1)]) == 2
    assert get_repr_function(my_object, [(object, 1), (MyClass, 2)]) == 2

# Generated at 2022-06-12 20:01:49.914902
# Unit test for function shitcode
def test_shitcode():
    assert shitcode('test') == 'test'
    assert shitcode(u'test') == 'test'
    assert shitcode('test' * 1000) == 'test' * 1000
    assert shitcode(u'test' * 1000) == 'test' * 1000
    assert shitcode(u'test') == 'test'
    assert shitcode(u'\u05d0') == '?'
    assert shitcode(u'\u05d0\u05d1\u05d2') == '???'
    assert shitcode(u'\x01\x02\x03\x04\x05') == '?????'



# Generated at 2022-06-12 20:01:59.091847
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr([1, 2, 3]) == '[1, 2, 3]'
    assert get_shortish_repr(set([1, 2, 3])) == '{1, 2, 3}'
    assert get_shortish_repr([1, 2, 3, 4], max_length=8) == '[1, 2, ...]'
    assert get_shortish_repr([1, 2, 3, 4], max_length=11) == '[1, 2, 3, ...]'
    assert get_shortish_repr([1, 2, 3, 4], max_length=12) == '[1, 2, 3, ...]'
    assert get_shortish_repr([1, 2, 3, 4], max_length=13) == '[1, 2, 3, 4]'
    assert get_shortish

# Generated at 2022-06-12 20:02:05.859340
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, []) is repr
    assert get_repr_function('', [(lambda x: True, lambda x: 'b')]) == 'b'
    assert get_repr_function(1, [(int, lambda x: 'a')]) == 'a'
    assert get_repr_function('', [(int, lambda x: 'a')]) == repr
    assert get_repr_function('', [(int, lambda x: 'a')]) == repr
    assert get_repr_function('', [(int, lambda x: 'a'), (bool, lambda x: 'b')]) == repr
    assert get_repr_function('', [(int, lambda x: 'a'), (bool, lambda x: 'b')]) == repr

# Generated at 2022-06-12 20:02:14.855475
# Unit test for function shitcode
def test_shitcode():
    one, two, three='asdf'
    assert shitcode(one+two) == one+two
    assert shitcode(one+two+three) == one+two+three
    assert shitcode('\x00\xFF') == '??'
    assert shitcode(u'\uFFFD') == '?'
    assert shitcode('\xFF') == '?'
    assert shitcode('\uFFFD') == '?'
    assert shitcode('\0') == '?'
    assert shitcode(u'\0') == '?'
    assert shitcode('\u0915') == '?'
    assert shitcode('\U0001F440') == '?'
    assert shitcode('\U0001F400') == '?'
    assert shitcode('\x92') == '?'
    assert shitcode('\u0092') == '?'

# Generated at 2022-06-12 20:02:22.137727
# Unit test for function get_repr_function
def test_get_repr_function():
    def repr_a(x):
        return 'a'
    def repr_b(x):
        return 'b'
    def repr_c(x):
        return 'c'

    custom_reprs = [
        (lambda x: x[:1] == 'a', repr_a),
        (lambda x: x[:1] == 'b', repr_b),
        (str, repr_c),
    ]

    assert get_repr_function('abc', custom_reprs) is repr_a
    assert get_repr_function('bbb', custom_reprs) is repr_b
    assert get_repr_function('ccc', custom_reprs) is repr_c
    assert get_repr_function('ddd', custom_reprs) is repr


# Generated at 2022-06-12 20:02:31.188516
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    result = get_shortish_repr(
        object(),
        max_length=17,
        custom_repr=(
            (lambda x: x == object(), lambda x: 'woooooo'),
        )
    )
    assert result == 'woooooo...'

    result = get_shortish_repr(
        3.2,
        max_length=17,
        custom_repr=(
            (lambda x: x == object(), lambda x: 'woooooo'),
        )
    )
    assert result == '3.2'


# Generated at 2022-06-12 20:02:40.924731
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('abcdefghijklmnopqrstuvwxyz') == \
                                                             'abcdefghijklmnopqrstuvwxyz'
    assert get_shortish_repr('abcdefghijklmnopqrstuvwxyz', max_length=3) == '...'
    ensure_tuple(None)



# Generated at 2022-06-12 20:02:44.460969
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class A(object): pass
    class B(A): pass
    class C(B): pass
    class D(C):
        def write(self, s):
            return 123

    c = C()
    assert not isinstance(c, WritableStream)

    c.write = lambda s: 123
    assert not isinstance(c, WritableStream)

    c.__class__ = D
    assert isinstance(c, WritableStream)

    c.write = None
    assert not isinstance(c, WritableStream)




if __name__ == '__main__':
    test_WritableStream_write()

# Generated at 2022-06-12 20:02:46.742402
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Foo(WritableStream):
        pass
    with pytest.raises(TypeError):
        foo = Foo()
        foo.write('hi')



# Generated at 2022-06-12 20:02:56.866339
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(5, []) is repr
    assert get_repr_function(5, [(lambda x: True, None)]) is repr
    assert get_repr_function(5, [(lambda x: False, None)]) is repr
    assert get_repr_function(5, [(lambda x: False, 'foo')]) is repr
    def my_repr(x):
        return 'foo'
    assert get_repr_function(5, [(lambda x: True, my_repr)]) is my_repr
    assert get_repr_function(5, [((5, 6), my_repr)]) is repr
    assert get_repr_function(5, [(5, my_repr)]) is my_repr

# Generated at 2022-06-12 20:03:00.116183
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class SomeStream(WritableStream):
        def write(self, s):
            pass
    assert issubclass(SomeStream, WritableStream)
    assert isinstance(SomeStream(), WritableStream)



# Generated at 2022-06-12 20:03:07.964574
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    from collections import namedtuple

    CustomRepr = namedtuple('CustomRepr', 'condition action')


# Generated at 2022-06-12 20:03:18.012912
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class Derp(object):
        def write(self, s):
            pass

    assert isinstance(Derp(), WritableStream)

    class Herp(object):
        pass

    assert not isinstance(Herp(), WritableStream)

    class PreviousHerp(object):
        # has `write` but it's a method
        def write(self, s):
            pass

    class CurrentHerp(PreviousHerp):
        # still has `write`, but it's a None now
        write = None

    assert not isinstance(CurrentHerp(), WritableStream)

    class Derp2(object):
        # has `write`, but it's not a method
        write = 'hello'

    assert not isinstance(Derp2(), WritableStream)




# Generated at 2022-06-12 20:03:23.709731
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class FakeFile(WritableStream):
        def write(self, s):
            pass

    class FakeFileSubclass(FakeFile):
        pass

    assert issubclass(FakeFile, WritableStream)
    assert issubclass(FakeFileSubclass, WritableStream)

    class FakeFileSubclassNoWrite(FakeFile):
        pass

    del FakeFileSubclassNoWrite.write

    assert not issubclass(FakeFileSubclassNoWrite, WritableStream)

    class FakeFileSubclassWriteNone(FakeFile):
        write = None

    assert not issubclass(FakeFileSubclassWriteNone, WritableStream)


test_WritableStream_write()

# Generated at 2022-06-12 20:03:32.818161
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('a') == "'a'"
    assert get_shortish_repr('a'*10) == "u'aaaaaaaaaa'"
    assert get_shortish_repr('a'*10, max_length=None) == "u'aaaaaaaaaa'"
    assert get_shortish_repr('a'*10, max_length=5) == "'a...a'"
    assert get_shortish_repr('a'*10, max_length=11) == "'aaaaaaaaaa'"
    assert get_shortish_repr('a'*10, max_length=10) == "'aaaaaaaaa'"
    assert get_shortish_repr(1) == '1'
    assert get_shortish_repr(1, max_length=None) == '1'
    assert get_

# Generated at 2022-06-12 20:03:43.552760
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    def WriteToStringStream(s):
        stream = StringIOWrapper()
        stream.write(s)
        return stream.getvalue()

    class StringIOWrapper(StringIO, WritableStream):
        pass

    assert WriteToStringStream('abc') == 'abc'

    class MyFile(object):
        def write(self, s):
            pass

    assert WriteToStringStream(MyFile()) == '<__main__.MyFile object at 0x{:x}>'.format(id(MyFile()))

    class MyFile2(MyFile):
        pass

    assert WriteToStringStream(MyFile2()) == '<__main__.MyFile2 object at 0x{:x}>'.format(id(MyFile2()))


# Generated at 2022-06-12 20:03:58.092606
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(str(object()), ()) is repr
    assert get_repr_function('hello', (lambda x: False, lambda x: 'ohno')) is \
           repr

# Generated at 2022-06-12 20:04:02.750289
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    class NoRepr(object):
        pass
    no_repr = NoRepr()

    assert get_shortish_repr(None) == 'None'
    assert get_shortish_repr([]) == '[]'
    assert get_shortish_repr(no_repr) == 'REPR FAILED'

    assert truncate(shiticode('עברית'), 20) == '?...?'

if __name__ == '__main__':
    test_get_shortish_repr()

# Generated at 2022-06-12 20:04:08.982827
# Unit test for method write of class WritableStream
def test_WritableStream_write():

    class Test(WritableStream):
        def write(self, s):
            raise AssertionError("Shouldn't get here because method `write` is "
                                 "abstract so we shouldn't be able to instantiate "
                                 "an object of class Test")

    try:
        Test()
    except TypeError:
        pass
    else:
        raise AssertionError("This test failed because the abstract class "
                             "`WritableStream` was not properly declared.")

    class TestWithWrite(WritableStream):
        def write(self, s):
            pass

    TestWithWrite()

# Generated at 2022-06-12 20:04:14.467415
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Dummy:
        def __init__(self):
            self.s = ''
        def write(self, s):
            self.s += s
    assert isinstance(Dummy(), WritableStream)
    dummy = Dummy()
    dummy.write('This is a test.')
    assert dummy.s == 'This is a test.'



# Generated at 2022-06-12 20:04:24.466977
# Unit test for function get_repr_function
def test_get_repr_function():
    def type_repr(x): return 'type repr: ' + repr(x)
    def int_repr(x): return 'int repr: ' + repr(x)

    assert (get_repr_function(0, ((str, repr), (int, int_repr)))
            == repr)
    assert (get_repr_function(0, ((str, lambda x: 'str: ' + repr(x)),
                                  (int, int_repr))) == int_repr)
    assert (get_repr_function(0, ((str, lambda x: 'str: ' + repr(x)),
                                  (int, int_repr), (type, type_repr)))
            == int_repr)

# Generated at 2022-06-12 20:04:30.804680
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1, [(int, lambda x: 'x')]) == 'x'
    assert get_repr_function('hi', [(int, lambda x: 'x')]) == repr
    assert get_repr_function('hi', [(int, lambda x: 'x'),
                                    (str, lambda x: 'x')]) == 'x'
    assert get_repr_function(3.14, [(int, lambda x: 'x'),
                                    (str, lambda x: 'x')]) == repr



# Generated at 2022-06-12 20:04:42.088282
# Unit test for function get_shortish_repr
def test_get_shortish_repr():

    assert get_shortish_repr(1) == '1'
    assert get_shortish_repr(1, max_length=1) == '1'
    assert get_shortish_repr(1, max_length=2) == '1'
    assert get_shortish_repr(1, max_length=3) == '1'

    assert get_shortish_repr(1, max_length=2) == '1'
    assert get_shortish_repr(1, max_length=1) == '1'

    assert get_shortish_repr(1234, max_length=None) == '1234'

    assert get_shortish_repr(1234, max_length=4) == '1234'

# Generated at 2022-06-12 20:04:44.413378
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Foo:
        def write(self, s):
            pass
    assert isinstance(Foo(), WritableStream)



# Generated at 2022-06-12 20:04:53.754997
# Unit test for function get_shortish_repr
def test_get_shortish_repr():

    def f():
        class Mine(object):
            def __repr__(self):
                return 'My class!'

        class Yours(Mine):
            pass

        assert get_shortish_repr(Yours(), max_length=13) == 'My class!'
        assert get_shortish_repr(Your(Mine()), max_length=13) == 'REPR FAILED'

    def f():


        def my_repr(x):
            return 'Yours'


        assert get_shortish_repr(object(), max_length=13,
                                 custom_repr=((object, my_repr),)) == 'Yours'


# Generated at 2022-06-12 20:04:56.886762
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class DummyWritableStream(WritableStream):
        def write(self, s):
            pass

    dummy_writable_stream = DummyWritableStream()
    assert issubclass(DummyWritableStream, WritableStream)
    assert isinstance(dummy_writable_stream, WritableStream)



# Generated at 2022-06-12 20:05:12.604829
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('hello') == "'hello'"
    assert get_shortish_repr((1, 2, 3)) == "(1, 2, 3)"
    assert get_shortish_repr(('a', 'b', 'c'), max_length=4) == "(...)"
    assert get_shortish_repr(('a', 'b', 'c'), max_length=3) == "(...)"
    assert get_shortish_repr(('a', 'b', 'c'), max_length=2) == "(...)"
    assert get_shortish_repr(('a', 'b', 'c'), max_length=8) == "(...)"
    assert get_shortish_repr(('a', 'b', 'c'), max_length=9) == "('a', ...)"
    assert get_

# Generated at 2022-06-12 20:05:17.649157
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import io
    my_string = 'hello world'
    x = WritableStream.register(io.StringIO)
    assert isinstance(io.StringIO, x)
    s = io.StringIO()
    assert isinstance(s, x)
    assert issubclass(io.StringIO, x)
    s.write(my_string)
    assert my_string == s.getvalue()

# Generated at 2022-06-12 20:05:24.545108
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(int, ()) is repr

    def test_function(x):
        return f'Hello, {x.__name__}'

    assert get_repr_function(int, ((lambda x: True, test_function),)) is test_function

    assert get_repr_function(int, ((int, id),)) == id




# Generated at 2022-06-12 20:05:26.712131
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Foo:
        def write(self, s): pass
    assert isinstance(Foo(), WritableStream)

test_WritableStream_write()

# Generated at 2022-06-12 20:05:29.644024
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class WritableStreamImplementation(WritableStream):
        def write(self, s):
            pass

    assert issubclass(WritableStreamImplementation, WritableStream)

# Generated at 2022-06-12 20:05:34.249047
# Unit test for function get_repr_function
def test_get_repr_function():
    # Test 1:
    assert get_repr_function(1, custom_repr=[]) is repr
    assert get_repr_function(1.0, custom_repr=[]) is repr
    assert get_repr_function('1', custom_repr=[]) is repr
    assert get_repr_function((1, 2, 3), custom_repr=[]) is repr
    assert get_repr_function([1, 2, 3], custom_repr=[]) is repr
    # Test 2:
    def repr1(x):
        assert isinstance(x, int)
        return str(x * 2)
    assert get_repr_function(1, custom_repr=[(int, repr1)]) is repr1

# Generated at 2022-06-12 20:05:43.578723
# Unit test for function get_repr_function
def test_get_repr_function():
    assert get_repr_function(1.2, (
        (int, lambda x: 'hi'),
        (float, lambda x: 'bye'),
        (type(1.2), lambda x: 'yo'),
    )) == 'yo'
    assert get_repr_function(1, (
        (int, lambda x: 'hi'),
        (float, lambda x: 'bye'),
        (str, lambda x: 'yo'),
    )) == 'hi'
    assert get_repr_function(1.2, (
        (int, lambda x: 'hi'),
        (str, lambda x: 'bye'),
        (type(1.2), lambda x: 'yo'),
    )) == 'yo'

# Generated at 2022-06-12 20:05:49.195341
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(1) == u'1'
    assert get_shortish_repr(repr) == u"<built-in function repr>"
    assert get_shortish_repr(test_get_shortish_repr) == \
                                            u"<function test_get_shortish_repr at 0x"



# Generated at 2022-06-12 20:05:57.189729
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    from .pycompat import StringIO
    from .string_tools import ensure_text
    for encoding in ('utf8', 'latin1', 'ascii'):
        class A(WritableStream):
            def __init__(self, encoding):
                self.result = ''
                self.encoding = encoding
            def write(self, s):
                self.result += ensure_text(s)
        a = A(encoding)
        # Test with mixed unicode and bytes:
        a.write('foo')
        a.write(b'bar')
        assert a.result == 'foobar'
        # Test with unicode:
        a = A(encoding)
        a.write('foobar')
        assert a.result == 'foobar'
        # Test with bytes:
        a = A(encoding)


# Generated at 2022-06-12 20:06:00.871922
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class MyWritableStream(object):
        def __init__(self):
            self.data = ''

        def write(self, s):
            self.data += s

    writable_stream = MyWritableStream()
    isinstance(writable_stream, WritableStream)

# Generated at 2022-06-12 20:06:14.815309
# Unit test for function get_repr_function
def test_get_repr_function():
    def f(x):
        return x * 17
    my_float = type('float', (object,), {})
    my_float.__name__ = 'float'
    my_complex = type('complex', (object,), {})
    my_complex.__name__ = 'complex'
    assert get_repr_function(3, ((my_float, f),
                                 (complex, lambda x: 'complex!'))) \
                          == normalize_repr
    assert get_repr_function(3.0, ((my_float, f),
                                   (complex, lambda x: 'complex!'))) == f
    assert get_repr_function('hi', ((my_float, f),
                                    (complex, lambda x: 'complex!'))) == repr

# Generated at 2022-06-12 20:06:18.758072
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    class MyObject(object):
        def __repr__(self):
            return 'this_is_a_really_long_string_for_testing'

    assert get_shortish_repr(MyObject()) == 'this_is_a_really_long_string_fo...'





# Generated at 2022-06-12 20:06:26.245165
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr(1) == '1'
    assert get_shortish_repr(1, ((int, str),)) == '1'
    assert get_shortish_repr(1, ((int, lambda x: 'i'),)) == 'i'
    assert get_shortish_repr(1, ((int,), (str,))) == '1'
    assert get_shortish_repr(1, ((int,), (str, lambda x: x))) == '1'
    assert get_shortish_repr(1, ((int,), (str, lambda x: 'i'))) == 'i'
    assert get_shortish_repr(1, ((str, lambda x: x), (int, 'i'))) == '1'



# Generated at 2022-06-12 20:06:29.470881
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    a = [1, 2, 3] * 100
    b = set(a)
    assert get_shortish_repr(a) == u'[1, 2, 3, 1, 2, 3, ...]'
    assert get_shortish_repr(b) == u'{1, 2, 3, 1, 2, 3, ...}'



# Generated at 2022-06-12 20:06:30.234261
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    pass



# Generated at 2022-06-12 20:06:36.041598
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    from .pycompat import StringIO
    class MyStream(WritableStream):
        def __init__(self):
            self.string = ''
        def write(self, s):
            self.string += s

    stream = MyStream()
    stream.write('floop')
    assert stream.string == 'floop'



# Generated at 2022-06-12 20:06:42.331998
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    import sys

    class FakeStream(WritableStream):
        def __init__(self):
            self.data = ''

        def write(self, s):
            self.data += s

    real_stdout = sys.stdout
    sys.stdout = fake_stdout = FakeStream()

    print('hello')
    assert sys.stdout is fake_stdout
    assert fake_stdout.data == 'hello\n'

    sys.stdout = real_stdout

# Generated at 2022-06-12 20:06:51.545395
# Unit test for function get_repr_function
def test_get_repr_function():

    class Duck(object):
        pass

    duck = Duck()

    def custom_repr(item):
        return 'this is custom repr'

    assert get_repr_function(1, custom_repr=((Duck, custom_repr),)) is repr

    assert get_repr_function(duck, custom_repr=((Duck, custom_repr),))(
                                                                   duck) == \
                                                                  'this is custom repr'

    assert get_repr_function(1, custom_repr=((2, custom_repr),)) is repr

    assert get_repr_function(2, custom_repr=((2, custom_repr),))(2) == \
                                                                 'this is custom repr'


# Generated at 2022-06-12 20:06:58.107694
# Unit test for function get_repr_function
def test_get_repr_function():

    class A(object):
        pass

    class B(A):
        pass

    assert get_repr_function(
        A()
    )(A) == '<class \'cute_iter_tools._toolbox.A\'>'

    assert get_repr_function(
        B(),
        custom_repr=(
            (lambda x: isinstance(x, A), lambda x: 'I was an A'),
        )
    )(A) == 'I was an A'



# Generated at 2022-06-12 20:07:03.608966
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    a = 'a'
    b = 'x' * 100
    c = 'y' * 200
    d = Exception('hi')

    def custom_repr(x):
        return shitcode(str(x))

    custom_repr_iterable = [
        (Exception, custom_repr),
    ]

    assert get_shortish_repr('log message') == "'log message'"

    assert get_shortish_repr(a) == "'a'"
    assert get_shortish_repr(a, max_length=1) == "'a'"
    assert get_shortish_repr(a, max_length=2) == "'a'"
    assert get_shortish_repr(a, max_length=3) == "'a'"

# Generated at 2022-06-12 20:07:20.650458
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class Stream(WritableStream):
        def __init__(self):
            self.text = ''
        def write(self, s):
            self.text += s
        def flush(self):
            pass
    stream = Stream()
    stream.write('hello')
    assert stream.text == 'hello'

# Generated at 2022-06-12 20:07:23.620583
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class WritableStreamSubclass(WritableStream):
        def write(self, s):
            pass
    assert issubclass(WritableStreamSubclass, WritableStream)



# Generated at 2022-06-12 20:07:30.750519
# Unit test for function get_repr_function
def test_get_repr_function():

    def my_repr(number):
        return '(my_repr although it\'s just a number)'

    custom_repr = (
        (lambda x: x % 2 == 1, my_repr),
    )

    assert get_repr_function(5, custom_repr) is my_repr
    assert get_repr_function(6, custom_repr) is repr
    assert get_repr_function(6, custom_repr=None) is repr
    assert get_repr_function(6.2, custom_repr) is repr

    assert 'my_repr' in get_shortish_repr(5, custom_repr)
    assert 'my_repr' not in get_shortish_repr(6, custom_repr)

    assert 'my_repr' in get_

# Generated at 2022-06-12 20:07:40.273387
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('Hello', max_length=10) == 'Hello'

    assert get_shortish_repr('Hello', max_length=3) == 'Hel'

    assert get_shortish_repr('Hello', max_length=2) == 'He'

    assert get_shortish_repr('Hello', max_length=1) == 'H'

    assert get_shortish_repr('Hello', max_length=0) == ''

    assert get_shortish_repr('Hello', max_length=None) == 'Hello'

    assert get_shortish_repr('\r\r\r\r\r\r\r\r\r\r', max_length=3) == '\r\r\r'


# Generated at 2022-06-12 20:07:47.600685
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    class C(object):
        def __repr__(self):
            return 'self'
    assert get_shortish_repr(C()) == 'self'

    custom_repr = ((lambda x: x == C(),
                    lambda x: 'custom repr'),)

    assert get_shortish_repr(C(), custom_repr=custom_repr) == 'custom repr'

    assert get_shortish_repr(C(), custom_repr=custom_repr,
                             max_length=10, normalize=True) == 'custom repr'

    assert truncate('abcdefghi', 10) == 'abcdefghi'
    assert truncate('abcdefghi', 5) == '...hi'
    assert truncate('abcdefghi', 6) == '...ghi'

# Generated at 2022-06-12 20:07:56.302677
# Unit test for function get_shortish_repr
def test_get_shortish_repr():
    assert get_shortish_repr('Hi there, I am a very long string that needs '
                             'truncating.', max_length=20) == \
                             'Hi there, I...truncating.'
    assert get_shortish_repr('Hi there, I am a very long string that needs '
                             'truncating.', max_length=20, normalize=True) == \
                             'Hi there, I ... truncating.'
    assert get_shortish_repr('Hi there, I am a very long string that needs '
                             'truncating.', max_length=None) == \
                             'Hi there, I am a very long string that needs ' \
                             'truncating.'

# Generated at 2022-06-12 20:08:02.117272
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class DummyWritableStream(WritableStream):
        def __init__(self):
            self.writes = []
        def write(self, s):
            self.writes.append(s)
    dummy_writable_stream = DummyWritableStream()
    assert isinstance(dummy_writable_stream, WritableStream)
    dummy_writable_stream.write(b'yay')
    assert dummy_writable_stream.writes == [b'yay']



# Generated at 2022-06-12 20:08:10.380174
# Unit test for function get_repr_function
def test_get_repr_function():

    class Foo():
        pass

    class Bar():
        pass

    def repr_foo(x):
        return 'foo'

    def repr_int(x):
        return 'int'

    def repr_bar(x):
        return 'bar'

    custom_repr = ((Foo, repr_foo), (int, repr_int), (Bar, repr_bar))
    assert get_repr_function(Foo(), custom_repr) is repr_foo
    assert get_repr_function(Bar(), custom_repr) is repr_bar
    assert get_repr_function(1, custom_repr) is repr_int
    assert get_repr_function(1.5, custom_repr) is repr

    def condition_foo(x):
        return (x is Foo())


# Generated at 2022-06-12 20:08:19.389070
# Unit test for function get_repr_function
def test_get_repr_function():
    class X(object):pass
    x = X()
    assert get_repr_function(x, [(X, lambda x: None)]) is None
    assert get_repr_function(x, [(lambda x: False, lambda x: None)]) is not None
    assert get_repr_function(x, [(lambda x: False, lambda x: None),
                                 (X, lambda x: None)]) is None
    assert get_repr_function(x, [(lambda x: False, lambda x: None),
                                 (X, lambda x: None),
                                 (None, lambda x: None)]) is None

# Generated at 2022-06-12 20:08:22.218016
# Unit test for method write of class WritableStream
def test_WritableStream_write():
    class DummyWritableStream(WritableStream):
        def write(self, s):
            return s
    assert isinstance(DummyWritableStream(), WritableStream)
    assert isinstance(DummyWritableStream(), object)
    assert not isinstance(object(), WritableStream)